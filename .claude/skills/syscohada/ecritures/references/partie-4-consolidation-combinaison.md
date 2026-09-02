# Partie 4 — Comptes consolidés et combinés (Applications 128 à 142)

Cette partie couvre le périmètre, les méthodes et les mécanismes de la consolidation et de la combinaison des comptes selon l'Acte uniforme relatif au droit comptable et à l'information financière (art. 74 à 113). Elle prolonge la Partie 2 (écritures individuelles) sur un terrain différent : ici, l'écriture ne corrige pas un compte d'une entité, elle construit les comptes du groupe à partir des comptes individuels retraités.

## Chapitre 1 — Périmètre et méthodes de consolidation (App. 128 à 131)

### Pourcentage de contrôle et pourcentage d'intérêt

Le **pourcentage de contrôle** mesure la capacité du groupe à diriger une entité, directement ou indirectement, par les droits de vote substantiels détenus. Trois précisions :
- les actions sans droit de vote sont exclues du calcul ;
- les actions à droit de vote double comptent double ;
- les droits de vote potentiels (obligations convertibles, options, contrats à terme) ne comptent que s'ils sont substantifs, c'est-à-dire que l'entité mère aurait la capacité pratique de les exercer.

Le **pourcentage d'intérêt** mesure la part du groupe dans les capitaux propres d'une entité. C'est lui qui sert dans toutes les écritures de consolidation (partage des capitaux propres, écarts d'évaluation). Il est égal à la participation directe majorée du produit des participations le long de chaque chaîne ; en cas de chaînes multiples, on additionne les pourcentages obtenus chaîne par chaîne.

**Application 128 — Organigramme, pourcentages de contrôle et d'intérêt.** Groupe H (holding pure) → A, B, C (détenues à 90 % chacune) → D (détenue à 25 %, contrôle conjoint). A détient 60 % de E, B détient 30 % de F, C détient 55 % de G, D détient 70 % de I.

| Entité | % contrôle | Nature du contrôle | % intérêt |
|---|---|---|---|
| A, B, C | 90 % | Contrôle exclusif | 90 % |
| D | 25 % | Contrôle conjoint | 25 % |
| E | 60 % | Contrôle exclusif | 90 % × 60 % = 54 % |
| F | 30 % | Influence notable | 90 % × 30 % = 27 % |
| G | 55 % | Contrôle exclusif | 90 % × 55 % = 49,5 % |
| I | 0 % | Pas de contrôle | 25 % × 70 % = 17,5 % |

Le pourcentage de contrôle et le pourcentage d'intérêt divergent dès qu'une chaîne passe par une entité sous contrôle conjoint ou sous influence notable : au-delà de ce maillon, le contrôle s'arrête (I n'est pas contrôlée), mais l'intérêt financier continue de se calculer par multiplication.

**Application 129 — Périmètre avec actions à vote double, sans droit de vote et droits de vote potentiels.** Le capital de H comprend 40 000 actions ordinaires, 4 000 actions à vote double, 8 000 actions sans droit de vote. MERAS détient 12 000 actions ordinaires et 3 800 actions à vote double, plus 20 000 obligations convertibles (1 action pour 2 obligations, sur un total de 20 000 OCA émises). Les droits de vote potentiels sont substantifs.

Pourcentage de contrôle de MERAS dans H :

(12 000 × 1) + (3 800 × 2) + (10 000 × 1)
──────────────────────────────────────────── = 51,03 %
(40 000 × 1) + (4 000 × 2) + (8 000 × 0) + (10 000 × 1)

Le numérateur et le dénominateur intègrent les droits de vote potentiels (10 000 actions issues de la conversion des 20 000 OCA détenues, sur les 10 000 actions potentielles totales issues des 20 000 OCA émises par H) — c'est ce qui bascule le contrôle de minoritaire à majoritaire.

Pourcentage d'intérêt de MERAS dans H (hors droits potentiels, sur le seul capital existant) :

12 000 + 3 800
──────────────────── = 30,38 %
40 000 + 4 000 + 8 000

Périmètre de consolidation retenu : MERAS, A, B, C, D, F, G, H (E est exclue : ni contrôle ni influence notable).

### Trois méthodes de consolidation

| Situation | Méthode |
|---|---|
| Contrôle exclusif | Intégration globale |
| Contrôle conjoint (art. 80 al. 2) | Intégration proportionnelle |
| Influence notable (art. 80 al. 3) | Mise en équivalence |

**Application 130 — Participations circulaires.** M détient 70 % de F1, M détient 30 % de F2, F1 détient 40 % de F2. F2 est sous contrôle conjoint. La circularité (F2 reboucle sur M via F1) interdit un calcul direct ; deux voies :

*Par la formule directe* (limite de la somme géométrique des allers-retours dans la boucle) :

Dans M = (1 − 0,30) / [1 − (0,7 × 0,4 × 0,3)] = 76,42 %
Dans F1 = [(1 − 0,3) × 0,7] / [1 − (0,7 × 0,4 × 0,3)] = 53,49 %
Dans F2 = [(1 − 0,3) × 0,7 × 0,4] / [1 − (0,7 × 0,4 × 0,3)] = 21,39 %

*Par un système d'équations*, en intégrant une « mère fictive » détenant 70 % de M (100 % − 30 %, puisque F2 reverse 30 % dans M) :

M = 0,7 + 0,3 × F2 ; F1 = 0,7 × M ; F2 = 0,4 × F1

