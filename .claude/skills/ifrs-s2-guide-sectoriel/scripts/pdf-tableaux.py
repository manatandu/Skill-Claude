#!/usr/bin/env python3
"""Extrait les tableaux d'un PDF en Markdown et garde une capture PNG de chacun.

Usage :
    python3 pdf-tableaux.py source.pdf --pages 210-232 --out references/xxx/

Produit :
    <out>/tableaux.md        un tableau Markdown par tableau detecte, avec le
                             renvoi vers sa capture
    <out>/images/p<N>-t<k>.png  la capture de la zone du tableau

Pourquoi : l'extraction texte d'un PDF (pdftotext, get_text) rend une colonne
unique. Les chiffres arrivent en file, on ne sait plus a quelle colonne ils
appartiennent. find_tables() retrouve la grille ; la capture sert de preuve
quand la grille elle-meme est douteuse.

Dependance : pymupdf (pip install pymupdf).
"""
import argparse
import pathlib
import re
import sys

import pymupdf

NOMBRE = re.compile(r"^\(?-?[\d\s .,]+\)?%?$")


def parse_pages(spec, npages):
    """'1-3,7' -> [0,1,2,6] (index 0). Vide -> toutes les pages."""
    if not spec:
        return list(range(npages))
    out = []
    for bloc in spec.split(","):
        bloc = bloc.strip()
        if "-" in bloc:
            a, b = bloc.split("-", 1)
            out.extend(range(int(a) - 1, int(b)))
        else:
            out.append(int(bloc) - 1)
    return [p for p in out if 0 <= p < npages]


def nettoie(cell):
    if cell is None:
        return ""
    return " ".join(str(cell).split()).replace("|", "\\|")


def en_nombre(txt):
    """'48,600,415' -> 48600415.0 ; '(1 2)' -> -12.0 ; sinon None."""
    t = txt.strip()
    if not t or not NOMBRE.match(t):
        return None
    negatif = t.startswith("(") and t.endswith(")")
    t = t.strip("()%").replace(" ", "").replace(" ", "")
    if "," in t and "." in t:
        t = t.replace(",", "") if t.rfind(".") > t.rfind(",") else t.replace(".", "").replace(",", ".")
    elif t.count(",") > 1 or re.match(r"^-?\d{1,3}(,\d{3})+$", t):
        t = t.replace(",", "")
    else:
        t = t.replace(",", ".")
    try:
        v = float(t)
    except ValueError:
        return None
    return -v if negatif else v


def controle_totaux(lignes):
    """Compare chaque ligne 'total' a la somme des lignes numeriques au-dessus.

    Retourne la liste des ecarts constates, sous forme lisible.
    """
    ecarts = []
    if len(lignes) < 3:
        return ecarts
    ncol = max(len(r) for r in lignes)
    for i, ligne in enumerate(lignes):
        if not ligne or "total" not in nettoie(ligne[0]).lower():
            continue
        for c in range(1, ncol):
            cible = en_nombre(nettoie(ligne[c])) if c < len(ligne) else None
            if cible is None:
                continue
            valeurs = [en_nombre(nettoie(r[c])) for r in lignes[:i]
                       if c < len(r) and en_nombre(nettoie(r[c])) is not None]
            if len(valeurs) < 2:
                continue
            somme = sum(valeurs)
            if abs(somme - cible) > max(1.0, abs(cible) * 1e-6):
                ecarts.append(
                    f"ligne « {nettoie(ligne[0])} », colonne {c + 1} : "
                    f"lu {cible:,.0f}, somme des lignes au-dessus {somme:,.0f}")
    return ecarts


def markdown(lignes):
    ncol = max(len(r) for r in lignes)
    lignes = [[nettoie(c) for c in r] + [""] * (ncol - len(r)) for r in lignes]
    tete, corps = lignes[0], lignes[1:]
    if not any(tete):
        tete = [f"col {i + 1}" for i in range(ncol)]
        corps = lignes[1:]
    out = ["| " + " | ".join(tete) + " |",
           "|" + "|".join([" --- "] * ncol) + "|"]
    out += ["| " + " | ".join(r) + " |" for r in corps]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--pages", default="", help="ex. 210-232,240 (1-indexe)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--dpi", type=int, default=200)
    ap.add_argument("--marge", type=float, default=8.0, help="marge de la capture, en points")
    args = ap.parse_args()

    out = pathlib.Path(args.out)
    (out / "images").mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(args.pdf)
    pages = parse_pages(args.pages, doc.page_count)

    blocs, total = [], 0
    for pno in pages:
        page = doc[pno]
        try:
            tables = page.find_tables().tables
        except Exception as e:                       # page illisible, on continue
            print(f"p.{pno + 1} : find_tables a echoue ({e})", file=sys.stderr)
            continue
        for k, t in enumerate(tables, 1):
            lignes = [r for r in t.extract() if any(nettoie(c) for c in r)]
            if not lignes:
                continue
            total += 1
            nom = f"p{pno + 1}-t{k}.png"
            rect = pymupdf.Rect(t.bbox) + (-args.marge, -args.marge, args.marge, args.marge)
            page.get_pixmap(clip=rect, dpi=args.dpi).save(out / "images" / nom)
            ecarts = controle_totaux(lignes)
            bloc = [f"### p. {pno + 1}, tableau {k}", "", markdown(lignes), "",
                    f"![p. {pno + 1} tableau {k}](images/{nom})", "",
                    "> Capture de la zone d'origine. Si un chiffre est utilise, "
                    "l'ouvrir et le relire dessus."]
            if ecarts:
                bloc += ["", "> Controle des totaux, ecart constate : "
                             + " ; ".join(ecarts) + "."]
            blocs.append("\n".join(bloc))

    entete = [f"# Tableaux extraits de `{pathlib.Path(args.pdf).name}`", "",
              f"{total} tableau(x) sur {len(pages)} page(s) traitee(s). "
              f"Captures a {args.dpi} dpi dans `images/`.", ""]
    (out / "tableaux.md").write_text("\n".join(entete) + "\n" + "\n\n".join(blocs) + "\n",
                                     encoding="utf-8")
    print(f"{total} tableau(x) ecrit(s) dans {out / 'tableaux.md'}")


if __name__ == "__main__":
    main()
