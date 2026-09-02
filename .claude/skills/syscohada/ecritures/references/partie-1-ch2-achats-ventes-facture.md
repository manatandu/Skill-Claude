# Partie 1 — Chapitre 2 : Achats et ventes de biens et de services

> **Montants et taux pédagogiques.** Les nombres des Applications (TVA 10 %, 20 %…) sont des illustrations, pas les taux réels. Pour les taux RDC (TVA 16 %, etc.) → `fiscalite-rdc-socle`. Écritures présentées en tableau 5 colonnes : Débit (compte débité) | Crédit (compte crédité) | Date et libellé | Montant débit | Montant crédit.

## Section 1 — Opérations brutes

### 1.1 Achats

Trois types d'achats :
- **Biens durables** (investissements/immobilisations) : crédités au **481** Fournisseurs d'investissements ou **404** Fournisseurs, acquisitions courantes d'immobilisations (traités au ch. 5).
- **Biens consommables** : crédités au **401** Fournisseurs d'exploitation, en charges classe **60**, pour le montant net de taxes récupérables + frais accessoires :
  - 601 marchandises (revendues sans transformation) ; 602 matières premières (transformées) ; 604 matières consommables (utilisées sans se retrouver dans le produit) ; 602 fournitures liées ; 604 fournitures non liées ; 608 emballages non immobilisés.
  - Frais accessoires : directement en 601/602/604/608, ou en frais sur achats **6015, 6025, 6045, 6085**.
- **Services** : charges en **61, 62, 63** : 61 transports (hors courrier/télécom) ; 621-625 services rattachés aux immobilisations ; 626-638 services d'exploitation et financiers. Supposés immédiatement consommés.

**Recommandation SYSCOHADA (flux de trésorerie)** : contrepartie systématique = **401** pour les achats de biens/services (hors immobilisations) ; **481 ou 404** pour les immobilisations.

### Application 1 — Acquisition de matériels et fournitures de bureau

Facture n°1 : 1 caisse enregistreuse 300, 10 ordinateurs 200 = 2 000, 100 ramettes à 5 = 500. Sous-total 2 800, transport 10 % = 280, TVA 10 % = 308, net à payer 3 388.
Données : caisse = immobilisation du détaillant (rubrique 26) ; ordinateurs destinés à la revente (marchandises) ; papier destiné à la revente à raison de 90 paquets (10 ramettes = matières consommables non stockées) ; TVA récupérable.

Variante avec frais séparés :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 2443.26 |  | Matériel bureautique (300 + 10 %×300) | 330 |  |
| 6011.26 |  | Achats marchandise ordinateurs | 2 000 |  |
| 6015.26 |  | Frais sur achats ordinateurs | 200 |  |
| 6011.17 |  | Achats marchandises papier | 450 |  |
| 6055.17 |  | Fourniture de bureau non stockables | 50 |  |
| 6015.17 |  | Frais sur achats papier | 50 |  |
| 4451 |  | TVA récupérable sur immobilisations (330×10 %) | 33 |  |
| 4452 |  | TVA récupérable sur achats [(2 000+200+450+50+50)×10 %] | 275 |  |
|  | 4812 | Fournisseurs d'investissements A (330 + 33) |  | 363 |
|  | 4011.. | Fournisseurs A |  | 3 025 |

Variante frais incorporés au compte d'achat : 6011.26 = 2 200, 6011.17 = 495, 6055.17 = 55, 4452 = 275 [(2 200+495+55)×10 %], mêmes crédits 4812 = 363 et 4011 = 3 025.

### 1.2 Ventes

Crédit du compte principal **70**, débit d'un compte client :
- 701 marchandises ; 702 produits finis ; 703 produits intermédiaires ; 704 produits résiduels ; 705 ventes de travaux (BTP) ; 706 ventes d'autres services ; 707 produits accessoires (biens ex. 7071 emballages, services ex. 7073 locations). Un produit accessoire qui devient l'activité principale d'une entité → 706 Services vendus.

### Application 2 — Ventes de marchandises et de produits finis

Facture n°1 vue du fournisseur : caisse et papier achetés (marchandises), ordinateurs fabriqués (produits finis).

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4111.. |  | Client B | 3 388 |  |
|  | 7011.26 | Ventes marchandises |  | 300 |
|  | 7021.26 | Ventes produits finis |  | 2 000 |
|  | 7011.17 | Ventes marchandises |  | 500 |
|  | 7071.. | Ports facturés |  | 280 |
|  | 4431 | TVA facturée sur ventes |  | 308 |

