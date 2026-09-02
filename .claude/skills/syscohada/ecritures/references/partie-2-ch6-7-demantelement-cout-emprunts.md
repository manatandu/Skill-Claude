# Partie 2 — Chapitres 6 et 7 : Démantèlement / remise en état, coût d'emprunts

> Montants pédagogiques. Écritures en tableau 5 colonnes : Débit | Crédit | Date et libellé | Montant débit | Montant crédit.

## Chapitre 6 — Coût de démantèlement, d'enlèvement et de remise en état du site (Application 35)

Matériel industriel lourd acquis 01/01/N, 200 000 000 F, durée 10 ans. Frais de démantèlement actuels 8 203 480 F. Inflation 2 %, actualisation 12 %. Travaux réalisés en février N+10, coût effectif 10 000 000 F.

**Calculs.**
- Coût ajusté de l'inflation : 8 203 480 × (1,02)¹⁰ ≈ **10 000 000 F**.
- Valeur actualisée des frais : 10 000 000 × (1,12)⁻¹⁰ = **3 219 732 F** → incorporée au coût de l'immobilisation.
- Coût d'acquisition total = 200 000 000 + 3 219 732 = **203 219 732 F**.

**Tableau des provisions pour démantèlement** (charges de désactualisation cumulées = 6 780 268) :

| Période | Coût ajusté actualisé | Provision | Charge de désactualisation |
|---|---|---|---|
| 01/01/N | 3 219 732 | 3 219 732 | — |
| 31/12/N | 3 606 100 | 386 368 | 386 368 |
| 31/12/N+1 | 4 038 832 | 432 732 | 432 732 |
| 31/12/N+2 | 4 523 492 | 484 660 | 484 660 |
| 31/12/N+3 | 5 066 311 | 542 819 | 542 819 |
| 31/12/N+4 | 5 674 269 | 607 958 | 607 958 |
| 31/12/N+5 | 6 355 181 | 680 912 | 680 912 |
| 31/12/N+6 | 7 117 802 | 762 621 | 762 621 |
| 31/12/N+7 | 7 971 939 | 854 137 | 854 137 |
| 31/12/N+8 | 8 928 571 | 956 632 | 956 632 |
| 31/12/N+9 | 10 000 000 | 1 071 429 | 1 071 429 |
| **TOTAL** | | **10 000 000** | **6 780 268** |

Charges de désactualisation = provision N-1 × 12 %. Compte : **6971 Dotations aux provisions financières pour risques et charges**.

**Acquisition (01/01/N)** — actif de support :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 24111 |  | 01/01/N — Matériel industriel — Actif de support | 200 000 000 |  |
|  | 4812 | Fournisseurs d'investissements |  | 200 000 000 |

Actif de démantèlement — **Méthode 1** :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 24112 |  | 01/01/N — Matériel industriel — Actif de démantèlement | 3 219 732 |  |
|  | 1984 | Provisions pour démantèlement et remise en état |  | 3 219 732 |

Méthode 2 : 6911 · 1984 (3 219 732), puis 24112 · 7911 (3 219 732).

**Clôture N** — désactualisation puis amortissement (support 200 000 000/10 = 20 000 000 ; démantèlement 3 219 732/10 = 321 973) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6971 |  | 31/12/N — Dotations aux prov. financières (désactualisation) | 386 368 |  |
|  | 1984 | Provisions pour démantèlement et remise en état |  | 386 368 |
| 6813 |  | Dotations aux amort. des immob. corp. | 20 321 973 |  |
|  | 28411 | Amort. matériel et outillage — Actif de support |  | 20 000 000 |
|  | 28412 | Amort. matériel et outillage — Actif de démantèlement |  | 321 973 |

Clôture N+9 : même schéma (désactualisation 1 071 429 ; amortissement 20 321 973).

**Travaux (février N+10)** :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6244 |  | 02/N+10 — Charges de démantèlement et remise en état | 10 000 000 |  |
|  | 401 | Fournisseurs |  | 10 000 000 |

**Clôture N+10** — reprise de la provision (montant initial + désactualisations) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 1984 |  | 31/12/N+10 — Provisions pour démantèlement et remise en état | 10 000 000 |  |
|  | 7911 | Reprises de provisions d'exploitation pour risques et charges |  | 3 219 732 |
|  | 7971 | Reprises de provisions financières pour risques et charges |  | 6 780 268 |

## Chapitre 7 — Coût d'emprunts (Application 36)

Emprunt contracté le 01/03/N, remboursable in fine dans 5 ans, 120 000 000 F au taux 12 %, pour construire un immeuble (siège social). Construction du 01/04/N au 15/11/N+1 (20 mois), coût total 120 000 000 F. Placements temporaires du 01/05 au 30/09/N générant 800 000 F de revenus financiers.

**Détermination (calcul, pas d'écriture spécifique).**
- Intérêts courus au 31/12/N : 120 000 000 × 12 % × 10/12 = 12 000 000 F.
- Coût d'emprunt incorporable à la construction (durée 9 mois, du 01/04 au 31/12/N) : 120 000 000 × 12 % × 9/12 = 10 800 000 F.
- Déduction des intérêts de placement : 800 000 F.
- **Montant à incorporer au coût de l'actif éligible** = 10 800 000 − 800 000 = **10 000 000 F**.
