# Partie 1 — Chapitre 6 : Régularisations périodiques

> Montants et taux pédagogiques. Écritures en tableau 5 colonnes : Débit | Crédit | Date et libellé | Montant débit | Montant crédit.

Écritures d'inventaire passées à chaque situation intermédiaire ou au plus tard en fin d'exercice. Elles régularisent les stocks, constatent les dépréciations, et effectuent les autres régularisations de charges et produits (créances et dettes).

## Section 1 — Régularisation des stocks

### 1.1 Inventaire intermittent
Stocks de fin constatés par inventaire physique, substitués aux stocks de début via un compte de variation : **603** (amont : marchandises 6031, matières et fournitures liées 6032, autres approvisionnements 6033) ou **73** (aval : produits en cours 734, services en cours 735, produits finis 736, produits intermédiaires et résiduels 737). Nouveau stock > ancien → stockage (soldes créditeurs) ; nouveau < ancien → déstockage (soldes débiteurs). Exemple stock 10 → 12 (stockage +2) : report 10, annulation 10, constatation 12 (solde 3… débiteur 12, variation créditeur 2) ; ou mise à jour par la seule variation +2.

### 1.2 Inventaire permanent
Comptes classe 3 « à part entière » enregistrant toutes entrées/sorties (flux bruts) : montant des stocks, coût d'achat des marchandises vendues, coût des matières engagées connus à chaque instant. Les achats seraient enregistrés directement en classe 3 ; 603 et 73 enregistrent les différences d'inventaire (manquants au débit, excédents au crédit). Pour ne pas déroger au jeu des comptes 601/602/604/608 (gestion, statistiques, vérification fiscale), le SYSCOHADA étend le schéma intermittent à toutes les entrées/sorties : reports (a), sorties b (consommation/manquants) crédit 603-73, entrées c (achats/excédents) débit 3…

### 1.3 Charges constatées d'avance
Partie non consommée extraite des charges → **476 Charges constatées d'avance** (créance sur l'exercice suivant). Ex. : fournitures 6054 = 60 consommées aux 3/4 (stock final 15) ; fournitures 6055 = 50 consommées à moitié (stock final 25) → 476 débité de 40, charges réelles 45 et 25.

## Section 2 — Amortissements

### 2.1 Dotations (art. 45 AUDCIF)
Amortissement = répartition du montant amortissable sur la durée d'utilité selon un plan. Constaté par une dotation (charge non suivie d'une dépense) et une diminution de valeur. Débit **681** (exploitation, incorporelle/corporelle courante) ou **852** (H.A.O. : destruction accidentelle, restructuration, abandon) ; crédit **281 à 284** (amortissement indirect, solde créditeur soustrait à l'actif).

### Application 17 — Dotations aux amortissements
a) brevet 50 à 10 % ; b) matériel de transport 150 acquis le 1er juillet à 20 % ; c) matériel industriel 50, cumul amort. 30, mis au rebut ; d) ensemble informatique 120, amorti 25 % durant 30 mois, abandonné en fin d'exercice (fusion).

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6812 |  | a — Dotations aux amort. des immob. incorp. | 5 |  |
|  | 2812 | Amortissements des brevets |  | 5 |
| 6813 |  | b — Dotations aux amort. des immob. corp. | 15 |  |
|  | 2845 | Amortissements du matériel de transport |  | 15 |
| 812 |  | c — Val. compt. des cessions d'immob. corp. | 20 |  |
| 2841 |  | Amort. du matériel et outillage comm. et indus. | 30 |  |
|  | 2411 | Matériel industriel |  | 50 |
| 6813 |  | d — Dotations aux amort. des immob. corp. (120 × 25 %) | 30 |  |
|  | 2844 | Amortissements du matériel et mobilier |  | 30 |
| 852. |  | exercice N+1 — Dotations aux amortissements H.A.O. (bien abandonné maintenu) | 15 |  |
|  | 2844 | Amortissements du matériel et mobilier |  | 15 |

