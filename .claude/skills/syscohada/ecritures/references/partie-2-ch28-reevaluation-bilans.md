# Partie 2 — Chapitre 28 : Réévaluation des bilans

> Montants pédagogiques. Écritures en tableau 5 colonnes : Débit | Crédit | Date et libellé | Montant débit | Montant crédit.

Deux régimes : **réévaluation légale** (écart au compte **1061**, ou **154 Provision spéciale de réévaluation** si neutralité fiscale imposée) et **réévaluation libre** (écart au compte **1062**). La valeur réévaluée retenue est la plus faible entre valeur indiciaire et valeur actuelle.

## Application 99 — Réévaluation légale

Ensemble immobilier acquis le 01/01/N-4 : terrain 100 000 000 ; bâtiment 300 000 000 (durée 30 ans) ; titres de participation (contrôle exclusif) 25 000 000. Valeur actuelle au 31/12/N : terrain 150 000 000, bâtiment 375 000 000, titres 28 000 000. Indice de réévaluation 1,2.

**Écarts de réévaluation.**
- Terrain : valeur indiciaire 100 000 000 × 1,2 = 120 000 000 < valeur actuelle 150 000 000 → retenue 120 000 000 ; écart **20 000 000**.
- Bâtiment : VNC avant = 300 000 000 − (300 000 000 × 1/30 × 5 = 50 000 000) = 250 000 000. Valeur indiciaire 250 000 000 × 1,2 = 300 000 000 < 375 000 000 → retenue 300 000 000. Valeur d'origine et amortissements réévalués à l'indice : origine 300 000 000 × 1,2 = 360 000 000 (écart 60 000 000) ; amortissements 50 000 000 × 1,2 = 60 000 000 (écart 10 000 000) ; écart net **50 000 000**.
- Titres : valeur indiciaire 25 000 000 × 1,2 = 30 000 000 > valeur actuelle 28 000 000 → retenue 28 000 000 ; écart **3 000 000** (indice effectif 1,12).
- Total écart : **73 000 000**.

**Comptabilisation (31/12/N).**

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 223 |  | 31/12/N — Terrains bâtis | 20 000 000 |  |
| 261 |  | Titres de participation (contrôle exclusif) | 3 000 000 |  |
|  | 1061 | Écarts de réévaluation légale |  | 23 000 000 |
| 2311 |  | Bâtiments industriels | 60 000 000 |  |
|  | 28311 | Amortissement de bâtiments industriels |  | 10 000 000 |
|  | 1061 | Écarts de réévaluation légale |  | 50 000 000 |

**Amortissement N+1 sur base réévaluée** : VNC réévaluée 300 000 000, durée résiduelle 25 ans → 12 000 000 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6813 |  | 31/12/N+1 — Dotations aux amort. des immo. corporelles | 12 000 000 |  |
|  | 2831 | Amortissements des bâtiments industriels |  | 12 000 000 |

**Variante neutralité fiscale (compte 154).** L'écart bâtiment est crédité au **154** au lieu du 1061 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 2311 |  | 31/12/N — Bâtiments industriels | 60 000 000 |  |
|  | 28311 | Amortissement de bâtiments industriels |  | 10 000 000 |
|  | 154 | Provision spéciale de réévaluation |  | 50 000 000 |

Reprise annuelle du 154 à hauteur du supplément d'amortissement (12 000 000 − 10 000 000 = 2 000 000) via le compte **861 Reprises de provisions réglementées** :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6813 |  | 31/12/N+1 — Dotations aux amort. des immo. corporelles | 12 000 000 |  |
|  | 2831 | Amortissements des bâtiments industriels |  | 12 000 000 |
| 154 |  | Provision spéciale de réévaluation | 2 000 000 |  |
|  | 861 | Reprises de provisions réglementées |  | 2 000 000 |

Impact net sur le résultat N+1 : 12 000 000 − 2 000 000 = 10 000 000 (= l'amortissement historique).

## Application 100 — Réévaluation libre

Bâtiment acquis le 02/01/N-5 pour 150 000 000, amorti linéairement sur 30 ans. Valeur actuelle au 31/12/N : 135 000 000.

**Écart.** Amortissements cumulés 150 000 000 × 6/30 = 30 000 000 ; VNC 120 000 000. Écart de réévaluation = 135 000 000 − 120 000 000 = **15 000 000**. Valeur brute réévaluée 135 000 000 × 30/24 = 168 750 000 ; amortissements réévalués 168 750 000 × 6/30 = 33 750 000.

**Méthode 1 — ajustement proportionnel des amortissements :**

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 23 |  | 31/12/N — Bâtiments (168 750 000 − 150 000 000) | 18 750 000 |  |
|  | 283 | Amortissement des bâtiments (33 750 000 − 30 000 000) |  | 3 750 000 |
|  | 1062 | Écarts de réévaluation libre |  | 15 000 000 |

**Méthode 2 — élimination des amortissements puis enregistrement de la valeur réévaluée.**

*Étape 1 — annulation des amortissements antérieurs :*

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 283 |  | 31/12/N — Amortissement des bâtiments | 30 000 000 |  |
|  | 23 | Bâtiments |  | 30 000 000 |

*Étape 2 — écart de réévaluation :*

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 23 |  | 31/12/N — Bâtiments | 15 000 000 |  |
|  | 1062 | Écarts de réévaluation libre |  | 15 000 000 |

*Vérification* : compte 23 = 150 000 000 − 30 000 000 + 15 000 000 = 135 000 000 ; compte 283 = 0.
