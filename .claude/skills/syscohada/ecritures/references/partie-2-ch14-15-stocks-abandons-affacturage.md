# Partie 2 — Chapitres 14 et 15 : Stocks et en-cours, abandons de créances / affacturage / titrisation

> Montants pédagogiques. Écritures en tableau 5 colonnes : Débit | Crédit | Date et libellé | Montant débit | Montant crédit.

## Chapitre 14 — Stocks et en-cours de production

### Application 52 — Valorisation de stocks (imputation rationnelle)

Produit P1, capacité normale 5 000 unités/mois. Décembre N : production effective 4 000 unités. Coûts : matières 3 500 000 ; MOD 2 200 000 ; frais généraux variables prod. 1 500 000 ; frais généraux fixes prod. 1 000 000 ; administration générale 500 000 ; stockage PF 100 000. Stock final 1 000 unités. Stock initial 2 750 000. FIFO.

**Coût de production** (charges fixes imputées au coefficient 4 000/5 000 = 0,8) :

| Composant | Montant |
|---|---|
| Matières premières | 3 500 000 |
| Main-d'œuvre directe | 2 200 000 |
| Frais généraux variables de production | 1 500 000 |
| Frais généraux fixes (1 000 000 × 80 %) | 800 000 |
| **Coût total de production** | **8 000 000** |

Exclus (charges) : administration générale, stockage des PF. Coût de sous-activité (chômage) = 1 000 000 × 20 % = **200 000** (minore le résultat). Stock final = 1 000 × (8 000 000/4 000 = 2 000) = **2 000 000**.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 736 |  | 31/12/N — Variations des stocks de produits finis | 2 750 000 |  |
|  | 36 | Stocks de produits finis (annulation stock initial) |  | 2 750 000 |
| 36 |  | Stocks de produits finis | 2 000 000 |  |
|  | 736 | Variations des stocks de produits finis (stock final) |  | 2 000 000 |

### Application 53 — Stocks de marchandises (VNR et contrat ferme)

Stock acquis 10 000 000 ; frais de commercialisation restants 2 000 000.

**Hypothèse 1** — prix de vente probable 10 500 000, contrat ferme conclu à 11 500 000. VNR (sur contrat) = 11 500 000 − 2 000 000 = 9 500 000 → dépréciation 10 000 000 − 9 500 000 = 500 000 (sans contrat ferme, elle serait 1 500 000) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6593 |  | 31/12/N — Charges pour dépréciations de stocks | 500 000 |  |
|  | 391 | Dépréciations des stocks de marchandises |  | 500 000 |

**Hypothèse 2** — contrat ferme à 13 500 000. VNR = 11 500 000 > coût 10 000 000 → plus-value latente non comptabilisée (prudence). Pas d'écriture.

### Application 54 — Stocks de matières premières (baisse des cours)

Stock coût d'entrée 10 000 F/unité (9 600 unités), soit prix d'achat + 12 % de charges directes. Prix d'achat en forte baisse, estimés 7 000. La baisse se répercutera sur les prix de vente des PF (vente à perte notable).

**Continuité d'exploitation.** Pas de dépréciation des matières si les PF se vendent au moins à leur coût de revient. Si vente déficitaire, retenir le coût actuel de remplacement des matières :
- coût d'achat (remplacement) 7 000 + charges accessoires 12 % (840) = coût actuel d'achat **7 840**.
- valeur d'entrée = 10 000 × 9 600 = 96 000 000 ; valeur actuelle = 7 840 × 9 600 = 75 264 000 ; dépréciation = **20 736 000** :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6593 |  | 31/12/N — Charges pour dépréciations de stocks | 20 736 000 |  |
|  | 392 | Dépréciations des stocks de matières premières |  | 20 736 000 |

> Si la perte finale sur PF est nettement inférieure (ex. 12 000 000), retenir comme valeur actuelle 96 000 000 − 12 000 000 = 84 000 000.

**Absence de continuité d'exploitation** : retenir la valeur probable nette de réalisation (prix de cession − frais de vente).

## Chapitre 15 — Abandons de créances, affacturage, titrisation

### Application 55 — Abandons de créances

**Opération 1 — abandon commercial** (client stratégique en difficulté), 10 000 000 le 30/09/N.

Chez le fournisseur (charge HAO) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 836 |  | 30/09/N — Abandons de créances consentis | 10 000 000 |  |
|  | 411 | Clients |  | 10 000 000 |

Chez le client (produit HAO) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 401 |  | 30/09/N — Fournisseurs | 10 000 000 |  |
|  | 846 | Abandons de créances obtenus |  | 10 000 000 |

**Opération 2 — abandon financier** (mère-filiale, créance sur prêt LT 12 000 000), le 30/06/N.

Chez la mère :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 836 |  | 30/06/N — Abandons de créances consentis | 12 000 000 |  |
|  | 277 | Créances rattachées à des participations |  | 12 000 000 |

Chez la filiale :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 181 |  | 30/06/N — Dettes liées à des participations | 12 000 000 |  |
|  | 846 | Abandons de créances obtenus |  | 12 000 000 |

### Application 56 — Opérations d'affacturage

**Opération 1 — affacturage classique.** Cession de créances 28 500 000 le 01/07/N ; bordereau reçu le 03/07 ; commission d'affacturage 250 000 ; commission de financement 200 000.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4716 |  | 01/07/N — Compte d'affacturage | 28 500 000 |  |
|  | 411 | Clients |  | 28 500 000 |
| 521 |  | 03/07/N — Banques | 28 050 000 |  |
| 6314 |  | Commissions d'affacturage | 250 000 |  |
| 6745 |  | Intérêts bancaires et sur opérations de financement | 200 000 |  |
|  | 4716 | Compte d'affacturage |  | 28 500 000 |

**Opération 2 — affacturage inversé (reverse factoring).** A demande au factor de régler son fournisseur Tartapillon (dette 20 000 000). Factor verse le 01/07/N au fournisseur, déduction commission de financement 1 000 000. À l'échéance (30/09/N), A règle le factor + commission d'affacturage 20 000.

Chez Tartapillon (fournisseur) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 521 |  | 01/07/N — Banques | 19 000 000 |  |
| 6745 |  | Intérêts bancaires et sur opérations de financement | 1 000 000 |  |
|  | 411 | Clients |  | 20 000 000 |

Chez l'entité A :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 401 |  | 01/07/N — Fournisseurs | 20 000 000 |  |
|  | 4716 | Compte d'affacturage |  | 20 000 000 |
| 4716 |  | 30/09/N — Compte d'affacturage | 20 000 000 |  |
| 6314 |  | Commissions d'affacturage | 20 000 |  |
|  | 521 | Banques |  | 20 020 000 |

### Application 57 — Opérations de titrisation

Entité T cède le 01/04/N des créances clients (valeur nominale 80 000 000) à un FCTC. Le 10/04/N, virement reçu 70 000 000 (prix de cession).

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4716 |  | 01/04/N — Compte de titrisation | 80 000 000 |  |
|  | 411 | Clients |  | 80 000 000 |
| 521 |  | 10/04/N — Banques | 70 000 000 |  |
| 6782 |  | Pertes sur opérations financières | 10 000 000 |  |
|  | 4716 | Compte de titrisation |  | 80 000 000 |

> Le SYSCOHADA recommande le compte 4716 pour les créances sur factors et FCTC.