### 2.2 Amortissements dérogatoires
Dotation fiscale > dotation économique : débit **851** Dotations aux provisions réglementées (H.A.O.), crédit **151** Amortissements dérogatoires. Dotation fiscale < économique : reprise, débit **151**, crédit **861** Reprises de provisions réglementées (H.A.O.).

### Application 18 — Amortissements dérogatoires
Matériel de transport 600, économique linéaire 4 ans (150/an), fiscal dégressif 40 %.

| Année | Fiscal | Économique | Dotation 851 | Reprise 861 |
|---|---|---|---|---|
| n | 240 | 150 | 90 | — |
| n+1 | 144 | 150 | — | 6 |
| n+2 | 108 | 150 | — | 42 |
| n+3 | 108 | 150 | — | 42 |
| Total | 600 | 600 | 90 | 90 |

Attention : malgré leur nom, « Dotations et Reprises d'amortissements dérogatoires » sont des dotations/reprises de provisions réglementées (donc H.A.O.).

### 2.3 Reprises d'amortissement
Reprises dérogatoires comme ci-dessus ; celles liées aux plus-values à réinvestir → ch. 5 §4.6. Autres reprises (révision du plan) : débit **28..**, crédit **798** (caractère exceptionnel).

## Section 3 — Dépréciations

Distinction (art. 46 et 48 AUDCIF) : **dépréciation** = perte de valeur d'un actif ; **provision** = passif externe (dette) dont l'échéance ou le montant est incertain.

