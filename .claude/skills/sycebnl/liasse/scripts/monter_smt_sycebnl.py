#!/usr/bin/env python3
"""
monter_smt_sycebnl.py — Monte les états financiers du SYSTÈME MINIMAL DE
TRÉSORERIE du SYCEBNL (Partie 4, ch. 4 du Journal officiel : bilan GA→HZ,
compte de résultat KA→KZC, 5 notes annexes) à partir d'une balance, dans un
classeur professionnel construit de toutes pièces.

    python monter_smt_sycebnl.py balance_N.xlsx [balance_N1.xlsx] \
        --sortie etats-smt-sycebnl.xlsx --entite "..." --identifiant "..." \
        --exercice "31/12/N" --duree 12

Entités visées : petites EBNL sous le seuil de 30 M FCFA de ressources
annuelles (Acte uniforme, art. 5-6) tenant une comptabilité de trésorerie.

Jeu d'états produit :
  - BILAN ACTIF (GA→GZ) et BILAN PASSIF (HA→HZ), une feuille chacun ;
  - COMPTE DE RÉSULTAT (KA→KZC : recettes/dépenses corrigées des variations
    de stocks, créances, dettes et des dotations) ;
  - NOTE 1 (acquisition et suivi des immobilisations), NOTE 2 (état des
    stocks), NOTE 3 (créances et dettes non échues), NOTE 4 (journal unique
    de trésorerie, ventilations officielles), NOTE 5 (dotations) ;
  - GARDE / BALANCE / BALANCE_N1 / CONTROLES / ANOMALIES.

Chaque montant est une FORMULE Excel (SUMIF sur BALANCE / BALANCE_N1) —
correspondance : references/correspondance-smt-sycebnl.tsv (construction du
moteur : le ch. 4 ne publie pas de table de correspondance).
"""

import argparse
import os
import sys

import openpyxl

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from formules_sycebnl import (
    formule_tokens, set_lignes_max,
    F_TITRE, F_SOUS_TITRE, F_ENTETE, F_NORMAL, F_GRAS,
    R_TITRE, R_ENTETE, R_BANDE, R_TOTAL, BORD_FIN, AL_CENTRE, AL_GAUCHE,
    FMT_MONTANT, style_entetes, style_zone_donnees, style_ligne_total,
    largeurs, style_titre,
)
from monter_etats_sycebnl import lire_balance, entete_etat

CR_NOM = "COMPTE DE RESULTAT"


def _c(f):
    return f[1:] if f and f.startswith("=") else (f or "0")


def _tok(s):
    return [t.strip() for t in s.split(",") if t.strip()]


def f_actif(ref, bal):
    if ref == "GA":
        return formule_tokens(_tok("2"), "nd", bal)
    if ref == "GB":
        return formule_tokens(_tok("3"), "nd", bal)
    if ref == "GC":
        deb4 = _c(formule_tokens(_tok("4"), "d", bal))
        dep = _c(formule_tokens(_tok("49,590,591"), "c", bal))
        titres = _c(formule_tokens(_tok("50,51"), "nd", bal))
        return f"={deb4}-({dep})+({titres})"
    if ref == "GD":
        return formule_tokens(_tok("57"), "nd", bal)
    if ref == "GE":
        banques = _c(formule_tokens(_tok("52,53,55,56,58"), "nd", bal))
        dep = _c(formule_tokens(_tok("592,593,595"), "c", bal))
        return f"={banques}-({dep})"
    return None


def f_passif(ref, bal, kzc_row):
    if ref == "HA":
        return formule_tokens(_tok("10"), "nc", bal)
    if ref == "HB":
        f13 = _c(formule_tokens(_tok("13"), "nc", bal))
        col = "D" if bal == "BALANCE" else "E"
        return f"='{CR_NOM}'!{col}{kzc_row}+({f13})"
    if ref == "HC":
        return formule_tokens(_tok("11,12,14,15,16,17,18,19"), "nc", bal)
    if ref == "HD":
        cred4 = _c(formule_tokens(_tok("4"), "c", bal, exclude=_tok("49")))
        p599 = _c(formule_tokens(_tok("599"), "nc", bal))
        return f"={cred4}+({p599})"
    return None


