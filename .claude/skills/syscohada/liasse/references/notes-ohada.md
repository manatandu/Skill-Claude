# Notes annexes OHADA — liste officielle et couverture

**Source : AUDCIF, Titre IX, chapitre 6, section 2 (liste officielle des Notes annexes).** Cette liste remplace toute reconstitution de mémoire ou reprise d'un modèle tiers.

L'annexe normalisée du Système normal va de **NOTE 1 à NOTE 36**. La numérotation **n'est pas continue** : la note 3 se subdivise de **3A à 3F** (il n'y a pas de 3G), il n'y a **pas de 15C** ni de **16D**. Le total des numéros de tête est donc bien 36.

## Liste officielle (intitulés AUDCIF)

| Note | Intitulé officiel | Statut |
|------|-------------------|--------|
| 1 | Dettes garanties par des sûretés réelles | Déclaratif |
| 2 | Informations obligatoires | Déclaratif |
| 3A | Immobilisation brute | Mouvements |
| 3B | Biens pris en location acquisition | Mouvements |
| 3C | Immobilisations : amortissements | Mouvements |
| 3D | Immobilisations : plus-values et moins-value de cession | Mouvements |
| 3E | Informations sur les réévaluations effectuées par l'entité | Mouvements |
| 3F | Tableau d'étalement des charges immobilisées | Mouvements |
| 4 | Immobilisations financières | Soldes |
| 5 | Actif circulant HAO (sert aussi le passif DH) | Soldes |
| 6 | Stocks et en-cours | Soldes |
| 7 | Clients (produits à recevoir) | Soldes |
| 8 | Autres créances | Soldes |
| 9 | Titres de placement | Soldes |
| 10 | Valeurs à encaisser | Soldes |
| 11 | Disponibilités | Soldes |
| 12 | Écarts de conversion | Soldes |
| 13 | Capital : valeur nominale des actions ou parts | Soldes |
| 14 | Primes et réserves | Soldes |
| 15A | Subventions et provisions réglementées | Mouvements |
| 15B | Autres fonds propres | Mouvements |
| 16A | Dettes financières et ressources assimilées | Mouvements |
| 16B | Engagements de retraite et avantages assimilés (méthode actuarielle) | Déclaratif |
| 16B bis | Engagements de retraite et avantages assimilés (méthode actuarielle) | Déclaratif |
| 16C | Actifs et passifs éventuels | Déclaratif |
| 17 | Fournisseurs d'exploitation | Soldes |
| 18 | Dettes fiscales et sociales | Soldes |
| 19 | Autres dettes et provisions pour risques à court terme | Soldes |
| 20 | Banques, crédit d'escompte et de trésorerie | Soldes |
| 21 | Chiffre d'affaires et autres produits | Soldes |
| 22 | Achats | Soldes |
| 23 | Transports | Soldes |
| 24 | Services extérieurs | Soldes |
| 25 | Impôts et taxes | Soldes |
| 26 | Autres charges | Soldes |
| 27A | Charges de personnel | Soldes |
| 27B | Effectifs, masse salariale et personnel extérieur | Déclaratif |
| 28 | Provisions et dépréciations inscrites au bilan | Mouvements |
| 29 | Charges et revenus financiers | Soldes |
| 30 | Autres charges et produits HAO | Soldes |
| 31 | Répartition du résultat et éléments des cinq derniers exercices | Mouvements (historique) |
| 32 | Production de l'exercice | Soldes |
| 33 | Achats destinés à la production | Soldes |
| 34 | Fiche de synthèse des principaux indicateurs financiers | Calculé |
| 35 | Liste des informations sociales, environnementales et sociétales à fournir | Déclaratif |
| 36 | Tables des codes | Nomenclature |

## Coquilles du modèle Excel fourni (« Modele_Type »)

Le gabarit reproduit fidèlement plusieurs coquilles que l'AUDCIF signale lui-même. À connaître pour ne pas les prendre pour la règle :

- La feuille intitulée **« NOTE 8A »** est en réalité la **NOTE 3F** (tableau d'étalement des charges immobilisées). Il **n'existe aucune NOTE 8A** dans la liste officielle.
- L'en-tête de la page **NOTE 3C** porte « NOTE 3B (Amortissements) » : coquille de numérotation, le contenu est bien la 3C.
- La **NOTE 3B** (biens pris en location acquisition) ouvre par erreur des lignes d'immobilisations **incorporelles**, alors que le Titre VIII limite les contrats de location aux corporelles.
- La feuille **« NOTE 36 »** du modèle affiche un texte de forme sociale ; l'objet officiel de la note 36 est **Tables des codes** (nomenclatures NAEMA/NOPEMA).

## Trois statuts

- **Soldes** : ventilation de soldes de la balance. Mécanisable avec la logique de mappage déjà en place.
- **Mouvements** : exige des flux que la seule balance de clôture ne porte pas (valeurs brutes et amortissements de début, acquisitions, cessions, échéances). Nécessite la balance N-1, un état des immobilisations ou un échéancier.
- **Déclaratif / Nomenclature / Calculé** : information extra-comptable ou dérivée, à saisir ou à calculer à part.

## Couverture du moteur (v3 — `scripts/notes_sn.py`)

Le moteur alimente désormais les notes directement dans le gabarit
officiel, **en formules Excel** (SUMIF sur les feuilles BALANCE /
BALANCE_N1 injectées) — chaque chiffre est retraçable au compte près :

1. **Notes de soldes — entièrement calculées** : 4, 5, 6, 7, 8, 9, 10, 11,
   12 (section transferts de charges), 14, 15A, 15B (avances
   conditionnées), 16A, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27A, 29,
   30. Les affectations ligne à ligne sont dans `scripts/notes_sn.py`
   (chaque numéro vérifié au plan de comptes) ; les colonnes N-1 sont
   servies quand la balance N-1 est fournie ; les totalisations manquantes
   ou tronquées du modèle Excel officiel sont corrigées (liste
   `TOTAUX_FIXES`, documentée dans le script).
2. **Notes de mouvements — partiellement calculées** : 3A (brut), 3C
   (amortissements), 3D (plus/moins-values : VNC 81x et prix 82x par
   famille), 28 (provisions/dépréciations). Ouverture depuis N-1, clôture
   par la formule du gabarit ; flux depuis les colonnes de mouvement de la
   balance quand elles existent, sinon variation nette posée en formule
   `MAX(0, N−(N-1))` — présentation « en net » signalée, à ajuster depuis
   l'état des immobilisations ou l'échéancier.
3. **NOTE 34 (fiche de synthèse) — calculée** : SIG, CAFG, structure
   financière, en formules croisées vers ACTIF/PASSIF/CR/TFT.
4. **Notes déclaratives — gabarits pré-identifiés** : 1, 2, 3B, 3E,
   8A (=3F), 13, 16B, 16B bis, 16C, 27B, 31, 32, 33, 35, 36. L'en-tête
   (entité, exercice, durée) est rempli sur toutes les feuilles.

La feuille **CONTROLES** recoupe chaque note calculée avec son poste de
bilan ou de compte de résultat (écarts « doit être 0 », en formules).
