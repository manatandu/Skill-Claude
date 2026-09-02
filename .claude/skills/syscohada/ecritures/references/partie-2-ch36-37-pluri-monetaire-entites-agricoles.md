# Partie 2 — Chapitres 36 et 37 : Comptabilité pluri monétaire ; Opérations spécifiques des entités agricoles

> Montants pédagogiques. Tableau 5 colonnes : Débit | Crédit | Date et libellé | Montant débit | Montant crédit.

## Chapitre 36 — Comptabilité pluri monétaire (Applications 113-114)

Trois méthodes : **intégration directe** (mono monétaire, comptabilité tenue en francs), **intégration différée** (comptabilités auxiliaires par devise, liaison via sous-comptes du 184), **intégration mixte** (devises en partie simple + francs en partie double).

### Application 113 — Intégration directe et intégration différée

Opérations : 03/03/N achat 1 000 $ à Princeton payable fin mai par traite (cours 520) ; 30/04 vente comptant 800 000 F ; 18/05 achat de 1 000 $ à 517 ; 31/05 règlement de la traite (cours 522).

#### 1. Intégration directe — cours du jour

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 601 |  | 03/03/N — Achats de marchandises (1 000 × 520) | 520 000 |  |
|  | 401 | Fournisseur Princeton, dettes en compte |  | 520 000 |
| 401 |  | Fournisseur Princeton, dettes en compte | 520 000 |  |
|  | 402 | Fournisseurs, effets à payer |  | 520 000 |
| 5211 |  | 30/04/N — Banques en monnaie nationale | 800 000 |  |
|  | 701 | Ventes de marchandises |  | 800 000 |
| 5215 |  | 18/05/N — Banques en devises (1 000 × 517) | 517 000 |  |
|  | 5211 | Banques en monnaie nationale |  | 517 000 |
| 402 |  | 31/05/N — Fournisseurs, effets à payer (1 000 × 522) | 522 000 |  |
|  | 5215 | Banques en devises |  | 522 000 |
| 5215 |  | Banques en devises (gain sur $ : (522 − 517) × 1 000) | 5 000 |  |
|  | 776 | Gains de change financiers |  | 5 000 |
| 656 |  | Pertes de change sur dettes commerciales ((522 − 520) × 1 000) | 2 000 |  |
|  | 402 | Fournisseurs, effets à payer |  | 2 000 |

**Résultat** : ventes 800 000 + gains 5 000 − achats 520 000 − pertes 2 000 = **283 000**.

#### 2. Intégration directe — cours fixe (standard 507)

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 601 |  | 03/03/N — Achats de marchandises (1 000 × 507) | 507 000 |  |
|  | 401 | Fournisseur Princeton, dettes en compte |  | 507 000 |
| 401 |  | Fournisseur Princeton, dettes en compte | 507 000 |  |
|  | 402 | Fournisseurs, effets à payer |  | 507 000 |
| 5211 |  | 30/04/N — Banques en monnaie nationale | 800 000 |  |
|  | 701 | Ventes de marchandises |  | 800 000 |
| 5215 |  | 18/05/N — Banques en devises (1 000 × 517) | 517 000 |  |
|  | 5211 | Banques en monnaie nationale |  | 517 000 |
| 402 |  | 31/05/N — Fournisseurs, effets à payer (1 000 × 507) | 507 000 |  |
|  | 5215 | Banques en devises |  | 507 000 |
| 676 |  | Pertes de change financières (517 000 − 507 000) | 10 000 |  |
|  | 5215 | Banques en devises |  | 10 000 |

Résultat identique : 800 000 − 507 000 − 10 000 = **283 000**. Le choix cours du jour / cours fixe est neutre sur le résultat, mais non sur sa ventilation (achats vs différences de change).

#### 3. Intégration différée

Comptabilité auxiliaire par devise, liaison via sous-comptes du **184** (« Comptabilité francs » côté devises, « Comptabilité dollars » côté francs). Les comptes tenus en devises sont convertis au cours d'inventaire (fin mai 522).

*Comptabilité en dollars* (montants en $) : 03/03 601 · 401 (1 000) puis 401 · 402 (1 000) ; 18/05 5215 · 1853 (1 000) et 402 · 5212 (1 000).
*Comptabilité en francs* : 30/04 5211 · 701 (800 000) ; 18/05 1852 · 5211 (517 000).

**Intégration en fin de période** — transfert de la comptabilité dollars (au cours 522) puis solde des comptes de liaison :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 601 |  | 31/05/N — Achats de marchandises (transfert compta $) | 522 000 |  |
|  | 1853 | Comptabilité francs |  | 522 000 |
| 1853 |  | Comptabilité francs | 522 000 |  |
|  | 1852 | Comptabilité dollars |  | 517 000 |
|  | 756 | Gains de change sur dettes commerciales |  | 5 000 |

