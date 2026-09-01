# Partie 2 — Chapitre 41 : Première application du SYSCOHADA révisé

> Montants pédagogiques. Tableau 5 colonnes : Débit | Crédit | Date et libellé | Montant débit | Montant crédit.

**Compte pivot** : **4751** Compte transitoire, ajustement spécial lié à la révision du SYSCOHADA — compte actif. Il reçoit au bilan d'ouverture les soldes des postes que la révision fait disparaître ou reclasse, puis se résorbe sur l'exercice ou sur la durée résiduelle (maximum 5 ans) par le débit ou le crédit des comptes de charges/produits par nature concernés.

## Application 123 — Frais d'établissement et primes de remboursement des obligations

### Opération 1 — Frais de constitution

Entité créée le 1er janvier 2017. Frais de constitution réglés comptant par chèque : honoraires du notaire 5 000 000, frais d'actes 100 000, droit d'enregistrement 900 000. Immobilisés et amortis sur 4 ans. Au 1er janvier 2018 (première application du SYSCOHADA révisé), le solde du compte frais d'établissement est étalé sur la période restant à amortir.

**Principe.** Les comptes de charges immobilisées (hors primes de remboursement des obligations et frais de prospection), enregistrés avant la révision, sont virés au compte **4751**, puis repris sur l'exercice ou étalés sur la durée résiduelle (5 ans maximum) via les comptes de charges par nature concernés.

**Rappel des écritures antérieures**

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6324 |  | 01/01/2017 — Honoraires des professions règlementées | 5 000 000 |  |
| 6325 |  | Frais d'actes et de contentieux | 100 000 |  |
| 646 |  | Droit d'enregistrement | 900 000 |  |
|  | 4011 | Fournisseurs |  | 6 000 000 |
| 4011 |  | Fournisseurs | 6 000 000 |  |
|  | 521 | Banques |  | 6 000 000 |
| 2011 |  | 31/12/2017 — Frais de constitution | 6 000 000 |  |
|  | 781 | Transferts de charges d'exploitation |  | 6 000 000 |
| 6811 |  | Dotations aux amortissements des charges immobilisées | 1 500 000 |  |
|  | 2011 | Frais de constitution (amort. 6 000 000/4) |  | 1 500 000 |

Solde du 2011 au 01/01/2018 : 6 000 000 − 1 500 000 = 4 500 000. Durée restant à courir : 3 ans. Montants à étaler par nature : 6324 = 5 000 000 × 3/4 = 3 750 000 ; 6325 = 100 000 × 3/4 = 75 000 ; 646 = 900 000 × 3/4 = 675 000. Total : **4 500 000**.

**Bilan d'ouverture (01/01/2018)**

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4751 |  | Compte transitoire, ajustement spécial lié à la révision du SYSCOHADA — compte actif | 4 500 000 |  |
|  | 2011 | Frais de constitution |  | 4 500 000 |

**Écriture annuelle d'étalement (31/12/2018, 2019, 2020 — identique chaque année)**

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6324 |  | Honoraires des professions règlementées (3 750 000 × 1/3) | 1 250 000 |  |
| 6325 |  | Frais d'actes et de contentieux (75 000 × 1/3) | 25 000 |  |
| 646 |  | Droit d'enregistrement (675 000 × 1/3) | 225 000 |  |
|  | 4751 | Compte transitoire, ajustement spécial lié à la révision du SYSCOHADA — compte actif |  | 1 500 000 |

Le 4751 s'épuise en 3 exercices : 4 500 000 = 1 500 000 × 3.

### Opération 2 — Primes de remboursement des obligations

Emprunt émis le 01/01/2017 : 300 000 000 F (3 000 obligations de 100 000 F, émises à 95 000 F, remboursables à 110 000 F). Taux d'intérêt 10 %, remboursement in fine le 31/12/2020. Prime amortie sur 4 ans.

**Principe.** Le compte **206** Primes de remboursement des obligations est crédité par le débit du compte **161** Emprunts obligataires. Au fur et à mesure du remboursement (ou au prorata des intérêts courus si le remboursement est in fine), les primes échues passent au débit du compte **6714**. Les primes non échues figurent en engagements hors bilan dans les Notes annexes.

