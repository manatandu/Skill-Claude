"""
formules.py — Générateur de formules Excel traçables pour la liasse SYSCOHADA.

Principe : plutôt que d'injecter des valeurs figées, le moteur écrit dans les
états et les notes annexes de vraies formules Excel (SUMIF) pointant vers la
feuille BALANCE (exercice N) ou BALANCE_N1 (exercice N-1) du classeur produit.
Chaque chiffre de la liasse est ainsi retraçable jusqu'aux comptes de la
balance qui l'alimentent — l'utilisateur peut auditer n'importe quel poste en
suivant la formule.

Disposition des feuilles BALANCE / BALANCE_N1 (écrites par monter_liasse.py) :
  A Compte | B Intitulé | C Préfixe 2 | D Préfixe 3 | E Préfixe 4
  F Solde final débit | G Solde final crédit | H Mouvement débit
  I Mouvement crédit | J Poste(s) d'affectation

Un jeton de maquette de 2 chiffres se compare à la colonne C, de 3 chiffres à
la colonne D, de 4 chiffres à la colonne E — même convention d'englobement que
lib_mapping.token_match. La clause « sauf » se traduit par des SUMIF soustraits.

Modes de sommation (mêmes conventions que monter_liasse.somme) :
  'd'  : somme des soldes débiteurs (colonne F seule)
  'c'  : somme des soldes créditeurs (colonne G seule)
  'nd' : net débiteur  (F - G)  — actif brut, charges
  'nc' : net créditeur (G - F)  — amortissements, passif, produits
  'md' : somme des mouvements débit (colonne H)
  'mc' : somme des mouvements crédit (colonne I)
"""

from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# --------------------------------------------------------------------------
# Formules SUMIF sur la balance
# --------------------------------------------------------------------------

