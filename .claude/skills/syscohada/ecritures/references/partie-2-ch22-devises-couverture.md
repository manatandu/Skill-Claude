# Partie 2 — Chapitre 22 : Opérations en devises et contrats de couverture sur marchés financiers

> Montants pédagogiques. Écritures en tableau 5 colonnes : Débit | Crédit | Date et libellé | Montant débit | Montant crédit. Base : articles 51 à 58 de l'AUDCIF. Écarts de conversion à la clôture (478 actif / 479 passif), contrepassés à la réouverture ; provision pour perte de change (194 financier / 499 exploitation) sur la perte latente non couverte.

## Rappel des comptes d'écart de conversion

- **4781 / 4791** — écart actif/passif, créances d'**exploitation** (diminution / augmentation).
- **4782 / 4792** — écart actif/passif, créances **financières**.
- **4783 / 4793** — écart actif/passif, dettes d'**exploitation**.
- **4784 / 4794** — écart actif/passif, dettes **financières**.
- **4788 / 4798** — écarts compensés par couverture de change.
- **194** provisions pour pertes de change ; **6971 / 7971** dotations / reprises financières ; **6591 / 7591** et **4991** provisions pour risques à court terme (exploitation).
- **656 / 756** pertes / gains de change sur créances et dettes **commerciales** ; **676 / 776** pertes / gains de change **financiers**.

## Application 84 — Créances commerciales en devises

Export 10/12/N à Rio : 250 000 réals. Règlement 15/02/N+1. Cours : 10/12/N 190 F ; 31/12/N H1 180 F / H2 210 F ; 15/02/N+1 H1 175 F / H2 215 F.

**À la facturation (10/12/N)** — 250 000 × 190 = 47 500 000 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 411 |  | 10/12/N — Clients | 47 500 000 |  |
|  | 701 | Ventes de marchandises |  | 47 500 000 |

**Clôture — Hypothèse 1** (baisse à 180) : perte latente 250 000 × (190 − 180) = 2 500 000 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4781 |  | 31/12/N — Écart de conversion actif, dim. créances d'exploitation | 2 500 000 |  |
|  | 411 | Clients (perte latente) |  | 2 500 000 |

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6591 |  | 31/12/N — Charges pour prov. sur risques à court terme | 2 500 000 |  |
|  | 4911 | Prov. pour risques à CT sur opérations d'exploitation |  | 2 500 000 |

Contrepassation de l'écart au 01/01/N+1 : 411 · 4781 pour 2 500 000.

**Clôture — Hypothèse 2** (hausse à 210) : gain latent 250 000 × (210 − 190) = 5 000 000 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 411 |  | 31/12/N — Clients (gain latent) | 5 000 000 |  |
|  | 4791 | Écart de conversion passif, augm. créances d'exploitation |  | 5 000 000 |

Contrepassation au 01/01/N+1 : 4791 · 411 pour 5 000 000 (pas de provision sur un gain latent).

**Règlement — Hypothèse 1 (15/02/N+1, cours 175)** — perte réalisée 250 000 × (190 − 175) = 3 750 000 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 521 |  | 15/02/N+1 — Banques (250 000 × 175) | 43 750 000 |  |
| 656 |  | Pertes de change sur créances et dettes commerciales | 3 750 000 |  |
|  | 411 | Clients (250 000 × 190) |  | 47 500 000 |

Reprise de la provision (31/12/N+1) : 4911 · 7591 pour 2 500 000.

**Règlement — Hypothèse 2 (cours 215)** — gain réalisé 250 000 × (215 − 190) = 6 250 000 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 521 |  | 15/02/N+1 — Banques (250 000 × 215) | 53 750 000 |  |
|  | 411 | Clients (250 000 × 190) |  | 47 500 000 |
|  | 756 | Gains de change sur créances et dettes commerciales |  | 6 250 000 |

## Application 85 — Avances et acomptes en devise sur commande d'immobilisation

Acompte 50 000 $ le 15/11/N ; facture matériel 300 000 $ le 10/12/N ; solde réglé 20/03/N+1. Cours : 15/11 620 ; 10/12 600 ; 31/12 585 ; 20/03/N+1 580.