M = 0,7 + 0,3 × (0,4 × 0,7 × M) = 0,7 + 0,084 M → 0,916 M = 0,7 → M = 76,42 %
F1 = 0,7 × 76,42 % = 53,49 % ; F2 = 0,4 × 53,49 % = 21,39 %

Les deux voies convergent, ce qui vaut vérification.

**Application 131 — Entité ad hoc.** Une entité A est créée par les dirigeants de l'entité consolidante C pour acquérir des équipements loués aux filiales de C. Les dirigeants de C détiennent la majorité en AGE de A et se sont portés garants auprès de la banque.

Trois critères d'appréciation du contrôle d'une entité ad hoc :
1. l'entité consolidante dispose en réalité des pouvoirs de décision sur l'entité ad hoc (même non exercés) ;
2. l'entité consolidante bénéficie, de fait, de la majorité des avantages économiques de l'entité ad hoc ;
3. l'entité consolidante supporte la majorité des risques relatifs à l'entité ad hoc.

L'entité ad hoc est consolidée si (1 et 2) ou (1 et 3) sont réunis ; elle l'est aussi si (2 et 3) sont réunis sans le critère 1. La prédominance du critère des pouvoirs de décision ne joue que pour les entités ad hoc issues d'une cession de créances.

Ici : C détient les pouvoirs de décision (majorité en AGE) et s'est portée garante (risques). Contrôle exclusif — intégration globale.

## Chapitre 2 — Mise en œuvre des méthodes de consolidation (App. 132 à 134)