CR_LIGNES = [
    ("KA", "Revenus encaissés", "70", "nc", "4", False),
    ("KB", "Autres recettes sur activités",
     "71,72,75,77,78,79,82,84,86,88", "nc", "4", False),
    ("KX", "TOTAL DES REVENUS ENCAISSÉS (A)", None, None, "", True),
    ("JA", "Dépenses sur achats", "60!603", "nd", "4", False),
    ("JB", "Dépenses sur loyers", "622", "nd", "4", False),
    ("JC", "Dépenses sur salaires", "66", "nd", "4", False),
    ("JD", "Dépenses sur impôts et taxes", "64", "nd", "4", False),
    ("JE", "Charges d'intérêts", "67", "nd", "4", False),
    ("JF", "Autres dépenses sur activités", "61,62!622,63,65,81,83,87",
     "nd", "4", False),
    ("JX", "TOTAL DÉPENSES SUR CHARGES (B)", None, None, "", True),
    ("KZ", "SOLDE : excédent (+) ou insuffisance (-) de recettes (C = A - B)",
     None, None, "", True),
    ("VA", "+ Variations des stocks sur les achats [N - (N-1)]",
     None, None, "2", False),
    ("VB", "+ Variation des créances [N - (N-1)] — à saisir depuis la Note 3",
     None, None, "3", False),
    ("VC", "- Variation des dettes d'exploitation [N - (N-1)] — à saisir "
           "depuis la Note 3", None, None, "3", False),
    ("JG", "DOTATIONS AUX AMORTISSEMENTS", "68,69,85", "nd", "", False),
    ("KZC", "RÉSULTAT NET DE L'EXERCICE", None, None, "", True),
]


def construire_cr(wb, avec_n1, ident):
    ws = wb.create_sheet(CR_NOM)
    entete_etat(ws, "COMPTE DE RÉSULTAT — SMT",
                "SYCEBNL, Système minimal de trésorerie (Partie 4, ch. 4)",
                ident, 5)
    r = 7
    for i, h in enumerate(["REF", "LIBELLÉS", "Note", "Exercice N",
                           "Exercice N-1"], start=1):
        ws.cell(r, i, h)
    style_entetes(ws, r, 1, 5)
    rows = {}
    for ref, lib, jetons, mode, note, total in CR_LIGNES:
        r += 1
        rows[ref] = r
        ws.cell(r, 1, ref)
        ws.cell(r, 2, lib)
        ws.cell(r, 3, note)
        if jetons:
            inc, exc = (jetons.split("!") + [""])[:2]
            for col, bal, actif in ((4, "BALANCE", True),
                                    (5, "BALANCE_N1", avec_n1)):
                if actif:
                    ws.cell(r, col).value = formule_tokens(
                        _tok(inc), mode, bal, exclude=_tok(exc))
        if total:
            style_ligne_total(ws, r, 1, 5, cols_montant=(4, 5))

    def pose(ref, fN, fN1):
        ws.cell(rows[ref], 4).value = fN
        if avec_n1:
            ws.cell(rows[ref], 5).value = fN1

    pose("KX", f"=D{rows['KA']}+D{rows['KB']}", f"=E{rows['KA']}+E{rows['KB']}")
    jd = "+".join(f"D{rows[x]}" for x in ("JA", "JB", "JC", "JD", "JE", "JF"))
    je = "+".join(f"E{rows[x]}" for x in ("JA", "JB", "JC", "JD", "JE", "JF"))
    pose("JX", f"={jd}", f"={je}")
    pose("KZ", f"=D{rows['KX']}-D{rows['JX']}", f"=E{rows['KX']}-E{rows['JX']}")
    if avec_n1:
        s_n = _c(formule_tokens(_tok("3"), "nd", "BALANCE"))
        s_n1 = _c(formule_tokens(_tok("3"), "nd", "BALANCE_N1"))
        ws.cell(rows["VA"], 4).value = f"=({s_n})-({s_n1})"
    else:
        v603 = _c(formule_tokens(_tok("603"), "nc", "BALANCE"))
        v73 = _c(formule_tokens(_tok("73"), "nc", "BALANCE"))
        ws.cell(rows["VA"], 4).value = f"=({v603})+({v73})"
    ws.cell(rows["VB"], 4).value = 0
    ws.cell(rows["VC"], 4).value = 0
    pose("KZC",
         f"=D{rows['KZ']}+D{rows['VA']}+D{rows['VB']}-D{rows['VC']}-D{rows['JG']}",
         f"=E{rows['KZ']}+E{rows['VA']}+E{rows['VB']}-E{rows['VC']}-E{rows['JG']}")
    style_zone_donnees(ws, 8, r, 1, 5, cols_montant=(4, 5))
    for ref in ("KX", "JX", "KZ", "KZC"):
        style_ligne_total(ws, rows[ref], 1, 5, cols_montant=(4, 5))
    r += 2
    ws.cell(r, 1, "Les variations de créances (VB) et de dettes (VC) se "
                  "saisissent depuis l'état extra-comptable de la Note 3 ; si "
                  "la balance porte une classe 4 mouvementée (base "
                  "engagement), les laisser à zéro.")
    largeurs(ws, {"A": 7, "B": 62, "C": 7, "D": 17, "E": 17})
    return rows