**Acompte (15/11/N)** — 50 000 × 620 = 31 000 000 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 252 |  | 15/11/N — Avances et acomptes versés sur immo. corporelles | 31 000 000 |  |
|  | 521 | Banques |  | 31 000 000 |

**Facturation (10/12/N)** — coût = 50 000 × 620 + 250 000 × 600 = 181 000 000. L'acompte reste figé à son cours d'origine ; le solde (250 000 $) entre à 600 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 2411 |  | 10/12/N — Matériel industriel | 181 000 000 |  |
|  | 252 | Avances et acomptes versés sur immo. corporelles |  | 31 000 000 |
|  | 4812 | Fournisseurs d'investissements — immo. corporelles |  | 150 000 000 |

**Clôture (31/12/N)** — dette 250 000 $ ; écart 250 000 × (600 − 585) = 3 750 000, **gain latent** (diminution de la dette) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4812 |  | 31/12/N — Fournisseurs d'investissements — immo. corporelles | 3 750 000 |  |
|  | 4793 | Écart de conversion passif, dim. des dettes d'exploitation |  | 3 750 000 |

Contrepassation au 01/01/N+1 : 4793 · 4812 pour 3 750 000.

**Règlement (20/03/N+1, cours 580)** — gain réalisé 250 000 × (600 − 580) = 5 000 000 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4812 |  | 20/03/N+1 — Fournisseurs d'investissements — immo. corporelles | 150 000 000 |  |
|  | 521 | Banques (250 000 × 580) |  | 145 000 000 |
|  | 756 | Gain de change sur créances et dettes commerciales |  | 5 000 000 |

## Application 86 — Disponibilités en devises

Achat 50 000 $ le 01/10/N (620). 45 000 $ utilisés au 31/12. Solde 5 000 $. Cours 31/12 : 570.

**Achat (01/10/N)** — 50 000 × 620 = 31 000 000 : 5215 (Banques en devises) · 521 pour 31 000 000.

**Clôture (31/12/N)** — perte de change sur le disponible résiduel : 5 000 × (620 − 570) = 250 000. La disponibilité en devise est un poste de trésorerie : la perte est **réalisée** (compte 676), sans écart de conversion :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 676 |  | 31/12/N — Pertes de change financières | 250 000 |  |
|  | 5215 | Banques en devises |  | 250 000 |

## Application 87 — Emprunts affectant plusieurs exercices (article 56)

Emprunt 300 000 $ le 01/08/N, amortissements constants sur 2 ans, intérêt 8 %/an. Cours : 01/08/N 620 ; 31/12/N 625 ; 01/08/N+1 635 ; 31/12/N+1 622.

**01/08/N** — 300 000 × 620 = 186 000 000 : 521 · 162 pour 186 000 000.

**Au 31/12/N.** Dette réévaluée 300 000 × 625 = 187 500 000, soit perte latente 1 500 000. Intérêts courus non échus : 187 500 000 × 8 % × 5/12 = 6 250 000.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4784 |  | 31/12/N — Écart de conversion actif, augm. des dettes financières | 1 500 000 |  |
|  | 162 | Emprunts auprès des établissements de crédit |  | 1 500 000 |

