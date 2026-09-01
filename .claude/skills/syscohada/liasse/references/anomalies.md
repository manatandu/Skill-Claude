# Anomalies de balance — catalogue et solutions

Le moteur ne se contente pas de monter la liasse : il inspecte la balance et sort une feuille `ANOMALIES` triée par gravité. Rien n'est corrigé en silence ; l'arbitrage revient à l'humain.

## Gravités

- **BLOQUANT** : la liasse ne peut pas boucler. À régler avant tout.
- **A_TRAITER** : la présentation sera fausse ou l'équilibre fuira. À régler avant remise.
- **A_VERIFIER** : plausible mais suspect. À confirmer.
- **MINEUR** : sans effet réel (arrondi).
- **INFO** : information de cadrage.

## Anomalies couvertes

**Balance déséquilibrée** (BLOQUANT). Total des soldes débiteurs ≠ total des soldes créditeurs, au-delà de l'arrondi. Une balance qui ne boucle pas ne peut donner un bilan qui boucle. *Solution :* reprendre la saisie ou l'extraction avant montage.

**Écart d'arrondi** (MINEUR). Déséquilibre inférieur au centime. *Solution :* sans effet, peut être ignoré.

**Compte non affecté** (A_TRAITER). Un solde des classes 1 à 8 que la maquette ne rattache à aucune rubrique. Il fait fuir l'équilibre exactement de son montant net. *Solution :* vérifier le préfixe OHADA du numéro, ou compléter la correspondance pour ce cas.

**Compte non conforme** (A_TRAITER). Classe hors 1-8 (souvent classe 9, comptabilité analytique ou engagements) ou numéro trop court. *Solution :* se référer au libellé, réaffecter au compte OHADA équivalent avant montage.

**Charge (classe 6) au solde créditeur** (A_VERIFIER). *Solution :* contrôler un transfert de charge, une RRR obtenue ou une erreur d'imputation.

**Produit (classe 7) au solde débiteur** (A_VERIFIER). *Solution :* contrôler une RRR accordée, une annulation de produit ou une erreur d'imputation.

**Immobilisation (classe 2 hors 28/29) au solde créditeur** (A_VERIFIER). *Solution :* vérifier une cession non soldée, un avoir sur immobilisation ou une mauvaise ventilation.

**Résultat logé à deux endroits** (A_VERIFIER). Classes 6/7/8 ouvertes ET classe 13 mouvementée : risque de double comptage du résultat. *Solution :* fournir soit une balance avant clôture (6/7/8 ouverts, 13 vide), soit après (13 seul).

**Résultat nul** (INFO). Classes 6/7/8 non mouvementées : le compte de résultat ressortira à zéro. *Solution :* pour un compte de résultat renseigné, fournir la balance avant affectation.

## Articulation du résultat

Le résultat net du bilan (poste CJ) est écrit comme le résultat du compte de résultat (`XI`) augmenté du solde éventuel de la classe 13. Un seul des deux est non nul selon que la balance est avant ou après affectation. La liasse boucle dans les deux cas, sans réglage manuel.

## À enrichir

Pistes pour les versions suivantes : compte d'amortissement (28x) sans immobilisation brute correspondante (et l'inverse) ; TVA déductible et collectée de sens contraire à l'attendu ; comptes de liaison (18x, 47x) non soldés en fin d'exercice ; provision (19x, 29x, 39, 49x, 59x) sans base ; capitaux propres négatifs (alerte de continuité).

## Évolutions v3

- Les postes des états et les lignes calculées des notes sont désormais des
  **formules Excel** (SUMIF sur la feuille BALANCE) : une anomalie de
  correspondance se voit directement dans le classeur, en remontant la
  formule du poste au compte.
- La feuille CONTROLES recoupe chaque note calculée avec son poste (écarts
  « doit être 0 »).
- Sans balance N-1, les notes de mouvements (3A, 3C, 28) portent la clôture
  en colonne d'ouverture : signalé en `INFO`.
- Correction de signe du TFT (FB/FC/FD) : voir
  `tft-formules-praticien.md`, section « Convention de signe ».
- Le SMT a son propre catalogue d'anomalies (`monter_smt.py`) : mêmes
  gravités, plus un rappel `INFO` des seuils d'assujettissement (AUDCIF
  art. 13) et un garde-fou sur les lignes VB/VC (voir `notes-smt.md`).