### 3.1-3.2 Dotations pour dépréciations
Immobilisations → dotation ; autres actifs → charge pour dépréciations. Dotations : **691** (exploitation : incorporelle 6913, corporelle 6914), **697** (financière 6972), **853** (H.A.O.). Crédit **291 à 297** (solde créditeur soustrait à l'actif).

### 3.3 Charges pour dépréciations
**659** (exploitation : stocks 6593, créances 6594), **679** (financières, titres de placement 6795), **839** (H.A.O.). Crédit **391-398** (stocks), **490-499** (tiers), **590-599** (trésorerie).

### 3.4 Reprises de dépréciations
Caractère réversible : à n+1, annulation systématique + nouvelle dépréciation, ou ajustement. Augmentation = dotation/charge nouvelle. Diminution/annulation = reprise, au crédit des produits par le débit des comptes de dépréciation. Reprises de dépréciations (immobilisations, débit 29) : **7913** (incorp.), **7914** (corp.), **7972** (financières), **863** (H.A.O.). Reprises de charges pour dépréciations (débit 39/49/59) : **759** (7593 stocks, 7594 créances), **779** (7795 titres de placement), **849** (H.A.O.).

### Application 19 — Dépréciations
| Élément | n | n+1 |
|---|---|---|
| a. Fonds commercial | 100 | 150 |
| b. Titres de participation (influence notable) | 20 | 18 |
| c. Stocks de marchandises | 40 | 35 |
| d. Créance 12 sur client A | 75 % | 50 % |
| e. Créance 10 sur débiteur divers B | 60 % | 100 % |
| f. Titres de placement | 17 | 11 |

Fin d'exercice « n » :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6913 |  | a — Dot. aux dépréc. d'exploit. des immo. incorp. | 100 |  |
|  | 2915 | Dépréciations du fonds commercial |  | 100 |
| 6972 |  | b — Dotations aux dépréc. des immob. financières | 20 |  |
|  | 2963 | Dépréciations des titres de participations |  | 20 |
| 6593 |  | c — Charges pour dépréciations sur stocks | 40 |  |
|  | 391. | Dépréciations des stocks de marchandises |  | 40 |
| 6594 |  | d & e — Charges pour dépréciations sur créances | 15 |  |
|  | 4912 | Dépréciations des comptes clients |  | 9 |
|  | 497. | Dépréciations des comptes débiteurs divers |  | 6 |
| 6795 |  | f — Charges pour dépréciations sur titres de placement | 17 |  |
|  | 590. | Dépréciations des titres de placement |  | 17 |

Fin d'exercice « n + 1 » :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6913 |  | a — Dot. aux dépréc. d'exploit. des immo. incorp. | 50 |  |
|  | 2915 | Dépréciations du fonds commercial |  | 50 |
| 2963 |  | b — Dépréciations des titres de participations | 2 |  |
|  | 7972 | Reprises de dépréc. des immo. financières |  | 2 |
| 391. |  | c — Dépréciations des stocks de marchandises | 5 |  |
|  | 7593 | Reprises de charges pour dépréc. sur stocks |  | 5 |
| 4912 |  | d — Dépréciations des comptes clients | 3 |  |
|  | 7594 | Reprises de charges pour dépréc. sur créances |  | 3 |
| 6594 |  | e — Charges pour dépréciations sur créances | 4 |  |
|  | 497. | Dépréciations des comptes débiteurs divers |  | 4 |
| 590. |  | f — Dépréciations des titres de placement | 6 |  |
|  | 7795 | Reprises de charges pour dépréc. fin. sur titres de placement |  | 6 |

Note codification (3 chiffres suffisants pour servir le CR) : dotations 691/697/853 · reprises 791/797/863 ; charges 659/679/839 · reprises 759/779/849.

## Section 4 — Provisions pour risques et charges

### 4.1 Dotations et charges pour provisions
Passif externe (art. 48). Provisions à **plus d'un an** → dotation ; à **moins d'un an** → charge pour provisions pour risques à court terme.
- Plus d'un an : débit **6911** (exploitation), **6971** (financière), **854** (H.A.O.) ; crédit **19** (191-194, 1983 risques ; 195-1981, 1984, 1985 charges).
- Moins d'un an : débit **659** (exploit., ex. 6591), **679**, **839** ; crédit **499** (tiers, dettes circulantes) ou **599** (financier, passif circulant).

### 4.2 Reprises
Réversibilité : à n+1, augmentation (nouvelle dotation/charge) ou reprise. Provisions à plus d'un an (19) reprises par crédit **7911** (exploit.), **7971** (fin.), **864** (H.A.O.). Provisions à moins d'un an (499/599) reprises par crédit **759**, **779**, **849**.

### Application 20 — Provisions
| Élément | n | n+1 |
|---|---|---|
| a. Litige ancien salarié (< 1 an) | 10 | 15 |
| b. Service après-vente (> 1 an, réduite 10 %) | 20 | 18 |
| c. Difficulté d'exécution de marché (< 1 an) | 0 | 7 |
| d. Dette fournisseurs en $ (hausse cours) | 3 | 4 |
| e. Dette emprunt en devise (hausse cours) | 11 | 8 |
| f. Indemnités de départ à la retraite | 27 | 26 |
| g. Rappels d'impôts (> 1 an) | 8 | 0 |
| h. Intérêts de retard impôts courants (< 1 an) | 1 | 0 |
| i. Pénalités impôts courants (> 1 an) | 2 | 0 |

Fin d'exercice « N » :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6591 |  | a — Charges pour prov. risques à C.T. d'exploitation | 10 |  |
|  | 4991 | Provisions pour risques à court terme |  | 10 |
| 6911 |  | b — Dotations aux provisions d'exploitation | 20 |  |
|  | 192 | Prov. pour garanties données aux clients |  | 20 |
| 6591 |  | d — Charges pour prov. risques à C.T. d'exploitation | 3 |  |
|  | 4991 | Prov. pour risques à C.T. d'exploitation |  | 3 |
| 6971 |  | e — Dotations aux provisions financières | 11 |  |
|  | 194 | Provisions pour pertes de change |  | 11 |
| 6911 |  | f — Dotations aux provisions d'exploitation | 27 |  |
|  | 1961 | Prov. pour pensions et obligations similaires |  | 27 |
| 854 |  | g — Dotations aux prov. pour risques et charges H.A.O. | 8 |  |
|  | 195 | Provisions pour impôts |  | 8 |
| 6591 |  | h — Charges pour prov. risques à C.T. d'exploitation | 1 |  |
|  | 4991 | Provisions pour risques à court terme |  | 1 |
| 6911 |  | i — Dotations aux provisions d'exploitation | 2 |  |
|  | 1981 | Provisions pour amendes et pénalités |  | 2 |

Fin d'exercice « n + 1 » :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6591 |  | a — Charges pour prov. risques à C.T. d'exploitation | 5 |  |
|  | 4991 | Provisions pour risques à court terme |  | 5 |
| 192 |  | b — Prov. pour garanties données aux clients | 2 |  |
|  | 7911 | Reprise de provisions d'exploitation |  | 2 |
| 6591 |  | c — Charges pour prov. risques à C.T. d'exploitation | 7 |  |
|  | 4991 | Provisions pour risques à court terme |  | 7 |
| 6591 |  | d — Charges pour prov. risques à C.T. d'exploitation | 1 |  |
|  | 4991 | Prov. pour risques à C.T. d'exploitation |  | 1 |
| 194 |  | e — Provisions pour pertes de change | 3 |  |
|  | 7971 | Reprises de provisions financières |  | 3 |
| 1961 |  | f — Prov. pour pensions et obligations similaires | 1 |  |
|  | 7911 | Reprises de provisions d'exploitation |  | 1 |
| 195 |  | g — Provisions pour impôts | 8 |  |
|  | 864 | Reprises de provisions pour risques H.A.O. |  | 8 |
| 4991 |  | h — Provisions pour risques à court terme | 1 |  |
|  | 7591 | Reprises de provisions pour risques à C.T. |  | 1 |
| 1981 |  | i — Provisions pour amendes et pénalités | 2 |  |
|  | 7911 | Reprise de provisions d'exploitation |  | 2 |

## Section 5 — Autres régularisations de charges

### 5.1 Principe (art. 59)
Indépendance des exercices : rattacher à l'exercice ses seuls événements. Corriger les charges (classe 6 et comptes impairs classe 8) pour n'inclure que l'exercice (éliminer les montants ultérieurs, ajouter les montants omis).

### 5.2 Charges constatées d'avance
Partie concernant n+1 → crédit du compte de charge par débit **476 Charges constatées d'avance** (créance sur l'exercice suivant) : autres achats 605, primes d'assurances, abonnements, intérêts payés d'avance. Achats déjà facturés mais non livrés → **38 Stocks en cours de route, en consignation ou en dépôt** (pas de régularisation de charge). Les CCA n'apparaissent pas directement au bilan (incluses dans « Autres créances »). Régularisations hors TVA récupérable.