_MODE_COLS = {"d": ("F",), "c": ("G",), "nd": ("F", "G"), "nc": ("G", "F"),
              "md": ("H",), "mc": ("I",)}

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
    return (f"SUMIF({feuille}!$A$2:$A${_LIGNE_MAX},\"{token}*\","
            f"{feuille}!${col}$2:${col}${_LIGNE_MAX})")


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
    les additionner tous compterait les subdivisions deux fois)."""
    ts = sorted(set(tokens), key=len)
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
# Styles partagés (présentation professionnelle des feuilles ajoutées)
# --------------------------------------------------------------------------

BLEU_FONCE = "1F4E5F"
BLEU_CLAIR = "DDEBF0"
GRIS_CLAIR = "F2F2F2"
OR_TOTAL = "FCE4D6"

F_TITRE = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
F_SOUS_TITRE = Font(name="Calibri", size=11, bold=True, color=BLEU_FONCE)
F_ENTETE = Font(name="Calibri", size=10, bold=True, color="FFFFFF")
F_NORMAL = Font(name="Calibri", size=10)
F_GRAS = Font(name="Calibri", size=10, bold=True)

R_TITRE = PatternFill("solid", fgColor=BLEU_FONCE)
R_ENTETE = PatternFill("solid", fgColor="2E75B6")
R_BANDE = PatternFill("solid", fgColor=GRIS_CLAIR)
R_TOTAL = PatternFill("solid", fgColor=OR_TOTAL)

BORD_FIN = Border(*(Side(style="thin", color="BFBFBF"),) * 4)

AL_CENTRE = Alignment(horizontal="center", vertical="center", wrap_text=True)
AL_GAUCHE = Alignment(horizontal="left", vertical="center", wrap_text=True)

FMT_MONTANT = "#,##0;[Red]-#,##0"
FMT_PCT = "0.0%"


def style_titre(ws, cell_range, texte):
    """Bandeau de titre fusionné sur cell_range (ex. 'A1:G1')."""
    ws.merge_cells(cell_range)
    first = cell_range.split(":")[0]
    c = ws[first]
    c.value = texte
    c.font = F_TITRE
    c.fill = R_TITRE
    c.alignment = AL_CENTRE


def style_entetes(ws, row, col_min, col_max):
    for col in range(col_min, col_max + 1):
        c = ws.cell(row, col)
        c.font = F_ENTETE
        c.fill = R_ENTETE
        c.alignment = AL_CENTRE
        c.border = BORD_FIN


def style_zone_donnees(ws, row_min, row_max, col_min, col_max,
                       cols_montant=(), bandes=True):
    for r in range(row_min, row_max + 1):
        for col in range(col_min, col_max + 1):
            c = ws.cell(r, col)
            c.border = BORD_FIN
            if c.font is None or not c.font.bold:
                c.font = F_NORMAL
            if bandes and r % 2 == 0:
                if c.fill is None or c.fill.fgColor.rgb in (None, "00000000"):
                    c.fill = R_BANDE
            if col in cols_montant:
                c.number_format = FMT_MONTANT


def style_ligne_total(ws, row, col_min, col_max, cols_montant=()):
    for col in range(col_min, col_max + 1):
        c = ws.cell(row, col)
        c.font = F_GRAS
        c.fill = R_TOTAL
        c.border = BORD_FIN
        if col in cols_montant:
            c.number_format = FMT_MONTANT


def largeurs(ws, spec):
    """spec : dict lettre -> largeur."""
    for lettre, l in spec.items():
        ws.column_dimensions[lettre].width = l


def format_montants(ws, cellules):
    """Applique le format montant à une liste de références 'B12'..."""
    for ref in cellules:
        ws[ref].number_format = FMT_MONTANT


# --------------------------------------------------------------------------
# Nettoyage typographique et pages de présentation communes
# --------------------------------------------------------------------------

def retirer_tirets(wb):
    """Remplace tirets cadratins (—) et demi-cadratins (–) par un tiret
    simple dans toutes les cellules texte : aucun « — » dans les livrables."""
    from openpyxl.cell.cell import MergedCell
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c, MergedCell):
                    continue
                v = c.value
                if isinstance(v, str) and ("—" in v or "–" in v):
                    v = v.replace(" — ", " - ").replace("—", "-")
                    v = v.replace(" – ", " - ").replace("–", "-")
                    c.value = v


def construire_identification(wb, ident, referentiel, systeme, position=1):
    """Fiche d'identification et de renseignements généraux (page de
    présentation) : champs connus pré-remplis, le reste à compléter."""
    entite, identifiant, exercice, duree = ident
    ws = wb.create_sheet("IDENTIFICATION", position)
    ws.sheet_view.showGridLines = False
    style_titre(ws, "A1:D1", "FICHE D'IDENTIFICATION ET RENSEIGNEMENTS GENERAUX")
    ws.merge_cells("A2:D2")
    ws["A2"] = f"{referentiel} - {systeme}"
    ws["A2"].font = F_SOUS_TITRE
    ws["A2"].alignment = AL_CENTRE
    champs = [
        ("Dénomination / raison sociale de l'entité", entite),
        ("Sigle usuel", ""),
        ("Forme juridique / type d'entité", ""),
        ("Numéro d'identification", identifiant),
        ("Registre (RCCM, F92, convention...)", ""),
        ("Adresse complète (immeuble, rue, quartier)", ""),
        ("Ville / Pays", ""),
        ("Téléphone", ""),
        ("Adresse électronique", ""),
        ("Activité principale / mission", ""),
        ("Référentiel comptable", referentiel),
        ("Système d'états financiers", systeme),
        ("Exercice clos le", exercice),
        ("Durée de l'exercice (en mois)", duree),
        ("Exercice précédent clos le", ""),
        ("Unité monétaire légale de présentation", ""),
        ("Date d'arrêté effectif des comptes", ""),
        ("Organe ayant arrêté les états financiers", ""),
        ("Responsable des états financiers (nom et qualité)", ""),
        ("Cabinet / expert-comptable (nom, adresse, téléphone)", ""),
        ("Auditeur / commissaire aux comptes, le cas échéant", ""),
    ]
    r = 3
    for lab, val in champs:
        r += 1
        ws.cell(r, 1, lab)
        ws.cell(r, 1).font = F_GRAS
        ws.cell(r, 1).alignment = AL_GAUCHE
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=4)
        ws.cell(r, 2, val)
        for col in (1, 2, 3, 4):
            ws.cell(r, col).border = BORD_FIN
    r += 2
    ws.cell(r, 1, "Visa et signatures")
    ws.cell(r, 1).font = F_SOUS_TITRE
    r += 1
    for lab in ("Signataire des états financiers (nom, qualité, date, signature)",
                "Visa de l'expert-comptable ou du comptable agréé"):
        r += 1
        ws.cell(r, 1, lab)
        ws.cell(r, 1).alignment = AL_GAUCHE
        ws.merge_cells(start_row=r, start_column=2, end_row=r + 1, end_column=4)
        for rr in (r, r + 1):
            for col in (1, 2, 3, 4):
                ws.cell(rr, col).border = BORD_FIN
        r += 2
    largeurs(ws, {"A": 46, "B": 22, "C": 22, "D": 22})
    return ws


def construire_fiche_notes(wb, parties, ident, sous_titre, position=None,
                           note_pied=None):
    """Fiche récapitulative des notes annexes présentées : colonnes
    NOTES | INTITULÉS | A (Applicable) | N/A (Non applicable).
    `parties` : liste de (titre_partie, [(numero, intitule), ...])."""
    entite, identifiant, exercice, duree = ident
    ws = (wb.create_sheet("FICHE NOTES", position) if position is not None
          else wb.create_sheet("FICHE NOTES"))
    ws.sheet_view.showGridLines = False
    style_titre(ws, "A1:D1", "FICHE RECAPITULATIVE DES NOTES ANNEXES PRESENTEES")
    ws.merge_cells("A2:D2")
    ws["A2"] = sous_titre
    ws["A2"].font = F_SOUS_TITRE
    ws["A2"].alignment = AL_CENTRE
    ws["A4"] = f"Désignation entité : {entite}"
    ws["A4"].font = F_GRAS
    ws["A5"] = f"Numéro d'identification : {identifiant}"
    ws["C4"] = f"Exercice clos le : {exercice}"
    ws["C4"].font = F_GRAS
    ws["C5"] = f"Durée (en mois) : {duree}"
    r = 7
    ws.cell(r, 1, "NOTES")
    ws.cell(r, 2, "INTITULES")
    ws.cell(r, 3, "A (1)")
    ws.cell(r, 4, "N/A (1)")
    style_entetes(ws, r, 1, 4)
    debut = r + 1
    for titre_partie, lignes in parties:
        r += 1
        ws.cell(r, 1, titre_partie)
        ws.cell(r, 1).font = F_SOUS_TITRE
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=4)
        for numero, intitule in lignes:
            r += 1
            ws.cell(r, 1, numero)
            ws.cell(r, 2, intitule)
    style_zone_donnees(ws, debut, r, 1, 4)
    r += 2
    ws.cell(r, 1, note_pied or
            "(1) A : applicable ; N/A : non applicable. Les notes non "
            "documentées ne doivent pas être jointes aux états financiers ; "
            "dans une note, les lignes non chiffrées doivent être supprimées.")
    ws.merge_cells(start_row=r, start_column=1, end_row=r + 1, end_column=4)
    ws.cell(r, 1).alignment = AL_GAUCHE
    largeurs(ws, {"A": 12, "B": 78, "C": 8, "D": 8})
    return ws


def ordonner_feuilles(wb, ordre):
    """Réordonne les feuilles : celles citées dans `ordre` d'abord (dans cet
    ordre), les autres ensuite dans leur ordre actuel."""
    pos = {nom: i for i, nom in enumerate(ordre)}
    base = len(ordre)
    actuels = {ws.title: i for i, ws in enumerate(wb._sheets)}
    wb._sheets.sort(key=lambda w: pos.get(w.title, base + actuels[w.title]))