**Rappel des écritures antérieures**

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 521 |  | 01/01/2017 — Banques (95 000 × 3 000) | 285 000 000 |  |
| 206 |  | Primes de remboursement des obligations ((110 000 − 95 000) × 3 000) | 45 000 000 |  |
|  | 1611 | Emprunts obligataires ordinaires (110 000 × 3 000) |  | 330 000 000 |
| 6872 |  | 31/12/2017 — Dotations aux amort. des primes de remboursement | 11 250 000 |  |
|  | 206 | Primes de remboursement des obligations (45 000 000/4) |  | 11 250 000 |

Solde du 206 au 01/01/2018 : 45 000 000 − 11 250 000 = 33 750 000. Durée restant à courir : 3 ans. Intérêts courus par exercice : 300 000 000 × 10 % = 30 000 000/an ; total 2018-2020 = 90 000 000. Quote-part annuelle du 206 rattachée à chaque exercice : 33 750 000 × 30 000 000/90 000 000 = **11 250 000**.

**Bilan d'ouverture (01/01/2018)**

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 1611 |  | Emprunts obligataires ordinaires | 33 750 000 |  |
|  | 206 | Primes de remboursement des obligations |  | 33 750 000 |

**Écriture annuelle (31/12/2018, 2019, 2020 — identique)**

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6714 |  | Primes de remboursement des obligations | 11 250 000 |  |
|  | 1661 | Intérêts courus sur emprunts obligataires |  | 11 250 000 |

### Note 8A — Tableau d'étalement des charges immobilisées (structure)

| Libellés | Frais d'établissement | Charges à répartir sur plusieurs exercices | Primes de remboursement des obligations |
|---|---|---|---|
| Montant global à étaler au 01/01/2018 | 4 500 000 | — | 33 750 000 |
| Durée d'étalement retenue | 3 ans | — | 3 ans |
| Exercice 2018 (comptes/montants) | 6324 : 1 250 000 ; 6325 : 25 000 ; 646 : 225 000 | — | 6714 : 11 250 000 |
| Total exercice 2019 | 1 500 000 | — | 6714 : 11 250 000 |
| Total exercice 2020 | 1 500 000 | — | 6714 : 11 250 000 |
| **Total général** | **4 500 000** | — | **33 750 000** |

## Application 124 — Approche par composants

Matériel industriel acquis le 01/01/2008 (depuis 10 ans), valeur 500 000 000, amortissable sur 20 ans. Au 31/12/2017 : brut 500 000 000, cumul amortissements 250 000 000, VNC 250 000 000. Selon études techniques, le composant représente 25 % de la VNC avec une durée résiduelle de 5 ans ; la structure représente 75 %, durée résiduelle inchangée (10 ans).

**Principe — méthode de réallocation des valeurs nettes comptables.** La VNC globale de l'immobilisation n'est pas modifiée à l'ouverture ; elle est répartie entre composants selon des VNC théoriques (référence aux biens d'occasion, ou composants d'un bien neuf amortis depuis l'origine). Le pourcentage de répartition est appliqué aux valeurs brutes et aux amortissements. Les valeurs brutes ventilées deviennent les nouvelles bases amortissables ; le passage aux durées résiduelles se fait de façon prospective. **Aucun impact sur les capitaux propres.**

### Ventilation au 31/12/2017

| Éléments | Immobilisation | Structure (75 %) | Composant (25 %) |
|---|---|---|---|
| Valeur brute | 500 000 000 | 375 000 000 | 125 000 000 |
| Cumul des amortissements | 250 000 000 | 187 500 000 | 62 500 000 |
| Valeur nette comptable | 250 000 000 | 187 500 000 | 62 500 000 |
| Amortissement annuel à compter de la réallocation | — | 18 750 000 (187 500 000/10) | 12 500 000 (62 500 000/5) |

L'annuité globale passe de 25 000 000 (500 000 000/20) à **31 250 000** (18 750 000 + 12 500 000).

