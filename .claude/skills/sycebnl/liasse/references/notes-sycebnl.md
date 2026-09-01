# Notes annexes SYCEBNL (associations et ordres professionnels) — liste officielle et couverture

**Source : Journal officiel OHADA n° spécial du 22 février 2023, Partie 4, chapitre 2, section 4 (fiche récapitulative des notes annexes).**

L'annexe normalisée pour les associations et ordres professionnels va de la **Note 1 à la Note 35**. La numérotation n'est pas continue à deux endroits : la note 5 se subdivise de **5A à 5H** et la note 29 de **29A à 29B**.

## Liste officielle

| Note | Intitulé officiel | Statut |
|---|---|---|
| 1 | Dettes garanties par des sûretés réelles, engagements financiers et contributions volontaires en nature | Soldes + déclaratif |
| 2 | Informations obligatoires | Déclaratif |
| 3 | Evénements postérieurs à la clôture de l'exercice | Déclaratif |
| 4 | Changements de méthodes comptables, d'estimations et corrections d'erreurs | Déclaratif |
| 5A | Dons et legs d'immobilisations non reçus destinés à la vente et usufruit temporaire | Mouvements |
| 5B | Immobilisations brutes | Mouvements |
| 5C | Biens pris en location-acquisition | Mouvements |
| 5D | Dons et legs d'immobilisations non reçus... (amortissements et dépréciations) | Mouvements |
| 5E | Immobilisations : Amortissements | Mouvements |
| 5F | Immobilisations : Dépréciations | Mouvements |
| 5G | Immobilisations : Plus-values et moins-values de cession | Mouvements |
| 5H | Informations sur les réévaluations effectuées par l'entité | Déclaratif |
| 6 | Immobilisations financières | Soldes |
| 7 | Actif circulant et dettes circulantes HAO | Soldes |
| 8 | Stocks et encours | Soldes |
| 9 | Adhérents, clients-usagers | Soldes |
| 10 | Autres créances | Soldes |
| 11 | Titres de placement | Soldes |
| 12 | Valeurs à encaisser | Soldes |
| 13 | Disponibilités | Soldes |
| 14 | Ecarts de conversion | Soldes |
| 15 | Dotation | Soldes |
| 16 | Réserves | Soldes |
| 17A | Subventions et provisions réglementées | Soldes + mouvements |
| 17B | Fonds affectés et reportés | Soldes + mouvements |
| 18A | Dettes financières et ressources assimilées | Mouvements |
| 18B | Actifs et passifs éventuels | Déclaratif |
| 19 | Fournisseurs d'exploitation | Soldes |
| 20 | Dettes fiscales et sociales | Soldes |
| 21 | Autres dettes et provisions pour risques et charges à court terme | Soldes |
| 22 | Banques, crédit d'escompte et de trésorerie | Soldes |
| 23 | Revenus et autres produits | Soldes |
| 24 | Achats | Soldes |
| 25 | Transports | Soldes |
| 26 | Services extérieurs | Soldes |
| 27 | Impôts et taxes | Soldes |
| 28 | Autres charges | Soldes |
| 29A | Charges de personnel | Soldes |
| 29B | Effectifs, masse salariale et personnel extérieur | Déclaratif |
| 30 | Dotations et charges pour provisions et dépréciations | Mouvements |
| 31 | Charges et revenus financiers | Soldes |
| 32 | Autres charges et produits HAO | Soldes |
| 33 | Fiche de synthèse des principaux indicateurs financiers | Calculé |
| 34 | Liste des informations sociales, environnementales et sociétales | Déclaratif |
| 35 | Tableau d'exécution budgétaire | Déclaratif + mouvements |

*(1) les Notes non documentées ne doivent pas être jointes aux états financiers ; les lignes non chiffrées d'une note doivent être supprimées.*

## Trois statuts, même lecture que le skill syscohada

- **Soldes** : ventilation de soldes de la balance de clôture. Mécanisable avec la même logique de mappage que le bilan et le compte de résultat (itération suivante de ce moteur).
- **Mouvements** : exige des flux que la seule balance de clôture ne porte pas (valeurs brutes et amortissements de début, acquisitions, cessions, échéances de fonds affectés). Nécessite la balance N-1, un état des immobilisations ou un échéancier des fonds.
- **Déclaratif / Calculé** : information extra-comptable (identité de l'entité, effectifs, faits marquants) ou dérivée (ratios de la note 33), à saisir ou calculer à part.

## Ce que le moteur couvre (v3 — `scripts/notes_sycebnl.py`)

Les **45 feuilles de notes** (Notes 1 à 35 avec leurs subdivisions) sont
désormais **construites dans leur présentation officielle** et alimentées
en **formules Excel** (SUMIF sur les feuilles BALANCE / BALANCE_N1) :

1. **Notes de soldes — entièrement calculées** : 6, 7, 8, 9, 10, 11, 12,
   13, 14 (totaux 478/479), 15 (rappels 101-104), 16, 17A, 17B, 18A, 19,
   20, 21, 22, 23, 24, 25, 26, 27, 28, 29A, 31, 32. Affectations ligne à
   ligne dans `scripts/notes_sycebnl.py`, chaque numéro vérifié au plan
   des comptes SYCEBNL. Colonnes N-1 et variations servies quand la
   balance N-1 est fournie.
2. **Notes de mouvements — partiellement calculées** : 5A, 5B, 5C
   (location-acquisition via les comptes 2x16/2x46/2456), 5D, 5E, 5F
   (ouverture N-1, clôture en formule, flux en variation nette
   `MAX(0, N−(N-1))` à ajuster depuis l'inventaire), 5G (VNC 81x et prix
   82x par famille), 30 (provisions/dépréciations par nature).
3. **NOTE 33 (fiche de synthèse)** : SIG, CAFG, fonds de roulement, BFG,
   trésorerie nette, ratios — en formules croisées vers
   ACTIF/PASSIF/Compte de Resultat/TFT.
4. **NOTE 1** : rappels chiffrés en formules (dettes garanties par nature,
   contributions volontaires en nature depuis la classe 9) ; colonnes de
   sûretés et engagements à saisir depuis les actes.
5. **Notes déclaratives — gabarits pré-identifiés** : 2, 3, 4, 5H, 18B,
   29B (grille YA-YO), 34, 35 (exécution budgétaire, formules de
   réalisation/crédit/%).

La feuille **CONTROLES** recoupe chaque note calculée avec son poste
(écarts « doit être 0 », en formules). Le TFT boucle toujours avec la
trésorerie du bilan (ZB en résidu) ; ses lignes FA-FH restent à saisir
depuis le journal de trésorerie — limite structurelle d'une balance de
clôture, pas du moteur.

## Frontière avec les autres jeux d'états SYCEBNL

Ce fichier couvre le jeu **associations et ordres professionnels** (Partie
4, ch. 2). Les deux autres jeux ont leurs propres moteurs, maquettes et
notes :

- **Projets de développement et assimilés** (Partie 4, ch. 3) :
  `scripts/monter_projets.py`, `correspondance-projets.tsv`,
  `notes-projets.md` (notes 1 à 24) ;
- **Système minimal de trésorerie** (Partie 4, ch. 4, seuil 30 M FCFA) :
  `scripts/monter_smt_sycebnl.py`, `correspondance-smt-sycebnl.tsv`,
  `notes-smt-sycebnl.md` (notes 1 à 5).

Ne jamais appliquer la maquette d'un jeu à un autre : codes REF, comptes et
notes diffèrent.