## Section 2 — Stocks

Achats → entrée en classe 3 ; ventes → sortie. Le SYSCOHADA déroge dans le temps (inventaire intermittent généralisé) et dans l'espace (consommation immédiate de certains achats).

### 2.1 Méthode d'inventaire

**Inventaire intermittent** : neutralisation des comptes classe 3 en cours d'exercice, régularisation en fin d'exercice via **603** (marchandises, matières, fournitures, autres approvisionnements) ou **73** (produits). Deux écritures par catégorie (annulation stock initial + constatation stock final), réductibles à une seule constatant la variation.

**Application 3 — stock marchandises 10 → 11 (stockage +1)**

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6031 |  | Variations des stocks de marchandises (annulation stock début) | 10 |  |
|  | 31.. | Marchandises |  | 10 |
| 31.. |  | Marchandises (constatation stock fin) | 11 |  |
|  | 6031 | Variations des stocks de marchandises |  | 11 |

Ou une seule écriture pour la variation +1 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 31.. |  | Marchandises (ajustement stock fin) | 1 |  |
|  | 6031 | Variations des stocks de marchandises |  | 1 |

**Application 4 — stock produits finis 15 → 12 (déstockage −3)**

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 736 |  | Variations des stocks de produits finis (annulation) | 15 |  |
|  | 36.. | Produits finis |  | 15 |
| 36.. |  | Produits finis (constatation) | 12 |  |
|  | 736 | Variations des stocks de produits finis |  | 12 |

Ou une seule écriture pour −3 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 736 |  | Variations des stocks de produits finis (ajustement) | 3 |  |
|  | 36.. | Produits finis |  | 3 |

Au Compte de résultat : 603 en charges (soustraction si stockage) ; 73 en produits (soustraction si déstockage). En **inventaire permanent**, mêmes écritures mais passées à chaque entrée/sortie ; seule la fréquence diffère.

### 2.2 Opportunité des comptes de stocks

Biens obligatoirement stockés (classe 3) : marchandises (601→31→701), matières premières (602→32), produits finis (36→702), produits intermédiaires (37→703), produits résiduels (37→704), produits en cours (34). Autres approvisionnements : soit stockés en 33 (achetés en 604), soit **immédiatement consommés** en **605 Autres achats** (décision de l'entité selon valeur et contrôle).

En cas de non-stockage, régularisation possible en fin d'exercice via **476 Charges constatées d'avance**.

**Application 5 — fournitures de bureau, régularisation fin d'exercice** (achat 15 le 27/06/N, reste 3 au 31/12/N)

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6055 |  | 27/06/N — Fournitures de bureau non stockables (achat) | 15 |  |
|  | 4011 | Fournisseurs |  | 15 |
| 476 |  | 31/12/N — Charges constatées d'avance (stock fin) | 3 |  |
|  | 6055 | Fournitures de bureau non stockables |  | 3 |

Les matières et fournitures non stockables **physiquement** (ex. énergie électrique au compteur, eau du robinet) sont obligatoirement immédiatement consommées.

**Services en cours** (études/prestations engagées non facturées) : compte **35**, suivis en inventaire permanent ou constatés en intermittent.

## Section 3 — Éléments soustractifs de la facture

Achats/ventes comptabilisés au prix net de la facture DOIT. Retour/réduction inclus dans la facture initiale : non enregistrés séparément. S'ils font l'objet d'une facture d'AVOIR : enregistrés. L'escompte est enregistré dans les deux cas, en principe au règlement ; l'escompte sur immobilisation vient en déduction du coût d'acquisition (pas d'écriture séparée).

### 3.1 Retours

Contre-passation.

Chez le client :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 401. |  | Fournisseurs, dettes en compte | X |  |
|  | 60.. | Achats |  | X |

Chez le fournisseur :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 70.. |  | Ventes | X |  |
|  | 411 | Clients |  | X |

### 3.2 Réductions commerciales

- **Rabais** : défaut de qualité/conformité (se rapporte au bien).
- **Remise** : importance de l'opération ou profession du client (se rapporte à la personne).
- **Ristourne** : sur un ensemble d'opérations d'une période (fidélité).

Chez le **fournisseur** : toujours contre-passées (il connaît le rattachement, statistiques par produit) → **pas de comptes de RRR accordés**. Chez le **client** : contre-passées si rattachables ; sinon comptes à terminaison 9 (**6019 à 6089**) pour les biens. Réductions sur services : au crédit des sous-comptes 61/62/63 (pas de compte spécifique ; sous-comptes ad hoc possibles 619, 629, 639).

