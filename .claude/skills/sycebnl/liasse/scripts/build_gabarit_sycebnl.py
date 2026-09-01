#!/usr/bin/env python3
"""
build_gabarit_sycebnl.py — (Re)génère le gabarit Excel VIERGE du jeu d'états
des associations et ordres professionnels (assets/gabarit-etats-associations
.xlsx) : mêmes feuilles, mêmes formules et même présentation que le classeur
produit par monter_etats_sycebnl.py, mais avec des feuilles BALANCE /
BALANCE_N1 vides — utile comme modèle à consulter ou à remplir à la main.

    python build_gabarit_sycebnl.py

Il n'existe pas de fichier Excel officiel du SYCEBNL (seuls des tableaux
scannés ont été publiés au Journal officiel) : ce gabarit est une
construction, bâtie strictement sur les libellés et codes REF officiels
(Partie 4, ch. 2) et sur la maquette references/correspondance-associations
.tsv. Relancer ce script écrase le fichier existant.
"""

import os
import sys

import openpyxl

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_mapping_sycebnl import charger_maquette
from formules_sycebnl import formule_tokens
import monter_etats_sycebnl as m
import notes_sycebnl

ICI = os.path.dirname(os.path.abspath(__file__))
CORRESPONDANCE = os.path.join(ICI, "..", "references",
                              "correspondance-associations.tsv")
SORTIE = os.path.join(ICI, "..", "assets", "gabarit-etats-associations.xlsx")


def main():
    rubs = charger_maquette(CORRESPONDANCE)
    ident = ("", "", "", "12")
    avec_n1 = True

    wb = openpyxl.Workbook()
    wb.remove(wb.active)

    actif_rubs = [(ref, r) for ref, r in rubs.items() if r.etat == "BILAN-ACTIF"]
    passif_rubs = [(ref, r) for ref, r in rubs.items() if r.etat == "BILAN-PASSIF"]
    cr_rubs = [(ref, r) for ref, r in rubs.items() if r.etat == "COMPTE-DE-RESULTAT"]

    refs = {}
    refs["ACTIF"] = m.construire_etat(wb, "ACTIF", "BILAN — ACTIF",
                                      actif_rubs, rubs, avec_n1, ident, True)
    refs["PASSIF"] = m.construire_etat(wb, "PASSIF", "BILAN — PASSIF",
                                       passif_rubs, rubs, avec_n1, ident, False)
    refs["CR"] = m.construire_etat(wb, m.CR_NOM, "COMPTE DE RÉSULTAT",
                                   cr_rubs, rubs, avec_n1, ident, False)
    refs["TFT"] = m.construire_tft(wb, rubs, avec_n1, ident)

    P = wb["PASSIF"]
    row_ch, row_xe = refs["PASSIF"]["CH"], refs["CR"]["XE"]
    f13 = formule_tokens(["13"], "nc", "BALANCE")[1:]
    P.cell(row_ch, 4).value = f"='{m.CR_NOM}'!D{row_xe}+({f13})"
    f13b = formule_tokens(["13"], "nc", "BALANCE_N1")[1:]
    P.cell(row_ch, 5).value = f"='{m.CR_NOM}'!E{row_xe}+({f13b})"

    controles = notes_sycebnl.construire_notes(wb, avec_n1, ident, refs)
    m.ecrire_balance(wb, "BALANCE", [], rubs)
    m.ecrire_balance(wb, "BALANCE_N1", [], rubs)
    m.construire_controles(wb, [], refs, controles, avec_n1)
    m.construire_garde(wb, ident, avec_n1)

    os.makedirs(os.path.dirname(SORTIE), exist_ok=True)
    wb.save(SORTIE)
    print(f"Gabarit vierge écrit : {SORTIE} ({len(wb.sheetnames)} feuilles)")


if __name__ == "__main__":
    main()