### Application 21 — Charges constatées d'avance
a) produits d'entretien 6054 = 20, consommés 75 % ; b) fournitures 6055 = 30, consommées 80 % ; c) prime assurance auto échue 30 avril : 36 ; d) abonnement revue échu 31 mars : 16 ; e) intérêts trimestriels payés d'avance 1er nov. : 3 ; f) facture fournisseur enregistrée, marchandise non livrée : 20.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 476 |  | Charges constatées d'avance | 28 |  |
|  | 6054 | Fournitures d'entretien non stockables |  | 5 |
|  | 6055 | Fournitures de bureau non stockables |  | 6 |
|  | 6252 | Assurances matériel de transport |  | 12 |
|  | 6265 | Documentation générale |  | 4 |
|  | 6712 | Intérêts auprès établissement de crédit |  | 1 |
| 381 |  | Marchandises en cours de route | 20 |  |
|  | 6031 | Variations des stocks de marchandises |  | 20 |

### 5.3 Charges à payer
Charges certaines non encore enregistrées : débit des comptes de charges, crédit des tiers en compte divisionnaire à terminaison 8 : **408** (fournisseurs, factures non parvenues), **4818** (fournisseurs d'investissements, FNP), **4281/4286** (personnel), **4381-4386** (organismes sociaux), **4486** (État), **4198** (RRR et avoirs à accorder). Intérêts courus sur emprunts → **166**. TVA probable : débit **4455** (FNP) ou **4435** (factures à établir).

### Application 22 — Charges à payer
a) marchandises groupe même région, bon de livraison seul, 50 HT TVA 10 % ; b) matériel transport, BL seul, 100 HT TVA 20 % non récupérable ; c) ristourne promise à un client 10 HT TVA 10 % ; d) droit à congé salariés nationaux dès 1er juin : 7/12 de 240 ; e) cotisations sociales 25 % ; f) patente exercice n : 21 ; g) obligation cautionnée marchandises importées 52 dont 3 d'intérêts ; h) intérêts annuels d'emprunt échus 31 mars : 10 % de 1 000 ; i) intérêts de retard dus à un fournisseur : 7.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6013 |  | a — Achats de march. aux entités du gpe dans la région | 50 |  |
| 4455 |  | Etat, TVA récupérable sur fact. non parvenues | 5 |  |
|  | 4082 | Fournisseurs groupe, fact. non parvenues |  | 55 |
| 2451 |  | b — Matériel automobile | 120 |  |
|  | 4818 | Fournisseurs d'invest., fact. non parvenues |  | 120 |
| 701. |  | c — Ventes de marchandises | 10 |  |
| 4435 |  | Etat, TVA sur factures à établir | 1 |  |
|  | 4198 | R.R.R. et autres avoirs à accorder |  | 11 |
| 6611 |  | d — Appointements salaires | 140 |  |
|  | 4281 | Dettes provisionnées pour congés à payer |  | 140 |
| 6641 |  | e — Charges sociales sur rémunération du pers. nat. | 35 |  |
|  | 4382 | Charges sociales sur congés à payer |  | 35 |
| 6412 |  | f — Patentes, licences et taxes annexes | 21 |  |
|  | 4486 | Etat, charges à payer |  | 21 |
| 6012 |  | g — Achats de marchandises hors région | 49 |  |
| 6743 |  | Intérêts sur obligations cautionnées | 3 |  |
|  | 4491 | Etat, obligations cautionnées |  | 52 |
| 6712 |  | h — Intérêts emprunts auprès des établissements de crédit | 75 |  |
|  | 1662 | Intérêts courus sur emprunts auprès étab. crédit |  | 75 |
| 6744 |  | i — Intérêts sur dettes commerciales | 7 |  |
|  | 4086 | Fournisseurs, intérêts courus |  | 7 |

