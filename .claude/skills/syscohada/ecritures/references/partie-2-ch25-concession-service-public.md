# Partie 2 — Chapitre 25 : Contrat de concession de service public

> Montants et TVA (18 %) pédagogiques ; TVA réelle RDC 16 % → `fiscalite-rdc-socle`. Écritures en tableau 5 colonnes : Débit | Crédit | Date et libellé | Montant débit | Montant crédit.

## Application 95, Première partie — Partenariat public/privé (PPP)

Un opérateur privé finance, construit, entretient et exploite un pont à péage pendant 10 ans.
- Phase de construction : coûts 400 000 000 (en charges par nature) ; fraction des redevances pour la seule prestation de construction 420 000 000.
- Phase post-construction : redevance annuelle fin de période N = 72 000 000 (réglée au comptant au 31/12/N), décomposée en : construction 42 000 000 ; coût de financement refacturé 5 000 000 ; prestations post-construction 25 000 000.
- Droits de passage collectés en espèces pour le compte de la collectivité, reversés en fin d'exercice sous déduction des redevances.
- Recette 1er jour (01/01/N) 475 200 ; total des recettes annuelles 135 000 000.

**Principes.**
- *Phase de construction* : coûts et CA traités comme un contrat pluri-exercices (chap. 23). Le CA = fraction des redevances de construction, hors coûts de financement, enregistré au débit du **2734 Créances sur le concédant** en attendant l'émission des factures de redevances.
- *Phase post-construction* : factures de redevances au débit du **411**, avec en contrepartie 2734 (fraction construction, pour solder), 77 (financement refacturé) et **706** (prestations post-construction). Droits de passage : à la collecte, trésorerie · **4731 Mandants, collectivité** ; au reversement, 4731 débité pour solde par la trésorerie.

**Phase de construction.**

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 6… |  | En cours — Compte de charges par nature (coût des travaux) | 400 000 000 |  |
|  | 401/521 | Fournisseurs / Banques |  | 400 000 000 |
| 2734 |  | À la fin — Créances sur le concédant | 420 000 000 |  |
|  | 705 | Travaux facturés |  | 420 000 000 |

**Phase post-construction.** Collecte de la recette journalière (01/01/N) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 571 |  | 01/01/N — Caisse | 475 200 |  |
|  | 4731 | Mandants, collectivité territoriale |  | 475 200 |

Constatation de la redevance annuelle (72 000 000) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 411 |  | 31/12/N — Clients | 72 000 000 |  |
|  | 2734 | Créances sur le concédant |  | 42 000 000 |
|  | 706 | Services vendus |  | 25 000 000 |
|  | 7713 | Intérêts sur créances diverses |  | 5 000 000 |

Reversement des droits collectés (135 000 000) sous déduction des redevances (72 000 000) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4731 |  | 03/07/N [texte officiel : date « 03/07/N »] — Mandants, collectivités territoriales | 135 000 000 |  |
|  | 411 | Clients |  | 72 000 000 |
|  | 521 | Banques |  | 63 000 000 |

## Application 95, Deuxième partie — Biens « de retour » et biens « de remise »

- **Opération 1** : l'État concède au Port Autonome (10 ans) un terrain (50 M) et un bâtiment (100 M) le 02/01/N.
- **Opération 2** : le Port Autonome acquiert du matériel lourd (HT 120 M, durée 10 ans) le 01/10/N, rétrocédé à l'État à la fin du contrat. TVA 18 %.

**Opération 1 — bien « de retour ».** Bien mis en concession par le concédant, qui lui revient en fin de contrat. Le concessionnaire n'en a pas le contrôle au sens du cadre conceptuel → **hors patrimoine** du Port Autonome ; simple mention dans les Notes annexes (engagements obtenus). Aucune écriture.

**Opération 2 — bien « de remise ».** Bien apporté par le concessionnaire, remis gratuitement au concédant en fin de contrat → **entre au patrimoine** et est amorti sur sa durée d'utilité (ne pouvant excéder la durée du contrat). Amortissement N : 120 000 000 × 10 % × 3/12 = 3 000 000.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 2411 |  | 01/10/N — Matériel industriel | 120 000 000 |  |
| 4451 |  | TVA déductible sur immobilisation | 21 600 000 |  |
|  | 4812 | Fournisseurs d'immobilisations corporelles |  | 141 600 000 |
| 6813 |  | 31/12/N — Dotations aux amort. des immo. corporelles | 3 000 000 |  |
|  | 28411 | Amortissement du matériel industriel |  | 3 000 000 |

**Rétrocession en fin de contrat** — cumul des amortissements = valeur d'origine 120 000 000, VNC = 0 :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 28411 |  | 01/01/N [texte officiel : date « 01/01/N »] — Amortissement du matériel | 120 000 000 |  |
|  | 2411 | Matériel industriel |  | 120 000 000 |
