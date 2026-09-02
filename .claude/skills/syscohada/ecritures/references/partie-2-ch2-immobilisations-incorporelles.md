# Partie 2 — Chapitre 2 : Brevets, marques, logiciels, sites internet, coût d'obtention du contrat, fonds commercial

> Montants pédagogiques (KF = millier de francs). Écritures en tableau 5 colonnes : Débit | Crédit | Date et libellé | Montant débit | Montant crédit. Critères d'activation → `audcif-acte-uniforme` ; numéros de comptes → `syscohada-comptes`.

## Application 26 — Brevets acquis et réglés au moyen de redevances périodiques

Brevet acquis le 01/01/N : versement immédiat 50 000 KF + redevances annuelles de 1 % du CA, payables 3 ans le 31/12. Taux d'actualisation 10 %. CA prévisionnel annuel 2 500 000 KF. Exploitation prévue 10 ans. CA HT réel : N = 3 250 000 ; N+1 = 2 250 000 ; N+2 = 2 000 000 KF.

**Principe.** La valeur actuelle d'un actif incorporel acquis contre redevance sur CA s'estime soit par la valeur actualisée des redevances probables (si évaluation fiable), soit par la valeur des droits d'enregistrement. Si les redevances ne sont pas évaluables de façon fiable, elles sont portées en charges (**634 Redevances pour brevets, licences, concessions et droits similaires**) et seule la partie fixe est immobilisée.

**Coût du brevet.**
- CA évaluable de façon fiable : Valeur d'entrée = 50 000 + (2 500 000 × 1 %) × [1 − (1,10)⁻³] / 0,10 = **112 170 KF**.
- CA non évaluable de façon fiable : Valeur d'entrée = **50 000 KF**.

**Comptabilisation au 01/01/N**

CA évaluable de façon fiable :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 2121 |  | 01/01/N — Brevets | 112 170 |  |
|  | 521 | Banques |  | 50 000 |
|  | 4811 | Fournisseurs d'investissements |  | 62 170 |

CA non évaluable de façon fiable :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 2121 |  | 01/01/N — Brevets | 50 000 |  |
|  | 521 | Banques |  | 50 000 |

**Règlement des redevances (31/12/N, N+1, N+2)** — assiette = CA réel × 1 %.

CA fiable, 31/12/N (3 250 000 × 1 % = 32 500) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4811 |  | 31/12/N — Fournisseurs d'investissements | 32 500 |  |
|  | 521 | Banques |  | 32 500 |

CA non fiable, 31/12/N :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6342 |  | 31/12/N — Redevances pour brevets (3 250 000 × 1 %) | 32 500 |  |
|  | 521 | Banques |  | 32 500 |

31/12/N+1 (2 250 000 × 1 % = 22 500) : même schéma, 4811/521 (fiable) ou 6342/521 (non fiable).

**Amortissement** (durée 10 ans) : fiable 112 170 / 10 = 11 217 ; non fiable 50 000 / 10 = 5 000, par 6812 · 2812.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6812 |  | 31/12/N — Dotations aux amort. des immob. incorp. | 11 217 |  |
|  | 2812 | Amortissements des brevets |  | 11 217 |

**31/12/N+2 (CA fiable)** — le compte 4811 est soldé et l'excédent versé passe en charges HAO. Solde 4811 après 2 règlements = 62 170 − (32 500 + 22 500) = 7 170 ; règlement N+2 = 2 000 000 × 1 % = 20 000.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4811 |  | 31/12/N+2 — Fournisseurs d'investissements | 7 170 |  |
| 831 |  | Charges H.A.O. constatées (20 000 − 7 170) | 12 830 |  |
|  | 521 | Banques |  | 20 000 |

## Application 27 — Marques

**Marque X** : développée en interne (coût 50 000 KF). Les dépenses de création interne d'une marque ne peuvent être distinguées du coût de développement de l'activité et ne sont pas évaluables de façon fiable → **non immobilisables, comptabilisées en charges**.

**Marque Y** : acquise le 01/10/N-4 pour 100 000 KF (chèque), durée d'utilité indéfinie ; l'entité décide le 01/01/N+1 de l'arrêter le 31/12/N+2 (durée devient définie : 2 ans).

Acquisition :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 214 |  | 01/10/N-4 — Marques | 100 000 |  |
|  | 4811 | Fournisseurs d'investissements — immob. incorp. |  | 100 000 |
| 4811 |  | Fournisseurs d'investissements — immob. incorp. | 100 000 |  |
|  | 521 | Banques |  | 100 000 |

Clôture N-4 à N : durée d'utilité indéfinie → **non amortissable**. À partir du 01/01/N+1, durée devient définie (2 ans), dotation N+1 = 100 000 / 2 = 50 000.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6812 |  | 31/12/N+1 — Dotations aux amort. des immob. incorp. | 50 000 |  |
|  | 2814 | Amortissements des marques |  | 50 000 |

## Application 28 — Logiciels (créé en interne)

Logiciel de calcul des coûts par méthode ABC. Phases : Q4 N-1 — étude préalable 18 000 000, analyse fonctionnelle 30 000 000, analyse organique 54 000 000. Q1 N — programmation 15 000 000, tests/jeux d'essai 60 000 000, documentation utilisateurs 39 000 000. Maintenance N = 15 000 000. Conditions d'immobilisation remplies. Durée 5 ans, mise en service 01/04/N.

