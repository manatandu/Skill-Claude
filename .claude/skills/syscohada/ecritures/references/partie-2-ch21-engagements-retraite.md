# Partie 2 — Chapitre 21 : Engagements de retraite et autres avantages assimilés

> Montants pédagogiques. Écritures en tableau 5 colonnes : Débit | Crédit | Date et libellé | Montant débit | Montant crédit. Méthode des unités de crédit projetées.

## Application 81 — Valeur actuelle de l'obligation

Salarié Alpha : âge d'embauche 25 ans, départ à 60 ans, embauche 01/01/N. Salaire moyen actuel (12 derniers mois au 31/12/N) 2 000 000. Progression salaires 5 %. Taux d'actualisation 5,85 %. Probabilité de présence 98,31 %, de survie 79 %. Charges fiscales et sociales 10 %. Convention : 40 % du salaire moyen (12 derniers mois) à la retraite.

**Calcul au 31/12/N** (carrière totale 35 ans, ancienneté actuelle 1 an) :
- Indemnité future = 2 000 000 × (1,05)³⁴ × 40 % × (1/35) = 120 077 F.
- Ancienneté actuelle / totale = 1/35.
- Probabilité d'atteinte de la retraite = 0,9831 × 0,79 = 0,77.
- Facteur d'actualisation = (1,0585)⁻³⁴.
- **Valeur actuelle de l'obligation au 31/12/N** = [2 000 000 × (1,05)³⁴ × 40 % × 1/35] × 0,77 × (1,0585)⁻³⁴ × 1,1 = **14 718 F**.

Provision au 31/12/N :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6911 |  | 31/12/N — Dotations aux prov. d'exploitation pour risques et charges | 14 718 |  |
|  | 1961 | Provisions pour pensions et obligations similaires — engagement de retraite |  | 14 718 |

Au 31/12/N+1, la valeur actuelle passe à 16 440 F, dont coût des services rendus 15 579 et coût financier 861 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6911 |  | 31/12/N+1 — Dotations aux prov. d'exploitation pour risques et charges | 15 579 |  |
| 6971 |  | Dotations aux prov. financières pour risques et charges | 861 |  |
|  | 1961 | Provisions pour pensions et obligations similaires — engagement de retraite |  | 16 440 |

## Application 82 — Écart actuariel

Données : valeur actuelle de l'obligation au 31/12/N = 14 718 ; coût des services rendus N+1 = 15 579 ; coût financier = 861 ; valeur actuelle **attendue** au 31/12/N+1 = 31 158 (14 718 + 15 579 + 861). Le taux d'actualisation passe de 5,85 % à 6 %.

**Valeur actuelle au 31/12/N+1 avec taux 6 %** = [2 000 000 × (1,05)³³ × 40 % × 2/35] × 0,77 × (1,06)⁻³³ × 1,1 = **29 736 F**.

**Écart actuariel** = valeur attendue − valeur au nouveau taux = 31 158 − 29 736 = **1 422 F** (gain actuariel).

Comptabilisation (gain → reprise) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 1961 |  | 31/12/N+1 — Provisions pour pensions et obligations similaires | 1 422 |  |
|  | 7971 | Reprises de prov. financières pour risques et charges (gain actuariel) |  | 1 422 |

> Un écart actuariel de **perte** se comptabiliserait par une dotation complémentaire (6911/6971 · 1961).

## Application 83 — Régimes couverts par des actifs

Police d'assurance souscrite le 31/12/N. Prime annuelle 10 000 (chèque au 31/12/N). Valeur actuelle de l'obligation au 31/12/N = 14 718. À la retraite (31/12/N+34) : valeur actuelle de l'obligation 4 202 678 ; valeur actuelle des primes versées 3 200 000. Le 01/01/N+35, la compagnie verse 3 200 000 au salarié (personnel local) et l'entité verse le complément par chèque.

Prime d'assurance versée (31/12/N) — actif de couverture :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4731 |  | 31/12/N — Assurances (actif de couverture) | 10 000 |  |
|  | 521 | Banques |  | 10 000 |

Constitution de la provision au 31/12/N (14 718) : 6911 · 1961.

**Départ à la retraite (01/01/N+35).** Complément à la charge de l'entité = 4 202 678 − 3 200 000 = 1 002 678 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 1961 |  | 01/01/N+35 — Provisions pour pensions et obligations similaires | 4 202 678 |  |
|  | 4731 | Assurances (versement de la compagnie) |  | 3 200 000 |
|  | 521 | Banques (complément versé par l'entité) |  | 1 002 678 |
