# Partie 2 — Chapitre 9 : Réserve de propriété

> Montants pédagogiques. Écritures en tableau 5 colonnes : Débit | Crédit | Date et libellé | Montant débit | Montant crédit. Comptes classe 9 = engagements hors bilan.

**Principe.** L'entité peut scinder ses comptes d'achats/ventes/immobilisations/stocks pour identifier les opérations avec clause de réserve de propriété (R/P), et utiliser la classe 9 (chez l'acheteur : engagement donné ; chez le vendeur : engagement obtenu). Utile chez l'acquéreur pour distinguer les biens juridiquement non encore siens (notion de risque, risque de faillite/discontinuité), et chez le vendeur pour identifier ses créances garanties par la propriété du bien.

## Application 39 — Réserve de propriété (acheteur)

Matériel industriel acquis 02/01/N avec clause R/P, 50 000 000. Règlement 01/06/N.

Acquisition + engagement donné (02/01/N) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 24116 |  | 02/01/N — Matériel industriel avec clause de R/P | 50 000 000 |  |
|  | 4816 | Fournisseurs d'investissements — Réserve de propriété |  | 50 000 000 |
| 9183 |  | Contrepartie des engagements accordés | 50 000 000 |  |
|  | 9083 | Achats avec clause de réserve de propriété |  | 50 000 000 |

Règlement + annulation de l'engagement (01/06/N) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4816 |  | 01/06/N — Fournisseurs d'investissements — R/P | 50 000 000 |  |
|  | 521 | Banques |  | 50 000 000 |
| 9083 |  | Achats avec clause de réserve de propriété | 50 000 000 |  |
|  | 9183 | Contrepartie des engagements accordés |  | 50 000 000 |
| 2411 |  | Matériel industriel | 50 000 000 |  |
|  | 24116 | Matériel industriel avec clause de R/P |  | 50 000 000 |

## Application 40 — Réserve de propriété (vendeur)

SOVAL vend à MK le 20/12/N une chaîne d'embouteillage 100 000 000 F (amortissable 6 ans), crédit de 60 000 000 au 31/12/N+1 après paiement comptant de 40 000 000. MK en difficulté, n'honore pas l'échéance du 30/11/N+1. Au 31/12/N+1, matériel mal entretenu/endommagé toujours chez MK, valeur nette probable de réalisation 42 000 000.

**Vente + engagement obtenu (20/12/N)** :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4116 |  | 20/12/N — Clients, réserve de propriété | 100 000 000 |  |
|  | 701 | Ventes de marchandises |  | 100 000 000 |
| 9043 |  | Ventes avec clause de réserve de propriété | 100 000 000 |  |
|  | 9143 | Contrepartie des engagements obtenus |  | 100 000 000 |

**Provision (31/11/N+1).** Créance 60 000 000 ; valeur probable de réalisation après revendication 42 000 000 ; perte probable = 18 000 000.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4162 |  | 31/11/N+1 — Créances douteuses | 60 000 000 |  |
|  | 4116 | Clients, réserve de propriété |  | 60 000 000 |
| 6594 |  | 31/12/N+1 — Charges pour dépréciations sur créances | 18 000 000 |  |
|  | 4912 | Dépréciations des comptes clients (créances douteuses) |  | 18 000 000 |

**Revendication (20/02/N+2).** Restitution obtenue, valeur probable de réalisation nette 37 000 000 → entrée du bien à sa « valeur actuelle » :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 601 |  | 20/02/N+2 — Achats marchandises | 37 000 000 |  |
|  | 4162 | Créances douteuses |  | 37 000 000 |

**Revente insuffisante (10/04/N+2).** Prix net 40 000 000 ; frais de revente 2 000 000 ; montant récupéré = 38 000 000. Correction de la valeur d'entrée (+1 000 000) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 521 |  | 10/04/N+2 — Banques | 40 000 000 |  |
|  | 701 | Ventes de marchandises |  | 40 000 000 |
| 601 |  | Achats de marchandises (40 000 000 − 2 000 000 − 37 000 000) | 1 000 000 |  |
|  | 4162 | Créances douteuses |  | 1 000 000 |

Solde 4162 = 60 000 000 − (37 000 000 + 1 000 000) = **22 000 000** (débiteur).

**Inventaire fin N+2.** Syndic : récupération 30 % des créances chirographaires → perte probable 70 % = 22 000 000 × 0,7 = 15 400 000 ; la provision de 18 000 000 est réduite de 2 600 000.

**Variante — revente supérieure au restant dû.** Prix 65 000 000, frais 3 000 000, récupéré 62 000 000 ; valeur d'entrée majorée de 37 000 000 à 62 000 000 (+25 000 000) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 601 |  | 14/04/N+2 — Achats de marchandises | 25 000 000 |  |
|  | 4162 | Créances douteuses |  | 25 000 000 |

Solde 4162 = 60 000 000 − (37 000 000 + 25 000 000) = 2 000 000 créditeur → remboursement :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4162 |  | 31/04/N+2 — Créances douteuses MK | 2 000 000 |  |
|  | 521 | Banque X |  | 2 000 000 |