Résultat : 800 000 + 5 000 − 522 000 = **283 000** (identique à l'intégration directe).

### Application 114 — Intégration mixte

Devises en partie simple, francs en partie double. Opérations : (1) vente 1 000 $ à 507 ; (2) règlement 1 000 $ à 510 ; (3) vente 1 200 $ à 508 ; (4) règlement partiel 900 $ à 511 ; (5) frais de déplacement 300 $ à 509 ; (6) vente 1 400 $ à 512. Cours d'inventaire 510.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 411 |  | 03/03/N — Clients US | 507 000 |  |
|  | 701 | Ventes de marchandises (1 000 $ à 507) |  | 507 000 |
| 5215 |  | Banques en devises | 510 000 |  |
|  | 411 | Clients US (1 000 $ à 510) |  | 510 000 |
| 411 |  | 30/04/N — Clients US | 609 600 |  |
|  | 701 | Ventes de marchandises (1 200 $ à 508) |  | 609 600 |
| 5215 |  | 18/05/N — Banques en devises | 459 900 |  |
|  | 411 | Clients US (900 $ à 511) |  | 459 900 |
| 6384 |  | 31/05/N — Missions (300 $ à 509) | 152 700 |  |
|  | 5215 | Banques en devises |  | 152 700 |
| 411 |  | Clients US | 716 800 |  |
|  | 701 | Ventes de marchandises (1 400 $ à 512) |  | 716 800 |

**Ajustement à l'inventaire (cours 510).**
- Compte « Clients US » : solde en devises 3 600 − 1 900 = 1 700 $ ; solde réel 1 700 × 510 = 867 000 ; différence de conversion **3 500** (à ajouter au débit) [texte officiel : le guide donne un solde en francs de « 863 500 » puis « 867 000 − 853 500 = 3 500 » — chiffres intermédiaires internes incohérents ; le montant retenu pour l'écriture est 3 500].
- Compte « Banques dollars » : solde en devises 1 900 − 300 = 1 600 $ ; solde réel 1 600 × 510 = 816 000 ; différence de conversion **1 200** (à ajouter au crédit).

Écritures d'ajustement (31/12/N) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 411 |  | 31/12/N — Clients US (différence de conversion) | 3 500 |  |
|  | 4791 | Écarts de conversion passif |  | 3 500 |
| 676 |  | Pertes de change (ajustement compte Banques dollars) | 1 200 |  |
|  | 5215 | Banques en devises |  | 1 200 |

## Chapitre 37 — Opérations spécifiques des entités agricoles (Application 115)

Comptes clés : **2245** Amélioration du fonds ; **2465** Plantations agricoles / **2496** Actifs biologiques en cours / **2846** Amortissements des actifs biologiques ; **2462** Cheptel, animaux reproducteurs ; **1047** Prélèvement autoconsommation / **724** Production auto-consommée ; **654 / 754** valeurs comptables / produits des cessions courantes d'immobilisations ; **414** Créances sur cessions courantes d'immobilisations.

**Opération 1 — achat de fumures à crédit (01/01/N, 362 000)** : amélioration du fonds.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 2245 |  | 01/01/N — Amélioration du fonds | 362 000 |  |
|  | 4812 | Fournisseurs d'investissement (achat de fumures) |  | 362 000 |

**Opération 2 — hévéas entrés en production le 01/01/N**, plantés le 02/01/N-5, plein rendement 40 ans, valeur 150 000 000. Transfert de l'actif biologique en cours vers les plantations, puis amortissement 150 000 000 / 40 = 3 750 000 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 2465 |  | 01/01/N — Plantations agricoles | 150 000 000 |  |
|  | 2496 | Actifs biologiques en cours |  | 150 000 000 |
| 6813 |  | 31/12/N — Dotation aux amort. des immobilisations | 3 750 000 |  |
|  | 2846 | Amortissements des actifs biologiques |  | 3 750 000 |

**Opération 3 — autoconsommation de fruits (01/03/N, 50 000) :**

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 1047 |  | 01/03/N — Prélèvement autoconsommation | 50 000 |  |
|  | 724 | Production auto-consommée |  | 50 000 |

**Opération 4 — cession d'une vache laitière.** Achetée 01/07/N à 800 000 (production de lait 8 ans), cédée 01/07/N+2 à 1 000 000 (cessions récurrentes → cessions **courantes**). Dotation complémentaire 01/01→01/07/N+2 : 800 000 × 1/8 × 6/12 = 50 000. Cumul amortissements 800 000 × 1/8 × 24/12 = 200 000 ; VNC 600 000.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6813 |  | 01/01/N [texte officiel : date « 01/01/N »] — Dotation aux amort. des immobilisations | 50 000 |  |
|  | 2846 | Amortissement des actifs biologiques |  | 50 000 |
| 654 |  | 01/01/N — Valeurs comptables des cessions courantes d'immo. | 600 000 |  |
| 2846 |  | Amortissement des actifs biologiques | 200 000 |  |
|  | 2462 | Cheptel, animaux reproducteurs |  | 800 000 |
| 414 |  | 01/03/N [texte officiel : date « 01/03/N »] — Créances sur cessions courantes d'immo. | 1 000 000 |  |
|  | 754 | Produits des cessions courantes d'immobilisations |  | 1 000 000 |
