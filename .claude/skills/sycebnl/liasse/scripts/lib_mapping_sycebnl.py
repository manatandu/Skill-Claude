"""
lib_mapping_sycebnl.py — Coeur du montage des etats financiers SYCEBNL
(associations et ordres professionnels, Systeme normal).

Module autonome (aucune dependance a un autre skill), sur le meme principe
que syscohada/liasse/scripts/lib_mapping.py mais avec un analyseur de
cellule plus general : le tableau officiel de correspondance du SYCEBNL
melange, dans une meme case, des comptes sans condition et des comptes
soumis a une clause « solde crediteurs : ... » ou « solde debiteurs : ... »
(ex. poste DW : « 56, solde crediteurs : 52, 53 »). L'analyseur separe donc
trois groupes de jetons : inconditionnels, debiteurs-seuls, crediteurs-seuls.

La maquette (references/correspondance-associations.tsv) reste la seule
source des affectations. Ce module ne fait que l'interpreter.
"""

import csv
import re
from dataclasses import dataclass, field


_TOK = re.compile(r"\d{2,4}p?")


@dataclass
class Expr:
    include: list = field(default_factory=list)       # jetons inconditionnels
    include_deb: list = field(default_factory=list)    # jetons "solde debiteurs" seulement
    include_cred: list = field(default_factory=list)   # jetons "solde crediteurs" seulement
    exclude: list = field(default_factory=list)        # jetons retranches (clause "sauf")
    partiels: list = field(default_factory=list)       # jetons en "p" (reprise partielle)
    signe: str = ""                                    # documentation seule ('+', '-', '-/+')


def _tokens(s):
    return _TOK.findall(s)


def parse_expr(cell: str) -> Expr:
    e = Expr()
    if not cell or not cell.strip():
        return e
    s = cell.strip()

    m = re.match(r"\s*(-/\+|\+/-|\+|-)\s*", s)
    if m:
        e.signe = m.group(1)
        s = s[m.end():]

    # clause(s) "sauf X, Y" : retranchees globalement, quel que soit le groupe
    for msauf in re.finditer(r"sauf\s+([\d,\s]+)", s, re.I):
        e.exclude.extend(_tokens(msauf.group(1)))
    s = re.sub(r"\(?\s*sauf\s+[\d,\s]+\)?", " ", s, flags=re.I)

    # clause(s) "solde(s) debiteurs : ..." / "solde(s) crediteurs : ..." pouvant
    # apparaitre n'importe ou dans la cellule, pas seulement en tete
    def _extraire_sens(texte, motif, cible):
        def repl(mo):
            cible.extend(_tokens(mo.group(1)))
            return " "
        return re.sub(motif, repl, texte, flags=re.I)

    s = _extraire_sens(s, r"solde s?\s*debiteurs?\s*:\s*([\d,\s]+)", e.include_deb)
    s = _extraire_sens(s, r"solde s?\s*crediteurs?\s*:\s*([\d,\s]+)", e.include_cred)

    for tok in _tokens(s):
        if tok.endswith("p"):
            e.partiels.append(tok[:-1])
            e.include.append(tok[:-1])   # v1 : compte pris en entier, signale
        else:
            e.include.append(tok)

    e.include = list(dict.fromkeys(e.include))
    e.include_deb = list(dict.fromkeys(e.include_deb))
    e.include_cred = list(dict.fromkeys(e.include_cred))
    e.exclude = list(dict.fromkeys(e.exclude))
    return e


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


def normaliser_compte(brut) -> str:
    if brut is None:
        return ""
    s = str(brut).strip()
    if s.endswith(".0"):
        s = s[:-2]
    return re.sub(r"[^\d]", "", s)


def prefixe(compte: str, n: int) -> str:
    return compte[:n]


def _tok_match(compte: str, token: str) -> bool:
    L = len(token)
    return prefixe(compte, L) == token


def _exclu(compte: str, e: Expr) -> bool:
    return any(_tok_match(compte, t) for t in e.exclude)


def compte_dans_expr(compte: str, e: Expr) -> bool:
    if _exclu(compte, e):
        return False
    tous = e.include + e.include_deb + e.include_cred
    return any(_tok_match(compte, t) for t in tous)


def groupe_compte(compte: str, e: Expr):
    """Renvoie 'deb', 'cred' ou 'defaut' selon le groupe qui capte le compte."""
    if any(_tok_match(compte, t) for t in e.include_deb):
        return "deb"
    if any(_tok_match(compte, t) for t in e.include_cred):
        return "cred"
    return "defaut"
