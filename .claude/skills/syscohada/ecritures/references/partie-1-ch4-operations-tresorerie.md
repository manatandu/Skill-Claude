# Partie 1 — Chapitre 4 : Opérations de trésorerie

> Montants et taux pédagogiques (taux réels RDC → `fiscalite-rdc-socle`). Écritures en tableau 5 colonnes : Débit | Crédit | Date et libellé | Montant débit | Montant crédit.

## Section 1 — Conception et terminologie

Hors SMT (qui n'enregistre que recettes/dépenses), le Système normal enregistre séparément le **flux juridique « a »** (obligation ou droit constaté : factures, bulletins, déclarations) et le **flux financier « b »** (mouvements de trésorerie : caisse, chéquiers, virements, extraits). Les flux financiers = « règlements » ou « opérations de trésorerie ».

Enregistrement de base : flux juridiques en classes 6-7-8 et 4 ; flux financiers en classes 4 et 5. Charge/dépense : 6 et 8 impairs → classe 4 → classe 5. Produit/recette : 7 et 8 pairs → classe 4 → classe 5. Les flux financiers diffèrent selon le mode de règlement (effets de commerce ou autres) et le délai.

## Section 2 — Modes de règlement autres que par effets

### 2.1 Espèces
Débit **57 Caisse** en recette, crédit en dépense (pièces de caisse, tickets). Plusieurs caisses → subdivision par succursale/bureau. Devises : comptes séparés en devises et en unité légale à cours fixe, régularisés en fin de période. Gestion en caisse constante ou variable.

### 2.2 Chèque
**Débiteur** (prudence) : enregistre dès l'émission.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4... |  | Tiers | X |  |
|  | 52../53.. | Banques ou établissements financiers et assimilés |  | X |

Tolérance : n'enregistrer qu'à l'avis de débit, à condition que la régularisation de fin de période (après état de rapprochement) tienne compte des chèques en circulation.

**Créancier** : le chèque reçu transite par deux comptes de valeurs à encaisser avant la banque : **513** Chèques à encaisser (arrivée dans l'entité), **514** Chèques à l'encaissement (envoyé à la banque, sur bordereau).

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 513. |  | Réception du chèque — Chèques à encaisser | X |  |
|  | 4... | Tiers |  | X |
| 514. |  | Envoi à la banque — Chèques à l'encaissement | X |  |
|  | 513. | Chèques à encaisser |  | X |
| 52../53.. |  | Réception avis de crédit — Banques ou étab. financiers | X |  |
|  | 514 | Chèques à l'encaissement |  | X |

Tolérance : ventilation limitée aux en-cours de fin de période.

### 2.3 Carte bancaire ou de crédit
Mêmes règles que le chèque ; l'encaissement transite par **515** Cartes de crédit à encaisser.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 515. |  | Passage machine — Cartes de crédit à encaisser | X |  |
|  | 4.../70.. | Tiers ou Ventes |  | X |
| 52../53.. |  | Réception avis de crédit — Banques ou étab. financiers | net |  |
| 6315 |  | Commissions sur cartes de crédit | frais |  |
|  | 515. | Cartes de crédit à encaisser |  | brut |

### 2.4 Virement
Débiteur : traite l'ordre comme un chèque. Créancier : enregistre à réception de l'avis de virement (avis de crédit). Chèque postal = ordre de virement postal : traité comme chèque bancaire (trois volets reçus) ou comme virement (seul volet avis de crédit).

## Section 3 — Règlement par effets de commerce

### 3.1 Traites et billets
Effets = traites (lettres de change) et billets à ordre (dont billets de fonds). Traite établie par le créancier « tireur », en général acceptée par le débiteur « tiré ». Billet établi par le débiteur « souscripteur ». Comptabilisés de même : tiers **402/412** à l'émission, comptes 51-56 au règlement.

### 3.2 Effets à payer et à recevoir
Débiteur (acceptation traite / souscription billet) transfère la dette :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 401. |  | Fournisseurs, dettes en compte | X |  |
|  | 402. | Fournisseurs, effets à payer |  | X |
| 481. |  | Fournisseurs d'investissements | X |  |
|  | 482. | Fournisseurs d'investissement, effets à payer |  | X |

Ou constatation à l'importation (droit de douane, obligation cautionnée) : `60.. → 4491 Etat, obligations cautionnées`. Règlement de l'effet à l'échéance : débit 402/482/4494, crédit 52. Comptes 402/482/4491 subdivisables par échéance.

Créancier (signature traite / réception billet) transfère la créance :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 412. |  | Clients, effets à recevoir en portefeuille | X |  |
|  | 411. | Clients |  | X |
| 4852 |  | Créances sur cessions d'immobilisations, effets à recevoir | X |  |
|  | 4851 | Créances sur cessions d'immobilisations, en compte |  | X |

### 3.3 Effets à encaisser
Remise à l'encaissement d'un tiers → **512** Effets à l'encaissement (≠ 511, effets en portefeuille autres que clients) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 512. |  | Effets à l'encaissement | X |  |
|  | 412. | Clients, effets à recevoir |  | X |
|  | 4852 | Créances sur cessions d'immobilisations, effets à recevoir |  | X |

Bonne fin (avis de crédit) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 52../53.. |  | Banques ou établissements financiers | net |  |
| 6312 |  | Frais sur effets | commissions |  |
|  | 512. | Effets à l'encaissement |  | brut |

### 3.4 Effets à l'escompte
Remise à l'escompte (avant échéance) : transfert 412 → **415** Clients, effets escomptés non échus (4852 → 4855 pour les immobilisations). Acceptation par la banque (agio HT = frais financiers) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 52.. |  | Banques ou établissements financiers | net |  |
| 675. |  | Escomptes des effets de commerce | agios |  |
|  | 565. | Banques, escompte de crédit ordinaire |  | brut |
|  | 564. | Banques, escompte de crédit de campagne |  | brut |

Après échéance et bonne fin, compensation créance/dette : débit 565/564, crédit 415/4855. **Les effets escomptés non échus restent à l'actif** ; le crédit bancaire figure au passif (56) pour le même montant ; le compte Clients représente l'encours à la date du bilan.

### 3.5 Effets impayés
Retour de l'effet : soit retransfert 415 → 411, soit nouvelle traite/billet reprenant les écritures à partir de 415. Le nouvel effet comprend le principal + frais de retour récupérés (créancier : charge par nature puis **7078** ; débiteur **6312**) + intérêts de retard (créancier **7713**, débiteur **6744**) + frais de retraite/timbre (créancier **7078**, débiteur **6312**).

## Section 4 — Instruments de monnaie électronique

Valeur monétaire stockée sous forme électronique, créance sur l'émetteur.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 55.. |  | Chargement — Instruments de monnaie électronique | X |  |
|  | 52../53.. | Banques ou établissements financiers |  | X |
|  | 57.. | Caisses |  | X |
| 6317 |  | Frais de chargement — Frais sur instruments, monnaie élec. | X |  |
|  | 52../53.. / 57.. | Banques / Caisses |  | X |
| 4… |  | Règlement/transfert — Tiers | X |  |
|  | 55.. | Instruments de monnaie électronique |  | X |

En fin de période, rapprocher le solde comptable avec le solde réel (confirmé par l'émetteur).

## Section 5 — Délais de règlement

### 5.1 Règlement anticipé (escompte de règlement)
Réduction pour paiement avant échéance, pourcentage simple (1 à 3 %). Enregistré au paiement : **673** accordé, **773** obtenu (biens d'exploitation) ou en classe 2 (bien immobilier). Assiette de TCA réduite d'autant.

Chez le client débiteur (biens d'exploitation) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 401. |  | Fournisseurs, dettes en compte | X |  |
|  | 773. | Escomptes obtenus |  | X |
|  | 445. | Etat, TVA récupérable |  | X |
|  | 5… | Trésorerie |  | X |

Chez le client débiteur (biens immobiliers) : débit 481/404, crédit 2…, 445, 5… (l'escompte réduit le coût de l'immobilisation).

Chez le fournisseur créancier :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 5... |  | Trésorerie | X |  |
| 673. |  | Escomptes accordés | X |  |
| 443. |  | Etat, TVA facturée | X |  |
| 446. |  | Etat, autres TCA | X |  |
|  | 411. | Clients |  | X |

### 5.2 Règlement retardé
Impayé (chèque, carte, effet) : frais d'impayés **6318** par crédit 521, puis imputation du principal majoré des frais en **413** (chèques 4131, effets 4132, cartes 4133) par crédit 51 (principal) et 7078 (récupération des frais). Pas de compensation des frais en classe 6.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 4131 |  | Clients, chèques impayés | X |  |
| 4132 |  | Clients, effets impayés | X |  |
| 4133 |  | Clients, cartes de crédit impayées | X |  |
|  | 51 | Valeurs à encaisser |  | X |
|  | 7078 | Autres produits accessoires |  | X |

Intérêts de retard (taux légal ou contractuel) : débit 4131/4132, crédit **771** Intérêts des prêts.

### Application 11 — Chèques impayés
Client Gambiss (entité Guerdass) : chèque 42 500 000 remis le 15/12/N, à l'encaissement le 18/12/N, impayé le 21/12/N. Frais d'impayés 50 000 à la charge du client.

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 513 |  | 15/12/N — Chèques à encaisser (réception) | 42 500 000 |  |
|  | 411 | Clients |  | 42 500 000 |
| 514 |  | 18/12/N — Chèques à l'encaissement (remise) | 42 500 000 |  |
|  | 513 | Chèques à encaisser |  | 42 500 000 |
| 6318 |  | 21/12/N — Autres frais bancaires (bordereau d'impayé) | 50 000 |  |
|  | 521 | Banques |  | 50 000 |
| 4131 |  | Clients, chèques impayés (principal + frais) | 42 550 000 |  |
|  | 514 | Chèques à l'encaissement |  | 42 500 000 |
|  | 7078 | Autres produits accessoires |  | 50 000 |

Regroupement possible des deux dernières en une seule : débit 4131 = 42 550 000, crédit 514 = 42 500 000 et 521 = 50 000.

## Section 6 — Exemple de synthèse

### Application 12 — Synthèse sur les instruments de règlement
Créance-dette d'exploitation 1 200 TTC (1 000 HT). a) moitié payée au comptant par monnaie électronique, escompte 2 % (TVA 20 %) ; b) solde par deux traites A et B de même valeur, échéances 30 j (fin mois 1) et 90 j (fin mois 3) ; c) traite A conservée puis encaissée à l'échéance, commission 5 HT ; d) traite B négociée 45 j avant échéance, taux d'escompte 8 %, commission 5 HT ; e) elle revient impayée, frais de retour 3 ; f) nouvelle traite à 60 j (fin mois 5), timbre fiscal 1 et intérêts de retard 12 % l'an.

Écritures chez le client (débiteur) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 401. |  | a — Fournisseurs, dettes en compte | 600 |  |
|  | 773. | Escomptes obtenus (500 × 2 %) |  | 10 |
|  | 445. | Etat, TVA récupérable (10 × 20 %) |  | 2 |
|  | 554. | Porte-monnaie électronique |  | 588 |
| 401 |  | b — Fournisseurs, dettes en compte | 600 |  |
|  | 402.1 | Fournisseurs, effets à payer au… |  | 300 |
|  | 402.3 | Fournisseurs, effets à payer au… |  | 300 |
| 402.1 |  | c — Fournisseurs effet à payer au… | 300 |  |
|  | 5211 | Banques |  | 300 |
| 402.3 |  | f — Fournisseurs effets à payer au… | 300 |  |
| 6744 |  | Intérêts sur dettes commerciales (300 × 12 % × 60/360) | 6 |  |
| 6312 |  | Frais sur effets (3 + 1) | 4 |  |
| 445. |  | Etat, TVA récupérable (3 × 20 %) | 1 |  |
|  | 402.5 | Fournisseurs effets à payer au… |  | 311 |

Écritures chez le fournisseur (créancier) :

| Débit | Crédit | Date et libellé | Montant débit | Montant crédit |
|---|---|---|---|---|
| 513. |  | a — Chèques à encaisser | 588 |  |
| 673. |  | Escomptes accordés (500 × 2 %) | 10 |  |
| 443. |  | Etat, TVA facturée (10 × 20 %) | 2 |  |
|  | 411. | Clients |  | 600 |
| 514 |  | a1 — Chèques à l'encaissement | 588 |  |
|  | 513. | Chèques à encaisser |  | 588 |
| 5212 |  | a2 — Banque Y | 588 |  |
|  | 514. | Chèques à l'encaissement |  | 588 |
| 4121.1 |  | b — Clients, effets à recevoir au… | 300 |  |
| 4121.3 |  | Clients, effets à recevoir au… | 300 |  |
|  | 411. | Clients |  | 600 |
| 512. |  | c — Effets à l'encaissement | 300 |  |
|  | 4121.1 | Clients effets à recevoir au… |  | 300 |
| 5212 |  | c — Banques Y | 294 |  |
| 6312 |  | Frais sur effets | 5 |  |
| 445. |  | Etat, TVA récupérable (5 × 20 %) | 1 |  |
|  | 512. | Effets à l'encaissement |  | 300 |
| 415. |  | d — Clients, effets escomptés non échus | 300 |  |
|  | 4121.3 | Clients, effets à recevoir au… |  | 300 |
| 5212 |  | d1 — Banque Y | 291 |  |
| 675. |  | Escomptes des effets de commerce (300 × 8 % × 45/360 + 5) | 8 |  |
| 445. |  | Etat, TVA récupérable (5 × 20 %) | 1 |  |
|  | 565. | Banques, escompte de crédits ordinaires |  | 300 |
| 6312 |  | e — Frais sur effets | 3 |  |
|  | 5212 | Banque Y |  | 3 |
| 565. |  | e1 — Banques, escompte de crédits ordinaires (dénouement normal) | 300 |  |
|  | 415. | Clients, effets escomptés non échus |  | 300 |
| 4121.5 |  | f — Clients, effets à recevoir au… | 311 |  |
|  | 7712 | Intérêts de prêts (300 × 12 % × 60/360) |  | 6 |
|  | 7078 | Autres produits accessoires (3 + 1) |  | 4 |
|  | 443. | Etat, TVA facturée (3 × 20 %) |  | 1 |
|  | 415. | Clients, effets escomptés non échus |  | 300 |
