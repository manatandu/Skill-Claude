# Notes annexes du Système minimal de trésorerie (SYSCOHADA) — couverture du moteur

**Source : AUDCIF, Titre X, chapitres 1 à 3** (transcrit dans le skill
`audcif-acte-uniforme`, `references/titre-10-systeme-minimal-tresorerie.md`).
Le jeu d'états du SMT = Bilan + Compte de résultat + Notes annexes — **pas de
TFT** (propre au Système normal). Ne jamais servir les 36 notes du Titre IX à
une entité au SMT, ni l'inverse.

## Assujettissement

Entités dont le CA annuel HT ne dépasse pas les seuils de l'**article 13
AUDCIF** : négoce 60 M, artisanat et assimilées 40 M, services 30 M FCFA —
sauf option pour le Système normal. Le moteur le rappelle en `INFO` dans
`ANOMALIES` ; l'arbitrage revient à l'humain.

## Les notes et ce que le moteur en remplit

| Note | Intitulé officiel | Couverture du moteur (`monter_smt.py`) |
|---|---|---|
| NOTE 1 | Tableau SMT de suivi du matériel, du mobilier et des cautions | Pré-alimentée : une ligne par compte de classe 2 de la balance (formule SUMIF), total brut, cumul 28/29, valeur nette recoupant le poste Immobilisations du bilan. Dates, durées et cessions à compléter depuis le registre. |
| NOTE 2 | État des stocks | Lignes par compte de classe 3 (formules), VALEUR DU STOCK FINAL (classe 3 N), STOCK INITIAL (classe 3 N-1 si fournie), variation reportable en ligne D du compte de résultat. Le détail article/quantité/PU reste à saisir. |
| NOTE 3 | État des créances et des dettes non échues | Gabarit de saisie (l'inventaire extra-comptable fait foi) + lignes « rappel balance » en formules (classe 4 débiteurs / créditeurs) pour le recoupement. Les totaux alimentent VB/VC du compte de résultat. |
| NOTE 4 | Journal de trésorerie SMT | Gabarit (report à nouveau, colonnes recettes/dépenses/solde en formules de cumul, ventilations officielles). Un journal par banque + un pour la caisse. |
| — | Journaux de suivi des créances impayées / dettes à payer | Gabarits de saisie avec totaux en formules (pièces de base de la fiabilité, Titre X ch. 1). |

## Particularités du SMT respectées

- **Amortissement linéaire sans prorata temporis** (Titre X ch. 1) — rappelé
  sur la NOTE 1 ; le moteur ne calcule pas de dotation (elle vient du registre).
- **Banque (en + ou en –)** : pas de poste banques créditrices au passif — un
  découvert vient en moins de l'actif. La formule du poste laisse le signe
  s'exprimer.
- **Immobilisations à l'actif seulement si significatives** : renvoi (1)
  reproduit sur la feuille BILAN ACTIF.
- **Résultat** : `G = C – D + E – F`. Les lettres D/E ne sont pas attribuées
  explicitement dans le texte officiel `[texte officiel]` ; le moteur retient
  la lecture économique (résultat = solde de trésorerie + Δ stocks +
  Δ créances – Δ dettes – dotations), identique au modèle SMT du SYCEBNL.
- **VB / VC (variations créances/dettes)** : cellules de saisie, jamais
  calculées depuis la balance — l'information vit dans l'inventaire
  extra-comptable (NOTE 3). Si la balance porte une classe 4 mouvementée
  (base engagement), une anomalie `INFO` explique pourquoi VB/VC doivent
  alors rester à zéro.

## Correspondance compte → poste

Il n'existe **pas de table officielle** de correspondance pour le SMT : celle
du moteur (`correspondance-smt.tsv`) est une construction documentée ligne à
ligne, bâtie sur le plan de comptes SYSCOHADA (chaque numéro vérifié dans
`comptes/references/plan-comptes.tsv`). Points d'attention :

- classe 2 en **net** (le bilan SMT n'a pas de colonne amortissements) ;
- dépréciations de tiers (49) et de titres (590/591) en moins des créances,
  jamais en dettes ; 599 (provisions à caractère financier) en créditeurs ;
- 603 et 73 reclassés de leurs lignes d'achats/recettes vers la ligne
  « variation des stocks » pour éviter le double compte avec l'état des stocks ;
- l'impôt sur le résultat (89) rattaché à « Dépenses sur impôts et taxes »,
  seule ligne fiscale du modèle.
