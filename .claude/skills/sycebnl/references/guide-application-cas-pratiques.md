# GUIDE D'APPLICATION SYCEBNL — Cas pratiques corrigés (Applications 1 à 22)

Source : **Système comptable des entités à but non lucratif — Guide d'application**, OHADA/SYCEBNL. Document illustratif accompagnant l'Acte uniforme du 22 décembre 2022. Il fournit des cas pratiques de synthèse corrigés (écritures-types chiffrées) pour les producteurs d'états financiers des EBNL.

Le guide couvre les mêmes opérations spécifiques que la Partie 3 du référentiel, mais sous forme d'**exemples entièrement chiffrés**. Pour le mécanisme général (schémas avec `x`), voir les fichiers `partie3-ch1` à `partie3-ch6`. Pour un numéro ou intitulé de compte, vérifier dans `partie2-ch2-plan-comptes.md` et les fiches de fonctionnement `partie2-ch3-*`.

Découpage officiel du guide (les intitulés de parties du guide diffèrent de la numérotation des chapitres du corps) :
- Partie 1 : Fonds propres des associations, fondations et assimilés
- Partie 2 : Fonds affectés et reportés associations, fondations et assimilés
- Partie 3 : Fonds propres, projets de développement et assimilés
- Partie 4 : Dons
- Partie 5 : Cotisations des membres et versement des fondateurs
- Partie 5 : Autres opérations spécifiques `[texte officiel : la sixième partie est numérotée « Partie 5 » en doublon dans l'introduction du guide ; il s'agit de la Partie 6]`