def construire_bilan(wb, avec_n1, ident, kzc_row):
    lignes_a = [("GA", "Immobilisations (1)", "1"),
                ("GB", "Stocks", "2"),
                ("GC", "Adhérents, clients-usagers et autres débiteurs", "3"),
                ("GD", "Caisse", "4"),
                ("GE", "Banque (en + ou en -)", "4")]
    lignes_p = [("HA", "Dotations", "5"),
                ("HB", "Résultat net de l'exercice (en + ou en -)", ""),
                ("HC", "Autres fonds propres", ""),
                ("HD", "Fournisseurs et autres créditeurs", "3")]
    for nom, lignes, total_ref, total_lab, f_poste in (
            ("BILAN ACTIF", lignes_a, "GZ", "Total actif", f_actif),
            ("BILAN PASSIF", lignes_p, "HZ", "Total passif",
             lambda ref, bal: f_passif(ref, bal, kzc_row))):
        ws = wb.create_sheet(nom)
        entete_etat(ws, f"BILAN SMT — {'ACTIF' if 'ACTIF' in nom else 'PASSIF'}",
                    "SYCEBNL, Système minimal de trésorerie (Partie 4, ch. 4)",
                    ident, 5)
        r = 7
        ws.cell(r, 1, "REF")
        ws.cell(r, 2, nom.split()[1])
        ws.cell(r, 3, "Note")
        ws.cell(r, 4, "Exercice N")
        ws.cell(r, 5, "Exercice N-1")
        style_entetes(ws, r, 1, 5)
        premiere = r + 1
        for ref, lib, note in lignes:
            r += 1
            ws.cell(r, 1, ref)
            ws.cell(r, 2, lib)
            ws.cell(r, 3, note)
            ws.cell(r, 4).value = f_poste(ref, "BALANCE")
            if avec_n1:
                ws.cell(r, 5).value = f_poste(ref, "BALANCE_N1")
        r += 1
        ws.cell(r, 1, total_ref)
        ws.cell(r, 2, total_lab)
        ws.cell(r, 4).value = f"=SUM(D{premiere}:D{r-1})"
        if avec_n1:
            ws.cell(r, 5).value = f"=SUM(E{premiere}:E{r-1})"
        style_zone_donnees(ws, premiere, r - 1, 1, 5, cols_montant=(4, 5))
        style_ligne_total(ws, r, 1, 5, cols_montant=(4, 5))
        r += 2
        ws.cell(r, 1, "(1) à faire figurer sur l'état de situation si "
                      "montants significatifs (Partie 4, ch. 4)."
                if "ACTIF" in nom else
                "Autres fonds propres : réserves, report à nouveau, "
                "subventions, fonds affectés/reportés, emprunts et "
                "provisions (le modèle SMT ne les distingue pas).")
        largeurs(ws, {"A": 8, "B": 52, "C": 8, "D": 18, "E": 18})