### 3.3 Réductions financières (escompte)

Escompte de règlement = réduction pour paiement anticipé, en pourcentage simple du net (≠ escompte des effets, prorata temporis). Opération financière, enregistrée quel que soit le mode de présentation, en principe au paiement : **673** escompte accordé, **773** escompte obtenu (voir ch. 4).

### Application 6 — Remise et retour de marchandises

Client B : remise 20 % sur papier (sur facture I), remise 10 % sur caisse (avoir II), retour d'un ordinateur défectueux.
Facture I (fournisseur) : caisse 290, ordinateurs 2 000, papier réduit 20 % = 400. Total 2 690. Avoir II : remise 10 % caisse = 29, reprise ordinateur = 200. Total 229.

Chez le fournisseur A :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4111.. |  | Clients B (facture DOIT) | 2 690 |  |
|  | 7011.26 | Ventes marchandises (Région) |  | 290 |
|  | 7021.26 | Ventes produits finis (Région) |  | 2 000 |
|  | 7011.17 | Ventes marchandises (Région) |  | 400 |
| 7011.26 |  | Ventes marchandises (Région) — facture AVOIR | 29 |  |
| 7021.26 |  | Ventes produits finis (Région) | 200 |  |
|  | 4111.. | Clients B |  | 229 |

Chez le client B :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 2442.26 |  | Matériel informatique (facture DOIT) | 290 |  |
| 6011.26 |  | Achats marchandises ordinateurs | 2 000 |  |
| 6011.17 |  | Achats marchandises papier | 360 |  |
| 6055.17 |  | Achats fournitures de bureau (non stockés) | 40 |  |
|  | 4812.. | Fournisseurs d'investissements |  | 290 |
|  | 4011.. | Fournisseurs A |  | 2 400 |
| 4812.. |  | Fournisseurs d'investissements (facture AVOIR) | 29 |  |
| 4011.. |  | Fournisseurs A | 200 |  |
|  | 2442.26 | Matériel informatique |  | 29 |
|  | 6011.26 | Achats marchandises ordinateurs |  | 200 |

## Section 4 — Éléments additifs de la facture

### 4.1 Ports et emballages facturés
Chez le fournisseur : produits accessoires **7071** (pas de compensation avec une charge). Chez le client : majorent le coût d'achat → classe 2 ou comptes 60.

### 4.2 Emballages consignés

Consignation — chez le fournisseur (dette envers le client) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 41.. |  | Clients | X |  |
|  | 4194 | Clients, dettes pour emballages et matériels consignés |  | X |

Chez le client (créance sur le fournisseur) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4094 |  | Fournisseurs, créances pour emballages et matériels à rendre | X |  |
|  | 40.. | Fournisseurs |  | X |

Au retour, contre-passation. Le cas échéant, boni chez le fournisseur → **7074** :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4194 |  | Clients, dettes pour emballages et matériels consignés | brut |  |
|  | 7074 | Bonis sur reprises d'emballages |  | boni |
|  | 41… | Clients |  | net |

Mali chez le client → **6224** (assimilé location) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6224 |  | Malis sur emballage | mali |  |
| 40.. |  | Fournisseurs | net |  |
|  | 4094 | Fournisseurs, créances pour emballages et matériels à rendre |  | brut |

Non-retour (emballage vendu par le fournisseur → 7074 ; acheté par le client → 6082) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4194 |  | Clients, dettes pour emballages consignés (fournisseur) | X |  |
|  | 7074 | Cessions d'emballages |  | X |
| 6082 |  | Achats d'emballages récupérables non identifiables (client) | X |  |
|  | 4094 | Fournisseurs, créances pour emballages et matériels à rendre |  | X |

### 4.3 Taxes sur le chiffre d'affaires non récupérables
Taxes uniques, taxe à la production, sur prestations, etc. : chez le fournisseur = dette (crédit **446**), pas un produit ; chez le client = charge majorant le coût d'achat (ventilée dans les sous-comptes d'achat).

### 4.4 TVA

Fournisseur :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 41.. |  | Clients (taxe comprise) | TTC |  |
|  | 70.. | Ventes (hors taxes) |  | HT |
|  | 443. | Etat, TVA facturée |  | taxe |

Client autorisé à récupérer la TVA :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 60.. |  | Achats (hors taxe) | HT |  |
| 445. |  | Etat, TVA récupérable | taxe |  |
|  | 40.. | Fournisseurs (taxe comprise) |  | TTC |

Sinon la TVA est traitée comme les autres TCA (incorporée au coût).
