"""
formules.py — Générateur de formules Excel traçables pour la liasse SYSCOHADA.

Principe : plutôt que d'injecter des valeurs figées, le moteur écrit dans les
états et les notes annexes de vraies formules Excel (SUMIF) pointant vers la
feuille BALANCE (exercice N) ou BALANCE_N1 (exercice N-1) du classeur produit.
Chaque chiffre de la liasse est ainsi retraçable jusqu'aux comptes de la
balance qui l'alimentent — l'utilisateur peut auditer n'importe quel poste en
suivant la formule.

Disposition des feuilles BALANCE / BALANCE_N1 (écrites par monter_liasse.py) :
  A Compte | B Intitulé | C Solde d'ouverture débit
  D Solde d'ouverture crédit | E Mouvement débit | F Mouvement crédit
  G Solde de clôture débit | H Solde de clôture crédit

Les jetons de maquette se comparent au numéro de compte (colonne A) par
critère jocker (« 24* » capte 24 et ses subdivisions) — même convention
d'englobement que lib_mapping.token_match. La clause « sauf » se traduit par
des SUMIF soustraits.

Modes de sommation (mêmes conventions que monter_liasse.somme) :
  'd'  : somme des soldes de clôture débiteurs (colonne G seule)
  'c'  : somme des soldes de clôture créditeurs (colonne H seule)
  'nd' : net débiteur  (G - H)  — actif brut, charges
  'nc' : net créditeur (H - G)  — amortissements, passif, produits
  'md' : somme des mouvements débit (colonne E)
  'mc' : somme des mouvements crédit (colonne F)
"""

from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Charte graphique ETAFI partagée (palette, cartouche, niveaux de lignes,
# pages spéciales) : tout est ré-exporté ici pour les moteurs.
from theme_etafi import *          # noqa: F401,F403
from theme_etafi import q, nom_feuille, normaliser_ident  # noqa: F401

# --------------------------------------------------------------------------
# Formules SUMIF sur la balance
# --------------------------------------------------------------------------

# Colonnes des feuilles de balance (cf. theme_etafi.COLS_BALANCE) :
#   C-D solde d'ouverture | E-F mouvements | G-H solde de clôture
_MODE_COLS = {"d": ("G",), "c": ("H",), "nd": ("G", "H"), "nc": ("H", "G"),
              "md": ("E",), "mc": ("F",)}

# Dernière ligne des plages SUMIF : bornée (plutôt que colonne entière) pour
# des recalculs rapides. Le moteur la cale sur la taille réelle de la balance.
_LIGNE_MAX = 2000


def set_lignes_max(n):
    global _LIGNE_MAX
    _LIGNE_MAX = max(int(n), 50)


def _sumif(feuille, token, col):
    # critère jocker sur la colonne A (numéros de comptes écrits en texte) :
    # "24*" capte 24 et toutes ses subdivisions, quel que soit le nombre de
    # chiffres du jeton — même convention d'englobement que lib_mapping.
    f = q(feuille)
    return (f"SUMIF({f}!$A$2:$A${_LIGNE_MAX},\"{token}*\","
            f"{f}!${col}$2:${col}${_LIGNE_MAX})")


def _termes(tokens, mode, feuille, signe):
    """Liste de (signe, sumif) pour un jeu de jetons dans un mode donné."""
    cols = _MODE_COLS[mode]
    out = []
    for t in tokens:
        out.append((signe, _sumif(feuille, t, cols[0])))
        if len(cols) == 2:  # net : la 2e colonne vient en sens inverse
            out.append(("-" if signe == "+" else "+", _sumif(feuille, t, cols[1])))
    return out


def _dedupe(tokens):
    """Écarte les jetons déjà englobés par un jeton plus court de la liste :
    « 12, 121, 129 » -> « 12 » (un SUMIF « 12* » capte déjà 121 et 129 ;
    les additionner tous compterait les subdivisions deux fois).

    L'ordre est déterministe (longueur, puis numéro) : deux exécutions sur la
    même balance rendent des formules identiques au caractère près."""
    ts = sorted(set(tokens), key=lambda t: (len(t), t))
    out = []
    for t in ts:
        if not any(t != p and t.startswith(p) for p in out):
            out.append(t)
    return out


def formule_tokens(tokens, mode, feuille="BALANCE", exclude=()):
    """Formule Excel '=...' sommant les jetons donnés, moins les exclusions."""
    termes = _termes(_dedupe(tokens), mode, feuille, "+")
    termes += _termes(_dedupe(exclude), mode, feuille, "-")
    if not termes:
        return None
    corps = ""
    for i, (s, t) in enumerate(termes):
        corps += t if (i == 0 and s == "+") else s + t
    return "=" + corps


def formule_expr(e, mode_defaut, feuille="BALANCE"):
    """Formule pour une Expr de lib_mapping (sens conditionnel respecté)."""
    mode = mode_defaut
    if getattr(e, "sens", "net") == "debiteur":
        mode = "d"
    elif getattr(e, "sens", "net") == "crediteur":
        mode = "c"
    if not e.include:
        return None
    return formule_tokens(e.include, mode, feuille, exclude=e.exclude)


# --------------------------------------------------------------------------
# Présentation : la charte ETAFI (theme_etafi) fournit styles, cartouche,
# niveaux de lignes et pages spéciales. Ci-dessous, seuls subsistent des
# adaptateurs de compatibilité pour les anciens points d'entrée.
# --------------------------------------------------------------------------

def construire_identification(wb, ident, referentiel, systeme, position=1):
    """Compat : la fiche d'identification est désormais la « Fiche 1 »
    à cases codes de la charte ETAFI."""
    return construire_fiche1(wb, ident, referentiel, systeme)


def construire_fiche_notes(wb, parties, ident, sous_titre=None,
                           position=None, note_pied=None):
    """Compat : la fiche récapitulative est désormais la feuille
    « NOTES ANNEXES » de la charte ETAFI."""
    return construire_fiche_notes_etafi(wb, parties, ident,
                                        note_pied=note_pied)
