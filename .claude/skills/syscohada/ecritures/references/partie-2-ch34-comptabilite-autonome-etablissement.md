# Partie 2 — Chapitre 34 : Comptabilité autonome par établissement

> Montants pédagogiques. Tableau 5 colonnes : Débit | Crédit | Date et libellé | Montant débit | Montant crédit. Comptes de liaison : **184** Comptes permanents **bloqués** des établissements/succursales (sert de compte capital quand l'autonomie est totale) ; **1851/1852** Comptes permanents **non bloqués** (siège / succursale) ; **186** Comptes de liaison charges ; **187** Comptes de liaison produits.

## Application 108 — Fonctionnement du compte 185

L'entité E envoie 5 000 000 en espèces à sa succursale S (25/06/N). Le 184 est débité au siège du montant mis à disposition, crédité à la succursale du montant reçu.

**Au siège** (aucun mouvement de patrimoine, seul un transfert d'espèces) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 1851 |  | 25/06/N — Comptes permanents non bloqués succursale S | 5 000 000 |  |
|  | 571 | Caisse siège social |  | 5 000 000 |

**À la succursale :**

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 572 |  | 25/06/N — Caisse succursale | 5 000 000 |  |
|  | 1852 | Comptes permanents non bloqués siège |  | 5 000 000 |

Globalement les opérations se neutralisent au niveau de l'entité.

## Application 109 — Fonctionnement du compte 184 (création d'une succursale)

Le 01/12/N, l'entité G ouvre une succursale : fonds de commerce (incorporels 24 M ; constructions 84 M dont terrain 12 M ; matériel de bureau 20 M) réglé 50 % à crédit / 50 % au comptant, + virement 7 M au compte bancaire de la succursale. Total 135 000 000.

**Journal de la succursale :**

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 215 |  | 01/10/N [texte officiel : date « 01/10/N »] — Fonds commercial | 24 000 000 |  |
| 223 |  | Terrains bâtis | 12 000 000 |  |
| 231 |  | Bâtiments sur sol propre | 72 000 000 |  |
| 2441 |  | Matériel de bureau | 20 000 000 |  |
| 521 |  | Banques | 7 000 000 |  |
|  | 184 | Comptes permanents bloqués de la succursale (création) |  | 135 000 000 |

**Journal du siège** (financement : 50 % crédit / 50 % comptant) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 184 |  | 01/10/N — Comptes permanents bloqués de la succursale | 135 000 000 |  |
|  | 162 | Emprunts et dettes auprès des ét. de crédit |  | 67 500 000 |
|  | 521 | Banques |  | 67 500 000 |

En cas de regroupement, le 184 (créditeur en succursale, débiteur au siège) s'annule.

## Application 110 — Opérations de cessions internes

Décembre N. Opérations siège → succursale : (a) virement 18 900 000 ; (b) marchandises du stock siège coût 27 200 000 ; (c) achat à crédit livré directement à la succursale 5 000 000. Opérations de la succursale : (d) achat comptant 16 400 000 ; (e) retrait banque → caisse 8 000 000 ; (f) loyer 1 400 000 + assurance 900 000 par caisse ; (g) livraison de marchandises au siège coût 6 800 000 ; (h) taxe foncière 800 000 ; (i) ventes par banque 31 800 000 ; (j) stock final 600 000. Les cessions internes transitent par **186 (charges)** et **187 (produits)**.

**Journal de la succursale (extraits) :**

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 521 |  | déc. N — Banques (op. a) | 18 900 000 |  |
|  | 185 | Comptes permanents non bloqués du siège |  | 18 900 000 |
| 186 |  | Comptes de liaison charges (op. b) | 27 200 000 |  |
|  | 185 | Comptes permanents non bloqués du siège |  | 27 200 000 |
| 601 |  | Achats de marchandises (op. c) | 5 000 000 |  |
|  | 185 | Comptes permanents non bloqués du siège |  | 5 000 000 |
| 601 |  | Achats de marchandises (op. d) | 16 400 000 |  |
|  | 521 | Banques |  | 16 400 000 |
| 572 |  | Caisse succursale (op. e) | 8 000 000 |  |
|  | 521 | Banques |  | 8 000 000 |
| 622 |  | Locations et charges locatives (op. f) | 1 400 000 |  |
| 625 |  | Prime d'assurance | 900 000 |  |
|  | 572 | Caisse succursale |  | 2 300 000 |
| 185 |  | Comptes permanents non bloqués du siège (op. g) | 6 800 000 |  |
|  | 187 | Comptes de liaison produits |  | 6 800 000 |
| 641 |  | Impôts et taxes directs (op. h) | 800 000 |  |
|  | 521 | Banques |  | 800 000 |
| 521 |  | Banques (op. i) | 31 800 000 |  |
|  | 701 | Ventes de marchandises |  | 31 800 000 |
| 311 |  | Stocks de marchandises (op. j) | 600 000 |  |
|  | 6031 | Variations des stocks de marchandises |  | 600 000 |

Dotation aux amortissements de la succursale (bâtiments 300 000, matériel/mobilier 200 000) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6813 |  | déc. N — Dotations aux amortissements d'exploitation | 500 000 |  |
|  | 2831 | Amortissements des bâtiments |  | 300 000 |
|  | 2844 | Amortissements du matériel et mobilier |  | 200 000 |

**Journal du siège (extraits) — opérations réciproques :**

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 185 |  | déc. N — Comptes permanents non bloqués succursale (op. a) | 18 900 000 |  |
|  | 521 | Banques |  | 18 900 000 |
| 185 |  | Comptes permanents non bloqués du siège (op. b) | 27 200 000 |  |
|  | 187 | Comptes de liaison produits |  | 27 200 000 |
| 185 |  | Comptes permanents non bloqués du siège (op. c) | 5 000 000 |  |
|  | 401 | Fournisseurs, dettes en compte |  | 5 000 000 |
| 186 |  | Comptes de liaison charges (op. g) | 6 800 000 |  |
|  | 185 | Comptes permanents non bloqués du siège |  | 6 800 000 |

**Compte de résultat de la succursale** : ventes 31 800 000 ; charges (achats 21 400 000 ; variation stocks −600 000 ; loyer 1 400 000 ; assurance 900 000 ; impôts 800 000 ; amortissements 500 000) ; **bénéfice 7 400 000**.

## Application 111 — Intégration des comptes de l'établissement dans la comptabilité de l'entité

À la clôture, le siège réincorpore les comptes de la succursale. Dans la succursale, tous les comptes sont virés au **185** ; les comptes **186 et 187 s'annulent** entre établissements. Au siège, le compte de liaison est soldé en faisant apparaître les totaux dans les comptes analogues.

**Écritures de clôture dans la succursale** — solde du 185 (débit 219 500 000 / crédit 39 700 000) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 185 |  | 31/12/N — Comptes permanents non bloqués du siège | 219 500 000 |  |
|  | 186 | Comptes de liaison charges |  | 27 200 000 |
|  | 215 | Fonds commercial |  | 24 000 000 |
|  | 223 | Terrains bâtis |  | 12 000 000 |
|  | 231 | Bâtiments sur sol propre |  | 72 000 000 |
|  | 244 | Matériel et mobilier |  | 20 000 000 |
|  | 311 | Stocks de marchandises |  | 600 000 |
|  | 521 | Banques |  | 32 500 000 |
|  | 572 | Caisse |  | 5 700 000 |
|  | 601 | Achats de marchandises |  | 21 400 000 |
|  | 622 | Locations et charges locatives |  | 1 400 000 |
|  | 625 | Primes d'assurances |  | 900 000 |
|  | 641 | Impôts et taxes directs |  | 800 000 |
|  | 681 | Dotations aux amortissements |  | 500 000 |

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 187 |  | 31/12/N — Comptes de liaison produits | 6 800 000 |  |
| 2831 |  | Amortissements des bâtiments | 300 000 |  |
| 2844 |  | Amortissements du matériel et mobilier | 200 000 |  |
| 6031 |  | Variation des stocks de marchandises | 600 000 |  |
| 701 |  | Ventes de marchandises | 31 800 000 |  |
|  | 185 | Comptes permanents non bloqués du siège |  | 39 700 000 |

**Écritures au journal du siège (31/12/N)** — réintégration (le guide loge le résultat en compte 139/131) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 215 |  | 31/12/N — Fonds commercial | 24 000 000 |  |
| 223 |  | Terrains bâtis | 12 000 000 |  |
| 231 |  | Bâtiments sur sol propre | 72 000 000 |  |
| 244 |  | Matériel et mobilier | 20 000 000 |  |
| 311 |  | Stocks de marchandises | 600 000 |  |
| 521 |  | Banques | 32 500 000 |  |
| 572 |  | Caisse | 5 700 000 |  |
| 187 |  | Comptes de liaison produits | 27 200 000 |  |
|  | 186 | Comptes de liaison charges |  | 6 800 000 |
|  | 185 | Comptes permanents non bloqués de la succursale |  | 179 300 000 |
|  | 139 | Résultat net de la succursale [texte officiel : « Perte » 7 400 000] |  | 7 400 000 |
|  | 2831 | Amortissements des bâtiments |  | 300 000 |
|  | 2844 | Amortissements du matériel et mobilier |  | 200 000 |

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 131 |  | 31/12/N — Résultat net de la succursale | 7 400 000 |  |
|  | 601 | Achats de marchandises |  | 21 400 000 |
|  | 622 | Locations et charges locatives |  | 1 400 000 |
|  | 625 | Primes d'assurances |  | 900 000 |
|  | 641 | Impôts et taxes directs |  | 800 000 |
|  | 681 | Dotations aux amortissements |  | 500 000 |
|  | 6031 | Variation des stocks de marchandises |  | 600 000 |
|  | 701 | Ventes de marchandises |  | 31 800 000 |

> [texte officiel] La 2e réintégration présente une somme débit (7 400 000) inférieure au total des produits/charges repris ; le libellé du résultat oscille entre « 139 … Perte » et « 131 Résultat net ». Transcrit tel quel : les comptes 185, 186 et 187 sont soldés (comptes réciproques) et le résultat de la succursale entre dans le résultat global de l'entité.
