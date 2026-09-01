# Partie 1 — Chapitre 1 : Plan de comptes, subdivisions

> Cadre de lecture du plan, pas d'écriture. Pour le numéro et l'intitulé exact d'un compte → `syscohada-comptes`. Pour l'article de l'Acte uniforme → `audcif-acte-uniforme` (Titre VII, ch. 1-2).

## Section 1 — Plan de comptes

Le « plan des comptes » n'est pas la « liste des comptes ». Le Plan comprend, outre la liste détaillée à 2, 3 et 4 chiffres : la justification des critères de l'arborescence (classes, comptes principaux et divisionnaires), et des indications sur la codification décimale, les constantes et les parallélismes.

### 1.1 Les classes (art. 18 AUDCIF)

Distinction comptes de **situation** (patrimoine/bilan) en classes **1 à 5** et comptes de **gestion** (résultat) en classes **6, 7 et 8**.

**Comptes de situation** — lecture verticale puis horizontale du bilan :
- verticale : le « haut » du bilan vient des classes 1 et 2, le « bas » des classes 3, 4 et 5 ;
- horizontale (droite→gauche) : le passif synthétise la classe 1 et partiellement les classes mixtes 4 et 5 ; l'actif synthétise la classe 2 et partiellement les classes 4 et 5.

| ACTIF | PASSIF |
|---|---|
| 2 - Actif immobilisé | 1 - Ressources stables |
| 3 - Stocks | |
| 4 - Tiers (débiteurs) | 4 - Tiers (créditeurs) |
| 5 - Trésorerie (positive) | 5 - Trésorerie (négative) |

**Comptes de gestion** — définis par la fréquence de l'activité puis la place dans le circuit :
- activité ordinaire : 6 et 7 ; hors activité ordinaire : 8 ;
- amont (entrant / charge) : classe 6 et comptes **impairs** de la classe 8 (81, 83, 85, 87, 89) ;
- aval (sortant / produit) : classe 7 et comptes **pairs** de la classe 8 (82, 84, 86, 88).

### 1.2 Comptes principaux et divisionnaires

Chaque classe = en règle générale 10 comptes à deux chiffres (« comptes principaux »), le premier finissant par 0, le dernier par 9. Au-delà, les subdivisions se limitent à 9 positions : chaque compte principal se subdivise en 9 comptes à 3 chiffres, chacun en 9 comptes à 4 chiffres. Le premier finit par 1, le dernier par 9 ; le 0 garde son caractère générique sauf **490** et **590**.

Ex. : classe 5 → 50 Titres de placement, 51 Valeurs à encaisser, 58 Régie d'avances/accréditifs/virements internes, 59 Dépréciations et provisions pour risque à court terme. Compte 24 → 241, 245, 249 ; 245 → 2451 Matériel automobile … 2458 Autres (vélo, mobylette, moto).

Au-delà de 4 chiffres, la subdivision en sous-comptes est libre, dans le respect des nomenclatures.

### 1.3 Les constantes

- **Chiffre 8** en 3ᵉ ou 4ᵉ position : compte résiduel « divers » (ex. 168 Autres emprunts et dettes ; 2458 Autres matériels de transport).
- **Chiffre 9** en 2ᵉ position : compte de provision — en gestion une dotation (69) ou reprise (79), en situation (19, 29, 39, 49, 59) une provision/dépréciation. Les comptes 29, 39, 49, 59 ont un solde opposé aux autres comptes de leur classe.
- Caractère « d'opposant » aussi pour le 9 en 3ᵉ/4ᵉ position : 109 Apporteurs capital souscrit non appelé et 139 Résultat net : perte (solde débiteur, contre 10 et 13) ; 409 fournisseurs débiteurs (contre 40) ; 419 clients créditeurs (contre 41) ; 60x9 réductions obtenues non ventilables (contre 60x).

### 1.4 Les parallélismes

Numérotation décimale parallèle pour des opérations de sens contraire mais de même nature :
- **28 Amortissements** parallèle aux comptes **21 à 25** ;
- **77 Revenus financiers** parallèle au **67 Frais financiers** ;
- **79 Reprises de provisions** inspiré du **69**.

## Section 2 — Subdivision en sous-comptes

### 2.1 Du SYSCOHADA au plan comptable d'entité (PCE)

Le SYSCOHADA fournit des comptes à 4 chiffres ; l'entité construit son PCE en retenant les comptes utiles et en les subdivisant.

- Subdivision **par nature** (au moins deux positions → 6 chiffres) selon les nomenclatures : `UUUU.UU` = SYSCOHADA.nature. Ex. papier photocopieur = **6047.17** (6047 = achats fournitures de bureau ; 17 = papier).
- Subdivision **par fonction** (une ou deux positions → 7 ou 8 chiffres) : `UUUU.UU.UU` = SYSCOHADA.nature.fonction. Liée à la comptabilité analytique (coûts par regroupement de charges, marges par regroupement de produits). N'a de sens que dans les classes 6, 7, 8 ; entièrement libre. Ex. papier pour le service comptable (codé 02) = **6047.17.02**.

### 2.2 Nomenclatures

Relevés exhaustifs et codifiés de rubriques d'opérations ou d'agents (services nationaux/régionaux de la Statistique ou de la Comptabilité nationale). L'organisation comptable doit renseigner ces rubriques via des sous-comptes regroupables par une grille de passage. La numérotation des sous-comptes reste libre si le regroupement est possible.
