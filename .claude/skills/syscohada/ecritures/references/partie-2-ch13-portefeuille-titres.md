# Partie 2 — Chapitre 13 : Portefeuille titres

> Montants pédagogiques. Écritures en tableau 5 colonnes : Débit | Crédit | Date et libellé | Montant débit | Montant crédit. Les frais d'acquisition des titres cotés à court terme sont enregistrés séparément (502x/501x — comptes divisionnaires 6) ; pour les titres immobilisés et de participation, les frais sont incorporés au coût.

## Application 48 — Acquisition de titres

Commission 1,5 % du montant de chaque transaction, virements bancaires.
- 05/06 : 5 000 actions SICAV cotées à 12 000 (hausse anticipée à court terme) → titres de placement cotés.
- 09/06 : participation 80 % d'une entité non cotée, 2 500 actions à 16 000 → titres de participation.
- 16/06 : 1 500 obligations à 20 000, conservées durablement (gestion de portefeuille) → TIAP.
- 24/06 : bons du Trésor 3 000 000, placement court terme → titres de placement.
- 30/06 : 1 000 actions cotées à 18 000 (2 % du capital), conservées durablement → titres immobilisés.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 5022 |  | 05/06/N — Actions cotées (5 000 × 12 000) | 60 000 000 |  |
| 5026 |  | Frais d'acquisition des actions (60 000 000 × 1,5 %) | 900 000 |  |
|  | 521 | Banques (acquisition titres SICAV) |  | 60 900 000 |
| 261 |  | 09/06/N — Titres de participation, sociétés sous contrôle exclusif | 40 600 000 |  |
|  | 521 | Banques (2 500 × 16 000) + 1,5 % |  | 40 600 000 |
| 2741 |  | 16/06/N — Titres immobilisés de l'activité de portefeuille (TIAP) | 30 450 000 |  |
|  | 521 | Banques (1 500 × 20 000) + 1,5 % |  | 30 450 000 |
| 5011 |  | 24/06/N — Titres du Trésor à court terme | 3 000 000 |  |
| 5016 |  | Frais d'acquisition des titres de Trésor (× 1,5 %) | 45 000 |  |
|  | 521 | Banques |  | 3 045 000 |
| 2746 |  | 30/06/N — Titres immobilisés — Actions | 18 270 000 |  |
|  | 521 | Banques (1 000 × 18 000) + 1,5 % |  | 18 270 000 |

## Application 49 — Versement restant à effectuer sur titres non libérés

Entité A souscrit 20 000 actions de B (nominal 10 000, prime d'émission 2 000), libérées de moitié à la souscription le 01/05/N. A paie sa souscription + 1 000 000 de frais. Titres immobilisés.

Souscription (01/05/N) — coût = 20 000 × (10 000 + 2 000) + 1 000 000 = 241 000 000 ; libéré = 20 000 × (5 000 + 2 000) + 1 000 000 = 141 000 000 ; restant = 100 000 000 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 2746 |  | 01/05/N — Titres immob. actions | 241 000 000 |  |
|  | 472 | Versement restant à effectuer sur titres non libérés |  | 100 000 000 |
|  | 521 | Banques |  | 141 000 000 |

Libération de la 2e moitié (appelée 30/09, virement 08/11) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 472 |  | 08/11/N — Versement restant à effectuer sur titres non libérés | 100 000 000 |  |
|  | 521 | Banques |  | 100 000 000 |

## Application 50 — Cession de titres de participation

Titres COCO, valeur d'origine 50 000 000, dépréciation existante 6 000 000. Cession 15/08/N à crédit 48 000 000.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 816 |  | 15/08/N — Valeurs comptables des cessions d'immob. financières | 50 000 000 |  |
|  | 274 | Titres immobilisés |  | 50 000 000 |
| 4856 |  | Créances sur cessions d'immobilisations financières | 48 000 000 |  |
|  | 826 | Produits des cessions d'immobilisations financières |  | 48 000 000 |
| 2974 |  | Dépréciations des titres immobilisés | 6 000 000 |  |
|  | 7972 | Reprises de dép. des immobilisations financières |  | 6 000 000 |

Incidence résultat global : **+4 000 000** = +6 000 000 (financier) − 2 000 000 (HAO : 48 000 000 − 50 000 000).

## Application 51 — Cession de titres de placement

Portefeuille de 3 000 titres de F (entité D) au 01/09/N : 01/04/N-1 → 1 000 à 12 000 ; 01/09/N-1 → 500 à 12 500 ; 01/04/N → 1 200 à 11 000 ; 01/07/N → 300 à 10 000. Cours moyen déc. N-1 = 12 050. Cession de 2 500 titres à crédit, prix global 29 000 000.

**Dépréciation au 31/12/N-1.** Valeur d'entrée (1 000 × 12 000 + 500 × 12 500) = 18 250 000 ; valeur (1 500 × 12 050) = 18 075 000 ; dépréciation = 175 000 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6795 |  | 31/12/N-1 — Charges pour dép. sur titres de placement | 175 000 |  |
|  | 590 | Dépréciations de titres de placement |  | 175 000 |

**Cession (01/09/N) — méthode PEPS** (art. 44 Acte uniforme). Titres cédés : 1 000 (01/04/N-1) + 500 (01/09/N-1) + 1 000 sur 1 200 (01/04/N). Valeur d'entrée = 12 000 000 + 6 250 000 + 11 000 000 = 29 250 000 ; perte = 250 000 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4721 |  | 01/09/N — Créances sur cession de titres de placement | 29 000 000 |  |
| 6771 |  | Perte sur cessions des titres de placement | 250 000 |  |
|  | 50 | Titres de placement |  | 29 250 000 |

Portefeuille restant (PEPS) : 200 × 11 000 + 300 × 10 000 = 5 200 000.

**Variante — coût moyen pondéré.** Valeur totale = 34 450 000 pour 3 000 titres → CMP = 11 483,3333. Titres sortis = 11 483,3333 × 2 500 = 28 708 333 ; gain = 291 667 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4721 |  | 01/09/N — Créances sur cession de titres de placement | 29 000 000 |  |
|  | 50 | Titres de placement |  | 28 708 333 |
|  | 777 | Gains sur cessions de titres de placement |  | 291 667 |

Portefeuille restant (CMP) = 34 450 000 − 28 708 333 = 5 741 667 (500 × 11 483,3333).

> Le choix PEPS/CMP influe sur le résultat et l'évaluation des titres restants → respecter la permanence des méthodes.