### 5.4 Charges antérieures (art. 61)
Charges enregistrées en n mais concernant n−1 : restent dans le résultat n (ordinaire ou H.A.O.), mention en Notes annexes. Sous-comptes classe 6 « sur exercices antérieurs » ou tableau extra-comptable.

### 5.5 Contre-passation
CCA : au début (immédiate) ou à la fin de n+1. Charges à payer : au début/fin de n+1 ou au fur et à mesure des pièces (progressive). Contre-passation à l'ouverture vivement recommandée.

## Section 6 — Autres régularisations de produits

### 6.1 Principe (art. 59)
Corriger les produits (classe 7 et comptes pairs classe 8) pour n'inclure que l'exercice.

### 6.2 Produits constatés d'avance
Partie concernant n+1 → débit du compte de produit par crédit **477 Produits constatés d'avance** (dette envers l'exercice suivant) : factures émises avec livraison retardée, abonnements demandés aux clients, intérêts de prêts payés d'avance. Ventes facturées non livrées → coût défalqué du stock. Hors TVA récupérable.

### Application 23 — Produits constatés d'avance
a) facture client émise, marchandise A1 non livrée : 10 HT, marge 50 % ; b) facture client groupe, maintenance 1/10 au 30/9 : 12 HT ; c) intérêt semestriel sur titres immobilisés, payé d'avance 1/11 au 30/4 : 6.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6031 |  | a — Variations des stocks de marchandises | 5 |  |
|  | 3111 | Marchandises A1 |  | 5 |
| 7063 |  | b, c — Services vendus aux entités du gpe dans la région | 9 |  |
| 7713 |  | Intérêts sur créances diverses | 4 |  |
|  | 477 | Produits constatés d'avance |  | 13 |