En cours d'exercice, tous les frais en charges par nature (6…/comptes de tiers).

**Coût de production activable** : analyse organique (N-1) + phases Q1 N (hors étude préalable et analyse fonctionnelle, qui restent en charges).

Clôture N-1 — production immobilisée en cours (analyse organique 54 000 000) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 2193 |  | 31/12/N-1 — Logiciels en cours | 54 000 000 |  |
|  | 721 | Production immobilisée — immob. incorporelle |  | 54 000 000 |

Fin des travaux 01/04/N — coût total = 54 000 000 + (15 000 000 + 60 000 000 + 39 000 000) = **168 000 000** :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 2131 |  | 01/04/N — Logiciels | 168 000 000 |  |
|  | 2193 | Logiciels en cours |  | 54 000 000 |
|  | 721 | Production immobilisée incorporelle (114 000 000) |  | 114 000 000 |

Maintenance N (15 000 000) : charge par nature.

Inventaire 31/12/N — amortissement (168 000 000 × 1/5 × 9/12) = 25 200 000 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6812 |  | 31/12/N — Dotations aux amort. des immob. incorp. | 25 200 000 |  |
|  | 2813 | Amortissements des logiciels |  | 25 200 000 |

## Application 29 — Sites internet (e-commerce)

Site e-commerce répondant aux critères d'activation. Phases : études préalables 425 000 ; sélection fournisseurs 100 000 ; nom de domaine 295 000 ; logiciel d'exploitation 375 000 ; logiciels et bases de données 1 950 000 ; codes 260 000 ; documentation technique 550 000 ; enregistrement moteurs de recherche 300 000. Mise en service 01/11/N, durée 5 ans.

**Non activables (charges)** : études de faisabilité, sélection des fournisseurs (dépenses de recherche) et enregistrement auprès des moteurs de recherche (exploitation).

**Coût de production du site** :

| Élément | Montant |
|---|---|
| Obtention nom de domaine et immatriculation | 295 000 |
| Développement du logiciel d'exploitation | 375 000 |
| Développement des codes | 260 000 |
| Développement des logiciels et bases de données | 1 950 000 |
| Documentation technique | 550 000 |
| **Coût de production du site** | **3 430 000** |

Base amortissable = 3 430 000 − 295 000 = **3 135 000** (nom de domaine non amortissable).

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 2132 |  | 01/11/N — Sites internet | 3 430 000 |  |
|  | 721 | Production immobilisée — immob. incorporelles |  | 3 430 000 |

Amortissement N : (3 135 000 / 5) × 2/12 = 104 500 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6812 |  | 31/12/N — Dotations aux amort. des immob. incorp. | 104 500 |  |
|  | 2813 | Amortissements du site internet |  | 104 500 |

## Application 30 — Coût d'obtention du contrat

Appel d'offres remporté (services sur 5 ans). Frais : juridiques externes (fiscaux) 750 000 ; déplacement 250 000 ; honoraires avocat + droits d'enregistrement 9 000 000. Total 10 000 000 F, réglés au comptant.

**Analyse.** Seuls les honoraires d'avocat et droits d'enregistrement (9 000 000), recouvrables et directement liés à l'obtention du contrat, sont activés. Les frais juridiques fiscaux et de déplacement ont été engagés indépendamment de l'obtention → charges.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 2182 |  | 31/12/N — Coûts d'obtention du contrat | 9 000 000 |  |
|  | 4811 | Fournisseurs d'investissement — immob. incorp. |  | 9 000 000 |
| 4811 |  | 31/12/N — Fournisseurs d'investissement — immob. incorp. | 9 000 000 |  |
|  | 521 | Banques |  | 9 000 000 |

Amortissement sur 8 ans (contrat 5 ans + renouvellement prévu 3 ans) : 9 000 000 / 8 = 1 125 000 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6811 |  | 31/12/N — Dotations aux amort. des immob. incorp. | 1 125 000 |  |
|  | 2813 | Amortissements des autres droits et valeurs similaires |  | 1 125 000 |

## Application 31 — Fonds commercial

Fonds de commerce acquis le 01/06/N pour 250 000 000 F. Actifs identifiables expertisés : brevet 40 000 000 ; droit au bail 25 000 000 ; licence 5 000 000 ; matériel et outillage industriel 87 500 000 (dont 27 500 000 d'outillage) ; matériel automobile 50 000 000.

Fonds commercial = 250 000 000 − (40 000 000 + 25 000 000 + 5 000 000 + 87 500 000 + 50 000 000) = **42 500 000**.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 2121 |  | 01/06/N — Brevets | 40 000 000 |  |
| 2122 |  | Licences | 5 000 000 |  |
| 2411 |  | Matériel industriel | 60 000 000 |  |
| 2412 |  | Outillage industriel | 27 500 000 |  |
| 215 |  | Fonds commercial | 42 500 000 |  |
| 216 |  | Droit au bail | 25 000 000 |  |
| 2451 |  | Matériel automobile | 50 000 000 |  |
|  | 481 | Fournisseurs d'investissements |  | 250 000 000 |
