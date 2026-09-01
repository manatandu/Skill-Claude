# Partie 1 — Chapitre 5 : Opérations d'investissement et de désinvestissement

> Montants et taux pédagogiques. Écritures en tableau 5 colonnes : Débit | Crédit | Date et libellé | Montant débit | Montant crédit. Pour l'article et les critères → `audcif-acte-uniforme` (Titre VIII).

## Section 1 — Conception et terminologie

### 1.1 Notion d'immobilisation
Éléments corporels et incorporels destinés à servir de façon durable (« qui dure plus d'une année », l'exercice étant assimilé à l'année civile). Le principe d'importance significative admet que des biens durables de faible valeur unitaire soient traités en consommations (SYSCOHADA ne fixe **pas** de seuil). Extension : immobilisations **incorporelles** (brevet, logiciel), **financières** (titres, prêts conservés > 1 an).

### 1.2 Vie d'une immobilisation
Entrée (acquisition ou production), service et usure (mise en service, répartition du montant amortissable, dépréciation éventuelle), sortie (rebut, destruction, vente, échange).

## Section 2 — Comptabilisation de l'immobilisation

### 2.1 Processus
Classe 2 : incorporelles **21**, corporelles **22 à 24**, financières **25 à 27**.

Achat précédé d'un acompte :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 25.. |  | Versement — Avances et acomptes versés sur immobilisations | X |  |
|  | 5… | Trésorerie |  | X |
| 2... |  | Réception facture — Immobilisations | X |  |
| 4451 |  | Etat, TVA récupérable sur immobilisations | X |  |
|  | 25.. | Avances et acomptes versés sur immobilisations |  | X |
|  | 481. | Fournisseurs d'investissements |  | X |
|  | 404 | Fournisseurs, acquisitions courantes d'immobilisations |  | X |

Bien produit par l'entité (durée dépassant N) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 219./229./239./249. |  | À l'issue de N — Immobilisations en cours | X |  |
|  | 72.. | Production immobilisée |  | X |
|  | 787 | Transferts de charges financières |  | X |
| 2… |  | Achèvement — Immobilisations | X |  |
| 4451 |  | Etat, TVA récupérable sur immobilisations | X |  |
|  | 219./229./239./249. | Immobilisations en cours |  | X |
|  | 72.. | Production immobilisée |  | X |
|  | 787 | Transferts de charges financières |  | X |
|  | 4434 | Etat, TVA facturée sur production livrée à soi-même |  | X |

Bien acquis à titre gratuit (valeur actuelle) : débit **2...**, crédit **148** Autres subventions d'investissement (ou **841** Produits HAO constatés si montant non significatif).

### 2.2 Valeur comptabilisée (art. 36-37 AUDCIF)
Coût historique : coût réel d'acquisition (achat), de production (production immobilisée), valeur d'apport (apport), valeur actuelle (gratuit ou échange). Coût d'acquisition = prix d'achat net de remises/rabais/escompte + charges accessoires directes (transport, assurance, douane, transit, commissions, honoraires, droits d'enregistrement) + charges d'installation (préparation, montage, mise en route) + estimation initiale des coûts de démantèlement/remise en état. TVA comprise si non déductible, HT sinon. Coût de production = coût des matières + charges directes + charges indirectes rattachables. **Coûts d'emprunt** de la période de production jusqu'à la date d'acquisition/réception définitive : dans le coût du bien ; au-delà → charges (671).

## Section 3 — Immobilisation en service

### 3.1 Mise en service
Entrée dans le patrimoine dès l'acquisition/livraison ; la mise en service (état et lieu d'utilisation prévus) n'entraîne pas d'écriture mais constitue le point de départ de l'amortissement.

### 3.2 Amortissement
Répartition du montant amortissable (coût d'entrée − valeur résiduelle prévisionnelle) sur la durée d'utilité selon un plan. Modes : **linéaire** (charge constante), **dégressif à taux décroissant** (SOFTY), **unités d'œuvre**, ou tout autre mieux adapté. Interdits : amortissement fondé sur les revenus (corporelles) et amortissement financier.

**Dégressif à taux décroissant (SOFTY)** — taux = (années restant à courir) / (somme des numéros d'ordre des années). Durée 5 ans → somme 1+2+3+4+5 = 15 ; taux 5/15, 4/15, 3/15, 2/15, 1/15. Annuité = base amortissable × taux ; base constante. Formule : annuité(p) = 2V(n+1−p) / n(n+1).

**Application 13 — Dégressif SOFTY** (machine coût 550 000, valeur résiduelle 50 000, durée 5 ans ; base 500 000)

| Date | Base | Taux | Annuité | Cumul | VNC |
|---|---|---|---|---|---|
| 31/12/N | 500 000 | 5/15 | 166 667 | 166 667 | 383 333 |
| 31/12/N+1 | 500 000 | 4/15 | 133 333 | 300 000 | 250 000 |
| 31/12/N+2 | 500 000 | 3/15 | 100 000 | 400 000 | 150 000 |
| 31/12/N+3 | 500 000 | 2/15 | 66 667 | 466 667 | 83 333 |
| 31/12/N+4 | 500 000 | 1/15 | 33 333 | 500 000 | 50 000 |

**Unités d'œuvre** — annuité = base amortissable × (unités consommées de l'exercice / total prévu). Pas de prorata temporis (fonction des unités, pas du temps).

**Application 14 — Unités d'œuvre** (mêmes données ; unités N+1 à N+5 : 150 000, 250 000, 250 000, 50 000, 50 000 ; total 750 000 ; base 500 000)

| Date | Base | Amortissement | Cumul | VNC |
|---|---|---|---|---|
| 31/12/N | 500 000 | 100 000 (500 000×150 000/750 000) | 100 000 | 450 000 |
| 31/12/N+1 | 500 000 | 166 667 | 266 667 | 283 333 |
| 31/12/N+2 | 500 000 | 166 667 | 433 334 | 116 666 |
| 31/12/N+3 | 500 000 | 33 333 | 466 667 | 83 333 |
| 31/12/N+4 | 500 000 | 33 333 | 500 000 | 50 000 |

**Comptabilisation (amortissement indirect)** :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 681. |  | Dotations aux amortissements d'exploitation | X |  |
| 852. |  | Dotations aux amortissements H.A.O. | X |  |
|  | 28.. | Amortissements |  | X |

Dotations 681 en règle générale (même exercice antérieur) ; 852 seulement pour restructuration ou événements extraordinaires. **Amortissements dérogatoires** (provisions réglementées) : débit **851**, crédit **151**. Révision du plan → reprises : débit 28.., crédit **798** (ou **862** HAO).

## Section 4 — Décomptabilisation de l'immobilisation

### 4.1 Principes
Trois écritures : (1) valeur de sortie si > 0 au **82** ; (2) amortissement complémentaire jusqu'à la date de cession ; (3) décomptabilisation pour la VNC des seuls amortissements au **81** (les dépréciations sont reprises). En pratique la 1ʳᵉ est passée en cours d'exercice (facture de vente), les deux dernières à l'inventaire. Cessions **courantes** (fréquentes/récurrentes, ex. transporteurs, loueurs) : comptes **654** (VC) et **754** (prix de cession) au lieu de 81/82. Quatre cas : rebut, destruction, vente, échange.

### 4.2 Mise au rebut
Retrait sans contrepartie (une épave cédée = vente). Deux opérations :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 681. |  | Amortissement complémentaire — Dotations aux amortissements d'exploitation | X |  |
|  | 28.. | Amortissements |  | X |
| 81../654. |  | Valeurs comptables des cessions d'immobilisations (reprise valeur brute) | X |  |
|  | 22..à24.. | Actif immobilisé |  | X |
| 28.. |  | Amortissements (cumul pratiqué) | X |  |
|  | 81../654. | Valeurs comptables des cessions d'immobilisations |  | X |

### 4.3 Destruction
Non assurée / non couverte : traitée comme le rebut. Indemnité d'assurance : opération assimilée à une vente (indemnité = prix de cession).

### 4.4 Vente
Écritures du rebut + créance sur cession :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 485. |  | Créances sur cessions d'immobilisations | X |  |
|  | 82.. | Produits des cessions d'immobilisations |  | X |

Cession courante : débit **414**, crédit **754**. La plus/moins-value n'apparaît pas ; elle se déduit de la comparaison 82/81 (ou 754/654).

### 4.5 Échange
Ancien bien remplacé par un nouveau (soulte). Enregistrer séparément la vente de l'ancien (au prix de reprise) et l'acquisition du nouveau (valeur actuelle = prix de reprise + soulte) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 681. |  | a — Dotations aux amortissements | X |  |
|  | 28.. | Amortissements |  | X |
| 81.. |  | b — Valeurs comptables des cessions d'immobilisations | X |  |
|  | 22..à24.. | Actif immobilisé |  | X |
| 28.. |  | Amortissements | X |  |
|  | 81.. | Valeurs comptables des cessions d'immobilisations |  | X |
| 485. |  | c — Créances sur cessions d'immobilisations | X |  |
|  | 82.. | Produits des cessions d'immobilisations |  | X |
| 2... |  | d — Actif immobilisé (nouveau bien) | X |  |
|  | 481. | Fournisseurs d'investissements |  | X |

Cession courante → 654 à la place de 81, 754 à la place de 82.

### 4.6 Vente ou échange avec plus-value à réinvestir
La plus-value (82 − 81 ou 754 − 654) augmente le résultat. Certaines législations l'exonèrent sous condition de réinvestissement, la base d'amortissement du nouveau bien étant diminuée d'autant (report de la charge d'impôt). Provision réglementée constituée en fin d'exercice de cession :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 851. |  | Dotations H.A.O. aux provisions réglementées | X |  |
|  | 152. | Plus-values de cession à réinvestir |  | X |

Reprise (remploi total ou partiel) : débit **152**, crédit **861** Reprises H.A.O. de provisions réglementées.

### Application 15 — Décomptabilisation d'un matériel informatique
Cédé à crédit le 30/06/N+5 pour 500. Prix d'achat en N : 10 000. Amortissements cumulés au 30/06/N+5 : 9 800 dont 1 800 de dotation complémentaire.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4852 |  | 30/06/N+5 — Créances sur cessions d'immo. corporelles | 500 |  |
|  | 822 | Produits des cessions d'immo. corporelles (prix de vente) |  | 500 |
| 6812 |  | 31/12/N+5 — VNC des cessions d'immo. corp. (dotation complémentaire) | 1 800 |  |
|  | 28442 | Amortissement du matériel informatique |  | 1 800 |
| 812 |  | VNC des cessions d'immo. corporelles | 200 |  |
| 28442 |  | Amortissement du matériel informatique | 9 800 |  |
|  | 2442 | Matériel informatique (décomptabilisation) |  | 10 000 |

### Application 16 — Plus-value à réinvestir
Matériel de transport 1 200 HT (TVA 20 %), acquis le 2/1/N, amorti linéaire 15 %, cédé le 30/09/N+2 à 1 105. Engagement de réinvestir ; nouveau matériel 1 500 HT acquis le 2/1/N+3, amorti 25 %.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 2451 |  | 02/01/N — Matériel automobile | 1 200 |  |
| 4451 |  | Etat, TVA récupérable sur immobilisations | 240 |  |
|  | 4812 | Fournisseurs d'immobilisations |  | 1 440 |
| 6813 |  | 31/12/N et N+1 — Dotations aux amort. des immob. | 180 |  |
|  | 2845 | Amort. du matériel de transport |  | 180 |
| 6813 |  | 30/09/N+2 — Dotations aux amort. (180 × 9/12) | 135 |  |
|  | 2845 | Amort. du matériel de transport |  | 135 |
| 2845 |  | Amort. du matériel de transport (180+180+135) | 495 |  |
|  | 812. | Val. compt. des cessions d'immob. corp. |  | 495 |
| 812 |  | Val. compt. des cessions d'immob. corp. | 1 200 |  |
|  | 2451. | Matériel automobile |  | 1 200 |
| 4851 |  | Créances sur cessions d'immobilisations | 1 105 |  |
|  | 822. | Produits des cessions d'immob. corp. |  | 1 105 |
| 851. |  | 31/12/N+2 — Dotations H.A.O. aux provisions réglementées [1 105 − (1 200 − 495) = 400] | 400 |  |
|  | 152. | Plus-values de cession à réinvestir |  | 400 |
| 2451 |  | 02/01/N+3 — Matériel automobile | 1 500 |  |
| 4451 |  | Etat, TVA récupérable sur immobilisations | 300 |  |
|  | 4812 | Fournisseurs d'immobilisations corp. |  | 1 800 |
| 6813 |  | 31/12/N+3 — Dotations aux amort. (1 500 × 25 %) | 375 |  |
|  | 2845 | Amort. du matériel de transport |  | 375 |
| 152. |  | Plus-values de cession à réinvestir (400 × 25 %) | 100 |  |
|  | 861. | Reprises H.A.O. de provisions réglementées |  | 100 |

Regroupement possible des deux écritures de sortie du 30/09/N+2 : débit 812 = 705 et 2845 = 495, crédit 2451 = 1 200.
