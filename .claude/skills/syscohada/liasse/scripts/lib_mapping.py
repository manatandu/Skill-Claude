"""
lib_mapping.py — Cœur du montage de la liasse SYSCOHADA (Système normal).

Deux responsabilités :
  1. Normaliser une balance quelconque : chaque compte est ramené à ses
     préfixes OHADA (2, 3, 4 chiffres). Un compte personnalisé 24421000
     se lit 24 / 244 / 2442 : les 4 premiers chiffres portent le sens OHADA,
     le reste n'est qu'une subdivision interne.
  2. Affecter chaque solde à sa rubrique du bilan et du compte de résultat,
     en appliquant les conventions de la maquette vérifiée (englobement,
     clause « sauf », reprise partielle « p », sens du solde).

La maquette (references/correspondance.tsv) reste la seule source des
affectations. Ce module ne fait que l'interpréter.
"""

import csv
import re
from dataclasses import dataclass, field


# --------------------------------------------------------------------------
# Lecture d'une expression de comptes de la maquette
# --------------------------------------------------------------------------

@dataclass
class Expr:
    """Expression de comptes analysée à partir d'une cellule de la maquette."""
    include: list = field(default_factory=list)   # tokens à inclure (2,3,4 chiffres)
    exclude: list = field(default_factory=list)   # tokens retranchés (clause 'sauf')
    sens: str = "net"        # 'net' | 'debiteur' | 'crediteur'
    partiels: list = field(default_factory=list)  # tokens en 'p' (reprise partielle)
    signe: str = ""          # pour le résultat : '+', '-', '-/+'


_TOK = re.compile(r"\d{2,4}p?")


def parse_expr(cell: str) -> Expr:
    """Analyse une cellule 'comptes_brut' ou 'comptes_amort_deprec'."""
    e = Expr()
    if not cell or not cell.strip():
        return e
    s = cell.strip()

    # signe de tête pour le compte de résultat
    m = re.match(r"\s*(-/\+|\+|-)\s*", s)
    if m:
        e.signe = m.group(1)
        s = s[m.end():]

    # sens conditionnel
    low = s.lower()
    if low.startswith("soldes débiteurs") or low.startswith("soldes debiteurs"):
        e.sens = "debiteur"
        s = s.split(":", 1)[1]
    elif low.startswith("soldes créditeurs") or low.startswith("soldes crediteurs"):
        e.sens = "crediteur"
        s = s.split(":", 1)[1]

    # clause 'sauf' : les comptes cités partent dans une autre rubrique
    # (peut apparaître globalement ou juste après un token : '24 (sauf 245, 2495)')
    for msauf in re.finditer(r"sauf\s+([\d,\s]+)", s, re.I):
        for tok in _TOK.findall(msauf.group(1)):
            e.exclude.append(tok)
    s_wo_sauf = re.sub(r"\(?\s*sauf\s+[\d,\s]+\)?", " ", s, flags=re.I)

    for tok in _TOK.findall(s_wo_sauf):
        if tok.endswith("p"):
            e.partiels.append(tok[:-1])
            e.include.append(tok[:-1])   # v1 : on prend le compte en entier, on signale
        else:
            e.include.append(tok)

    # dédoublonnage en gardant l'ordre
    e.include = list(dict.fromkeys(e.include))
    e.exclude = list(dict.fromkeys(e.exclude))
    return e


# --------------------------------------------------------------------------
# Chargement de la maquette
# --------------------------------------------------------------------------

@dataclass
class Rubrique:
    etat: str
    ref: str
    libelle: str
    brut: Expr
    amort: Expr
    formule: str
    note: str = ""


def charger_maquette(chemin: str):
    rubs = {}
    with open(chemin, encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            rubs[row["ref"]] = Rubrique(
                etat=row["etat"],
                ref=row["ref"],
                libelle=row["rubrique"],
                brut=parse_expr(row["comptes_brut"]),
                amort=parse_expr(row["comptes_amort_deprec"]),
                formule=row["formule"],
                note=row.get("note", ""),
            )
    return rubs


# --------------------------------------------------------------------------
# Normalisation d'un numéro de compte
# --------------------------------------------------------------------------

def normaliser_compte(brut) -> str:
    """Ramène un code de compte à sa forme chiffrée (sans .0, sans espaces)."""
    if brut is None:
        return ""
    s = str(brut).strip()
    if s.endswith(".0"):
        s = s[:-2]
    s = re.sub(r"[^\d]", "", s)   # on ne garde que les chiffres
    return s


def prefixe(compte: str, n: int) -> str:
    """n premiers chiffres du compte."""
    return compte[:n]


# --------------------------------------------------------------------------
# Correspondance compte -> rubrique
# --------------------------------------------------------------------------

def token_match(compte: str, token: str) -> bool:
    """
    Le compte relève-t-il du token de la maquette ?
    Convention : un token de 2 chiffres englobe tous ses divisionnaires ;
    un token de 3 ou 4 chiffres ne vaut que pour lui-même et ses subdivisions.
    On compare donc sur le préfixe de la longueur du token.
    """
    L = len(token)
    return prefixe(compte, L) == token


def compte_dans_expr(compte: str, e: Expr) -> bool:
    if not e.include:
        return False
    if any(token_match(compte, t) for t in e.exclude):
        return False
    return any(token_match(compte, t) for t in e.include)