def construire_note1(wb, bal, ident):
    ws = wb.create_sheet("NOTE 1 IMMOBILISATIONS")
    entete_etat(ws, "NOTE 1 — TABLEAU D'ACQUISITION ET DE SUIVI DU MATÉRIEL, "
                    "DU MOBILIER ET AUTRES IMMOBILISATIONS", "", ident, 7)
    r = 7
    for i, h in enumerate(["Date", "Désignation", "Montant",
                           "Date d'acquisition", "Durée d'utilité",
                           "Date de sortie", "Prix de cession"], start=1):
        ws.cell(r, i, h)
    style_entetes(ws, r, 1, 7)
    premiere = r + 1
    for l in bal:
        c = l["compte"]
        if c.startswith("2") and not c.startswith(("28", "29")) \
                and abs(l["sd"] - l["sc"]) > 0.005:
            r += 1
            ws.cell(r, 2, f"{c} — {l['libelle']}")
            ws.cell(r, 3).value = formule_tokens([c], "nd", "BALANCE")
    r += 1
    ws.cell(r, 2, "TOTAL IMMOBILISATIONS BRUTES")
    ws.cell(r, 3).value = (f"=SUM(C{premiere}:C{r-1})" if r > premiere else 0)
    r += 1
    ws.cell(r, 2, "Amortissements et dépréciations cumulés (28/29)")
    ws.cell(r, 3).value = formule_tokens(_tok("28,29"), "nc", "BALANCE")
    r += 1
    ws.cell(r, 2, "VALEUR NETTE (= poste GA du bilan)")
    ws.cell(r, 3).value = f"=C{r-2}-C{r-1}"
    style_zone_donnees(ws, premiere, r, 1, 7, cols_montant=(3, 7))
    style_ligne_total(ws, r, 1, 7, cols_montant=(3,))
    largeurs(ws, {"A": 11, "B": 48, "C": 15, "D": 15, "E": 13, "F": 13, "G": 15})


def construire_note2(wb, bal, avec_n1, ident):
    ws = wb.create_sheet("NOTE 2 STOCKS")
    entete_etat(ws, "NOTE 2 — ÉTAT DES STOCKS", "", ident, 5)
    r = 7
    for i, h in enumerate(["Référence", "Désignation", "Quantité",
                           "Prix unitaire", "Montant"], start=1):
        ws.cell(r, i, h)
    style_entetes(ws, r, 1, 5)
    premiere = r + 1
    for l in bal:
        if l["compte"].startswith("3") and not l["compte"].startswith("39") \
                and abs(l["sd"] - l["sc"]) > 0.005:
            r += 1
            ws.cell(r, 1, l["compte"])
            ws.cell(r, 2, l["libelle"])
            ws.cell(r, 5).value = formule_tokens([l["compte"]], "nd", "BALANCE")
    r += 3
    ws.cell(r, 2, "VALEUR DU STOCK FINAL")
    ws.cell(r, 5).value = formule_tokens(_tok("3"), "nd", "BALANCE")
    style_ligne_total(ws, r, 1, 5, cols_montant=(5,))
    r += 1
    ws.cell(r, 2, "VALEUR DU STOCK INITIAL")
    ws.cell(r, 5).value = (formule_tokens(_tok("3"), "nd", "BALANCE_N1")
                           if avec_n1 else 0)
    style_ligne_total(ws, r, 1, 5, cols_montant=(5,))
    style_zone_donnees(ws, premiere, r - 4, 1, 5, cols_montant=(5,))
    largeurs(ws, {"A": 12, "B": 46, "C": 12, "D": 14, "E": 16})


