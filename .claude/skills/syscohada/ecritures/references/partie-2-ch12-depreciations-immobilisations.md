# Partie 2 — Chapitre 12 : Dépréciations des immobilisations

> Montants pédagogiques. Écritures en tableau 5 colonnes : Débit | Crédit | Date et libellé | Montant débit | Montant crédit.

## Application 44 — Dépréciation, évaluation ultérieure et reprise

Matériel industriel VB 30 000 000 F, acquis 01/01/N-1, amorti 6 ans (5 000 000/an). Après 2 ans, VNC = 20 000 000. Clôture N : test de dépréciation, valeur actuelle 8 000 000. Clôture N+2 : valeur actuelle 9 000 000.

**Conséquences.**
- Clôture N : perte de valeur = 20 000 000 − 8 000 000 = **12 000 000**. Nouvelle VNC 8 000 000, nouvel amortissement 8 000 000/4 = 2 000 000/an (durée résiduelle 4 ans).
- Fin N+2 : VNC = 8 000 000 − 2 × 2 000 000 = 4 000 000. Valeur actuelle 9 000 000. VNC sur base historique = 30 000 000 − 4 × 5 000 000 = 10 000 000 (plafond). Reprise = 9 000 000 − 4 000 000 = **5 000 000** (9 000 000 < 10 000 000 plafond). Nouvelle VNC 9 000 000, nouvel amortissement 9 000 000/2 = 4 500 000/an (durée résiduelle 2 ans).

**Plan révisé** :

| Année | Base amort. | Dotation | Cumul | Dép. dotation | Dép. reprise | VNC clôture |
|---|---|---|---|---|---|---|
| N-1 | 30 000 000 | 5 000 000 | 5 000 000 | | | 25 000 000 |
| N | 30 000 000 | 5 000 000 | 10 000 000 | 12 000 000 | | 8 000 000 |
| N+1 | 8 000 000 | 2 000 000 | 12 000 000 | | | 6 000 000 |
| N+2 | 8 000 000 | 2 000 000 | 14 000 000 | | 5 000 000 | 9 000 000 |
| N+3 | 9 000 000 | 4 500 000 | 18 500 000 | | | 5 000 000 |
| N+4 | 9 000 000 | 4 500 000 | 23 000 000 | | | 0 |

> Si la valeur actuelle N+2 avait été 13 000 000, la reprise serait plafonnée à 6 000 000 (10 000 000 − 4 000 000) pour ne pas réévaluer l'actif.

## Application 45 — Dépréciation d'un groupe d'actifs immobilisés

Groupe (VNC globale 260 000 000) : fonds commercial 20 000 000 ; terrains bâtis 50 000 000 ; immeuble industriel 150 000 000 ; camions 40 000 000. Valeur actuelle globale au 31/12/N : 200 000 000.

Perte globale = 260 000 000 − 200 000 000 = **60 000 000**.

**Ventilation.** D'abord au fonds commercial (20 000 000, jamais reprise). Solde 40 000 000 réparti proportionnellement à la VNC des autres actifs (base 240 000 000) :
- Terrains bâtis : 40 000 000 × 50 000 000/240 000 000 = 8 333 333
- Immeuble industriel : 40 000 000 × 150 000 000/240 000 000 = 25 000 000
- Camions : 40 000 000 × 40 000 000/240 000 000 = 6 666 667

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6913 |  | 31/12/N — Dotations aux dép. des immob. incorporelles | 20 000 000 |  |
| 6914 |  | Dotations aux dép. des immob. corporelles | 40 000 000 |  |
|  | 2915 | Dépréciations du fonds commercial |  | 20 000 000 |
|  | 2923 | Dépréciations des terrains bâtis |  | 8 333 333 |
|  | 2931 | Dép. bâtiments industriels/agri/adm/com sur sol propre |  | 25 000 000 |
|  | 2945 | Dépréciations du matériel de transport |  | 6 666 667 |

## Application 46 — Pertes de valeur suite à une réévaluation

Bâtiment industriel réévalué (valeur comptable réévaluée 100 000 000). Perte de valeur au 31/12/N = 15 000 000. Écart de réévaluation en capitaux propres = 6 000 000. La perte s'impute d'abord sur l'écart de réévaluation (6 000 000), le surplus (9 000 000) en charge.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 1062 |  | 31/12/N — Écarts de réévaluation libre | 6 000 000 |  |
| 6914 |  | Dotations aux dép. des immob. corporelles | 9 000 000 |  |
|  | 2931 | Dépréciations des bâtiments industriels |  | 15 000 000 |

## Application 47 — Dépréciations d'immobilisations subventionnées

Matériel VNC 20 000 000, financé par subvention. Solde subvention non rapporté = 12 000 000. Valeur actuelle après test = 6 000 000. Deux méthodes, **même impact résultat (−2 000 000)**.

**Méthode 1** — dépréciation = (VNC − solde subvention) − valeur actuelle = (20 000 000 − 12 000 000) − 6 000 000 = 2 000 000 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6914 |  | 31/12/N — Dotations aux dép. des immob. corporelles | 2 000 000 |  |
|  | 2941 | Dépréciations du matériel |  | 2 000 000 |

**Méthode 2** — dépréciation = VNC − valeur actuelle = 14 000 000, avec reprise de la subvention (12 000 000) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6914 |  | 31/12/N — Dotations aux dép. des immob. corporelles | 14 000 000 |  |
|  | 2941 | Dépréciations du matériel |  | 14 000 000 |
| 1411 |  | Subventions d'équipement | 12 000 000 |  |
|  | 799 | Reprises de subventions d'investissement |  | 12 000 000 |

Impact net = −14 000 000 + 12 000 000 = −2 000 000 (identique à la méthode 1).
