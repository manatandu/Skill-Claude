# Partie 2 — Chapitre 20 : Emprunt obligataire

> Montants pédagogiques. Écritures en tableau 5 colonnes : Débit | Crédit | Date et libellé | Montant débit | Montant crédit.

**Principes.** À l'émission, la dette constatée = prix d'émission. La prime de remboursement (prix de remboursement − prix d'émission) est étalée sur la durée : au prorata du **nombre d'obligations échues** (amortissements constants, dégressifs, annuités constantes) ou au prorata des **intérêts courus** (remboursement in fine), par 6714 Primes de remboursement des obligations · 1661 Intérêts courus sur emprunts obligataires. Les frais d'émission (6316 Frais d'émission d'emprunts) passent en charge de l'exercice d'engagement.

## Application 78 — Emprunt obligataire avec prime (amortissements constants)

01/01/N : 10 000 obligations, nominal 5 000, prix d'émission 4 900, prix de remboursement 5 100, taux 5 %, amortissements constants sur 4 ans, frais d'émission 750 000. Échéances 31/12 (N à N+3).

**Souscription et réception des fonds (10 000 × 4 900 = 49 000 000)** :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 47131 |  | 01/01/N — Obligataires-obligations à placer (10 000 × 4 900) | 49 000 000 |  |
|  | 1611 | Emprunts obligataires ordinaires |  | 49 000 000 |
| 47132 |  | Obligataires, compte de souscription | 49 000 000 |  |
|  | 47131 | Obligataires-obligations à placer |  | 49 000 000 |
| 521 |  | Banques | 49 000 000 |  |
|  | 47132 | Obligataires, compte de souscription |  | 49 000 000 |

> Prise ferme par une banque : écriture unique 521 · 1611 (49 000 000).

Frais d'émission : 6316 · 521 (750 000).

**Tableau de remboursement** (coupon 10 000 × 5 % × 5 000 = 500/oblig ; 2 500 oblig amorties/an ; valeur amortie 2 500 × 5 100 = 12 750 000) :

| Exercice | Oblig. vivantes | Charges d'intérêts | Oblig. amorties | Valeur | Annuité |
|---|---|---|---|---|---|
| N | 10 000 | 5 000 000 | 2 500 | 12 750 000 | 17 750 000 |
| N+1 | 7 500 | 3 750 000 | 2 500 | 12 750 000 | 16 500 000 |
| N+2 | 5 000 | 2 500 000 | 2 500 | 12 750 000 | 15 250 000 |
| N+3 | 2 500 | 1 250 000 | 2 500 | 12 750 000 | 14 000 000 |
| **Total** | | 12 500 000 | 10 000 | 51 000 000 | 63 500 000 |

Prime totale = 10 000 × (5 100 − 4 900) = 2 000 000, étalée au prorata des obligations échues : 500 000/an.

**Règlement 1re annuité (31/12/N)** :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 1611 |  | 31/12/N — Emprunts obligataires ordinaires (12 750 000 − 500 000) | 12 250 000 |  |
| 6711 |  | Charges d'intérêts | 5 000 000 |  |
| 6714 |  | Prime de remboursement des obligations | 500 000 |  |
|  | 521 | Banques |  | 17 750 000 |

Annuités suivantes : même schéma (N+1 : 12 250 000 / 3 750 000 / 500 000 → 16 500 000, etc.).

## Application 79 — Emprunt obligataire avec prime (remboursement in fine)

01/01/N : 5 000 obligations, nominal 10 000, prix d'émission 9 500, remboursement in fine le 31/12/N+4 à 10 500. Intérêts 6 %/an, à terme échu.

**Souscription (5 000 × 9 500 = 47 500 000)** : mêmes écritures via 47131/47132/521 · 1611.

**Tableau** (coupon 5 000 × 6 % × 10 000 = 3 000 000/an ; remboursement final 5 000 × 10 500 = 52 500 000) :

| Exercice | Oblig. vivantes | Charges d'intérêts | Amortissement | Annuité |
|---|---|---|---|---|
| N à N+3 | 5 000 | 3 000 000 | — | 3 000 000 |
| N+4 | 5 000 | 3 000 000 | 52 500 000 | 55 500 000 |
| **Total** | | 15 000 000 | 52 500 000 | 67 500 000 |

Prime totale = 5 000 × (10 500 − 9 500) = 5 000 000, étalée **au prorata des intérêts courus** (in fine) : 5 000 000 × 3 000 000/15 000 000 = 1 000 000/an.

**Règlement 1re annuité (31/12/N)** :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6711 |  | 31/12/N — Charges d'intérêts | 3 000 000 |  |
|  | 521 | Banques |  | 3 000 000 |

Rattachement de la prime (31/12/N) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6714 |  | 31/12/N — Primes de remboursement des obligations | 1 000 000 |  |
|  | 1661 | Intérêts courus sur emprunts obligataires |  | 1 000 000 |

## Application 80 — Emprunt obligataire convertible en actions

01/01/N : 25 000 obligations de 15 000 convertibles à chaque date anniversaire à partir de 2 ans, ou remboursables en numéraire au terme de 6 ans. Émission à 13 000, prise ferme. Rapport d'échange : 4 obligations (nominal 10 000) contre 3 actions. Le 01/01/N+2, 4 000 obligations converties, aucune remboursée. Prime totale provisionnée.

**Principe.** Seul le prix d'émission est constaté (1612 Emprunts obligataires convertibles) ; la prime n'est pas comptabilisée ni étalée. Une provision pour risque de payer la prime (cas de remboursement numéraire) est dotée à la clôture d'émission (69 · 19) et reprise en cas de conversion (19 · 79). Pour les obligations remboursées, la quote-part de provision est reprise et la prime portée au débit du 6714.

**Émission (25 000 × 13 000 = 325 000 000)** + provision de prime (25 000 × (15 000 − 13 000) = 50 000 000) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 521 |  | 01/01/N — Banques | 325 000 000 |  |
|  | 1612 | Emprunts obligataires convertibles |  | 325 000 000 |
| 6971 |  | 31/12/N — Dotations aux prov. financières pour risques et charges | 50 000 000 |  |
|  | 1988 | Autres provisions pour divers risques et charges |  | 50 000 000 |

**Conversion (01/01/N+2).** 4 000 oblig. → 4 000 × 3/4 = 3 000 actions ; augmentation de capital 3 000 × 10 000 = 30 000 000 ; prime de conversion = (4 000 × 13 000) − 30 000 000 = 22 000 000 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 1612 |  | 01/01/N+2 — Emprunts obligataires convertibles (4 000 × 13 000) | 52 000 000 |  |
|  | 1013 | Capital souscrit, appelé, versé, non amorti |  | 30 000 000 |
|  | 1054 | Prime de conversion |  | 22 000 000 |

Reprise de la provision correspondant aux 4 000 obligations converties (4 000 × (15 000 − 13 000) = 8 000 000) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 1988 |  | 31/12/N+3 — Autres provisions divers pour risques et charges | 8 000 000 |  |
|  | 7971 | Reprises de prov. et dép. financières pour risques et charges |  | 8 000 000 |
