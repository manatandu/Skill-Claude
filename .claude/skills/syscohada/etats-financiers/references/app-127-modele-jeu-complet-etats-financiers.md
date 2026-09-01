# Application 127 — Modèle type d'un jeu complet d'états financiers (Système normal)

Cette Application (Guide d'application SYSCOHADA, Partie 3 « Présentation des états financiers annuels », chapitre 2, p. 341 à 394) est un exemple entièrement rempli, pour une entité fictive « SYSTEME COMPTABLE OHADA » (SYSCOHADA), du jeu complet d'états financiers déposé à l'administration fiscale : page de garde, fiches d'identification R1 à R4, bilan, compte de résultat, tableau des flux de trésorerie, notes annexes 1 à 36.

**Portée de ce fichier.** Il ne s'agit pas ici d'écritures de journal, mais d'un gabarit de présentation — d'où son rattachement à `syscohada-etats-financiers` plutôt qu'à `syscohada-ecritures`. Ce fichier étend le périmètre du module, qui excluait jusqu'ici le TFT et les notes annexes.

**Ce que ce fichier ne couvre pas.** Ce fichier ne traite que l'Application 127 (chapitre 2, l'exemple rempli). Le chapitre 1 de cette même Partie 3 — logique des postes, des masses et des rubriques — est encodé séparément dans `chapitre-1-logique-postes-masses.md`, à consulter pour comprendre *pourquoi* le bilan et le compte de résultat sont construits ainsi.

**Anomalie du texte officiel.** L'Application 127 date l'exercice du 1er janvier N au 31 décembre N mais indique un « arrêté effectif des comptes » au 30 avril N+1 et un dépôt le 30 avril N+1 — cohérent avec un délai légal de dépôt, mais à ne pas confondre avec la date de clôture comptable (31/12/N) qui reste la date d'arrêté des états financiers eux-mêmes.

## 1. Conditions de recevabilité (rappel administratif)

Pour les entités déposant sur imprimés : n'utiliser que des imprimés normalisés, remplir chaque page lisiblement sans décalage de lignes, ne créer aucune rubrique, éviter toute surcharge (explications sur feuille séparée), n'utiliser que les codes des tables, imprimés en noir et blanc uniquement.

Pour les entités produisant les états à l'aide de l'outil informatique : reproduire à l'identique la contexture des imprimés normalisés, fournir une liasse complète (fiche d'identification + renseignements divers + états financiers), ne créer aucune rubrique, n'utiliser que les codes des tables, imprimés en noir et blanc uniquement.

Les rubriques et postes du bilan, du compte de résultat, des flux de trésorerie, ainsi que les notes non chiffrées, peuvent être supprimés s'ils ne s'appliquent pas à l'entité — mais aucune rubrique nouvelle ne peut être créée.

## 2. Page de garde et fiches R1 à R4

**Page de garde.** Centre de dépôt (fisc), mention « ETATS FINANCIERS NORMALISES — SYSTEME COMPTABLE OHADA (SYSCOHADA) », exercice clos le 31 décembre N, désignation de l'entité, système retenu (Normal / SMT), liste des documents déposés (fiche d'identification, bilan, compte de résultat, TFT, notes annexées), date de dépôt et cachet de l'administration.