**Provision, article 56 (étalement de la perte latente sur la durée restant à courir jusqu'au terme = 19 mois).** Part différée : 1 500 000 × 19/24 = 1 187 500. À provisionner : 1 500 000 − 1 187 500 = 312 500 (ou directement 1 500 000 × 5/24) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6971 |  | 31/12/N — Dotations aux prov. pour risques et charges (financier) | 312 500 |  |
|  | 194 | Provisions pour pertes de change |  | 312 500 |

Intérêts courus : 6712 · 1662 pour 6 250 000. Au 01/01/N+1 : contrepassation de l'écart (162 · 4784 pour 1 500 000) et des intérêts courus (1662 · 6712 pour 6 250 000).

**À l'échéance (01/08/N+1).** Amortissement 150 000 $ × 635 = 95 250 000 (> 93 000 000) : perte de change réalisée 2 250 000. Intérêts 300 000 × 635 × 8 % = 15 240 000. Annuité 110 490 000 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 162 |  | 01/08/N+1 — Emprunts auprès des ét. de crédit | 93 000 000 |  |
| 6712 |  | Intérêts des emprunts auprès des ét. de crédit | 15 240 000 |  |
| 676 |  | Pertes de change financières | 2 250 000 |  |
|  | 521 | Banques |  | 110 490 000 |

**Au 31/12/N+1.** Dette résiduelle 150 000 × 622 = 93 300 000 (> 93 000 000) : perte latente 300 000. Intérêts courus 150 000 × 622 × 8 % × 5/12 = 3 110 000.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4784 |  | 31/12/N+1 — Écart de conversion actif, augm. des dettes financières | 300 000 |  |
|  | 162 | Emprunts auprès des ét. de crédit |  | 300 000 |

Provision à couvrir : part différée 300 000 × 7/24 = 87 500 ; à couvrir 300 000 − 87 500 = 212 500 (ou 300 000 × 17/24). Provision existante 312 500 → reprise de 100 000 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 194 |  | 31/12/N+1 — Provisions pour pertes de change | 100 000 |  |
|  | 7971 | Reprises de prov. pour risques et charges (financier) |  | 100 000 |

Intérêts courus 31/12/N+1 : 6712 · 1662 pour 3 110 000.

## Application 88 — Position globale de change (article 57)

Prêt de 100 000 $ à la filiale le 01/09/N (remb. 31/03/N+2) et emprunt de 80 000 $ (même terme). Cours 01/09/N 620 ; 31/12/N 550.

**Prêt (créance financière).** Écart actif = 100 000 × (620 − 550) = 7 000 000 (perte latente) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4782 |  | 31/12/N — Écart de conversion actif, dim. des créances financières | 7 000 000 |  |
|  | 277 | Créances rattachées à des participations |  | 7 000 000 |

**Emprunt (dette financière).** Écart passif = 80 000 × (620 − 550) = 5 600 000 (gain latent) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 162 |  | 31/12/N — Emprunt auprès des ét. de crédit | 5 600 000 |  |
|  | 4794 | Écart de conversion passif, dim. des dettes financières |  | 5 600 000 |

**Position globale (article 57).** La provision ne couvre que le risque **non compensé** : 7 000 000 − 5 600 000 = 1 400 000 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6971 |  | 31/12/N — Dotations aux prov. pour risques et charges | 1 400 000 |  |
|  | 194 | Provisions pour pertes de change |  | 1 400 000 |

## Application 89 — Couverture fixant définitivement le cours à l'échéance (article 58-3)

Achat 05/12/N de marchandises 250 000 $ (cours 620), règlement 05/02/N+1. Garantie interne obtenue de la centrale de trésorerie du groupe **le 01/12/N** (avant l'opération), cours garanti 650.

**Principe (art. 58-3).** Une garantie interne de change entre centrale de trésorerie et entité du même groupe (ou une garantie d'assurance-crédit export) qui fixe définitivement le cours transforme la créance/dette en devise en créance/dette en monnaie légale.
- Couverture **avant** l'opération : la dette est enregistrée directement au cours garanti → pas d'écart de conversion ni de provision.
- Couverture **après** l'opération : écarts et provisions constatés (art. 54 s.) jusqu'à la mise en place, puis conversion au cours de couverture (écart en résultat financier), provisions reprises.

Ici la couverture précède l'achat → tout est comptabilisé au cours garanti 650 (250 000 × 650 = 162 500 000) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 601 |  | 05/12/N — Achats de marchandises (250 000 × 650) | 162 500 000 |  |
|  | 401 | Fournisseurs |  | 162 500 000 |
| 401 |  | 05/02/N+1 — Fournisseurs | 162 500 000 |  |
|  | 521 | Banques |  | 162 500 000 |

## Application 90 — Couverture de change, opération symétrique

Achat 100 000 $ le 01/12/N (cours 600), payable 10/02/N+1. Couverture : souscription 10/12/N d'un **prêt en devises** de 75 000 $ (même terme, cours 610). Cours 31/12/N : 625.

**Comptabilisation initiale.** Achat 100 000 × 600 = 60 000 000 (601 · 401). Prêt 75 000 × 610 = 45 750 000 (271 · 521).

**Clôture (31/12/N).**
- Dette fournisseur : écart actif 100 000 × (625 − 600) = 2 500 000 (perte latente).
- Prêt : écart passif 75 000 × (625 − 610) = 1 125 000 (gain latent).
- La perte latente sur l'élément couvert est compensée par le gain latent de l'élément de couverture : provision limitée à 2 500 000 − 1 125 000 = 1 375 000.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4783 |  | 31/12/N — Écart de conversion actif, augm. des dettes d'exploitation | 2 500 000 |  |
|  | 401 | Fournisseurs |  | 2 500 000 |
| 271 |  | Prêts | 1 125 000 |  |
|  | 4792 | Écart de conversion passif, augm. des créances financières |  | 1 125 000 |
| 4788 |  | Écart actif — différences compensées par couverture de change | 1 125 000 |  |
|  | 4783 | Écart actif, augm. des dettes d'exploitation |  | 1 125 000 |
| 6591 |  | Charges pour prov. sur risques à court terme | 1 375 000 |  |
|  | 4991 | Prov. pour risques à CT sur opérations d'exploitation |  | 1 375 000 |

## Application 91 — Couverture de transactions futures (article 58-2)

Vente à l'export prévue 400 000 $ (1er semestre N+1). Le 01/05/N : vente à terme 400 000 $, échéance 30/04/N+1. Vente réalisée 31/07/N+1, créance réglée 10/02/N+2. Option d'**étalement du report/déport**. Cours : 01/05/N comptant 600 / terme 590 ; 31/12/N 580 ; 30/04/N+1 575 ; 31/07/N+1 550 ; 31/12/N+1 530 ; 10/02/N+2 515.

**Principes (art. 58-2).** Contrats qualifiés de couverture identifiés dès l'origine ; variations de valeur logées dans le compte transitoire **54 Instruments de trésorerie**, rapportées au résultat sur la durée de vie résiduelle de l'élément couvert (ou symétriquement au résultat de cet élément). Comptes **4786 (actif) / 4797 (passif)** — différences d'évaluation sur instruments de trésorerie. Report/déport = écart comptant − terme. Pour les couvertures de créances/dettes, il est **obligatoirement étalé** dans le compte **6784 Pertes et charges sur instruments de trésorerie**.

**Clôture N.** Report/déport = 400 000 × (600 − 590) = 4 000 000. Étalement (8 mois sur 12) : 4 000 000 × 8/12 = 2 666 667 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6784 |  | 31/12/N — Pertes et charges sur instruments de trésorerie | 2 666 667 |  |
|  | 54 | Instruments de trésorerie |  | 2 666 667 |

**Dénouement de la vente à terme (30/04/N+1).** Résultat de couverture 400 000 × (600 − 575) = 10 000 000. Solde du report/déport 4 000 000 × 4/12 = 1 333 333 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 521 |  | 30/04/N+1 — Banques | 10 000 000 |  |
|  | 4797 | Différences d'évaluation sur instruments de trésorerie |  | 10 000 000 |
| 54 |  | Instruments de trésorerie | 2 666 667 |  |
| 6784 |  | Pertes et charges sur instruments de trésorerie | 1 333 333 |  |
|  | 521 | Banques |  | 4 000 000 |

**À la vente (31/07/N+1).** Vente 400 000 × 550 = 220 000 000 (411 · 70). Imputation du résultat de couverture en résultat d'exploitation :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4797 |  | 31/07/N+1 — Différences d'évaluation sur instruments de trésorerie | 10 000 000 |  |
|  | 756 | Gains de change sur créances et dettes commerciales |  | 10 000 000 |

**Clôture N+1 (31/12/N+1).** Écart latent 400 000 × (550 − 530) = 8 000 000 (perte) : 4781 · 411 pour 8 000 000, et provision 6591 · 4991 pour 8 000 000. Contrepassation au 01/01/N+2 : 411 · 4781 pour 8 000 000.

**Règlement (10/02/N+2).** Perte réalisée 400 000 × (550 − 515) = 14 000 000 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 521 |  | 10/02/N+2 — Banques | 206 000 000 |  |
| 656 |  | Perte de change sur créances et dettes commerciales | 14 000 000 |  |
|  | 411 | Clients |  | 220 000 000 |

Reprise de provision : 4991 · 7591 pour 8 000 000.
