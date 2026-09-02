# Partie 2 — Chapitres 3 à 5 : Ressources minérales, approche par composants, révisions majeures

> Montants pédagogiques. Écritures en tableau 5 colonnes : Débit | Crédit | Date et libellé | Montant débit | Montant crédit.

## Chapitre 3 — Frais de prospection et d'exploitation des ressources minérales (Application 32)

Entité minière, exercice N. 05/01/N : études géographiques/géologiques avant obtention des droits légaux, facture 75 000 000 F (réglée par chèque le 25/05/N). 20/10/N : obtention pour 150 000 000 F du droit de prospecter une zone délimitée (réglé le même jour). 15/03/N+1 : faisabilité technique et viabilité commerciale établies. L'entité choisit d'immobiliser les dépenses d'exploration/évaluation obtenues après les droits.

**Règle.** Ne sont pas activés : les frais encourus **avant** l'obtention des droits légaux de prospecter (avant le 20/10/N : 75 000 000) ni ceux encourus **après** que la faisabilité et la viabilité aient été démontrées (après le 15/03/N+1). Si l'actif de prospection est incorporel : **2181 Frais de prospection et évaluation des ressources minérales**.

Études préalables (05/01/N) — charge :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6261 |  | 05/01/N — Études et recherches | 75 000 000 |  |
|  | 401 | Fournisseurs |  | 75 000 000 |
| 401 |  | 25/05/N — Fournisseurs | 75 000 000 |  |
|  | 521 | Banques |  | 75 000 000 |

Droit de prospecter (immobilisation) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 2181 |  | 25/05/N — Frais de prospection et d'évaluation | 150 000 000 |  |
|  | 521 | Banques |  | 150 000 000 |

Variante — si l'entité choisit de passer les dépenses en charges : **6346 Redevances pour concessions** · 521, 150 000 000.

## Chapitre 4 — Approche par composants (Application 33)

Bâtiment administratif acquis le 02/01/N, 150 000 000 F, durée 30 ans. Ascenseur estimé 30 000 000 F, renouvelable après 10 ans. Ascenseur finalement remplacé au bout de 8 ans pour 25 000 000 F.

Décomposition : structure 120 000 000 (150 000 000 − 30 000 000) ; composant ascenseur 30 000 000.

Acquisition :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 23131 |  | 02/01/N — Bâtiments administratifs - structure | 120 000 000 |  |
| 23132 |  | Bâtiments administratifs — composant ascenseur | 30 000 000 |  |
|  | 4812 | Fournisseurs d'investissements |  | 150 000 000 |

Clôture N — dotation : structure 120 000 000/30 = 4 000 000 ; ascenseur 30 000 000/10 = 3 000 000 ; total 7 000 000 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6813 |  | 31/12/N — Dotations aux amort. des immob. corp. | 7 000 000 |  |
|  | 283131 | Amort. bâtiments administratifs - structure |  | 4 000 000 |
|  | 283132 | Amort. bâtiments administratifs - composant ascenseur |  | 3 000 000 |

**Renouvellement de l'ascenseur (02/01/N+8).** Sortie de l'ancien : amort. pratiqués = 30 000 000 × 1/10 × 8 = 24 000 000 ; VNC = 6 000 000.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 283132 |  | 02/01/N+8 — Amort. composant ascenseur | 24 000 000 |  |
| 812 |  | Valeurs comptables des cessions d'immob. corp. | 6 000 000 |  |
|  | 23132 | Bâtiments administratifs — composant ascenseur |  | 30 000 000 |

Immobilisation du nouvel ascenseur :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 23132 |  | 02/01/N+8 — Bâtiments administratifs — composant ascenseur | 25 000 000 |  |
|  | 4812 | Fournisseurs d'investissements |  | 25 000 000 |

> Le renouvellement d'un composant peut augmenter la valeur d'origine de l'immobilisation corporelle.

## Chapitre 5 — Frais d'inspections ou de révisions majeures, sécurité et mise en conformité (Application 34)

Matériel industriel acquis 02/01/N, 190 000 000 F, durée 6 ans. Contrat de révision majeure tous les 2 ans, coût 10 000 000 F. Décomposition par composant :
- structure : 190 000 000 − 10 000 000 = 180 000 000, sur 6 ans → 30 000 000/an ;
- révision majeure (composant) : 10 000 000, sur 2 ans → 5 000 000/an.

Acquisition :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 24111 |  | 02/01/N — Matériel industriel - structure | 180 000 000 |  |
| 24112 |  | Matériel industriel — composant | 10 000 000 |  |
|  | 4812 | Fournisseurs d'investissements |  | 190 000 000 |

Clôture N — dotation totale 35 000 000 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6813 |  | 31/12/N — Dotations aux amort. des immob. corp. | 35 000 000 |  |
|  | 284111 | Amort. matériel industriel - structure |  | 30 000 000 |
|  | 284112 | Amort. matériel industriel - composant |  | 5 000 000 |