### Écritures au 01/01/2018 (bilan d'ouverture)

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 23111 |  | [texte officiel : l'énoncé porte sur un matériel industriel, mais le guide utilise ici les comptes de « Bâtiments industriels » (2311/28311) — incohérence non corrigée] Bâtiments industriels — structure | 375 000 000 |  |
| 23112 |  | Bâtiments industriels — composant | 125 000 000 |  |
|  | 2311 | Bâtiments industriels |  | 500 000 000 |
| 28311 |  | Amortissements des Bâtiments industriels | 250 000 000 |  |
|  | 283111 | Amortissements des Bâtiments industriels — structure |  | 187 500 000 |
|  | 283112 | Amortissements des Bâtiments industriels — composant |  | 62 500 000 |

### Écritures au 31/12/2018

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 68131 |  | Dotations aux amortissements des immobilisations corporelles | 31 250 000 |  |
|  | 283111 | Amortissements — structure [texte officiel : « bâtiments administratifs » dans le guide] |  | 18 750 000 |
|  | 283132 | Amortissements — composant [texte officiel : idem, numérotation « 283132 » incohérente avec « 283112 » ci-dessus] |  | 12 500 000 |

## Application 125 — Engagement de retraite

Entité faisant appel public à l'épargne. Évaluation actuarielle des indemnités de départ à la retraite : cumul au 31/12/2017 = 75 000 000 (évalué, non comptabilisé antérieurement) ; cumul au 31/12/2018 = 90 000 000. L'entité choisit, pour sa première année d'application, d'étaler linéairement sur 5 ans la partie de l'indemnité relative aux engagements antérieurs non comptabilisés.

**Principe.** La première comptabilisation des indemnités de fin de carrière (crédit du compte **196** Provisions pour pensions et obligations similaires, par le débit du **4751**) est un changement de méthode comptable. Le retraitement est en principe rétrospectif : les engagements antérieurs non comptabilisés (nets d'impôt) sont normalement affectés aux postes de report à nouveau. Deux autres méthodes sont admises à la première application : comptabilisation de la totalité de la charge en fin de premier exercice, ou étalement linéaire sur 5 ans maximum (retenue dans cette Application).

### Bilan d'ouverture (01/01/2018)

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4751 |  | Compte transitoire, ajustement spécial lié à la révision du SYSCOHADA — compte actif | 75 000 000 |  |
|  | 196 | Provisions pour pensions et obligations similaires — engagement de retraite |  | 75 000 000 |

### Écritures au 31/12/2018

**Engagements nés au cours de l'exercice.** Variation de l'obligation : 90 000 000 − 75 000 000 = 15 000 000. Coût financier : 75 000 000 × 6 % = 4 500 000. Coût des services rendus : 15 000 000 − 4 500 000 = 10 500 000.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6911 |  | Dotations aux provisions d'exploitation pour risques et charges | 10 500 000 |  |
| 6971 |  | Dotations aux provisions financières pour risques et charges | 4 500 000 |  |
|  | 1961 | Provisions pour pensions et obligations similaires — engagement de retraite |  | 15 000 000 |

**Étalement des engagements antérieurs** : 75 000 000 / 5 = 15 000 000.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6911 |  | Dotations aux provisions d'exploitation pour risques et charges | 15 000 000 |  |
|  | 4751 | Compte transitoire, ajustement spécial lié à la révision du SYSCOHADA — compte actif |  | 15 000 000 |

## Application 126 — Changement de méthode comptable et contrat à long terme

Entité spécialisée dans l'installation et la maintenance de panneaux solaires, utilisant la méthode à l'achèvement jusqu'au 31/12/2017. Au 01/01/2018, obligation de passer à la méthode à l'avancement. Contrat en cours : prix de vente prévisionnel 12 000 000 (2017 et 2018) ; produits contractuels (facturations intermédiaires) : néant en 2017, 1 250 000 en 2018 ; coût des prestations exécutées (travaux acceptés par le cocontractant) : 2 500 000 en 2017, 2 000 000 en 2018 ; coût total prévisionnel de revient : 7 500 000 en 2017, réestimé avec fiabilité à 9 000 000 en 2018. L'entité impute les produits non enregistrés antérieurement au résultat de l'exercice 2018.

**Principe.** Les comptes **475** Créances sur travaux non encore facturables et **34/35** Produits en cours/Services en cours, constitués selon la méthode d'achèvement, sont soldés au bilan d'ouverture. Le 475 est crédité par le débit du **4751**, puis rapporté globalement ou par fractions égales sur 5 ans par le débit du compte **651** Pertes sur créances clients et autres débiteurs. Les comptes 34/35 sont crédités par le débit du compte **4181** Clients, factures à établir.

**Rappel de l'écriture au 31/12/2017**

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 352 |  | Prestations de services en cours | 2 500 000 |  |
|  | 7352 | Variations de prestations de services en cours |  | 2 500 000 |

**Écriture au 01/01/2018 (bilan d'ouverture)**

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4181 |  | Clients, factures à établir | 2 500 000 |  |
|  | 352 | Prestations de services en cours (changement de méthode comptable) |  | 2 500 000 |