Convention de lecture des écritures : chaque écriture est présentée en table `Compte | Intitulé | Débit | Crédit`, précédée de sa date et de son libellé. Les montants sont pédagogiques (exprimés dans l'unité monétaire du guide).

---

## CHAPITRE 1 : Fonds propres des associations, fondations et assimilés

### APPLICATION 1 — Dotation consomptible et non consomptible

**Énoncé.** À la constitution de l'association, les adhérents décident le 21 mai N d'apporter à titre définitif : mobilier de bureau 15 000 000, matériel informatique 8 000 000, matériel automobile 10 000 000. Des espèces de 5 000 000 sont apportées pour couvrir les premières charges de fonctionnement. Certains adhérents mettent des biens à disposition provisoire (convention fixant les modalités de reprise) : mobilier de bureau 30 000 000, espèces 1 000 000, chèque bancaire émis par la présidente 3 000 000. Réalisation des apports définitifs le 15 juin N. Tous les fonds dédiés au fonctionnement ont été utilisés au cours de l'exercice.

**Note préliminaire.** Se référer à la loi de l'État partie régissant les EBNL, aux statuts et au règlement intérieur. Si les documents prévoient une phase de souscription et de libération, utiliser les comptes 45 Apporteurs pour constater les étapes ; sinon, enregistrer les apports lors de leur libération.

Les apports durables mis à disposition **de façon définitive** = dotation non consomptible sans droit de reprise. Les ressources durables apportées pour couvrir les **charges de fonctionnement** = dotation consomptible. Les apports durables mis à disposition **de façon provisoire** = dotation non consomptible avec droit de reprise.

**Hypothèse 1 — souscription et libération des apports**

Souscription des apports (21/05/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 4511 | Apporteurs en nature (15 000 000 + 10 000 000 + 8 000 000) | 33 000 000 | |
| 4512 | Apporteurs en numéraire | 5 000 000 | |
| 1015 | Dotation non consomptible sans droit de reprise en nature | | 33 000 000 |
| 1041 | Dotation consomptible | | 5 000 000 |

Libération des apports (15/06/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 2442 | Matériel informatique | 8 000 000 | |
| 2441 | Mobilier de bureau | 15 000 000 | |
| 2451 | Matériel automobile | 10 000 000 | |
| 571 | Caisse | 5 000 000 | |
| 4511 | Apporteurs en nature | | 33 000 000 |
| 4512 | Apporteurs en numéraire | | 5 000 000 |

Souscription des apports à titre provisoire (21/05/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 4511 | Apporteurs en nature | 30 000 000 | |
| 4512 | Apporteurs en numéraire (1 000 000 + 3 000 000) | 4 000 000 | |
| 1025 | Dotation non consomptible avec droit de reprise en nature | | 30 000 000 |
| 1021 | Dotation non consomptible avec droit de reprise en numéraire | | 4 000 000 |

Libération des apports à titre provisoire (15/06/N) `[texte officiel : le sous-titre de cette écriture est libellé « Libération des apports à titre définitif » dans le guide, alors que l'écriture porte sur les apports provisoires]` :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 2441 | Mobilier de bureau | 30 000 000 | |
| 52 | Banques | 3 000 000 | |
| 57 | Caisse | 1 000 000 | |
| 4511 | Apporteurs en nature | | 30 000 000 |
| 4512 | Apporteurs en numéraire | | 4 000 000 |

À la clôture de l'exercice — couverture des charges engagées à partir des dotations consomptibles (31/12/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 1049 | Dotation consomptible inscrite au compte résultat | 5 000 000 | |
| 703 | Quote-part des dotations consomptibles transférées | | 5 000 000 |

**Hypothèse 2 — les statuts ne prévoient pas de souscription/libération.** Aucune écriture de souscription/libération. Les apports sont enregistrés dans les comptes de bilan lors de la réalisation.

Réalisation des apports (15/06/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 2442 | Matériel informatique | 8 000 000 | |
| 2441 | Mobilier de bureau | 15 000 000 | |
| 2451 | Matériel automobile | 10 000 000 | |
| 571 | Caisse | 5 000 000 | |
| 1015 | Dotation non consomptible sans droit de reprise en nature | | 33 000 000 |
| 1041 | Dotation consomptible | | 5 000 000 |

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 2441 | Mobilier de bureau | 30 000 000 | |
| 52 | Banques | 3 000 000 | |
| 57 | Caisse | 1 000 000 | |
| 1021 | Dotation non consomptible avec droit de reprise en numéraire | | 4 000 000 |
| 1025 | Dotation non consomptible avec droit de reprise en nature | | 30 000 000 |

Clôture — couverture des charges engagées (31/12/N) : même écriture 1049 / 703 pour 5 000 000.

---

### APPLICATION 2 — Droit d'adhésion et appel de cotisations de nouveaux membres

**Énoncé.** Le 10 janvier, une association lance un appel de versement de droit d'adhésion, de dépôt restituable et d'appel de cotisations des nouveaux membres, valeur globale 50 000 000. Statuts : 15 % = dépôt restituable (délai 48 mois), 10 % = appel de cotisations, le solde = droit d'entrée. Le 15 janvier N, tous les adhérents se sont acquittés. Nota : les statuts prévoient un recouvrement par tout moyen de la cotisation en cas de défaillance.

**Note préliminaire.** Si l'entité peut justifier le droit d'agir pour recouvrer l'appel, le compte 411 Adhérents peut être utilisé pour constater la créance. Sinon, constater le produit lors de l'encaissement effectif.

Appel du droit d'entrée et des cotisations (10/01/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 411 | Adhérents | 50 000 000 | |
| 103 | Droit d'entrée | | 37 500 000 |
| 1851 | Dépôts reçus | | 7 500 000 |
| 701 | Cotisations des adhérents | | 5 000 000 |

Encaissement (15/01/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 52 | Banques | 50 000 000 | |
| 411 | Adhérents | | 50 000 000 |

---

### APPLICATION 3 — Subventions d'investissement destinées à une association

**Énoncé.** L'association AGIR reçoit le 10 mai N de l'Union européenne une notification de subvention d'équipement de 120 000 000 (acquisition d'un terrain nu + construction d'un entrepôt de stockage de médicaments). Fonds virés en banque le 01/06/N. Le 01/10/N, achat d'un terrain à 20 000 000. Le 01/07/N+1, construction de l'entrepôt (100 000 000) terminée et mise en service, réglée par chèque. Amortissement de l'entrepôt sur 20 ans. Aucune clause d'inaliénabilité.

Écritures de l'exercice N :

Notification (10/05/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 4731 | Subventions d'investissement à recevoir | 120 000 000 | |
| 1417 | Subventions d'équipement — Organismes internationaux | | 120 000 000 |

Réception des fonds (01/06/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 5211 | Banques en monnaie nationale | 120 000 000 | |
| 4731 | Subventions d'investissement à recevoir | | 120 000 000 |

Acquisition du terrain (01/10/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 2221 | Terrains à bâtir | 20 000 000 | |
| 4812 | Fournisseurs d'investissement, immo. corporelles | | 20 000 000 |

Règlement du terrain (01/10/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 4812 | Fournisseurs d'investissement, immo. corporelles | 20 000 000 | |
| 5211 | Banques en monnaie nationale | | 20 000 000 |

**Terrain.** Immobilisation non amortissable : la subvention est reprise sur 10 ans en l'absence de clause d'inaliénabilité, à raison de 1/10 par exercice, sans prorata temporis. Reprise en N et sur les exercices suivants : 20 000 000 × 1/10 = 2 000 000.

Reprise de la subvention (terrain) au 31/12/N :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 1417 | Subventions d'équipement — Organismes internationaux | 2 000 000 | |
| 799 | Reprises de subventions d'investissement | | 2 000 000 |

**Bâtiment (exercice N+1).** Amortissement sur 20 ans à compter de la mise en service ; reprise de subvention au même rythme. Amortissement N+1 : 100 000 000 × 1/20 × 6/12 = 2 500 000. Reprise N+1 : 100 000 000 × 1/20 × 6/12 = 2 500 000.

Acquisition de l'entrepôt (01/07/N+1) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 231 | Bâtiment sur sol propre | 100 000 000 | |
| 4812 | Fournisseurs d'investissement, immo. corporelles | | 100 000 000 |

Règlement de l'entrepôt (01/07/N+1) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 4812 | Fournisseurs d'investissement, immo. corporelles | 100 000 000 | |
| 5211 | Banques en monnaies locales | | 100 000 000 |

Amortissement de l'entrepôt (31/12/N+1) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 6813 | Dotations aux amortissements des immo. corporelles | 2 500 000 | |
| 2838 | Amortissements du bâtiment sur sol propre | | 2 500 000 |

Reprise de subvention (entrepôt) (31/12/N+1) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 1417 | Subventions d'équipement — Organismes internationaux | 2 500 000 | |
| 799 | Reprises de subventions d'investissement | | 2 500 000 |

Reprise de subvention (terrain) (31/12/N+1) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 1417 | Subventions d'équipement — Organismes internationaux | 2 000 000 | |
| 799 | Reprises de subventions d'investissement | | 2 000 000 |

Virement de compte à compte du terrain (31/12/N+1) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 2234 | Terrains bâtis pour bâtiment affecté aux autres opérations professionnelles | 20 000 000 | |
| 2221 | Terrains à bâtir | | 20 000 000 |

---

## CHAPITRE 2 : Fonds affectés et reportés associations, fondations et assimilés

### APPLICATION 4 — Fonds non utilisés en fin d'exercice destinés à un projet spécifique

**Énoncé.** Le 15 octobre N, une ONG reçoit de la BAD la notification d'une donation de 45 000 000 affectée à un projet d'hydraulique villageoise (région du Nord). Virement bancaire reçu le 02 novembre N (45 000 000). En fin d'exercice, les ressources affectées ont été consommées à 1/3 (contexte COVID-19). Le reste est consommé en N+1.

Réception de la donation (15/10/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 52 | Banque | 45 000 000 | |
| 165 | Fonds affectés à un projet spécifique | | 45 000 000 |

Fonds consommés au 1/3 (31/12/N) — 45 000 000 × 1/3 :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 165 | Fonds affectés à un projet spécifique | 15 000 000 | |
| 7925 | Reprises de fonds affectés à un projet spécifique | | 15 000 000 |

Couverture des dépenses engagées (31/12/N+1) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 165 | Fonds affectés à un projet spécifique | 30 000 000 | |
| 7925 | Reprises de fonds affectés à un projet spécifique | | 30 000 000 |

---

### APPLICATION 5 — Fonds provenant des dons et des legs d'immobilisations

**Énoncé.** Le 1er avril N, l'association accepte l'actif net successoral d'un legs : bâtiment administratif (durée 30 ans) 400 000 000, mobilier de bureau (10 ans) 25 000 000, matériel informatique (2 ans) 10 000 000, matériel automobile (3 ans) 12 000 000, dettes successorales 25 000 000, obligation d'entretenir la tombe du testateur pendant 25 ans (coût estimé 12 500 000). Dettes successorales réglées par virement le 10 mai.

Réception du legs (01/04/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 2313 | Bâtiments administratifs | 400 000 000 | |
| 2442 | Matériel informatique | 10 000 000 | |
| 2441 | Mobilier de bureau | 25 000 000 | |
| 2451 | Matériel automobile | 12 000 000 | |
| 4861 | Dettes des dons et legs d'immobilisations | | 25 000 000 |
| 167 | Fonds provenant des dons et legs d'immobilisations | | 422 000 000 |

Paiement des dettes du donateur (10/05/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 4861 | Dettes des dons et legs d'immobilisations | 25 000 000 | |
| 52 | Banques | | 25 000 000 |

Provision pour charges sur legs et dons (31/12/N) — obligation d'entretenir la tombe :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 1679 | Engagement auprès du donateur | 12 500 000 | |
| 192 | Provisions pour charges sur legs et dons | | 12 500 000 |

Amortissements de l'exercice (prorata 9/12) :
- Bâtiments administratifs : 400 000 000 × 1/30 × 9/12 = 10 000 000
- Matériel informatique : 10 000 000 × 1/2 × 9/12 = 3 750 000
- Mobilier de bureau : 25 000 000 × 1/10 × 9/12 = 1 875 000
- Matériel automobile : 12 000 000 × 1/3 × 9/12 = 3 000 000

Dotations aux amortissements (31/12/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 6813 | Dotations aux amortissements des immo. corporelles | 18 625 000 | |
| 28313 | Amortissements des bâtiments administratifs | | 10 000 000 |
| 28442 | Amortissements du matériel informatique | | 3 750 000 |
| 28444 | Amortissements du mobilier de bureau `[texte officiel : imprimé « 28444 » dans le guide alors que le bien est en 2441 ; les trois autres lignes suivent le schéma 28 + racine du bien (28313, 28442, 28451), ce qui donnerait « 28441 »]` | | 1 875 000 |
| 28451 | Amortissements du matériel automobile | | 3 000 000 |

Reprise des fonds affectés (31/12/N) — à concurrence de la dotation aux amortissements des immobilisations acquises par ces fonds :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 167 | Fonds provenant des dons et legs | 18 625 000 | |
| 7923 | Reprises de fonds affectés provenant de dons et legs d'immobilisations | | 18 625 000 |

---

### APPLICATION 6 — Legs et donations non encore reçus d'immobilisations destinées à la vente

**Énoncé.** Le 5 janvier N, l'association accepte par acte authentique un legs de biens disponibles en janvier N+2, destinés à la vente : bâtiment administratif 400 000 000, mobilier de bureau 25 000 000, matériel informatique 10 000 000, matériel automobile 12 000 000. À la clôture N+1, test de dépréciation : dépréciation de 25 % de la valeur du bâtiment. Le 20 février N+2, vente du bâtiment à 250 000 000, du mobilier et du matériel à 60 000 000. Le 10 mars N+2, encaissement par chèque.

Comptabilisation initiale (05/01/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 203 | Bâtiments destinés à la vente provenant de legs non encore reçus | 400 000 000 | |
| 204 | Matériels destinés à la vente provenant de legs non encore reçus (25 000 000 + 10 000 000 + 12 000 000) | 47 000 000 | |
| 172 | Legs non encore reçus d'immobilisations destinées à la vente | | 447 000 000 |

Dépréciation à la clôture N+1 (31/12/N+1) — 400 000 000 × 25 % = 100 000 000 :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 6952 | Dotations aux dépréciations des immobilisations destinées à la vente provenant de legs non encore reçus | 100 000 000 | |
| 2902 | Dépréciations des immobilisations destinées à la vente provenant de legs non encore reçus | | 100 000 000 |

Décomptabilisation des immobilisations cédées (20/02/N+2) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 818 | VNC Immobilisations reçues destinées à la vente provenant de legs | 447 000 000 | |
| 203 | Bâtiments destinés à la vente provenant de legs non encore reçus | | 400 000 000 |
| 204 | Matériels destinés à la vente provenant de legs non encore reçus | | 47 000 000 |

Créance sur cession (20/02/N+2) — 250 000 000 + 60 000 000 = 310 000 000 :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 485 | Créances sur cessions d'immobilisations | 310 000 000 | |
| 828 | Produits des cessions d'immobilisations reçues destinées à la vente provenant de legs | | 310 000 000 |

Encaissement (10/03/N+2) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 52 | Banques | 310 000 000 | |
| 485 | Créances sur cessions d'immobilisations | | 310 000 000 |

Solde du compte de legs non encore reçus (31/12/N+2) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 172 | Legs non encore reçus d'immobilisations destinées à la vente | 447 000 000 | |
| 7962 | Reprises de fonds reportés provenant de legs d'immobilisations reçues destinées à la vente | | 447 000 000 |

Solde de la dépréciation devenue sans objet (31/12/N+2) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 2902 | Dépréciations des immobilisations destinées à la vente provenant de legs non encore reçus | 100 000 000 | |
| 7952 | Reprises des dépréciations d'immobilisations reçues destinées à la vente provenant de legs | | 100 000 000 |

---

### APPLICATION 7 — Donation temporaire d'usufruit

**Énoncé.** Une association bénéficie par acte authentique de l'usufruit d'un immeuble pour 10 ans, le 02/01/N. Une partie est mise en location, loyer annuel payable d'avance 12 000 000. Le 10/01/N, le locataire remet un chèque du loyer annuel. Valeur de l'immeuble estimée à 150 000 000. À la clôture N, indice de perte de valeur : test révélant une dépréciation de 25 000 000.

**Note préliminaire.** En cas d'indice de perte de valeur, une dépréciation doit en principe être constatée. Toutefois, par simplification, le SYCEBNL recommande de ne pas constater de dépréciation mais de fournir l'information dans la **Note 5D — Dons et legs d'immobilisations non reçus destinés à la vente et usufruit temporaire (amortissements et dépréciations)**.

Réception de l'usufruit (02/01/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 2011 | Usufruit temporaire | 150 000 000 | |
| 171 | Donation temporaire d'usufruit | | 150 000 000 |

Constatation du loyer annuel (10/01/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 412 | Clients-usagers | 12 000 000 | |
| 7082 | Revenus d'usufruit | | 12 000 000 |

Encaissement du loyer (10/01/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 52 | Banques | 12 000 000 | |
| 412 | Clients-usagers | | 12 000 000 |

Amortissement de la donation d'usufruit (31/12/N) — 150 000 000 × 1/10 = 15 000 000 :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 680 | Dotations aux amortissements d'usufruit temporaire | 15 000 000 | |
| 280 | Amortissements d'usufruit temporaire | | 15 000 000 |

Reprise de la donation d'usufruit au même rythme (31/12/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 171 | Donation temporaire d'usufruit | 15 000 000 | |
| 7961 | Reprises de fonds provenant d'usufruit temporaire | | 15 000 000 |

Dépréciation : simple information en Note 5D (pas d'écriture, par simplification SYCEBNL).

Rétrocession au donateur au terme de la donation — décomptabilisation :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 280 | Amortissements d'usufruit temporaire | 150 000 000 | |
| 2011 | Usufruit temporaire | | 150 000 000 |

---

## CHAPITRE 3 : Fonds propres, projets de développement et assimilés

### APPLICATION 8 — Projet de développement

**Énoncé.** La Banque Mondiale décaisse le 5 janvier N un virement global de 150 000 000 pour un projet de développement. Le budget estime à 80 % la part investissement et 20 % la part fonctionnement.
Opérations d'investissement N : terrain 10 000 000, entrepôt de stockage (20 ans) 50 000 000, mobilier de bureau (10 ans) 5 000 000, matériel informatique (2 ans) 12 000 000, matériel automobile (4 ans) 35 000 000 — total 112 000 000.
Opérations de fonctionnement N : achats de fournitures (marché local) 10 075 000, autres achats 5 000 000, voyages et déplacements 1 500 000, services extérieurs 2 500 000, salaires nets 8 500 000, charges patronales sécurité sociale 255 000, charges patronales fiscales 170 000 — total 28 000 000.
Début N+1 : le projet engage le solde des fonds transférés (accord du bailleur) pour des prestations de services par chèque à hauteur de 10 000 000.

**Note préliminaire.** L'entité peut présenter des états financiers par bailleur ou sous-projet ; subdiviser alors les comptes par affectation d'un identifiant en fin de numéro. Si cette option est retenue, les états financiers combinés sont obligatoires. Exemple : Bailleur A identifié par la racine 25, Bailleur B par 42 → 245125 Matériel automobile ; 625225 Assurance auto (financement A) ; 245142 / 625242 (financement B).

Décaissement des bailleurs (05/01/N) — fonds investissement = 150 000 000 × 80 % = 120 000 000 :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 52 | Banque | 150 000 000 | |
| 162 | Fonds affectés aux investissements | | 120 000 000 |
| 462 | Fonds d'administration | | 30 000 000 |

Comptabilisation des opérations d'investissement :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 2234 | Terrains | 10 000 000 | |
| 2318 | Bâtiments | 50 000 000 | |
| 2442 | Matériel informatique | 12 000 000 | |
| 2441 | Mobilier de bureau | 5 000 000 | |
| 2451 | Matériel automobile | 35 000 000 | |
| 4812 | Fournisseurs d'investissement, immob. corporelles | | 112 000 000 |

Règlement des dépenses d'investissement :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 4812 | Fournisseurs d'investissement, immob. corporelles | 112 000 000 | |
| 52 | Banque | | 112 000 000 |

Charges de fonctionnement (hors personnel) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 6011 | Achats de fournitures | 10 075 000 | |
| 6050 | Autres achats | 5 000 000 | |
| 6181 | Voyages et déplacements | 1 500 000 | |
| 62/63 | Services extérieurs | 2 500 000 | |
| 40 | Fournisseurs | | 19 075 000 |

Règlement (hors personnel) : débit 40 Fournisseurs 19 075 000 / crédit 52 Banque 19 075 000.

Salaires bruts :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 6611 | Appointements, salaires et commissions | 8 500 000 | |
| 422 | Personnel, rémunérations dues | | 8 500 000 |

Charges fiscales sur salaires :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 6413 | Taxes sur appointements et salaires | 170 000 | |
| 4421 | État, Impôts et taxes d'État | | 170 000 |

Charges sociales :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 664 | Charges sociales | 255 000 | |
| 431 | Sécurité sociale | | 255 000 |

Règlement des impôts/taxes sur salaires et charges sociales :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 4421 | État, Impôts et taxes d'État | 170 000 | |
| 431 | Sécurité sociale | 255 000 | |
| 52 | Banque | | 425 000 |

Transfert des fonds d'administration — neutralisation des charges par un compte de produit :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 462 | Fonds d'administration | 28 000 000 | |
| 702 | Quote-part de fonds administration transférés | | 28 000 000 |

**À la clôture.** Aucune dotation aux amortissements n'est constatée : l'approche financière de l'amortissement (reconstituer les capitaux investis pour renouveler les immobilisations) n'est pas appropriée aux projets.

Constatation des fonds d'investissement non consommés (31/12/N) — 120 000 000 − 112 000 000 = 8 000 000 :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 162 | Fonds affectés aux investissements | 8 000 000 | |
| 165 | Fonds non consommés en fin d'exercice | | 8 000 000 |

Extourne au 1er janvier N+1 :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 165 | Fonds non consommés en fin d'exercice | 8 000 000 | |
| 162 | Fonds affectés aux investissements | | 8 000 000 |

Prestations de services N+1 :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 62/63 | Services extérieurs | 10 000 000 | |
| 4011 | Fournisseurs | | 10 000 000 |

Règlement : débit 4011 Fournisseurs 10 000 000 / crédit 5211 Banque 10 000 000.

Transfert des fonds d'administration N+1 :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 462 | Fonds d'administration | 10 000 000 | |
| 702 | Quote-part de fonds administration transférés | | 10 000 000 |

**Ajustements N+1.** Après utilisation des fonds selon la clé du bailleur, les fonds d'administration s'élèvent à 38 000 000 et les fonds d'investissement à 112 000 000. À la réception, à défaut d'information précise du bailleur, l'entité avait estimé : investissements 120 000 000, administration 30 000 000. Correction : déduire 8 000 000 des fonds d'investissement au profit des fonds d'administration :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 162 | Fonds affectés aux investissements | 8 000 000 | |
| 462 | Fonds d'administration | | 8 000 000 |

---

## CHAPITRE 4 : Dons

### APPLICATION 9 — Dons en nature à distribuer

**Énoncé.** L'association DONAS reçoit le 01/03/N des dons de produits alimentaires destinés aux nécessiteux, valeur 25 000 000 (collecte régulière auprès de sociétés agro-industrielles ; convention imposant une distribution aux seuls nécessiteux). À la clôture, stock de produits non distribués : 5 000 000.

Réception des dons à distribuer (01/03/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 654 | Dons en nature courants à distribuer | 25 000 000 | |
| 7542 | Dons en nature courants reçus à distribuer | | 25 000 000 |

Dons non consommés — stock (31/12/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 345 | Stock de dons en nature affectés | 5 000 000 | |
| 6035 | Variations de stocks de dons en nature | | 5 000 000 |

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 7542 | Dons en nature courants reçus à distribuer | 5 000 000 | |
| 4713 | Créditeurs, dons en nature courants non consommés | | 5 000 000 |

Réouverture des comptes (01/01/N+1) — contrepassation :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 6035 | Variations de stocks de dons en nature | 5 000 000 | |
| 345 | Stock de dons en nature affectés | | 5 000 000 |

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 4713 | Créditeurs, dons en nature courants non consommés | 5 000 000 | |
| 7542 | Dons en nature courants reçus à distribuer | | 5 000 000 |

---

### APPLICATION 10 — Dons en nature à vendre

**Énoncé.** Opération 1 : une association reçoit gratuitement, de façon périodique, des lots de vêtements de marque déstockés destinés à la vente (10/10/N). Le 15/04/N+1, vente à 12 000 000 ; les usagers règlent 25 % en espèces et le reste par chèque le 20/04/N+1.
Opération 2 : le 10/06/N, l'association XY reçoit gratuitement un camion (valeur argus 15 000 000), non nécessaire à son objet social, décide de le vendre. 30/08/N, paiement par chèque de 250 000 (frais de remise en état). 31/03/N+1, vente du camion à 13 000 000 par chèque.

**Note préliminaire.** Les dons en nature reçus destinés à la vente sont suivis via les comptes de contribution volontaire en nature jusqu'à la cession ; en fin d'exercice, les dons non vendus sont mentionnés en **Note 1 — Dettes garanties par des sûretés réelles, engagements financiers et contributions volontaires en nature**. Les frais engagés avant cession sont enregistrés en charges par nature ou en HAO selon le cas et rattachés à l'exercice de réalisation du don ; les frais afférents aux dons non vendus en fin d'exercice sont neutralisés par le compte 476 Charges comptabilisées d'avance, extourné au début de l'exercice suivant.

**Opération 1** (suivi extra-comptable jusqu'à cession) :

Vente (15/04/N+1) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 412 | Clients-usagers | 12 000 000 | |
| 7081 | Ventes de dons en nature | | 12 000 000 |

Règlement (20/04/N+1) — 25 % espèces, 75 % chèque :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 57 | Caisse | 3 000 000 | |
| 52 | Banques | 9 000 000 | |
| 412 | Clients-usagers | | 12 000 000 |

**Opération 2** :

Réception du don à vendre (10/06/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 901 | Mise à disposition gratuite de biens | 15 000 000 | |
| 910 | Dons en nature | | 15 000 000 |

Frais de remise en état (30/08/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 8311 | Charges sur dons et legs | 250 000 | |
| 52 | Banques | | 250 000 |

Neutralisation des frais (camion non vendu) (31/12/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 476 | Charges comptabilisées d'avance | 250 000 | |
| 8311 | Charges sur dons et legs | | 250 000 |

Extourne (01/01/N+1) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 8311 | Charges sur dons et legs | 250 000 | |
| 476 | Charges comptabilisées d'avance | | 250 000 |

Vente du camion (31/03/N+1) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 52 | Banques | 13 000 000 | |
| 8421 | Dons en nature HAO vendus | | 13 000 000 |

Solde des comptes de contribution volontaire (31/12/N+1) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 910 | Dons en nature | 250 000 | |
| 901 | Mise à disposition gratuite de bien | | 250 000 |

Notes : (1) si la vente n'est pas réalisée en N+1, contrepasser l'écriture d'extourne au 31/12/N+1 ; (2) l'écriture de solde des comptes 901/910 peut être passée dès la date de vente (31/03/N+1).

---

### APPLICATION 11 — Dons en numéraire et revenus des manifestations et édifices religieux

**Énoncé — Opération 1 (église).** Contributions de la générosité des fidèles : dons 10 000 000 par chèque ; denier du culte 6 000 000 espèces ; quête 8 000 000 espèces ; dîmes 1 000 000 espèces. Dons en numéraire de 8 000 000 notifiés par lettre d'engagement ferme, non encore encaissés à la clôture. Kermesse pour rénover la chapelle : recettes espèces 25 000 000 ; billets d'entrée avec stickers facturés 500 000 ; lots de tombola 3 500 000 ; factures billets et tombola réglées par chèque.
**Opération 2 (mosquée).** Dons 12 000 000 par chèque ; zakat 5 000 000 espèces ; recettes d'une célébration de mariage 2 000 000 espèces. Projet de mosquée annexe : avance de 100 000 000 par virement ; solde de la facture 150 000 000 réglé à la livraison par virement (sous escompte de 5 % sur le montant global), immédiatement mis en service pour la fête de la Tabaski.

**Opération 1 — revenus liés à la générosité :**

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 57 | Caisse | 15 000 000 | |
| 52 | Banques | 10 000 000 | |
| 70410 | Dons | | 10 000 000 |
| 70430 | Deniers de culte | | 6 000 000 |
| 70441 | Quête | | 8 000 000 |
| 70442 | Dîmes | | 1 000 000 |

Générosités à recevoir (31/12/N) — lettre d'engagement de dons :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 475 | Générosités financières à recevoir | 8 000 000 | |
| 7041 | Dons | | 8 000 000 |

Revenus des manifestations — factures billetterie et tombola :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 6061 | Billetteries | 500 000 | |
| 6062 | Tombola | 3 500 000 | |
| 401 | Fournisseurs | | 4 000 000 |

Règlement des factures : débit 401 Fournisseurs 4 000 000 / crédit 52 Banques 4 000 000.

Recettes de la manifestation :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 57 | Caisse | 25 000 000 | |
| 706 | Revenus des manifestations | | 25 000 000 |

**Opération 2 — revenus liés à la générosité :**

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 57 | Caisse | 7 000 000 | |
| 52 | Banques | 12 000 000 | |
| 7041 | Dons | | 12 000 000 |
| 7044 | Zakat | | 5 000 000 |
| 7045 | Célébrations | | 2 000 000 |

Construction de la mosquée annexe — avance :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 252 | Avances et acomptes versés sur immobilisations corporelles | 100 000 000 | |
| 52 | Banques | | 100 000 000 |

Livraison (facture sous escompte de 5 %) — 250 000 000 × 95 % = 237 500 000 :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 2327 | Édifices religieux et assimilés | 237 500 000 | |
| 252 | Avances et acomptes versés sur immobilisations corporelles | | 100 000 000 |
| 4812 | Fournisseurs d'investissement, immob. corporelles | | 137 500 000 |

Règlement du solde : débit 4812 Fournisseurs d'investissement 137 500 000 / crédit 52 Banques 137 500 000.

---

### APPLICATION 12 — Frais de recherche de fonds

**Énoncé.** Dépenses engagées pour la recherche de dons : transport de plis par DHL 25 000, bloc-notes 35 000, publicité dans les revues spécialisées 75 000. Règlement par chèque.

Frais de recherche de fonds — 25 000 + 35 000 + 75 000 = 135 000 :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 636 | Frais de recherche de fonds | 135 000 | |
| 40 | Fournisseurs | | 135 000 |

Règlement : débit 40 Fournisseurs 135 000 / crédit 52 Banques 135 000.

---

## CHAPITRE 5 : Cotisations des membres et contribution du fondateur

### APPLICATION 13 — Cotisations des membres

**Énoncé.** Cotisation mensuelle des membres de l'association VIDOLET : 2 500 000. Appel du mois de septembre N lancé le 20/09/N. Versement partiel en espèces de 2 000 000 le 5 octobre N. À la clôture, risque de non-recouvrement : le trésorier constitue une dépréciation de créances douteuses de 80 % des cotisations dues, globalement 12 000 000.

Appel de cotisation (20/09/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 411 | Adhérents | 2 500 000 | |
| 701 | Cotisations des adhérents | | 2 500 000 |

Recouvrement (05/10/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 57 | Caisse | 2 000 000 | |
| 411 | Adhérents | | 2 000 000 |

Transfert en créance douteuse (31/12/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 4161 | Adhérents, cotisations douteuses | 12 000 000 | |
| 411 | Adhérents | | 12 000 000 |

Constatation de la dépréciation (31/12/N) — 12 000 000 × 80 % = 9 600 000 :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 6594 | Charges pour dépréciations sur créances | 9 600 000 | |
| 4912 | Dépréciations des créances douteuses | | 9 600 000 |

---

### APPLICATION 14 — Contribution du fondateur pour couverture des frais de fonctionnement d'une fondation

**Énoncé.** Le fondateur verse 20 000 000 pour aider ponctuellement sa fondation à couvrir les frais de fonctionnement. Fonds versés par chèque le 09/09/N.

Versement reçu du fondateur (09/09/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 52 | Banques | 20 000 000 | |
| 752 | Contribution du fondateur | | 20 000 000 |

---

### APPLICATION 15 — Subventions et aides financières versées par les EBNL

**Énoncé.** Une association verse une aide financière en espèces le 3 juin N de 500 000 aux représentants d'un parti politique lors d'une campagne électorale municipale.

Contribution versée (03/06/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 652 | Subventions versées par l'entité | 500 000 | |
| 57 | Caisse | | 500 000 |

---

## CHAPITRE 6 : Autres opérations spécifiques

### APPLICATION 16 — Subventions d'exploitation se répartissant sur plusieurs exercices

**Énoncé.** Une association reçoit une subvention d'exploitation du Conseil Régional de 60 000 000 pour les exercices N, N+1 et N+2. Notification le 1er juillet N, encaissement le 5 juillet N.

Notification (01/07/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 4732 | Subventions d'exploitation à recevoir | 60 000 000 | |
| 711 | Subventions d'exploitation versées par les collectivités publiques | | 60 000 000 |

Réception des fonds (05/07/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 52 | Banques | 60 000 000 | |
| 4732 | Subventions d'exploitation à recevoir | | 60 000 000 |

Régularisation de fin d'exercice (31/12/N) — 60 000 000 × 2/3 = 40 000 000 :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 711 | Subventions d'exploitation versées par les collectivités publiques | 40 000 000 | |
| 477 | Produits constatés d'avance | | 40 000 000 |

Rattachement N+1 (31/12/N+1) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 477 | Produits constatés d'avance | 20 000 000 | |
| 711 | Subventions d'exploitation versées par les collectivités publiques | | 20 000 000 |

Rattachement N+2 (31/12/N+2) : même écriture 477 / 711 pour 20 000 000.

---

### APPLICATION 17 — Abandons de frais engagés par les bénévoles

**Énoncé.** En avril N, les frais engagés par les bénévoles : voyages et déplacements 275 000, missions 150 000, réceptions 75 000, fournitures de bureau non stockables 25 000. Le 15 mai, les bénévoles décident d'abandonner ces frais au profit de l'association.

Constatation des frais (04/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 6181 | Voyages et déplacements | 275 000 | |
| 6384 | Missions | 150 000 | |
| 6383 | Réceptions | 75 000 | |
| 6055 | Fournitures de bureau non stockables | 25 000 | |
| 4572 | Bénévoles | | 525 000 |

Abandon des frais (15/05/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 4572 | Bénévoles | 525 000 | |
| 7583 | Abandons de frais par les bénévoles | | 525 000 |

---

### APPLICATION 18 — Convention de mécénat

**Énoncé.** Convention de mécénat signée le 30/06 pour 50 000 000, portant sur une campagne de vaccination gratuite (démarrage 01/09/N). Le mécène verse 30 000 000 à la signature et le solde au 31/12/N.

Signature de la convention (30/06/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 4751 | Mécènes | 50 000 000 | |
| 7046 | Mécénats | | 50 000 000 |

Premier versement (30/06/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 52 | Banques | 30 000 000 | |
| 4751 | Mécènes | | 30 000 000 |

Versement du solde (31/12/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 52 | Banques | 20 000 000 | |
| 4751 | Mécènes | | 20 000 000 |

---

### APPLICATION 19 — Restitution de subvention non utilisée conformément à l'objet prévu dans la convention

**Énoncé.** Une ONG reçoit une subvention de l'Union Européenne de 90 000 000 pour l'exercice N : 75 000 000 destinés à l'acquisition d'équipement, le reste à la couverture des frais de fonctionnement. Notification le 10 octobre N, encaissement le 5 novembre N. Le 10 décembre N, les dirigeants constatent qu'une quote-part de la subvention d'équipement de 25 000 000 doit être remboursée (clauses non respectées). Virement au profit de l'UE le 20 décembre N.

Notification (10/10/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 4731 | Subvention d'investissement à recevoir | 75 000 000 | |
| 4732 | Subvention d'exploitation à recevoir | 15 000 000 | |
| 1417 | Subvention d'équipement — Organismes internationaux | | 75 000 000 |
| 713 | Subventions d'exploitation versées par les organismes internationaux | | 15 000 000 |

Réception des fonds (05/11/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 52 | Banques | 90 000 000 | |
| 4731 | Subvention d'investissement à recevoir | | 75 000 000 |
| 4732 | Subvention d'exploitation à recevoir | | 15 000 000 |

Constatation de la quote-part à reverser (10/12/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 1417 | Subvention d'équipement — Organismes internationaux | 25 000 000 | |
| 4739 | Organismes internationaux, subvention à reverser | | 25 000 000 |

Reversement (20/12/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 4739 | Organismes internationaux, subvention à reverser | 25 000 000 | |
| 52 | Banques | | 25 000 000 |

---

### APPLICATION 20 — Contributions volontaires en nature

**Énoncé.** Une association reçoit des fournitures de bureau pour sa gestion administrative, valeur 450 000. Pour sa campagne de collecte de dons d'avril N, elle mobilise 450 bénévoles durant 15 jours. Chacun a offert entre 5 et 60 heures ; temps moyen 18,5 heures ; total = 450 × 18,5 = 8 325 heures. Travail sans compétences particulières, valorisé au taux horaire du SMIG de 346.

Contribution en biens (…/04/N) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 901 | Mise à disposition gratuite de biens | 450 000 | |
| 910 | Dons en nature | | 450 000 |

Contribution en travail (…/04/N) — 8 325 × 346 = 2 880 450 :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 904 | Personnel bénévole | 2 880 450 | |
| 914 | Bénévolat | | 2 880 450 |

**Informations en Note 1 — Dettes garanties par des sûretés réelles, engagements financiers et contributions volontaires en nature :**

| Contributions volontaires en nature | Ressources | Emplois |
|---|---|---|
| Dons en nature fourniture de bureau | 450 000 | |
| Mise à disposition gratuite de fourniture de bureau | | 450 000 |
| Personnel bénévole | 2 864 880 | 2 864 880 |
| **TOTAL** | **3 314 880** | **3 314 880** |

`[texte officiel : le montant du personnel bénévole vaut 2 880 450 dans l'écriture comptable (8 325 × 346) mais 2 864 880 dans le tableau de la Note 1 ; l'écart n'est pas expliqué dans le guide]`

Commentaire : l'évaluation des contributions volontaires en nature est faite sur la base de la valeur actuelle des biens et services ; l'évaluation des heures de bénévolat sur la base du SMIG horaire de 346.

---

## CHAPITRE 7 : Tableaux de correspondance — projets de développement

`[texte officiel : ce chapitre est numéroté « CHAPITRE 6 : Tableaux de correspondance » dans la table des matières, en doublon avec le chapitre « Autres opérations spécifiques » ; le corps du guide le titre « CHAPITRE 7 »]`

### APPLICATION 21 — Tableau de correspondance : Tableau emplois-ressources

Correspondance poste (code REF) → source dans la balance. Les notes de renvoi (1) à (8) figurent après le tableau.

| Code | Poste | Source (balance) |
|---|---|---|
| FA | Fonds reçus, Bailleurs … | Balance mouvement crédit : comptes 161, 162, 462 (si plusieurs bailleurs, créer des sous-comptes de 161, 162, 462 pour remplir FB) |
| FB | Fonds reçus, Bailleurs … | Balance mouvement crédit : comptes 161, 162, 462 |
| FC | Fonds contrepartie État | Balance mouvement crédit : comptes 163, 463 |
| FD | Autres fonds reçus | Balance mouvement crédit : comptes 164, 464, 707 (1), 77 |
| **GR** | **I. RESSOURCES** | |
| FE | Immobilisations incorporelles | Balance mouvement débit : compte 21 (2) |
| FF | Terrains | Balance mouvement débit : compte 22 (2) |
| FG | Bâtiments | Balance mouvement débit : comptes 231, 232, 233, 2391, 2392, 2393, 2396 (2) |
| FH | Aménagements, agencements et installations | Balance mouvement débit : comptes 234, 235, 238, 2394, 2395, 2398 (2) |
| FI | Matériel, mobilier et actifs biologiques | Balance mouvement débit : comptes 24 (sauf 245 et 2495) (2) |
| FJ | Matériel de transport | Balance mouvement débit : comptes 245 et 2495 (2) |
| FK | Avances et acomptes sur immobilisations | Balance mouvement débit : comptes 25 |
| FL | Immobilisations financières | Balance mouvement débit : comptes 26, 27 (3) |
| **GS** | **A - TOTAL DES IMMOBILISATIONS** | |
| FM | Achats de biens et services | Balance mouvement débit : compte 60 (4) |
| FN | Transports | Balance mouvement débit : compte 61 (4) |
| FO | Services extérieurs | Balance mouvement débit : comptes 62, 63 (4) |
| FP | Impôts et taxes | Balance mouvement débit : compte 64 (5) |
| FQ | Autres charges | Balance mouvement débit : compte 65 (6) |
| FR | Charges de personnel | Balance mouvement débit : compte 66 (7) |
| FS | Charges financières | Balance mouvement débit : compte 67 (8) |
| FT | Avances sur charges (à justifier) | Balance solde débiteur : comptes 4091, 4093 |
| **GT** | **B - TOTAL DES CHARGES DE FONCTIONNEMENT** | |
| **GU** | **II. EMPLOIS (A+B)** | |
| **GV** | **III. EXCÉDENT / DÉFICIT DES FONDS REÇUS SUR LES EMPLOIS (I-II)** | |
| FU | Fonds Bailleur en début exercice N | Balance solde débiteur N-1 des fonds bailleurs : comptes 51, 52, 53, 55, 57 |
| FV | Fonds de contrepartie État en début exercice N | Balance solde débiteur N-1 des fonds de contrepartie État : comptes 51, 52, 53, 55, 57 |
| FW | Autres fonds en début exercice N | Balance solde débiteur N-1 des autres fonds : comptes 51, 52, 53, 55, 57 |
| **GW** | **IV. FONDS DISPONIBLE EN DÉBUT EXERCICE** | |
| **GX** | **V. MONTANT NET DE L'ENCAISSE DISPONIBLE (III+IV)** | |
| FX | Fonds Bailleur en fin exercice N | Balance solde débiteur N des fonds bailleurs : comptes 51, 52, 53, 55, 57 |
| FY | Fonds de contrepartie État en fin exercice N | Balance solde débiteur N des fonds de contrepartie État : comptes 51, 52, 53, 55, 57 |
| FZ | Autres fonds en fin exercice N | Balance solde débiteur N des autres fonds : comptes 51, 52, 53, 55, 57 |
| **GY** | **VI. FONDS DISPONIBLE EN FIN EXERCICE** | |
| **GZ** | **VII. CONTRÔLE : TOTAL V = TOTAL VI** | |

Renvois :
1. Produits d'exploitation à recevoir en cas de vente de cahier de charges, location de voiture, sous-location de bureau, etc.
2. Déduire la variation des dettes fournisseurs d'investissements (+ solde créditeur N-1 du compte 481 concerné sauf 4813 − solde créditeur N du compte 481 concerné sauf 4813). En sus, ne pas tenir compte des virements de compte à compte qui ne traduisent pas une acquisition d'immobilisation incorporelle et corporelle décaissée.
3. Déduire la variation des dettes rattachées aux versements restant à effectuer sur titres de participation et titres immobilisés non libérés (+ solde débiteur N-1 du compte 4813 − solde débiteur N du compte 4813). En sus, ne pas tenir compte du mouvement débit du compte 276 (intérêts courus sur immobilisations financières) ni des virements de compte à compte ne traduisant pas une acquisition d'immobilisation financière décaissée.
4. Déduire la variation des dettes fournisseurs d'exploitation (+ solde débiteur N-1 du compte 401 concerné − solde débiteur N du compte 401 concerné). En sus, ne pas tenir compte de la variation des stocks (compte 603) figurant dans le compte 60 Achats, ni des comptes 60 Achats et dettes équivalentes transférés en immobilisations (livraison à soi-même) pour éviter le double emploi.
5. Déduire la variation des dettes fiscales (+ solde débiteur N-1 du compte 44 − solde débiteur N du compte 44).
6. Déduire la variation des dettes rattachées au compte 65 Autres charges (+ solde débiteur N-1 du compte de tiers concerné − solde débiteur N du compte de tiers concerné). En sus, ne pas tenir compte des comptes Autres charges et dettes équivalentes transférés en immobilisations (livraison à soi-même) ni des dépréciations et provisions à court terme (comptes 49).
7. Déduire la variation des dettes rattachées aux charges de personnel (+ solde débiteur N-1 des comptes 42 et 43 − solde débiteur N des comptes 42 et 43). En sus, ne pas tenir compte des charges de personnel et dettes équivalentes transférées en immobilisations (livraison à soi-même).
8. Déduire le mouvement crédit du compte 166. En sus, ne pas tenir compte des comptes 67 Charges financières transférées en immobilisations (livraison à soi-même) ni des dépréciations et provisions à court terme (comptes 49).

---

### APPLICATION 22 — Tableau de correspondance : Tableau d'exécution budgétaire

Structure du tableau (colonnes) :

| Code (a) | Libellé (a) | Budget de l'exercice (b) [1] | Décaissement (c) [2] | Engagement (d) [3] | Réalisation [4 = 2+3] | Crédit disponible [5 = 1−4] | Exécution budget (%) [4/1] |
|---|---|---|---|---|---|---|---|
| … | … | | | | | | |
| **TOTAL** | | | | | | | |

Règles de remplissage :
- (a) Remplir code et libellé suivant la nomenclature budgétaire du projet.
- (b) Le plan comptable doit être conçu en tenant compte du budget du projet ; cette rubrique est remplie au vu du budget de l'exercice du projet, compte par compte.
- (c) Décaissement (si le plan comptable est conçu sur la base du budget), somme algébrique pour chaque item :
  - mouvement débit balance N des comptes immobilisations (compte 2), à l'exception des virements de compte à compte, + (solde créditeur N-1 du compte 481 − solde créditeur N du compte 481) ;
  - mouvement débit balance N des comptes de charges (comptes 6 et 8) + (solde créditeur N-1 du compte 40 sauf 409 − solde créditeur N du compte 40 sauf 409) + (solde débiteur balance N du compte 409 − solde débiteur balance N-1 du compte 409).
- (d) Engagement pour chaque item :
  - solde créditeur balance N des comptes fournisseurs d'exploitation (compte 40) et d'investissement (compte 481) ;
  - bons de commande de biens et services remis aux fournisseurs au cours de l'exercice budgétaire, non exécutés ;
  - contrats signés par les parties prenantes au cours de l'exercice budgétaire, non exécutés.
