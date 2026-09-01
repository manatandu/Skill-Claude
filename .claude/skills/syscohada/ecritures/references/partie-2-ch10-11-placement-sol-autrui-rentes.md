# Partie 2 — Chapitres 10 et 11 : Immeubles de placement, constructions sur sol d'autrui, rentes viagères

> Montants pédagogiques. Écritures en tableau 5 colonnes : Débit | Crédit | Date et libellé | Montant débit | Montant crédit.

## Chapitre 10 — Immeubles de placement (Application 41)

Immeuble de 4 étages acheté à crédit 200 000 000 F. L'entité occupe le 1er étage (administratif) et loue les 3 autres.

**Analyse.** Les parties étant vendables séparément → approche par composants : 1/4 (50 000 000) en immobilisations corporelles, 3/4 (150 000 000) en immeuble de placement. Si les parties ne sont pas vendables séparément, l'immeuble n'est classé en placement que si l'usage pour activités ordinaires est minoritaire.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 2313 |  | 31/12/N+10 — Bâtiments administratifs et commerciaux | 50 000 000 |  |
| 2315 |  | Bâtiments - immeubles de placement | 150 000 000 |  |
|  | 4812 | Fournisseurs d'investissements |  | 200 000 000 |

## Chapitre 11 — Constructions sur sol d'autrui et contrat de rentes viagères

### Application 42 — Construction sur sol d'autrui

Entité AUTRUAS construit en N un atelier industriel sur un terrain dont elle est locataire. Coût 60 000 000 F, travaux achevés/facturés 01/10/N. Durée d'utilité 15 ans = durée du bail. À l'expiration : indemnité d'éviction 10 000 000 F.

Acquisition + amortissement N ([(60 000 000 − 10 000 000)/15] × 3/12 = 833 333) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 232 |  | 01/10/N — Bâtiments industriels sur sol d'autrui | 60 000 000 |  |
|  | 4812 | Fournisseurs d'investissements — immob. corp. |  | 60 000 000 |
| 6813 |  | 31/12/N — Dotations aux amort. des immob. corp. | 833 333 |  |
|  | 2832 | Amortissement bâtiment industriel sur sol d'autrui |  | 833 333 |

**À l'expiration du bail (chez AUTRUAS)** — encaissement de l'indemnité, dernière annuité, décomptabilisation :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 521 |  | 01/10/N+15 — Banques | 10 000 000 |  |
|  | 822 | Produits des cessions d'immobilisations corp. |  | 10 000 000 |
| 6813 |  | 31/12/N+15 — Dotations aux amort. des immob. corp. | 3 333 333 |  |
|  | 2832 | Amort. bâtiment industriel sur sol d'autrui |  | 3 333 333 |
| 812 |  | Valeurs comptables des cessions d'immob. corp. | 10 000 000 |  |
| 2832 |  | Amort. bâtiment industriel sur sol d'autrui | 50 000 000 |  |
|  | 232 | Construction sur sol d'autrui |  | 60 000 000 |

**Chez le propriétaire du terrain à l'expiration.**
- 1er cas — indemnité prévue : 231 · 521 (10 000 000).
- 2e cas — aucune indemnité (valeur actuelle 10 000 000) : 231 · 841 Produits HAO constatés (10 000 000).

> Bien d'une valeur significative : utiliser 148 Autres subventions d'investissement (au lieu de 841) pour étaler le produit sur la durée d'amortissement.

### Application 43 — Rentes viagères

Ensemble immobilier acquis le 01/10/N, 350 000 000 (dont terrain 50 000 000). Bouquet 110 000 000, solde en rente viagère annuelle de 20 000 000 payable le 01/10. Durée d'utilité bâtiment 30 ans.

**Exercice N** — acquisition + amortissement (300 000 000 × 1/30 × 3/12 = 2 500 000) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 2232 |  | 01/10/N — Terrains bâtis | 50 000 000 |  |
| 2313 |  | Bâtiments Administratifs et Commerciaux | 300 000 000 |  |
|  | 521 | Banques |  | 110 000 000 |
|  | 1681 | Rentes viagères capitalisées |  | 240 000 000 |
| 6813 |  | 31/12/N — Dotations aux amort. des immob. corp. | 2 500 000 |  |
|  | 2831 | Amortissements des bâtiments |  | 2 500 000 |

**Exercice N+1** — versement de la rente + amortissement (300 000 000 × 1/30 = 10 000 000) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 1681 |  | 01/10/N+1 — Rentes viagères capitalisées | 20 000 000 |  |
|  | 521 | Banques |  | 20 000 000 |
| 6813 |  | 31/12/N+1 — Dotations aux amort. des immob. corp. | 10 000 000 |  |
|  | 2831 | Amortissements des bâtiments |  | 10 000 000 |

**Hypothèse 1 — Décès du crédirentier le 15/12/N+5.** 5 versements = 100 000 000 ; solde 1681 = 240 000 000 − 100 000 000 = 140 000 000, soldé en produit HAO :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 1681 |  | 15/12/N+5 — Rentes viagères capitalisées | 140 000 000 |  |
|  | 841 | Produits HAO constatés |  | 140 000 000 |

**Hypothèse 2 — Décès le 10/11/N+14.** Au 01/10/N+12, 12 versements = 240 000 000 → compte 1681 soldé. Les versements N+13 et N+14 passent en charges HAO :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 831 |  | 01/10/N+13 — Charges HAO constatées | 20 000 000 |  |
|  | 521 | Banques |  | 20 000 000 |
| 831 |  | 01/10/N+14 — Charges HAO constatées | 20 000 000 |  |
|  | 521 | Banques |  | 20 000 000 |

> Financement lié aux activités ordinaires : utiliser 6781 / 7781 au lieu de 831 / 841.