Les trois applications suivantes reprennent le même couple mère/filiale (M détient 45 % de F, actions de 10 000 F l'unité) sous trois hypothèses de contrôle différentes, pour donner à voir les trois méthodes sur un cas identique.

Bilans et comptes de résultat individuels au 31/12/N :

| Bilan M | Actif | | Passif | |
|---|---|---|---|---|
| Immobilisations | 135 000 000 | Capital | 100 000 000 |
| Titres F (225 actions) | 2 250 000 | Réserves | 25 000 000 |
| Actifs circulants | 12 750 000 | Résultat | 5 000 000 |
| | | Dettes | 20 000 000 |

| Bilan F | Actif | | Passif | |
|---|---|---|---|---|
| Immobilisations | 10 000 000 | Capital | 5 000 000 |
| Actifs circulants | 5 500 000 | Réserves | 4 000 000 |
| | | Résultat | 1 500 000 |
| | | Dettes | 5 000 000 |

Produits/Charges M : 400 000 000 / 395 000 000 → résultat 5 000 000. Produits/Charges F : 45 000 000 / 43 500 000 → résultat 1 500 000.

### Application 132 — Intégration globale (contrôle exclusif à 45 %, historique de prise de contrôle dès la création)

**Méthode.** L'intégration globale reprend 100 % des postes de bilan et de compte de résultat de la filiale, quel que soit le pourcentage détenu. Ensuite :
- élimination des titres de participation à l'actif de la mère par imputation sur les réserves ;
- partage des capitaux propres de la filiale (y compris le résultat) entre part du groupe et intérêts minoritaires.

**Reprise des comptes** (simple addition ligne à ligne des deux bilans et des deux comptes de résultat, sans retraitement puisqu'il n'y a pas d'opération réciproque dans cette application).

**Tableau de partage des capitaux propres de F (45 % / 55 %)**

| Éléments | Total F | Part groupe (45 %) | Part minoritaires (55 %) |
|---|---|---|---|
| Capital | 5 000 000 | 2 250 000 | 2 750 000 |
| Réserves | 4 000 000 | 1 800 000 | 2 200 000 |
| **Total** | **9 000 000** | **4 050 000** | **4 950 000** |
| Résultat | 1 500 000 | 675 000 | 825 000 |

La part groupe sur le capital + réserves (4 050 000) se décompose en : titres à éliminer 2 250 000, réserves consolidées 1 800 000.

**Écritures de partage**

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| Capital F, Réserves F | Titres F, Réserves consolidées, Intérêts minoritaires | 31/12/N — partage capitaux propres hors résultat de F | 5 000 000 / 4 000 000 | 2 250 000 / 1 800 000 / 4 950 000 |
| Résultat F | Réserves consolidées, Intérêts minoritaires | 31/12/N — partage du résultat de F | 1 500 000 | 675 000 / 825 000 |

**Bilan consolidé** : immobilisations 145 000 000, actifs circulants 18 250 000, total 163 250 000 — capital 100 000 000, réserves consolidées 26 800 000, résultat consolidé 5 675 000 (part groupe 132 475 000), intérêts minoritaires 5 775 000, dettes 25 000 000.

**Compte de résultat consolidé** : produits 445 000 000, charges 438 500 000, résultat de l'ensemble consolidé 6 500 000, dont part groupe 5 675 000 et intérêts minoritaires 825 000.

### Application 133 — Intégration proportionnelle (contrôle conjoint 45 % / 55 %)

Mêmes données, mais F est cette fois sous contrôle conjoint (accord contractuel entre M à 45 % et un second associé à 55 %).

**Méthode.** On intègre uniquement la fraction représentative des intérêts de la mère (45 %) dans chaque poste de bilan et de compte de résultat de F — aucun intérêt minoritaire n'est constaté, puisque seule la quote-part du groupe est reprise.

**Reprise des comptes de F, à 45 %** : immobilisations 4 500 000, actifs circulants 2 475 000 ; capital 2 250 000, réserves 1 800 000, résultat 675 000, dettes 2 250 000. Côté gestion : charges 19 575 000, résultat 675 000, produits 20 250 000 (43 500 000, 1 500 000 et 45 000 000, chacun × 45 %).

**Partage** — aucun partage entre groupe et minoritaires n'est nécessaire puisque seule la fraction du patrimoine appartenant au groupe a été intégrée :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| Capital F, Réserves F | Titres F, Réserves consolidées | 31/12/N — partage capitaux propres hors résultat de F (45 %) | 2 250 000 / 1 800 000 | 2 250 000 / 1 800 000 |
| Résultat F | Résultat consolidé | 31/12/N — partage du résultat de F (45 %) | 675 000 | 675 000 |

**Bilan consolidé** : immobilisations 139 500 000, actifs circulants 15 225 000, total 154 725 000 — capital 100 000 000, réserves consolidées 26 800 000, résultat consolidé 5 675 000, dettes 22 250 000.

**Compte de résultat consolidé** : produits 420 250 000, charges 414 575 000, résultat 5 675 000, aucun intérêt minoritaire.

### Application 134 — Mise en équivalence (influence notable, 45 % contre 55 % de contrôle exclusif détenu par un tiers)

Mêmes données ; cette fois une autre entité détient 55 % de F et en exerce le contrôle exclusif, si bien que M, avec ses 45 %, n'a plus qu'une influence notable.

**Méthode.** On substitue à la valeur comptable des titres la quote-part des capitaux propres (résultat compris) déterminée selon les règles de consolidation ; les comptes de F ne sont pas repris ligne à ligne, seuls ceux de M le sont.

**Titres mis en équivalence** : 45 % × (5 000 000 + 4 000 000 + 1 500 000) = 4 725 000.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| Titres mis en équivalence | Titres F, Réserves consolidées, Résultat consolidé | 31/12/N — substitution de la quote-part de capitaux propres | 4 725 000 | 2 250 000 / 1 800 000 / 675 000 |
| Résultat global | Quote-part dans les résultats des entités mises en équivalence | 31/12/N — reprise du résultat de F au compte de résultat consolidé | 675 000 | 675 000 |

**Bilan consolidé** : immobilisations 135 000 000, titres mis en équivalence 4 725 000, actifs circulants 12 750 000, total 152 475 000 — capital 100 000 000, réserves consolidées 26 800 000, résultat consolidé 5 675 000, dettes 20 000 000.

**Compte de résultat consolidé** : résultat net des entités intégrées 5 000 000, + quote-part dans les résultats des entités mises en équivalence 675 000 = résultat net de l'ensemble consolidé 5 675 000, sans intérêt minoritaire.

## Chapitre 3 — Écart de consolidation (App. 135 à 137)

### Principes

**Écart de consolidation** = coût d'acquisition des titres − part des capitaux propres que ces titres représentent (résultat de l'exercice d'acquisition compris), à la date d'entrée dans le périmètre.

L'écart de consolidation se décompose en deux éléments :

**Écart d'évaluation** — différence, sur des éléments identifiables de l'actif ou du passif, entre la juste valeur retenue au bilan consolidé et la valeur comptable dans l'entité contrôlée. Tout écart d'évaluation donne lieu à une imposition différée.

**Écart d'acquisition** — écart résiduel non affectable à des éléments identifiables de l'actif ou du passif. Deux façons équivalentes de le calculer :
1. écart de consolidation − part du groupe dans l'écart d'évaluation ;
2. coût d'acquisition − quote-part du groupe dans la juste valeur des actifs et passifs identifiables (capitaux propres réestimés à la juste valeur).

Aucun impôt différé sur l'écart d'acquisition lui-même.

La **date d'acquisition** est la date de prise de contrôle ou d'influence notable, donc la date d'entrée dans le périmètre — y compris en cas d'achats successifs, où elle correspond à la date d'obtention du contrôle. La **période d'évaluation**, pendant laquelle les montants provisoires peuvent être ajustés rétrospectivement, ne dépasse pas 12 mois à compter de cette date.

**Comptabilisation de l'écart d'acquisition positif (goodwill)** : inscription à l'actif immobilisé (immobilisations incorporelles), en contrepartie d'une diminution des titres de participation ou d'une augmentation des réserves consolidées.

**Amortissement** : si la durée d'utilité est limitée, amortissement linéaire sur cette durée ; si elle ne peut être déterminée de façon fiable, amortissement sur 10 ans ; si la durée d'utilité est non limitée, pas d'amortissement (mais test de dépréciation systématique, qu'il existe ou non un indice de perte de valeur). Le passage d'une durée non limitée à une durée limitée s'applique de façon prospective, après test de dépréciation.

**Dépréciation** : un écart d'acquisition, amortissable ou non, fait obligatoirement l'objet d'un test de dépréciation. Si la valeur actuelle ne peut être déterminée isolément, on teste le groupe d'actifs auquel il appartient ; la dépréciation constatée s'impute d'abord sur l'écart d'acquisition, puis sur les autres actifs du groupe. Les dépréciations de l'écart d'acquisition ne sont jamais reprises en résultat.

### Application 135 — Écart d'évaluation et d'acquisition positif (intégration globale)

M acquiert 80 % de F pour 50 000 000 le 01/01/N. Capitaux propres de F à cette date : 25 000 000. Terrain au bilan 15 000 000, juste valeur 30 000 000. Marque évaluée à 10 000 000 (non inscrite au bilan de F). Provisions pour engagements retraite non comptabilisées à hauteur de 7 500 000. Brevet au bilan pour 20 000 000, juste valeur 26 000 000. Durée d'utilité de l'écart d'acquisition non déterminable de façon fiable. Taux d'IS théorique 25 %.

**Écart de consolidation** : 50 000 000 − (25 000 000 × 80 %) = 30 000 000.

**Écart d'évaluation** :

Plus-value nette (I) = 15 000 000 (terrain) + 10 000 000 (marque) + 6 000 000 (brevet) − 7 500 000 (provision retraite) = 23 500 000
Impôt différé (II) = 23 500 000 × 25 % = 5 875 000
Écart d'évaluation (I − II) = 17 625 000

Part groupe : 17 625 000 × 80 % = 14 100 000. Part hors groupe (intérêts minoritaires) : 17 625 000 × 20 % = 3 525 000.

**Écart d'acquisition**, par les deux méthodes :

*1ère méthode* : 30 000 000 − 14 100 000 = 15 900 000.

*2ème méthode* : juste valeur des actifs et passifs identifiables = 25 000 000 + 17 625 000 = 42 625 000 ; écart d'acquisition = 50 000 000 − (80 % × 42 625 000) = 50 000 000 − 34 100 000 = 15 900 000.

Les deux méthodes se recoupent (vérification : 14 100 000 + 15 900 000 = 30 000 000).

**Écritures au bilan de l'écart d'évaluation**

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| Terrain, Marque, Brevet | Provision pour engagement de retraite, Impôt différé passif, Titres de participation, Intérêts minoritaires | Constatation de l'écart d'évaluation à la date d'acquisition | 15 000 000 / 10 000 000 / 6 000 000 | 7 500 000 / 5 875 000 / 14 100 000 / 3 525 000 |

Variante admise : logement de l'écart net dans un compte « Réserves de réestimation » (17 625 000), ventilé ensuite entre groupe et minoritaires lors du partage des capitaux propres, plutôt que ventilé dès la constatation de l'écart.

**Écritures de l'écart d'acquisition**

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| Écart d'acquisition | Titres de participation F (ou Réserves consolidées) | Constatation de l'écart d'acquisition | 15 900 000 | 15 900 000 |
| Résultat groupe (résultat consolidé) | Écart d'acquisition | Amortissement sur 10 ans (durée non déterminable) : 15 900 000 / 10 | 1 590 000 | 1 590 000 |
| Dotations aux amortissements | Résultat global | Reprise au compte de résultat consolidé | 1 590 000 | 1 590 000 |

### Application 136 — Écart d'acquisition positif, entité mise en équivalence

M acquiert 25 % de F1 le 01/10/N pour 170 000 000. Ensemble immobilier réévalué à 170 000 000 (terrain 40 000 000, bâtiment industriel 130 000 000) contre une valeur comptable nette de 110 000 000 (terrain 30 000 000, bâtiment 80 000 000). Le bâtiment réestimé a encore 20 ans de durée de vie. Écart d'acquisition non amortissable. Capitaux propres de F1 au 31/12/N : capital 200 000 000, réserves 70 500 000, résultat 40 000 000. Taux d'IS théorique 30 %.

**Principe propre à la mise en équivalence** : l'écart d'acquisition positif n'est pas inscrit séparément à l'actif en immobilisation incorporelle — il est inclus dans la valeur comptable des titres mis en équivalence. S'il est positif, aucune dépréciation spécifique des titres n'est à envisager de ce seul fait.

**Écart d'évaluation** :

Plus-value nette (I) = 10 000 000 (terrain) + 50 000 000 (bâtiment) = 60 000 000
Impôt différé (II) = 60 000 000 × 30 % = 18 000 000
Écart d'évaluation (I − II) = 42 000 000

Part groupe : 42 000 000 × 25 % = 10 500 000. Part hors groupe : 42 000 000 × 75 % = 31 500 000.

**Juste valeur des actifs et passifs identifiables**, à la date d'acquisition (quote-part du résultat courue du 01/10 au 31/12, soit 9/12 de 40 000 000 = 30 000 000) :

Capitaux propres (200 000 000 + 70 500 000 + 30 000 000) = 300 500 000
+ Écart d'évaluation 42 000 000
= 342 500 000

**Écart d'acquisition** : 170 000 000 − (25 % × 342 500 000) = 170 000 000 − 85 625 000 = 84 375 000.

**Valeur des titres mis en équivalence au 31/12/N** :

Quote-part dans la juste valeur des actifs et passifs identifiables à la date d'acquisition : 85 625 000
+ Écart d'acquisition : 84 375 000
+ Quote-part du résultat du 01/10 au 31/12 [(40 000 000 − 30 000 000) − (50 000 000 / 20 × 3/12 amortissement de la plus-value sur bâtiment)] × 25 % = 2 343 750
= **172 343 750**

**Écritures**

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| Titres mis en équivalence | Titres de participation, Quote-part du résultat mise en équivalence | 31/12/N — valorisation des titres mis en équivalence | 172 343 750 | 170 000 000 / 2 343 750 |
| Résultat global | Quote-part du résultat mise en équivalence | 31/12/N — reprise au compte de résultat consolidé | 2 343 750 | 2 343 750 |

### Application 137 — Écart d'acquisition négatif (badwill)

M acquiert 60 % de F pour 90 000 000. Capitaux propres de F : capital 50 000 000, réserves 100 000 000, résultat 10 000 000, soit 160 000 000. Plus-value identifiée sur une licence : 25 500 000. Taux d'IS théorique 30 %. L'énoncé retient l'hypothèse d'une reprise globale de l'écart négatif au résultat de l'exercice d'acquisition.

**Principe.** Un écart d'acquisition négatif traduit soit une acquisition à des conditions avantageuses, soit une rentabilité jugée insuffisante de l'entité acquise. Les actifs incorporels qui ne peuvent pas être évalués par référence à un marché actif ne doivent pas être comptabilisés s'ils ont pour effet de créer ou d'augmenter un badwill. L'écart négatif est en principe rapporté au résultat sur une durée reflétant les hypothèses et objectifs de l'acquisition ; les faits et circonstances peuvent justifier une reprise globale et immédiate, comme dans cette application. Avant toute comptabilisation d'un profit, l'acquéreur doit vérifier qu'il a correctement identifié et évalué tous les actifs acquis et passifs repris.

**Juste valeur des actifs et passifs identifiables** : 160 000 000 + [25 500 000 × (1 − 30 %)] = 160 000 000 + 17 850 000 = 177 850 000.

**Écart d'acquisition** : 90 000 000 − (60 % × 177 850 000) = 90 000 000 − 106 710 000 = **− 16 710 000**.

**Écritures**

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| Titres de participation | Résultat M | Constatation du badwill, reprise globale au résultat de l'exercice d'acquisition | 16 710 000 | 16 710 000 |
| Résultat global | Produit | Reprise au compte de résultat consolidé | 16 710 000 | 16 710 000 |

## Chapitre 4 — Conversion en unités monétaires locales des états financiers établis en devises (App. 138)

Une entité acquise ou contrôlée dont les comptes sont tenus dans une autre monnaie doit voir ses états financiers convertis avant intégration. Deux méthodes coexistent, chacune produisant un traitement différent de l'écart de change.

### Méthode temporelle (méthode du coût historique)

- Éléments **monétaires** du bilan : conversion au cours de clôture.
- Éléments **non monétaires**, capitaux propres compris, évalués au coût historique : conversion au cours historique (date de la transaction initiale).
- Produits et charges : conversion au cours de change de chaque transaction — en pratique le cours moyen, à condition qu'il soit proche du cours réel — sauf dotations aux amortissements et dépréciations, converties au cours historique de l'immobilisation correspondante.
- Le résultat de l'exercice n'est pas converti directement : il ressort de l'équilibre du bilan converti, ce qui fait apparaître un écart de change au compte de résultat, en charges ou produits financiers.

Cet écart appartient exclusivement au groupe ; il n'est jamais réparti avec les minoritaires, car il découle des seuls comptes de gestion.

### Méthode du cours de clôture

- Actifs et passifs, monétaires ou non, hors capitaux propres : conversion au cours de clôture de chaque bilan présenté (comparatifs compris). Traitement identique pour les écarts d'acquisition.
- Éléments de capitaux propres (capital, réserves) : conversion au cours historique, ou au cours moyen.
- Produits et charges : conversion au cours de clôture ou au cours moyen (moyenne des cours constatés sur l'exercice).

L'écart de conversion issu de cette méthode est une réserve consolidée, à répartir entre groupe et minoritaires selon le pourcentage d'intérêt de chacun — contrairement à l'écart de la méthode temporelle.

### Application 138 — Filiale N au Nigéria (Naira)

Prise de contrôle exclusif le 01/01/N, cours 1 Naira = 2 F. Bilan d'ouverture (Naira / Franc) : immobilisations 2 000 000 / 4 000 000, banques 3 000 000 / 6 000 000 ; capital 2 000 000 / 4 000 000, réserves 1 000 000 / 2 000 000, dettes 2 000 000 / 4 000 000.

Cours au 31/12/N : 1 Naira = 2,30 F. Cours moyen N : 1 Naira = 2,20 F. Résultat N : 500 000 Naira. Stock au 31/12/N (2 000 000 Naira) intégralement acquis à un cours de 1 Naira = 2,25 F.

Bilan N (Naira) : immobilisations 2 000 000, stocks 2 000 000, banque 1 000 000 ; capital 2 000 000, réserves 1 000 000, résultat 500 000, dettes 1 500 000.

Compte de résultat N (Naira) : achats 7 500 000, variation de stocks −2 000 000, autres charges 1 500 000, résultat 500 000 ; chiffre d'affaires 6 000 000, autres produits 1 500 000.

**Conversion selon la méthode temporelle**

Bilan converti : immobilisations 4 000 000 (cours historique 2), stocks 4 500 000 (cours du lot, 2,25), banque 2 300 000 (cours de clôture, 2,30) — total actif 10 800 000. Capital 4 000 000 et réserves 2 000 000 au cours historique (2), dettes 3 450 000 au cours de clôture (2,30). Le résultat (1 350 000) ressort par différence pour équilibrer le bilan.

Compte de résultat converti : achats 16 500 000 et autres charges 3 300 000 au cours moyen (2,20) ; variation de stocks −4 500 000 au cours du lot (2,25) ; chiffre d'affaires 13 200 000 et autres produits 3 300 000 au cours moyen (2,20) ; le résultat net (1 350 000) reporté du bilan implique un écart de conversion, en produit financier, de 150 000 F pour équilibrer le compte de résultat.

**Conversion selon la méthode du cours de clôture**

Compte de résultat, tout au cours moyen (2,20) : achats 16 500 000, variation de stocks −4 400 000, autres charges 3 300 000, résultat 1 100 000 ; chiffre d'affaires 13 200 000, autres produits 3 300 000.

Bilan, au cours de clôture (2,30) sauf capitaux propres au cours historique (2, hormis le résultat repris du compte de résultat converti) : immobilisations 4 600 000, stocks 4 600 000, banque 2 300 000 — total 11 500 000. Capital 4 000 000, réserves 2 000 000, écart de conversion 950 000, résultat 1 100 000 (capitaux propres 8 050 000), dettes 3 450 000.

L'écart de conversion de 950 000 F, ici, est une réserve consolidée à répartir entre groupe et minoritaires selon le pourcentage d'intérêt détenu dans la filiale — à la différence du produit financier de 150 000 F obtenu par la méthode temporelle.

## Chapitre 5 — Retraitements et élimination des opérations intergroupes (App. 139 et 140)

### Retraitements (Application 139)

Avant intégration, chaque compte individuel est retraité pour se conformer aux méthodes du groupe, indépendamment des choix fiscaux ou de gestion propres à chaque entité.

**Opération 1 — Écarts de conversion actif et passif.** F comptabilise un écart de conversion actif de 1 150 000 (ayant donné lieu à une dotation aux provisions pour risques et charges) et un écart de conversion passif de 750 000. Hypothèse fiscale des comptes individuels : écarts actifs déductibles, écarts passifs imposables ; provisions pour perte de change non déductibles, reprises non imposables.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| Provisions pour perte de change | Écart de conversion actif | Annulation de l'écart de conversion actif | 1 150 000 | 1 150 000 |
| Perte de change | Dotations aux provisions pour risques et charges | Reprise au compte de résultat | 1 150 000 | 1 150 000 |
| Écart de conversion passif | Résultat de l'entité | Annulation de l'écart de conversion passif | 750 000 | 750 000 |
| Résultat global | Gain de change | Reprise au compte de résultat | 750 000 | 750 000 |

Aucun impôt différé sur ces retraitements : l'impôt exigible individuel a déjà tenu compte des réintégrations et déductions correspondant à l'hypothèse fiscale retenue.

**Opération 2 — Provision pour engagement de retraite.** F1, hors espace OHADA, n'a pas comptabilisé de provision mais a indiqué le montant de ses engagements en Notes annexes. Indemnité au 31/12/N : 75 000 000 ; au 31/12/N-1 : 65 000 000. Taux d'IS théorique 30 %.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| Réserves F1 (65 000 000 × 70 %), Résultat F1 [(75 000 000 − 65 000 000) × 70 %], Impôts différés actif (75 000 000 × 30 %) | Provision pour engagement de retraite | Constatation de la provision non comptabilisée par F1 | 45 500 000 / 7 000 000 / 22 500 000 | 75 000 000 |
| Dotations aux provisions (75 000 000 − 65 000 000) | Résultat global (× 70 %), Impôt sur les bénéfices (× 30 %) | Dotation de l'exercice N | 10 000 000 | 7 000 000 / 3 000 000 |

**Opération 3 — Amortissement dérogatoire.** N-1 : 375 000 ; N : 200 000. Taux d'IS théorique 25 %.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| Amortissements dérogatoires | Résultat (200 000 × 0,75), Réserves (375 000 × 0,75), Impôt différé passif (575 000 × 0,25) | Élimination de l'amortissement dérogatoire, écarts cumulés N-1 et N | 575 000 | 150 000 / 281 250 / 143 750 |
| Résultat global (200 000 × 0,75), Impôt sur les bénéfices (200 000 × 0,25) | Dotations aux amortissements | Reprise au compte de résultat de l'exercice N | 150 000 / 50 000 | 200 000 |

**Opération 4 — Subventions.** L'entité PHILAS présente une subvention de 180 000 000 pour un matériel acquis début N-3 pour 500 000 000, subventionné à 60 %. 30 000 000 déjà virés au résultat sur la base des amortissements linéaires (10 ans). Le groupe reclasse la subvention en produit constaté d'avance ; la quote-part déjà virée au résultat n'est pas éliminée, conséquence du choix de reclassement retenu.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| Subvention d'investissement | Produit constaté d'avance | Reclassement de la subvention en produit constaté d'avance | 180 000 000 | 180 000 000 |

### Élimination des comptes réciproques et des résultats intragroupe (Application 140)

**Opération 1 — Dividendes intragroupe.** M a acquis F en N-1 et perçoit en novembre N des dividendes de 4 000 000 de F, enregistrés en produits financiers. Régime mère-filiale, dividendes en franchise d'impôt.

Les dividendes distribués en N proviennent du résultat N-1 : ils sont éliminés par imputation sur les réserves de M et sur le résultat consolidé. Côté F, si la distribution n'avait pas eu lieu, ce résultat serait resté en réserves — la contrepartie de l'élimination correspond donc à la part de M dans les réserves de F.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| Résultat M | Réserves | Élimination des dividendes reçus, imputés sur les réserves de F | 4 000 000 | 4 000 000 |
| Produits financiers | Résultat global | Reprise au compte de résultat consolidé | 4 000 000 | 4 000 000 |

**Opération 2 — Marge sur stock intragroupe.** M vend des marchandises à sa filiale F (intégrée globalement), taux de marge 20 %. Stock chez F au 31/12/N : 900 000 (300 000 au 31/12/N-1). Taux d'IS théorique 30 %.

La marge non réalisée à éliminer porte sur la variation du stock entre les deux exercices : (900 000 − 300 000) × 20 % = 120 000 sur le résultat de l'exercice, et 300 000 × 20 % = 60 000 sur les réserves (marge déjà logée dans le stock d'ouverture).

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| Résultat M [(900 000 − 300 000) × 0,2], Réserves M (300 000 × 0,2) | Stock de marchandises (900 000 × 0,2) | Élimination de la marge intragroupe logée dans le stock final | 120 000 / 60 000 | 180 000 |
| Impôts différés actif | Résultat M (120 000 × 0,3), Réserves M (60 000 × 0,3) | Constatation de l'impôt différé actif correspondant | 54 000 | 36 000 / 18 000 |
| Variation de stocks de marchandises [20 % × (300 000 − 900 000)] | Résultat, Impôt sur les bénéfices | Reprise au compte de résultat consolidé | 120 000 | 96 000 / 24 000 |

## Chapitre 6 — Variations du périmètre de consolidation (App. 141)

Une augmentation ou une diminution du pourcentage de détention **sans changement de méthode de consolidation** (le contrôle reste exclusif avant et après) n'affecte que les capitaux propres consolidés : elle rééquilibre la part du groupe et celle des minoritaires, sans reconstituer un nouvel écart d'acquisition. L'écart d'acquisition reste figé au montant déterminé à la date de la prise de contrôle initiale.

### Application 141 — Montée en participation de 70 % à 80 %

M acquiert 70 % de F en janvier N-2 pour 50 000 000. Capitaux propres à cette date : 45 000 000. Plus-values latentes identifiées lors de la prise de participation : terrain 12 000 000, bâtiment 8 000 000 (durée de vie résiduelle 10 ans). Début N, M porte sa participation à 80 % pour un complément de 9 700 000 ; capitaux propres de F à ce moment : 75 000 000. Capitaux propres de F au 31/12/N : 90 000 000. Écart d'acquisition à durée d'utilité indéfinie. Taux d'IS théorique 25 %.

**Étape 1 — écarts à la prise de contrôle initiale (70 %, janvier N-2)**

Écart de consolidation : 50 000 000 − (45 000 000 × 70 %) = 18 500 000.

Écart d'évaluation : plus-value latente (12 000 000 + 8 000 000) = 20 000 000, moins impôt différé passif (20 000 000 × 25 %) = 5 000 000, soit 15 000 000. Part groupe (70 %) : 10 500 000 ; part hors groupe (30 %) : 4 500 000.

Juste valeur des actifs et passifs identifiables : 45 000 000 + 15 000 000 = 60 000 000.

Écart d'acquisition : 50 000 000 − (70 % × 60 000 000) = 50 000 000 − 42 000 000 = 8 000 000. Vérification : 10 500 000 + 8 000 000 = 18 500 000.

**Étape 2 — écarts à la date de la montée en participation (10 % supplémentaires, début N)**

Le montant de l'écart d'évaluation s'amortit avec le temps (composante liée au bâtiment) : plus-value latente 20 000 000, moins amortissement de la fraction liée au bâtiment sur 2 ans (8 000 000 / 10 × 2) = 1 600 000, moins impôt différé sur le solde [(20 000 000 − 1 600 000) × 25 %][texte officiel : le calcul de la ligne « impôt différé passif » de cette étape applique un facteur (1 − 0,25) au lieu de 0,25 et aboutit à un résultat (13 800 000) supérieur à l'écart d'évaluation final annoncé (4 600 000) ; les deux valeurs semblent interverties dans le texte source — 18 400 000 × 25 % = 4 600 000 correspondrait à l'impôt différé, et 18 400 000 × 75 % = 13 800 000 à l'écart net d'impôt]. Le texte retient un écart d'évaluation de 4 600 000 à cette date.

