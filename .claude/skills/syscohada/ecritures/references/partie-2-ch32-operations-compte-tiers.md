# Partie 2 — Chapitre 32 : Opérations faites pour le compte de tiers

> Montants pédagogiques. Écritures en tableau 5 colonnes : Débit | Crédit | Date et libellé | Montant débit | Montant crédit.

Distinction fondamentale :
- **Commissionnaire** (agit en son nom pour le compte d'autrui) : comptabilise **toutes** les opérations dans ses charges/produits ; sa rémunération = marge (ventes − achats), non isolée.
- **Mandataire** (agit au nom du mandant) : n'enregistre en résultat que sa **rémunération** ; les opérations pour le compte du mandant transitent par le **4731 Mandant, opérations faites pour le compte de tiers**.

## Application 104 — Opération en qualité de commissionnaire

X demande à Y d'acheter 200 t de coton ; Y agit en commissionnaire, commission 5 %. Le 15/06, Y achète à CENTRAFRICTON 200 t à 40 000 F/t (8 000 000). Livrées le 25/06 à X.

**Chez le commettant (principe).** À l'achat, il enregistre le montant y compris la commission qu'il est réputé faire à l'intermédiaire ; à la vente, le montant net de commission. La commission de vente → **6322 Commissions et courtages sur ventes**.

**Chez Y (commissionnaire).** Achat 8 000 000, revente à X commission incluse 8 400 000 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 601 |  | 15/06/N — Achats de marchandises | 8 000 000 |  |
|  | 401 | Fournisseurs, dettes en compte |  | 8 000 000 |
| 411 |  | Clients X | 8 400 000 |  |
|  | 701 | Ventes de marchandises |  | 8 400 000 |

Le résultat n'apparaît que par la différence ventes (8 400 000) − achats (8 000 000) dans le résultat net.

## Application 105 — Opération en qualité de mandataire

Même trame, mais Y est **mandataire** de X. Le 22/06, Y paie le transporteur Z (180 000) pour livrer chez X. Deux hypothèses sur le transport.

**Principe (mandataire).** Achats pour le mandant : 4731 · **4712 Créditeurs divers** (au nom du fournisseur). Ventes pour le mandant : **4711 Débiteurs divers** · 4731. Rémunération : **706 Services vendus** si activité habituelle ; **7072 Commissions et courtages** si accessoire.

**Comptabilisation des achats-ventes chez Y.**

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4731 |  | 15/06/N — Mandant X, opérations faites pour le compte de tiers | 8 000 000 |  |
|  | 4712 | Créditeurs divers CENTRAFRICTON (acquisition pour X) |  | 8 000 000 |
| 4712 |  | 25/06/N — Créditeurs divers CENTRAFRICTON | 8 000 000 |  |
|  | 4731 | Mandant X, opérations faites pour le compte de tiers |  | 8 000 000 |
| 411 |  | Clients X | 400 000 |  |
|  | 706 | Services vendus (prestation vendue à X) |  | 400 000 |

**Comptabilisation du transport.**

*1re hypothèse — transport inclus dans la commission de Y* (charge propre de Y) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6015 |  | 22/06/N — Frais sur achats (transporteur Z pour X) | 180 000 |  |
|  | 521 | Banques locales |  | 180 000 |

*2e hypothèse — X rembourse Y franc pour franc* (débours porté au compte du mandant) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4731 |  | 22/06/N — Mandant X, opérations faites pour le compte de tiers | 180 000 |  |
|  | 521 | Banques locales (transporteur Z pour X) |  | 180 000 |
