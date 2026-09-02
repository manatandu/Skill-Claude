# Partie 2 — Chapitres 23 et 24 : Contrats pluri-exercices ; Abonnement des charges et produits

> Montants et taux de TVA (18 %) pédagogiques ; TVA réelle RDC 16 % → `fiscalite-rdc-socle`. Écritures en tableau 5 colonnes : Débit | Crédit | Date et libellé | Montant débit | Montant crédit.

## Chapitre 23 — Contrats pluri-exercices

Deux méthodes selon la fiabilité de l'estimation du résultat à terminaison :
- **résultat fiable → méthode à l'avancement** (CA et résultat au prorata du degré d'avancement) ;
- **résultat non fiable → méthode à l'achèvement** (CA limité aux charges de l'exercice, résultat nul jusqu'à l'achèvement).
Un contrat prévu **déficitaire** donne lieu à une provision pour pertes sur marchés à achèvement futur (compte 193) dès la connaissance de la perte.

Comptes clés : **4181** Clients, factures à établir ; **7051** Travaux facturés dans la région ; **4435** État, TVA sur facture à établir ; **4433** État, TVA facturée sur travaux ; **193** Provisions pour pertes sur marchés à achèvement futur.

### Application 92 — Contrat bénéficiaire

Ouvrage sur 22 mois. [texte officiel : « une période de à 22 mois »] Coût total estimé 750 000 000 ; coût engagé au 31/12/N 450 000 000 ; prix de vente 925 000 000. Facturation au client le 30/10/N+1. TVA 18 %.

**Hypothèse 1 — méthode à l'avancement.** Résultat à terminaison 925 000 000 − 750 000 000 = 175 000 000.

*Clôture N* : avancement 450 000 000 / 750 000 000 = 60 %. Résultat partiel 175 000 000 × 60 % = 105 000 000. CA partiel 925 000 000 × 60 % = 555 000 000 (= 450 000 000 charges + 105 000 000 résultat). Aucune facturation intermédiaire → produit à recevoir HT :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4181 |  | 31/12/N — Clients, factures à établir | 654 900 000 |  |
|  | 7051 | Travaux facturés dans la région |  | 555 000 000 |
|  | 4435 | État, TVA sur facture à établir (555 000 000 × 18 %) |  | 99 900 000 |

Extrait CR N : charges 450 000 000, travaux facturés 555 000 000, résultat 105 000 000.

*Contrepassation (01/01/N+1, ou au 30/10/N+1 date de livraison)* : 7051 · 4435 · 4181 pour 555 000 000 / 99 900 000 / 654 900 000.

*Facturation définitive (30/10/N+1)* — 925 000 000 HT, TVA 166 500 000 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4111 |  | 30/10/N+1 — Clients | 1 091 500 000 |  |
|  | 7051 | Travaux facturés dans la région |  | 925 000 000 |
|  | 4433 | État, TVA facturée sur travaux |  | 166 500 000 |

Extrait CR N+1 : charges 300 000 000 (750 − 450 M), travaux facturés 370 000 000 (925 − 555 M), résultat 70 000 000. Total sur 2 exercices : 105 + 70 = 175 000 000.

**Hypothèse 2 — méthode à l'achèvement.** CA limité aux charges de l'exercice.

*Clôture N* — CA = charges engagées 450 000 000, TVA 81 000 000 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4181 |  | 31/12/N — Clients, factures à établir | 531 000 000 |  |
|  | 7051 | Travaux facturés dans la région |  | 450 000 000 |
|  | 4435 | État, TVA sur facture à établir |  | 81 000 000 |

Résultat N = 0. Contrepassation au 01/01/N+1 (7051 · 4435 · 4181 pour 450 000 000 / 81 000 000 / 531 000 000), puis facturation 30/10/N+1 identique à l'H1 (4111 1 091 500 000 · 7051 925 000 000 · 4433 166 500 000). Résultat N+1 = 175 000 000. Total : 0 + 175 000 000.

### Application 93 — Contrat déficitaire

Prix de vente prévisionnel 120 000 000 ; coûts prévisionnels au 31/12/N-1 125 000 000 ; coût cumulé N-1 60 000 000 ; coût cumulé N 125 000 000. Livraison/facturation 20/12/N. TVA 18 %. Résultat à terminaison fiable : −5 000 000 (contrat déficitaire).

**Exercice N-1.** Avancement 60 000 000 / 125 000 000 = 48 %. CA à l'avancement 120 000 000 × 48 % = 57 600 000. Quote-part de perte 57 600 000 − 60 000 000 = −2 400 000 (= 48 % × 5 000 000).

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4181 |  | 31/12/N-1 — Clients, factures à établir | 67 968 000 |  |
|  | 7051 | Travaux facturés dans la région |  | 57 600 000 |
|  | 4435 | État, TVA sur facture à établir (57 600 000 × 18 %) |  | 10 368 000 |

Perte non encore réalisée 5 000 000 − 2 400 000 = 2 600 000 (= 52 % × 5 000 000) → provision :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6911 |  | 31/12/N-1 — Dotations aux prov. pour risques et charges | 2 600 000 |  |
|  | 193 | Provisions pour pertes sur marchés à achèvement futur |  | 2 600 000 |

Extrait CR N-1 : charges 60 000 000, dotations 2 600 000, travaux facturés 57 600 000, résultat (perte) 5 000 000.

**Exercice N.** Contrepassation du CA à l'avancement (01/01/N) : 7051 · 4435 · 4181 pour 57 600 000 / 10 368 000 / 67 968 000. Facturation définitive (20/12/N), 120 000 000 HT, TVA 21 600 000 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4111 |  | 20/12/N — Clients | 141 600 000 |  |
|  | 7051 | Travaux facturés dans la région |  | 120 000 000 |
|  | 4433 | État, TVA facturée sur travaux |  | 21 600 000 |

Reprise de provision (31/12/N) : 193 · 7911 pour 2 600 000. Extrait CR N : charges 65 000 000 (125 − 60 M), travaux facturés 62 400 000 (120 − 57,6 M), reprises 2 600 000, résultat 0.

## Chapitre 24 — Abonnement des charges et produits (Application 94)

Étalement mensuel des charges via le compte **4746 Répartition périodique des charges**. Prévision N au 1er janvier : 2 400 000 F HT. Facturation réelle du 1er trimestre : 780 000 F HT le 31/03/N. Ne pas tenir compte de la TVA.

**Janvier et février** — abonnement 2 400 000 / 12 = 200 000 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6243 |  | 31/01/N — Maintenance (abonnement) | 200 000 |  |
|  | 4746 | Répartition périodique des charges |  | 200 000 |

**Mars** — abonnement du mois **et** facture réelle du trimestre :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6243 |  | 31/03/N — Maintenance (abonnement) | 200 000 |  |
|  | 4746 | Répartition périodique des charges |  | 200 000 |
| 4746 |  | Répartition périodique des charges (facture trimestre) | 780 000 |  |
|  | 4011 | Fournisseurs |  | 780 000 |

**À partir d'avril** — révision de la redevance mensuelle. Montant annuel réestimé 2 400 000 + [780 000 − (200 000 × 3)] = 2 580 000. Déjà imputé 600 000. Reste 1 980 000 à répartir sur 9 mois = 220 000 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6243 |  | 30/04/N — Maintenance (abonnement 1 980 000 / 9) | 220 000 |  |
|  | 4746 | Répartition périodique des charges |  | 220 000 |