Lors de l'acquisition des 10 % supplémentaires, M acquiert aussi 10 % de cet écart d'évaluation : 4 600 000 × 10 % = 460 000.

Juste valeur des actifs et passifs identifiables supplémentaires acquis : (75 000 000 × 10 %) + 460 000 = 7 500 000 + 460 000 = 7 960 000.

**Aucun nouvel écart d'acquisition n'est constaté** sur ce complément de 10 % : l'écart d'acquisition de 8 000 000 déterminé à la prise de contrôle initiale reste seul retenu, même si le coût d'acquisition du complément (9 700 000) diffère de la juste valeur des actifs et passifs identifiables supplémentaires acquis (7 960 000).

**Écritures au bilan de l'écart d'évaluation** (constatation intégrale, avec quote-part groupe et minoritaires)

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| Terrain, Bâtiment | Titres de participation (20 000 000 × 75 % × 80 %), Intérêts minoritaires (20 000 000 × 75 % × 20 %), Impôt différé passif (20 000 000 × 25 %) | Constatation de l'écart d'évaluation | 12 000 000 / 8 000 000 | 12 000 000 / 3 000 000 / 5 000 000 |

Variante par un compte « Réserves de réestimation » (15 000 000), ventilé ensuite entre groupe et minoritaires.

**Écart d'acquisition et amortissement du bâtiment**

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| Écart d'acquisition | Titres de participation F (ou Réserves consolidées) | Constatation à la valeur figée de la prise de contrôle initiale | 8 000 000 | 8 000 000 |
| Résultat groupe (8 000 000/10 × 75 % × 80 %), Réserves groupe [(8 000 000/10 × 2) × 75 % × 80 %], Intérêts minoritaires [(8 000 000/10 × 3) × 75 % × 20 %], Impôts différés actif [(8 000 000/10 × 3) × 25 %] | Amortissement bâtiment | Amortissement cumulé du bâtiment (8 000 000/10 × 3 ans) | 480 000 / 960 000 / 360 000 / 600 000 | 2 400 000 |
| Dotations aux amortissements | Résultat global (× 75 %), Impôt sur le bénéfice (× 25 %) | Reprise au compte de résultat consolidé de l'exercice N | 800 000 | 600 000 / 200 000 |