**Fiche R1 — Identification et renseignements divers.** Dénomination sociale, sigle, adresse, n° d'identification fiscale, durée de l'exercice comptable et de l'exercice précédent, date d'arrêté effectif des comptes, greffe et n° registre du commerce, n° répertoire des entités, n° caisse sociale, code importateur, code d'activité principale, coordonnées (téléphone, email, boîte postale, ville), adresse géographique complète, désignation précise de l'activité, personne à contacter, professionnel ayant établi les états financiers (expert-comptable ou comptable agréé inscrit à l'Ordre), case « états financiers approuvés par l'Assemblée Générale », nom/qualité/date de signature du signataire, domiciliations bancaires.

**Fiche R2 — Forme juridique et activité.** Codes à deux chiffres pour la forme juridique, le régime fiscal, le pays du siège social (renvoi à la Note 36 pour les tables de codes) ; nombre d'établissements dans le pays et hors du pays avec comptabilité distincte ; première année d'exercice dans le pays ; case « contrôle de l'entité » (public / privé national / privé étranger) ; tableau de l'activité de l'entité par ligne d'activité (désignation, code nomenclature, chiffre d'affaires HT, % dans le CA HT total).

**Fiche R3 — Dirigeants et conseil d'administration.** Deux tableaux identiques dans leur structure : nom, prénoms, qualité (PCA, DG, Administrateur, etc.), n° d'identification fiscale (dirigeants uniquement), adresse.

**Fiche R4 — Liste des notes annexes applicables.** Tableau à 36 lignes (une par note), chacune cochée en colonne « A » (Applicable) ou « N/A » (Non applicable). C'est cette fiche qui autorise la suppression d'une note non pertinente sans créer de rubrique — la case cochée fait foi du périmètre réellement déposé. Dans l'exemple, sont cochées N/A : Note 3B (biens pris en location acquisition), Note 3F (tableau d'étalement des charges immobilisées), Note 9 (titres de placement), Note 10 (valeurs à encaisser), Note 15B (autres fonds propres), Note 16B et 16B bis (engagements de retraite méthode actuarielle — l'entité utilise une méthode simplifiée, cf. Note 16A), Note 16C (actifs et passifs éventuels), Note 20 (banques, crédit d'escompte et de trésorerie), Note 35 (informations sociales, environnementales et sociétales).

## 3. Bilan au 31 décembre N (avec codes de rubrique)

Les codes ci-dessous recoupent `references/maquette.tsv` de ce module ; ils servent de cas de contrôle croisé.

**Actif** (brut / amortissements-dépréciations / net N / net N-1, en unités de l'exemple)

| Réf | Rubrique | Brut | Amort./Dépréc. | Net N | Net N-1 |
|---|---|---|---|---|---|
| AD | Immobilisations incorporelles | 4 650 000 | 0 | 4 650 000 | 2 650 000 |
| AF | Brevets, licences, logiciels et droits similaires | 3 050 000 | | 3 050 000 | 1 050 000 |
| AG | Fonds commercial et droit au bail | 1 600 000 | | 1 600 000 | 1 600 000 |
| AI | Immobilisations corporelles | 1 012 410 344 | 321 157 361 | 691 252 983 | 203 544 627 |
| AJ | Terrains | 38 673 950 | | 38 673 950 | 35 173 950 |
| AK | Bâtiments | 741 411 100 | 160 048 641 | 581 362 459 | 136 097 141 |
| AL | Aménagements, agencements et installations | 73 328 267 | 71 328 267 | 2 000 000 | 0 |
| AM | Matériel, mobilier et actifs biologiques | 82 947 027 | 35 540 453 | 47 406 574 | 32 086 036 |
| AN | Matériel de transport | 76 050 000 | 54 240 000 | 21 810 000 | 187 500 |
| AP | Avances et acomptes versés sur immobilisations | 20 000 000 | | 20 000 000 | 0 |
| AQ | Immobilisations financières | 4 419 790 | 0 | 4 419 790 | 4 548 658 |
| AZ | TOTAL ACTIF IMMOBILISE | 1 041 480 134 | 321 157 361 | 720 322 773 | 210 743 285 |
| BA | Actif circulant HAO | 2 140 000 | | 2 140 000 | 380 000 |
| BB | Stocks et encours | 18 560 138 | | 18 560 138 | 15 868 433 |
| BG | Créances et emplois assimilés | 206 981 960 | 31 677 520 | 175 304 440 | 144 512 218 |
| BK | TOTAL ACTIF CIRCULANT | 227 682 098 | 31 677 520 | 196 004 578 | 160 760 651 |
| BS | Banques, chèques postaux, caisse et assimilés | 123 097 127 | 0 | 123 097 127 | 74 584 157 |
| BT | TOTAL TRESORERIE ACTIF | 123 097 127 | 0 | 123 097 127 | 74 584 157 |
| BU | Écart de conversion-Actif | 15 000 000 | | 15 000 000 | 0 |
| BZ | TOTAL GENERAL | 1 407 259 359 | 352 834 881 | 1 054 424 478 | 446 088 093 |

**Passif** (net N / net N-1)

| Réf | Rubrique | Net N | Net N-1 |
|---|---|---|---|
| CA | Capital | 400 000 000 | 100 000 000 |
| CB | Apporteurs capital non appelé (−) | −100 000 000 | |
| CD | Écarts de réévaluation | 3 500 000 | |
| CE | Réserves indisponibles | 20 000 000 | 20 000 000 |
| CF | Report à nouveau (+ ou −) | 76 069 991 | 47 450 317 |
| CG | Résultat net de l'exercice | 215 389 710 | 118 619 674 |
| CH | Subventions d'investissement | 2 000 000 | |
| CJ | Provisions réglementées | 40 000 000 | |
| CP | TOTAL CAPITAUX PROPRES ET RESSOURCES ASSIMILEES | 656 959 701 | 286 069 991 |
| DA | Emprunts et dettes financières diverses | 94 699 075 | 2 200 000 |
| DC | Provisions pour risques et charges | 62 116 366 | 54 864 697 |
| DD | TOTAL DETTES FINANCIERES ET RESSOURCES ASSIMILEES | 156 815 441 | 57 064 697 |
| DF | TOTAL RESSOURCES STABLES | 813 775 142 | 343 134 688 |
| DH | Dettes circulantes HAO | 156 649 942 | 399 942 |
| DJ | Fournisseurs d'exploitation | 38 210 222 | 55 894 206 |
| DK | Dettes fiscales et sociales | 42 668 247 | 36 010 298 |
| DM | Autres dettes | 620 000 | 10 648 959 |
| DP | TOTAL PASSIF CIRCULANT | 238 148 411 | 102 953 405 |
| DT | TOTAL TRESORERIE PASSIF | 0 | 0 |
| DV | Écart de conversion-Passif | 2 500 925 | |
| DZ | TOTAL GENERAL | 1 054 424 478 | 446 088 093 |

Contrôle d'équilibre : BZ (net, 1 054 424 478) = DZ (1 054 424 478). Colonne N-1 obligatoire, présente dans l'exemple.

## 4. Compte de résultat de l'exercice (avec codes)

| Réf | Libellé | N | N-1 |
|---|---|---|---|
| XA | MARGE COMMERCIALE | 40 000 000 | 0 |
| XB | CHIFFRE D'AFFAIRES (A+B+C+D) | 2 041 946 745 | 1 871 826 890 |
| XC | VALEUR AJOUTEE | 485 093 197 | 382 440 760 |
| XD | EXCEDENT BRUT D'EXPLOITATION | 266 876 104 | 173 588 509 |
| XE | RESULTAT D'EXPLOITATION | 240 364 791 | 141 972 754 |
| XF | RESULTAT FINANCIER | 4 000 000 | 0 |
| XG | RESULTAT DES ACTIVITES ORDINAIRES | 244 364 791 | 141 972 754 |
| XH | RESULTAT HORS ACTIVITES ORDINAIRES | 2 127 119 | 58 333 |
| XI | RESULTAT NET | 215 389 710 | 118 619 674 |

La structure en cascade (marge commerciale → chiffre d'affaires → valeur ajoutée → EBE → résultat d'exploitation → résultat financier → RAO → RHAO → résultat net) est celle du compte de résultat SYSCOHADA par nature ; chaque solde intermédiaire est un point de contrôle indépendant, pas seulement une sous-somme.

## 5. Tableau des flux de trésorerie (méthode indirecte, à partir de la CAFG)

| Réf | Libellé | N | N-1 |
|---|---|---|---|
| ZA | Trésorerie nette au 1er janvier | 74 584 157 | 33 595 404 |
| ZB | Flux de trésorerie des activités opérationnelles | 170 234 983 | 98 148 770 |
| ZC | Flux de trésorerie des opérations d'investissement | −328 722 013 | −17 160 017 |
| ZD | Flux de trésorerie des capitaux propres | 112 000 000 | −40 000 000 |
| ZE | Flux de trésorerie des capitaux étrangers | 95 000 000 | 0 |
| ZF | Flux de trésorerie des activités de financement (D+E) | 207 000 000 | −40 000 000 |
| — | Variation de la trésorerie nette (B+C+F) | 48 512 970 | 40 988 753 |
| ZH | Trésorerie nette au 31 décembre (G+A) | 123 097 127 | 74 584 157 |

Point de départ : la Capacité d'Autofinancement Globale (CAFG, 241 773 904 en N), puis correction par les variations de BFG (actif circulant HAO, stocks, créances et emplois assimilés, passif circulant). Contrôle de clôture obligatoire : trésorerie nette au 31/12/N = trésorerie actif N − trésorerie passif N (123 097 127 − 0 = 123 097 127, cohérent avec BT − DT du bilan).

## 6. Notes annexes 1 à 36 — table de correspondance

| Note | Intitulé | Contenu type (illustré dans l'exemple) |
|---|---|---|
| 1 | Dettes garanties par des sûretés réelles | Tableau libellé / montant brut / hypothèques / nantissements / gages — ex. hypothèque sur immobilier pour garantir un emprunt |
| 2 | Informations obligatoires | Déclaration de conformité au SYSCOHADA, règles et méthodes comptables, dérogations éventuelles aux postulats, informations complémentaires bilan/CR/TFT |
| 3A | Immobilisation brute | Tableau de mouvements : montant brut à l'ouverture + acquisitions/apports − cessions ± virements poste à poste = montant brut à la clôture, par rubrique |
| 3B | Biens pris en location acquisition | N/A dans l'exemple |
| 3C | Immobilisations : amortissements | Cumul à l'ouverture + dotations − amortissements sortis = cumul à la clôture ; taux retenus par catégorie |
| 3D | Immobilisations : plus-values et moins-values de cession | Montant brut, amortissements pratiqués, VNC, prix de cession, plus/moins-value |
| 3E | Informations sur les réévaluations effectuées | Nature et date, éléments réévalués par poste (coûts historiques / écarts et provisions spéciales), méthode retenue, traitement fiscal de l'écart |
| 3F | Tableau d'étalement des charges immobilisées | N/A dans l'exemple |
| 4 | Immobilisations financières | Prêts et dépôts, dépréciations, échéancier (à un an au plus / un à deux ans / plus de deux ans) |
| 5 | Actif circulant et dettes circulantes HAO | Deux tableaux distincts : créances HAO et dettes circulantes HAO, avec commentaire sur leur origine |
| 6 | Stocks et encours | Par catégorie (marchandises, matières premières, emballages), variation en valeur et en %, méthode de valorisation |
| 7 | Clients | Clients hors litige / créances litigieuses, dépréciations, échéancier |
| 8 | Autres créances | Personnel, associés compte courant, débiteurs divers, charges constatées d'avance, échéancier |
| 9 | Titres de placement | N/A dans l'exemple |
| 10 | Valeurs à encaisser | N/A dans l'exemple |
| 11 | Disponibilités | Banques locales, caisse, régies d'avances ; commentaire sur le rapprochement bancaire |
| 12 | Écarts de conversion et transferts de charges | Écarts actif/passif par devise (montant en devises, cours d'acquisition, cours de clôture) ; transferts de charges d'exploitation |
| 13 | Capital : valeur nominale des actions ou parts | Répartition par actionnaire, nature des actions, cessions/remboursements en cours d'exercice |
| 14 | Primes et réserves | Réserves indisponibles, report à nouveau, variation |
| 15A | Subventions et provisions réglementées | Origine, régime fiscal, échéances |
| 15B | Autres fonds propres | N/A dans l'exemple |
| 16A | Dettes financières et ressources assimilées | Emprunts par établissement, provisions pour pensions, échéancier, commentaire sur la méthode retenue pour les engagements de retraite (actuarielle ou simplifiée) |
| 16B / 16B bis | Engagements de retraite et avantages assimilés (méthode actuarielle) | N/A si méthode simplifiée retenue (comme dans l'exemple, cf. Note 16A) |
| 16C | Actifs et passifs éventuels | N/A dans l'exemple |
| 17 | Fournisseurs d'exploitation | Fournisseurs et fournisseurs factures non parvenues, fournisseurs débiteurs, échéancier |
| 18 | Dettes fiscales et sociales | Détail personnel/caisses/État, échéancier |
| 19 | Autres dettes et provisions pour risques à court terme | Associés compte courant, créditeurs divers |
| 20 | Banques, crédit d'escompte et de trésorerie | N/A dans l'exemple (pas de trésorerie passive) |
| 21 | Chiffre d'affaires et autres produits | Détail par nature de vente (région/hors région, remises), production immobilisée, autres produits |
| 22 | Achats | Marchandises, matières premières, autres achats (détail par nature) |
| 23 | Transports | Sur ventes, pour compte de tiers, du personnel, de plis, autres |
| 24 | Services extérieurs | Locations, entretien, assurances, télécommunications, honoraires, etc. |
| 25 | Impôts et taxes | Droits d'enregistrement, pénalités et amendes fiscales, autres |
| 26 | Autres charges | Pertes sur créances, dons et mécénat, charges diverses |
| 27A | Charges de personnel | Rémunérations, indemnités, charges sociales, médecine du travail, équipements |
| 27B | Effectifs, masse salariale et personnel extérieur | Tableau croisé qualification × nationaux/autres États OHADA/hors OHADA × masse salariale, personnel permanent/saisonnier, personnel extérieur facturé |
| 28 | Provisions et dépréciations inscrites au bilan | Tableau de mouvements (ouverture + dotations − reprises = clôture), par nature d'exploitation/financière/HAO |
| 29 | Charges et revenus financiers | Frais financiers, revenus financiers, par nature |
| 30 | Autres charges et produits HAO | Nature et origine (ex. don reçu) |
| 31 | Répartition du résultat et autres éléments caractéristiques des cinq derniers exercices | Structure du capital, opérations et résultats, dividendes distribués, personnel et politique salariale, sur cinq exercices comparés |
| 32 | Production de l'exercice | Par produit : quantité/valeur vendue dans le pays, dans les autres pays OHADA, hors OHADA, production immobilisée, stock ouverture/clôture |
| 33 | Achats destinés à la production | Par matière : quantité/valeur produits de l'État, produits importés (dans l'État / hors de l'État), variation des stocks |
| 34 | Fiche de synthèse des principaux indicateurs financiers | Soldes intermédiaires de gestion, CAFG, ratios de rentabilité économique/financière, structure financière (FR, BFE, BFHAO, trésorerie nette), variation de trésorerie, endettement financier net — voir détail ci-dessous |
| 35 | Liste des informations sociales, environnementales et sociétales à fournir | N/A dans l'exemple |
| 36 | Tables des codes | Code forme juridique, code régime fiscal, code pays du siège social, codes activités économiques — table de référence pour les Fiches R1/R2 |

### Note 34 en détail — Fiche de synthèse des indicateurs financiers

Structure en cinq blocs, chacun avec sa propre logique de calcul :

**Analyse de l'activité** — soldes intermédiaires de gestion (repris du compte de résultat) puis détermination de la CAFG :

CAFG = EBE + revenus financiers + produits HAO − frais financiers − impôts sur les résultats
Autofinancement = CAFG − distributions de dividendes opérées durant l'exercice

**Analyse de la rentabilité** :

Rentabilité économique = Résultat d'exploitation après impôt théorique / (Capitaux propres + dettes financières)
Rentabilité financière = Résultat net / Capitaux propres

**Analyse de la structure financière** — logique en cascade, chaque niveau se déduisant du précédent :

Ressources stables = Capitaux propres et ressources assimilées + Dettes financières et autres ressources assimilées
Fonds de roulement (1) = Ressources stables − Actif immobilisé
Besoin de financement d'exploitation (2) = Actif circulant d'exploitation − Passif circulant d'exploitation
Besoin de financement HAO (3) = Actif circulant HAO − Passif circulant HAO
Besoin de financement global (4) = (2) + (3)
Trésorerie nette (5) = (1) − (4), à contrôler par (Trésorerie actif − Trésorerie passif)

**Analyse de la variation de la trésorerie** — reprise des trois flux du TFT (opérationnel, investissement, financement).

**Analyse de la variation de l'endettement financier net** :

Endettement financier net = (Dettes financières + Trésorerie passif) − Trésorerie actif

Deux notes de bas de tableau, à reproduire dans tout usage de cette fiche : le résultat d'exploitation retenu pour la rentabilité économique est calculé après un impôt théorique (35 % dans l'exemple, taux à adapter) ; les écarts de conversion doivent être éliminés des dettes/créances concernées pour les ramener à leur valeur initiale avant tout calcul de ratio.

### Note 36 — Tables des codes (référence pour les Fiches R1/R2)

Trois tables de codes à deux chiffres : forme juridique (SA à participation publique = 00, SA = 01, SARL = 02, SCS = 03, SNC = 04, SP = 05, GIE = 06, Association = 07, SAS = 08, Autre = 09 — le premier chiffre passe à 1 si agrément prioritaire), régime fiscal (Réel normal = 1, Réel simplifié = 2, Synthétique = 3, Forfait = 4), pays du siège social (Bénin = 01 … Congo RDC = 17, autres pays africains = 21, France = 23, autres pays UE = 39, USA = 40, Canada = 41, autres pays américains = 49, pays asiatiques = 50, autres pays = 99). S'y ajoute la nomenclature des codes d'activités économiques (ex. C3100 = fabrication de meubles, dans l'exemple), structurée par grande division (agriculture, industries extractives, industries manufacturières, construction, commerce, transport, etc.).