def construire_note3(wb, avec_n1, ident):
    ws = wb.create_sheet("NOTE 3 CREANCES-DETTES")
    entete_etat(ws, "NOTE 3 — ÉTAT DES CRÉANCES ET DES DETTES NON ÉCHUES",
                "Inventaire extra-comptable au 31 décembre", ident, 6)
    r = 7
    for bloc, mode in (("CRÉANCES — nom des clients-usagers et autres débiteurs", "d"),
                       ("DETTES — nom des fournisseurs et autres créditeurs", "c")):
        ws.cell(r, 1, bloc)
        ws.cell(r, 1).font = F_SOUS_TITRE
        r += 1
        for i, h in enumerate(["Date", "Nom", "Montant au 31/12/N",
                               "Montant au 01/01/N", "Variation en valeur",
                               "Variation en %"], start=1):
            ws.cell(r, i, h)
        style_entetes(ws, r, 1, 6)
        premiere = r + 1
        for _ in range(6):
            r += 1
            ws.cell(r, 5).value = f"=C{r}-D{r}"
            ws.cell(r, 6).value = f"=IF(D{r}=0,\"\",(C{r}-D{r})/D{r})"
        r += 1
        ws.cell(r, 2, "TOTAL DES " + ("CRÉANCES" if mode == "d" else "DETTES"))
        for col in "CDE":
            ws[f"{col}{r}"] = f"=SUM({col}{premiere}:{col}{r-1})"
        style_ligne_total(ws, r, 1, 6, cols_montant=(3, 4, 5))
        style_zone_donnees(ws, premiere, r - 1, 1, 6, cols_montant=(3, 4, 5))
        r += 1
        f_n = _c(formule_tokens(_tok("4"), mode, "BALANCE"))
        f_n1 = (_c(formule_tokens(_tok("4"), mode, "BALANCE_N1"))
                if avec_n1 else "0")
        ws.cell(r, 2, "Rappel balance (classe 4, soldes "
                      + ("débiteurs" if mode == "d" else "créditeurs")
                      + ") — contrôle")
        ws.cell(r, 3).value = f"={f_n}"
        ws.cell(r, 4).value = f"={f_n1}"
        ws.cell(r, 3).number_format = FMT_MONTANT
        ws.cell(r, 4).number_format = FMT_MONTANT
        r += 3
    ws.cell(r, 1, "Reporter la variation des créances en VB et celle des "
                  "dettes en VC du compte de résultat.")
    largeurs(ws, {"A": 12, "B": 40, "C": 18, "D": 18, "E": 16, "F": 12})


def construire_note4(wb, ident):
    ws = wb.create_sheet("NOTE 4 JOURNAL TRESORERIE")
    entete_etat(ws, "NOTE 4 — JOURNAL UNIQUE DE TRÉSORERIE",
                "Un journal par banque et un pour la caisse ; regroupement "
                "mensuel possible (Partie 4, ch. 4)", ident, 11)
    r = 7
    entetes = ["Dates", "Libellés", "Recettes", "Dépenses", "Solde",
               "Vent. recettes : Cotisations", "Subventions", "Autres",
               "Vent. dépenses : Achats de biens liés à l'activité",
               "Autres achats / Transport / Services extérieurs",
               "Salaires / Autres"]
    for i, h in enumerate(entetes, start=1):
        ws.cell(r, i, h)
    style_entetes(ws, r, 1, 11)
    r += 1
    ws.cell(r, 2, "Report à nouveau")
    for _ in range(14):
        r += 1
        ws.cell(r, 5).value = f"=E{r-1}+C{r}-D{r}"
    r += 1
    ws.cell(r, 2, "Solde à reporter")
    ws.cell(r, 5).value = f"=E{r-1}"
    style_zone_donnees(ws, 8, r, 1, 11,
                       cols_montant=(3, 4, 5, 6, 7, 8, 9, 10, 11))
    style_ligne_total(ws, r, 1, 11, cols_montant=(5,))
    largeurs(ws, {"A": 11, "B": 32, "C": 13, "D": 13, "E": 13, "F": 14,
                  "G": 13, "H": 11, "I": 18, "J": 20, "K": 14})


def construire_note5(wb, ident):
    ws = wb.create_sheet("NOTE 5 DOTATIONS")
    entete_etat(ws, "NOTE 5 — DOTATION",
                "Nom et prénoms des membres | Nationalité | Montant | Avec ou "
                "sans droit d'entrée", ident, 4)
    r = 7
    for i, h in enumerate(["Nom et prénoms des membres", "Nationalité",
                           "Montant", "Avec / sans droit d'entrée"], start=1):
        ws.cell(r, i, h)
    style_entetes(ws, r, 1, 4)
    blocs = [("Dotation non consomptible", "101,102"),
             ("Droit d'entrée", "103"),
             ("Dotation consomptible", "104")]
    data = []
    for lab, expr in blocs:
        r += 1
        ws.cell(r, 1, lab + " — rappel balance")
        ws.cell(r, 1).font = F_GRAS
        ws.cell(r, 3).value = formule_tokens(_tok(expr), "nc", "BALANCE")
        ws.cell(r, 3).number_format = FMT_MONTANT
        data.append(r)
        for _ in range(3):
            r += 1
    r += 1
    ws.cell(r, 1, "TOTAL")
    ws.cell(r, 3).value = "=" + "+".join(f"C{d}" for d in data)
    style_ligne_total(ws, r, 1, 4, cols_montant=(3,))
    style_zone_donnees(ws, 8, r - 1, 1, 4, cols_montant=(3,))
    largeurs(ws, {"A": 44, "B": 16, "C": 16, "D": 24})