**Écriture de partage des capitaux propres au 31/12/N**

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| Capitaux propres (90 000 000) | Titres de participation (50 000 000 + 9 700 000 − 12 000 000 − 8 000 000 = 39 700 000), Intérêts minoritaires (90 000 000 × 20 %), Réserves groupe/consolidées (solde) | Partage des capitaux propres de F au 31/12/N | 90 000 000 | 39 700 000 / 18 000 000 / 32 300 000 |

## Chapitre 7 — Comptes combinés (Application 142)

### Principe

La combinaison rapproche des entités liées par une communauté d'intérêts sans lien capitalistique direct entre elles (ou sans entité mère établie dans l'espace OHADA). L'Acte uniforme impose des comptes combinés lorsqu'une entité mère hors espace OHADA contrôle des filiales situées, elles, dans l'espace OHADA : ces filiales, même sans lien capitalistique entre elles, doivent être combinées entre elles indépendamment de toute consolidation par la mère étrangère.

### Application 142 — Groupe X (hors OHADA) / B, C, D (dans l'espace OHADA)

X, dont le siège et l'activité sont hors espace OHADA, détient B à 90 %, C à 60 %, D à 70 %. B, C, D sont situées dans l'espace OHADA. Aucune opération réciproque entre B, C, D. Honoraires versés par B, C, D à leur maison mère X : respectivement 100, 150, 75 (sans effet sur la combinaison de B, C, D entre elles, X étant hors périmètre). B a constitué une provision pour dépréciation d'actifs de 60, justifiée économiquement mais non déductible fiscalement (déductible seulement lors de son utilisation). Taux d'IS 50 %.

