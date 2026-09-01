# Partie 2 — Chapitre 8 : Contrat de location

> Montants pédagogiques (KF = millier de francs). Écritures en tableau 5 colonnes : Débit | Crédit | Date et libellé | Montant débit | Montant crédit. Qualification et retraitements → `audcif-acte-uniforme` ; convergence IFRS 16 → skill `ifrs`.

## Application 37 — Contrat de location acquisition (chez le preneur / crédit-bail)

Machine financée par crédit-bail le 01/01/N. Valeur 450 000 KF. 7 versements à terme échu de 80 650 KF. Durée d'utilité 10 ans. Option d'achat incitative (levée prévue), prix résiduel 51 600 KF. Frais d'installation 50 000 KF réglés le 15/01/N.

**Qualification** : location acquisition (preneur raisonnablement certain de lever l'option).

**Taux implicite** : résout 450 000 = 80 650 × [1 − (1+i)⁻⁷] / i + 51 600 (1+i)⁻⁷ → **i = 8 %** (par tâtonnement).

**Évaluation initiale** : dette 450 000 ; coût d'acquisition = 450 000 + 50 000 (installation) = **500 000 KF**.

**Tableau d'amortissement de la dette** (intérêts = dette début × 8 %) :

| Échéance | Date | Loyer | Amort. dette | Intérêts | Dette restante |
|---|---|---|---|---|---|
| Signature | 01/01/N | — | — | — | 450 000 |
| 1 | 31/12/N | 80 650 | 44 650 | 36 000 | 405 350 |
| 2 | 31/12/N+1 | 80 650 | 48 220 | 32 430 | 357 130 |
| 3 | 31/12/N+2 | 80 650 | 52 080 | 28 570 | 305 050 |
| 4 | 31/12/N+3 | 80 650 | 56 245 | 24 405 | 248 805 |
| 5 | 31/12/N+4 | 80 650 | 60 745 | 19 905 | 188 080 |
| 6 | 31/12/N+5 | 80 650 | 65 605 | 15 045 | 122 455 |
| 7 | 31/12/N+6 | 80 650 | 70 855 | 9 795 | 51 600 |
| Levée option | 31/12/N+6 | 51 600 | 51 600 | 0 | 0 |
| **TOTAL** | | 616 150 | 450 000 | 166 150 | |

**Signature (01/01/N)** :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 2411 |  | 01/01/N — Matériel industriel | 500 000 |  |
|  | 173 | Dettes de location acquisition / crédit-bail mobilier |  | 450 000 |
|  | 4812 | Fournisseurs d'investissements |  | 50 000 |

Règlement des frais d'installation (15/01/N) : 4812 · 521, 50 000.

**Clôture N — redevance et éclatement.**

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 623 |  | 31/12/N — Redevances de location acquisition | 80 650 |  |
|  | 401 | Fournisseurs |  | 80 650 |
| 401 |  | Fournisseurs (règlement) | 80 650 |  |
|  | 521 | Banques |  | 80 650 |
| 173 |  | Dettes de location acquisition / crédit-bail mobilier | 44 650 |  |
| 672 |  | Intérêts dans loyers de location acquisition | 36 000 |  |
|  | 623 | Redevances de location acquisition |  | 80 650 |

> On crédite 401 (même pour une opération d'investissement) pour ne pas alourdir les retraitements du TFT.

Amortissement du bien loué : 500 000 × 1/10 = 50 000 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6813 |  | 31/12/N — Dotation aux amort. des immob. corp. | 50 000 |  |
|  | 28411 | Amort. du matériel industriel |  | 50 000 |

**Hypothèse 1 — Levée d'option (31/12/N+6).**

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 623 |  | 31/12/N+6 — Redevances de location acquisition | 51 600 |  |
|  | 521 | Banques |  | 51 600 |
| 173 |  | Dettes de location acquisition / crédit-bail mobilier | 51 600 |  |
|  | 623 | Redevances de location acquisition |  | 51 600 |

Puis amortissement N+6 : 6813 · 28411, 50 000.

**Hypothèse 2 — Non levée d'option (31/12/N+6).** Le matériel est repris par le bailleur ; on constate la sortie et l'annulation de la dette au prix de levée (traité comme une cession). Cumul amort. = 500 000 × 1/10 × 7 = 350 000 ; VNC = 150 000 ; prix de cession (dette annulée) = 51 600.

Dotation N+6 : 6813 · 28411, 50 000.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 812 |  | 31/12/N+6 — Valeurs comptables des cessions d'immob. | 150 000 |  |
| 28411 |  | Amort. du matériel industriel | 350 000 |  |
|  | 2411 | Matériel industriel |  | 500 000 |
| 173 |  | Dettes de location acquisition / crédit-bail mobilier | 51 600 |  |
|  | 822 | Produits des cessions d'immobilisations corp. |  | 51 600 |

## Application 38 — Contrat de location chez le bailleur (location financement)

Entité industrielle fabrique et met en location-vente un matériel spécialisé le 01/01/N (durée 10 ans = durée d'utilité). Coût de fabrication 400 000 KF ; prix de vente (prélevé sur stocks PF) 450 000 KF. Commission d'intermédiaire 2 000 KF réglée le 05/01/N. 10 loyers à terme échu de 70 000 KF, premier le 31/12/N. Taux implicite 10 %. Dernier loyer 51 570 KF. Valeur résiduelle nulle. Inventaire permanent.

**Tableau d'amortissement de la créance** (intérêts = créance début × 10 %) :

| Échéance | Date | Loyer | Amort. créance | Intérêts | Créance restante |
|---|---|---|---|---|---|
| Signature | 01/01/N | — | — | — | 450 000 |
| 1 | 31/12/N | 70 000 | 25 000 | 45 000 | 425 000 |
| 2 | 31/12/N+1 | 70 000 | 27 500 | 42 500 | 397 500 |
| 3 | 31/12/N+2 | 70 000 | 30 250 | 39 750 | 367 250 |
| 4 | 31/12/N+3 | 70 000 | 33 275 | 36 725 | 333 975 |
| 5 | 31/12/N+4 | 70 000 | 36 600 | 33 400 | 297 375 |
| 6 | 31/12/N+5 | 70 000 | 40 260 | 29 740 | 257 115 |
| 7 | 31/12/N+6 | 70 000 | 44 290 | 25 710 | 212 825 |
| 8 | 31/12/N+7 | 70 000 | 48 715 | 21 285 | 164 110 |
| 9 | 31/12/N+8 | 70 000 | 53 590 | 16 410 | 110 520 |
| 10 | 31/12/N+9 | 70 000 | 58 950 | 11 050 | 51 570 |
| Levée option | 31/12/N+9 | 51 570 | 51 570 | — | 0 |
| **TOTAL** | | 751 570 | 450 000 | 301 570 | |

Vente :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 2714 |  | 01/01/N — Créances de location financement / location-vente | 450 000 |  |
|  | 702 | Ventes de produits finis |  | 450 000 |
| 736 |  | Variations des stocks de produits finis | 400 000 |  |
|  | 361 | Stocks de produits finis |  | 400 000 |

Commission (05/01/N) : 6322 · 401 (2 000), puis 401 · 521 (2 000).

Premier loyer perçu (31/12/N) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 521 |  | 31/12/N — Banques | 70 000 |  |
|  | 2714 | Créances de location-financement |  | 25 000 |
|  | 775 | Intérêts dans loyers de location-financement |  | 45 000 |