def ecrire_balance_smt(wb, nom, bal):
    b = wb.create_sheet(nom)
    entetes = ["Compte", "Intitulé", "Préfixe 2", "Préfixe 3", "Préfixe 4",
               "Solde final débit", "Solde final crédit"]
    b.append(entetes)
    style_entetes(b, 1, 1, len(entetes))
    for l in bal:
        c = l["compte"]
        b.append([c, l["libelle"], c[:2], c[:3], c[:4],
                  round(l["sd"], 2), round(l["sc"], 2)])
    style_zone_donnees(b, 2, b.max_row, 1, len(entetes), cols_montant=(6, 7))
    largeurs(b, {"A": 12, "B": 42, "C": 9, "D": 9, "E": 9, "F": 15, "G": 15})
    b.freeze_panes = "A2"


def detecter_anomalies_smt(bal, seuil=1.0):
    a = []
    sd = sum(l["sd"] for l in bal)
    sc = sum(l["sc"] for l in bal)
    if abs(sd - sc) > seuil:
        a.append({"gravite": "BLOQUANT", "compte": "", "libelle": "Balance entière",
                  "probleme": f"Balance déséquilibrée : débit {sd:,.2f} ≠ crédit {sc:,.2f}",
                  "solution": "Reprendre la saisie avant montage."})
    for l in bal:
        c, net = l["compte"], l["sd"] - l["sc"]
        if abs(net) <= seuil:
            continue
        cl = c[0] if c else ""
        if len(c) < 2 or cl not in "123456789":
            a.append({"gravite": "A_TRAITER", "compte": c, "libelle": l["libelle"],
                      "probleme": f"Compte non conforme au plan SYCEBNL (classe '{cl}').",
                      "solution": "Réaffecter au compte équivalent avant montage."})
        if cl == "9":
            a.append({"gravite": "INFO", "compte": c, "libelle": l["libelle"],
                      "probleme": "Compte de classe 9 (contributions volontaires en nature).",
                      "solution": "Hors bilan et hors compte de résultat par construction."})
    if any(l["compte"].startswith("4") and abs(l["sd"] - l["sc"]) > seuil for l in bal):
        a.append({"gravite": "INFO", "compte": "", "libelle": "Classe 4",
                  "probleme": "La balance porte des comptes de tiers : recettes/dépenses "
                              "incluent des montants non encaissés/décaissés (base engagement).",
                  "solution": "Laisser VB/VC à zéro dans ce cas ; ne les servir que pour "
                              "une balance de trésorerie pure (Note 3)."})
    a.append({"gravite": "INFO", "compte": "", "libelle": "SMT — seuil",
              "probleme": "Vérifier l'assujettissement : ressources annuelles ≤ 30 M FCFA "
                          "(Acte uniforme SYCEBNL, art. 5-6).",
              "solution": "Au-delà, monter le jeu du Système normal "
                          "(monter_etats_sycebnl.py) ou des projets (monter_projets.py)."})
    return a


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("balance_N")
    ap.add_argument("balance_N1", nargs="?")
    ap.add_argument("--sortie", default="etats-smt-sycebnl.xlsx")
    ap.add_argument("--entite", default="")
    ap.add_argument("--identifiant", default="")
    ap.add_argument("--exercice", default="")
    ap.add_argument("--duree", default="12")
    args = ap.parse_args()

    bal, idx = lire_balance(args.balance_N)
    print(f"Balance N : {len(bal)} comptes. Colonnes repérées : {idx}")
    bal1 = None
    if args.balance_N1:
        bal1, _ = lire_balance(args.balance_N1)
        print(f"Balance N-1 : {len(bal1)} comptes.")
    avec_n1 = bal1 is not None
    set_lignes_max(max(len(bal), len(bal1 or [])) + 20)

    ident = (args.entite, args.identifiant, args.exercice, args.duree)
    wb = openpyxl.Workbook()
    wb.remove(wb.active)

    cr_rows = construire_cr(wb, avec_n1, ident)
    construire_bilan(wb, avec_n1, ident, cr_rows["KZC"])
    ordre = ["BILAN ACTIF", "BILAN PASSIF", CR_NOM]
    wb._sheets.sort(key=lambda w: ordre.index(w.title) if w.title in ordre else 99)

    construire_note1(wb, bal, ident)
    construire_note2(wb, bal, avec_n1, ident)
    construire_note3(wb, avec_n1, ident)
    construire_note4(wb, ident)
    construire_note5(wb, ident)

    ecrire_balance_smt(wb, "BALANCE", bal)
    if avec_n1:
        ecrire_balance_smt(wb, "BALANCE_N1", bal1)

    ctl = wb.create_sheet("CONTROLES")
    n = len(bal)
    ctl.append(["Contrôle", "Valeur", "Attendu"])
    style_entetes(ctl, 1, 1, 3)
    for lab, f, att in [
            ("Total solde débit balance", f"=SUM(BALANCE!F2:F{n+1})", ""),
            ("Total solde crédit balance", f"=SUM(BALANCE!G2:G{n+1})", ""),
            ("Écart balance (doit être 0)", "=B2-B3", 0),
            ("Total actif (GZ)", "='BILAN ACTIF'!D13", ""),
            ("Total passif (HZ)", "='BILAN PASSIF'!D12", ""),
            ("Écart actif - passif (doit être 0)", "=B5-B6", 0),
            ("Résultat net (compte de résultat, KZC)",
             f"='{CR_NOM}'!D{cr_rows['KZC']}", "")]:
        ctl.append([lab, f, att])
    style_zone_donnees(ctl, 2, ctl.max_row, 1, 3, cols_montant=(2,))
    largeurs(ctl, {"A": 56, "B": 20, "C": 10})

    anomalies = detecter_anomalies_smt(bal)
    an = wb.create_sheet("ANOMALIES")
    an.append(["Gravité", "Compte", "Intitulé", "Problème", "Solution proposée"])
    style_entetes(an, 1, 1, 5)
    ordre_g = {"BLOQUANT": 0, "A_TRAITER": 1, "A_VERIFIER": 2, "MINEUR": 3, "INFO": 4}
    for x in sorted(anomalies, key=lambda z: ordre_g.get(z["gravite"], 9)):
        an.append([x["gravite"], x["compte"], x["libelle"], x["probleme"], x["solution"]])
    style_zone_donnees(an, 2, max(an.max_row, 2), 1, 5)
    largeurs(an, {"A": 12, "B": 12, "C": 26, "D": 62, "E": 62})

    g = wb.create_sheet("GARDE", 0)
    g.sheet_view.showGridLines = False
    style_titre(g, "B2:F3", "ÉTATS FINANCIERS ANNUELS — SYCEBNL")
    g.merge_cells("B4:F4")
    g["B4"] = "SYSTÈME MINIMAL DE TRÉSORERIE (Partie 4, ch. 4)"
    g["B4"].font = F_SOUS_TITRE
    g["B4"].alignment = AL_CENTRE
    r = 6
    for lab, v in [("Désignation de l'entité", args.entite or "—"),
                   ("Numéro d'identification", args.identifiant or "—"),
                   ("Exercice clos le", args.exercice or "—"),
                   ("Durée de l'exercice (mois)", args.duree or "12"),
                   ("Balance N-1 fournie", "Oui" if avec_n1 else "Non")]:
        g[f"B{r}"] = lab
        g[f"B{r}"].font = F_GRAS
        g[f"D{r}"] = v
        r += 1
    r += 1
    for s in ["Bilan (GA→GZ / HA→HZ), une feuille par volet",
              "Compte de résultat (KA→KZC)",
              "Notes annexes 1 à 5",
              "Feuilles d'audit : BALANCE, BALANCE_N1, CONTROLES, ANOMALIES"]:
        g[f"B{r}"] = "• " + s
        r += 1
    largeurs(g, {"A": 3, "B": 38, "C": 12, "D": 26, "E": 14, "F": 14})

    wb.save(args.sortie)
    print(f"États SMT SYCEBNL écrits : {args.sortie}")
    bloquants = [a for a in anomalies if a["gravite"] in ("BLOQUANT", "A_TRAITER")]
    print(f"Anomalies : {len(anomalies)} dont {len(bloquants)} à traiter avant remise.")


if __name__ == "__main__":
    main()