**Détermination du périmètre de combinaison.** X devrait, en toute rigueur internationale, consolider B, C et D. Mais qu'elle établisse ou non des comptes consolidés, X — parce qu'elle contrôle des entités situées dans l'espace OHADA depuis un siège hors OHADA — doit obligatoirement faire établir des comptes combinés regroupant B, C et D entre elles, indépendamment de X.

**Bilans et comptes de résultat individuels (après retraitements d'homogénéité)**

| | B | C | D |
|---|---|---|---|
| Immobilisations | 200 | 300 | 150 |
| Autres actifs | 450 | 500 | 350 |
| Capital | 400 | 500 | 300 |
| Réserves | 100 | 150 | 50 |
| Résultat | 40 | 20 | 30 |
| Dettes fournisseurs | 110 | 130 | 120 |
| Chiffre d'affaires | 1 000 | 1 500 | 750 |
| Achats | 760 | 1 180 | 600 |

**Bilan combiné**

Immobilisations (200+300+150) = 650 ; autres actifs (450+500+350) = 1 300 ; impôts différés (60 × 50 %) = 30 (correspondant à la provision de B non déductible chez B, retraitée pour homogénéité fiscale du groupe) — total actif 1 980.

Capital et réserves combinés = (400+100) × 90 % + (500+150) × 60 % + (300+50) × 70 % = 450 × 0,9 + 650 × 0,6 + 350 × 0,7 = 405 + 390 + 245 = 1 040 [texte officiel : le calcul donne 1 040 alors que le montant retenu dans le tableau récapitulatif est 1 085 ; l'écart de 45 n'est pas expliqué dans le texte source, il peut provenir d'un arrondi ou d'un terme omis dans l'énoncé].

Résultat net combiné = (40+30) × 90 % + 20 × 60 % + 30 × 70 % = 63 + 12 + 21 = 96.

Part des minoritaires = (400+100+40+30) × 10 % + (500+150+20) × 40 % + (300+50+30) × 30 % = 57 + 268 + 114 = 439.

Part des ayants droit aux capitaux propres = total des capitaux propres combinés (1 620) − part des minoritaires (439) = 1 181. Total des capitaux propres combinés = 1 085 + 96 + 439 = 1 620. Dettes fournisseurs et divers (110+130+120) = 360. Total passif = 1 980, égal au total actif.

**Compte de résultat combiné**

Chiffre d'affaires (1 000+1 500+750) = 3 250 ; autres produits (50+100+30) = 180 ; total produits 3 430. Achats et autres charges combinés = 3 260. Résultat avant impôts = 170. Impôts exigibles sur résultats = −80 (somme des impôts individuels 30+20+30, sans retraitement). Impôts différés (variation, liée à la provision non déductible de B) = +30. Résultat net de l'ensemble combiné = 120, dont part des minoritaires 24 et part des ayants droit 96.

Ce dernier chiffre (96) recoupe le résultat net combiné calculé directement dans le tableau des capitaux propres — la cohérence entre les deux voies de calcul (bilan et compte de résultat) vaut vérification d'ensemble.

## Hors périmètre — Application 127 (modèle type d'états financiers)

Cette Application (page 341 et suivantes du Guide) présente un jeu complet d'états financiers normalisés SYSCOHADA (page de garde, fiches R1 à R4, bilan, compte de résultat, tableau des flux de trésorerie, notes annexes 1 à 36) rempli pour une entité fictive. Elle ne comporte aucune écriture de journal : c'est un modèle de présentation, pas un mécanisme comptable. Ce contenu relève de `syscohada-etats-financiers`, pas de ce skill, au même titre que la « Troisième partie : Présentation des états financiers annuels » du Guide_4 déjà signalée hors périmètre. Il n'a pas été encodé ici.