### 6.3 Produits à recevoir
Produits certains non encore enregistrés : crédit des produits, débit des tiers en compte à terminaison 8 (sauf 449) : **4098** (fournisseurs RRR à obtenir), **4181/4186** (clients, factures à établir / intérêts courus), **4858** (créances sur cessions d'immo., factures à établir), **4287** (personnel), **4387** (organismes sociaux), **4493-4496** (État, fonds/subventions à recevoir), **458** (organismes internationaux). Intérêts courus sur prêts → **506** (titres de placement) ou **276** (autres). TVA probable : crédit **4455** (avoir attendu du fournisseur) ou **4435** (facture à adresser au client).

### Application 24 — Produits à recevoir
a) ristourne promise par un fournisseur (non ventilable) 2 % de 1 000, TVA 10 % ; b) produit fini adressé à un client groupe, facture non établie, 40 HT TVA 10 % ; c) terrain à bâtir cédé, facture non établie, 30 HT TVA 20 % ; d) retenue de prime sur personnel national : 4 ; e) cotisations sociales à réduire 25 % ; f) subvention d'exploitation à recevoir : État 15, Fonds des Nations unies 25 ; g) intérêts à recevoir 6 % sur prêt de 100 au personnel, le 30 juin.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4098 |  | a — Fournisseurs, R.R.R. et autres avoirs à obtenir | 22 |  |
|  | 6019 | R.R.R. obtenus |  | 20 |
|  | 4455 | Etat, TVA récupérable sur factures non parvenues |  | 2 |
| 4181 |  | b — Clients, factures à établir | 44 |  |
|  | 7023 | Ventes de produits finis aux entités du groupe (Région) |  | 40 |
|  | 4435 | Etat, TVA sur factures à établir |  | 4 |
| 4858 |  | c — Créances sur cessions d'immo., factures à établir | 36 |  |
|  | 2221 | Terrain à bâtir |  | 30 |
|  | 4435 | Etat, TVA sur factures à établir |  | 6 |
| 4287 |  | d — Personnel, produits à recevoir | 4 |  |
|  | 6612 | Primes et gratifications |  | 4 |
| 4387 |  | e — Organismes sociaux, produits à recevoir | 1 |  |
|  | 6641 | Charges sociales sur rémunération du personnel national |  | 1 |
| 4495 |  | f — Etat, subventions d'exploitation à recevoir | 15 |  |
|  | 7181 | Autres subv. d'exploitation versées par l'État et les collectivités |  | 15 |
| 4582 |  | f — Organismes internationaux, subventions à recevoir | 25 |  |
|  | 7182 | Autres subv. d'exploitation versées par les organismes internationaux |  | 25 |
| 4287 |  | g — Personnel, produits à recevoir | 3 |  |
|  | 7712 | Intérêts de prêts |  | 3 |

### 6.4 Produits antérieurs (art. 61)
Produits enregistrés en n concernant n−1 : restent dans le résultat n, mention en Notes annexes.

### 6.5 Contre-passation
Comme pour les charges : PCA et produits à recevoir contre-passés à l'ouverture de n+1 (recommandé), en fin de n+1, ou progressivement.
