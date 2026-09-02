# Chapitre 1 — Préparation des états financiers (logique des postes, masses et rubriques)

Ce fichier couvre le chapitre 1 de la Partie 3 « Présentation des états financiers annuels » du Guide d'application SYSCOHADA (p. 326 à 340), auparavant absent du module. Il complète `app-127-modele-jeu-complet-etats-financiers.md`, qui ne couvrait que le chapitre 2 (l'exemple rempli). Les deux fichiers se lisent ensemble : celui-ci explique pourquoi les rubriques sont construites ainsi, l'Application 127 montre à quoi elles ressemblent une fois chiffrées.

Base légale citée dans le texte source : articles 8, 23, 29, 32 et 33 de l'Acte uniforme relatif au droit comptable et à l'information financière (AUDCIF).

## 1. Notion d'états financiers

L'article 23 impose, au titre de la synthèse annuelle, des états financiers arrêtés au plus tard dans les quatre mois suivant la clôture de l'exercice. Une simple sommation des comptes en deux masses — « gestion » (classes 6, 7, 8) et « patrimoine » (classes 1 à 5) — reviendrait à republier la balance : illisible pour un non-comptable, sans indication de gestion.

Le terme « états financiers » dérive de la terminologie anglo-saxonne (« financial accounting », « financial statements »). Il ne se rapporte ni aux comptes 67/77 dits « éléments financiers », ni à la seule classe 5 de trésorerie.

**Éléments communs aux quatre états.**

- Les postes ne sont pas numérotés en décimal comme les comptes ; ils sont lettrés par groupes de deux lettres (le bilan va de AD à DZ).
- Un poste correspond en général à un compte principal (BQ, BR ⇄ comptes 50, 51), mais parfois regroupe plusieurs comptes principaux (RH « Services extérieurs » ⇄ 62 et 63) ou au contraire ventile un seul compte principal sur plusieurs postes (60 ⇄ RA à RF).
- Les postes se regroupent en rubriques, elles-mêmes réunies en masses par sous-totaux. Exemple : AJ à AN forment la rubrique « immobilisations corporelles », intégrée à la masse ACTIF IMMOBILISÉ.
- Chaque état rappelle, à côté des chiffres de l'exercice N, ceux de l'exercice N-1, pour la comparabilité.

**Les quatre états prescrits par l'article 8** : Bilan (AD à DZ), Compte de résultat (RA à TO et XA à XI), Tableau des flux de trésorerie (FA à FQ et ZA à ZH), Notes annexes (postes non lettrés). Ils forment un tout indissociable. Les Notes ne sont pas un appendice : elles ont la même valeur que les trois autres états.

Des grilles de correspondance postes/comptes existent à deux niveaux : la balance d'exemple (indications par lettre) et les tableaux de correspondance du Plan comptable général OHADA, Titre IX chapitre 7 (indications par numéro de compte). C'est ce second niveau que `maquette.tsv` encode pour ce module.

## 2. Bilan

**Fonction** (art. 29). Le bilan décrit séparément l'actif et le passif constituant le patrimoine de l'entité, et fait apparaître distinctement les capitaux propres.

**Logique comptable.** Le bilan garde la structure d'un compte collectif : soldes débiteurs à gauche (actif), créditeurs à droite (passif).

En lecture verticale :
- haut de bilan : actif immobilisé (classe 2) ; passif interne — capitaux propres — et dettes financières (classe 1) ;
- bas de bilan : actif circulant (soldes débiteurs classes 3 et 4) et actif de trésorerie (soldes débiteurs classe 5) ; passif circulant (soldes créditeurs classe 4) et passif de trésorerie (soldes créditeurs classe 5).

**Aménagements par rapport à la logique comptable stricte.**

En lecture horizontale :
- les comptes d'amortissements (28) et de dépréciations (29 à 59), à solde créditeur, viennent en soustraction à l'actif — pas au passif ;
- les comptes 12 Report à nouveau et 139 Résultat net figurent toujours au passif, en addition si le solde est créditeur, en soustraction s'il est débiteur.

En lecture verticale : les postes suivent un ordre fonctionnel, avec un décalage volontaire — les écarts de conversion (comptes 478, 479) sont rejetés en pied de bilan plutôt que classés dans le circulant, parce que leur réalisation reste seulement probable.

**Tracé.** Présentation possible sur une seule page en mode paysage, ou sur deux pages (une pour l'actif, une pour le passif) — Plan comptable général OHADA, Titre IX chapitre 4.

## 3. Compte de résultat

**Fonction** (art. 29). Récapitulation en liste des produits et des charges, faisant apparaître par cascade les résultats intermédiaires puis le résultat net.

**Présentation en liste**, choisie pour son avantage : elle met en évidence, dans l'ordre, les soldes intermédiaires du plan comptable général. Cinq blocs de soldes structurent le compte de résultat.

**a) Marge commerciale.** TA (compte 701) moins RA (compte 601), ajusté de RB (compte 6031) — en addition si le solde est débiteur (déstockage), en soustraction s'il est créditeur (stockage). Sépare les opérations commerciales des opérations artisanales, industrielles ou de prestation de services.

**b) Chiffre d'affaires.** Somme des postes TA à TD (comptes 70).

**c) Résultats intermédiaires des activités ordinaires.**
- *Valeur ajoutée* : chiffre d'affaires (70) et autres produits (postes TE à TI, comptes 73, 72, 71, 75, 781), moins les achats (RA, RC, RE — comptes 601 à 608) ajustés des variations de stocks (RB, RD, RF — comptes 603, même règle addition/soustraction que ci-dessus), moins les autres consommations intermédiaires (RG à RJ, comptes 61 à 65).
- *Excédent brut d'exploitation (EBE)* : valeur ajoutée moins RK (compte 66, charges de personnel). Mesure le résultat de l'unité de production avant amortissements et politique financière. Sert aussi de point de départ à la capacité d'autofinancement par la méthode soustractive.
- *Résultat d'exploitation* : EBE ajusté des reprises d'exploitation (TJ — comptes 791, 798, 799) et des dotations d'exploitation (RL — comptes 681, 691).
- *Résultat financier* : revenus financiers (TK à TM — comptes 77, 797, 787) moins charges financières (RM, RN — comptes 67, 697).
- *Résultat des activités ordinaires* : somme du résultat d'exploitation et du résultat financier.

**d) Résultat hors activités ordinaires (HAO).** Produits HAO (TN, TO — comptes 82, 84, 86, 88) moins charges HAO (RM, RN — comptes 81, 83, 85). [texte officiel : le guide réutilise les mêmes libellés de postes RM/RN pour les charges financières et pour les charges HAO ; il s'agit de deux emplois distincts du même code de lettres dans le texte source, à ne pas fusionner]

**e) Résultat net de l'exercice.** Somme algébrique du résultat des activités ordinaires et du résultat HAO, diminuée de la participation des travailleurs (RQ — compte 87) et des impôts sur le résultat (RS — compte 89).

Ces soldes s'obtiennent soit comptablement, par virement successif des comptes de classes 6, 7, 8 dans les comptes 132 à 138, soit par simple calcul lors de l'établissement du compte de résultat (les comptes de gestion étant alors virés directement en 131 ou 139). Un solde intermédiaire négatif s'inscrit avec un signe − ; positif, avec un signe +.

**Tracé.** Plan comptable général OHADA, Titre IX chapitre 4.

## 4. Tableau des flux de trésorerie (TFT)

**Fonction** (art. 29). Retrace les entrées et sorties de liquidités de l'exercice, et fournit une lecture de la variation de trésorerie entre le 1er janvier et le 31 décembre.

Trois catégories de flux : activités opérationnelles, activités d'investissement, activités de financement.

**Principe de construction, en trois étapes.**

1. Déterminer la variation comptable des postes : pour le bilan, écart entre N et N-1 ; pour le compte de résultat, la charge ou le produit de l'exercice correspond directement à la variation.
2. En déduire les flux potentiels : variation comptable, corrigée des non-flux ou flux fictifs (tout ce qui n'a pas de caractère monétaire — amortissements, provisions, dépréciations).
3. En déduire les flux réels (encaissés/décaissés) : flux potentiels, corrigés de la variation des décalages de trésorerie (créances et dettes).

**Composantes du tableau** (art. 32) : trésorerie nette au début de l'exercice (ZA), flux des activités opérationnelles (FA à FE), flux des investissements (FF à FJ), flux des capitaux propres (FK à FN), flux des capitaux étrangers (FO à FQ), trésorerie nette en fin d'exercice (ZH).

**Principaux retraitements.**

*Trésorerie de début d'exercice.* Trésorerie-actif de N-1 (corrigée de la variation du compte 472, versements restant à effectuer sur titres de placement non libérés) moins trésorerie-passif de N-1.

*Flux des activités opérationnelles — cinq soldes.*
- Capacité d'autofinancement globale (CAFG) : EBE de l'exercice (poste XD), corrigé du solde des valeurs comptables des cessions courantes d'immobilisations (débit du 654) et diminué des produits de ces cessions (crédit du 754), plus le résultat financier (XF), plus les autres produits HAO (TO), moins les autres charges HAO (RP), moins la participation des travailleurs (RQ) et les impôts sur le résultat (RS). Calculée sur les produits et charges comptabilisés, pas sur les encaissements/décaissements réels : c'est une trésorerie potentielle, à corriger de la variation du besoin de financement pour obtenir un flux réel.
- Variation du besoin de financement lié aux activités opérationnelles : variation de l'actif circulant HAO (BA, hors créances liées aux immobilisations 485), des stocks et encours (BB), des créances et emplois assimilés (BG, à l'exclusion des créances liées aux immobilisations 414, des créances des apporteurs 467, des fonds à recevoir 458/4494, et du compte transitoire 4751), et du passif circulant (DP, à l'exclusion des dettes liées aux immobilisations 404/481/482, des dettes des apporteurs 467, du compte transitoire 4752, et des dettes sur titres 472) — après annulation, s'il y a lieu, de la correction liée à l'écart de conversion.

*Flux des activités d'investissement.* Seules les variations d'immobilisations ayant généré un flux de trésorerie y figurent.
- Acquisitions : somme de la variation des immobilisations nettes (AD, AI, AN) et des dotations aux amortissements/dépréciations et valeurs nettes de cession de l'exercice, diminuée du montant des réévaluations (comptes 106, 154), des provisions pour démantèlement, des acquisitions financées par une dette de location-acquisition (aucun décaissement), et des créances 2714 (contrat de location-vente chez le bailleur — la part remboursement de cette créance, elle, compte comme un remboursement d'immobilisation financière).
- Décaissement lié aux acquisitions : montant reconstitué ci-dessus, diminué de la dette fournisseurs d'investissements (comptes 481, 404) en cas d'achat partiellement à crédit ; diminué des avances déjà versées les exercices antérieurs (compte 25) en cas d'acquisition par avances/acomptes ; pour le paiement d'une dette antérieure, montant réellement décaissé sur l'exercice (comptes 481, 482, 404, hors virements internes dettes-en-compte vers effets à payer) ; pour un nouveau versement d'avance, montant versé sur l'exercice (compte 25).
- Encaissement lié aux cessions : crédit des comptes 82 ou 754 si comptant ; différence entre ce crédit et le débit des comptes 485/414 (créances sur cessions) si vente partiellement à crédit ; encaissement de la créance des exercices antérieurs via 485/414 sinon.

*Flux des capitaux propres.*
- Augmentation de capital par apport nouveau : variation des comptes de classe 10 (hors 106 écarts de réévaluation et 109 capital souscrit non appelé), du compte 467, du compte 4581.
- Subvention d'investissement : variation du compte 14 (hors quote-part virée au résultat), des comptes 4582 et 4494, plus les avances reçues.
- Prélèvement sur le capital : variation des comptes de classe 10 (mêmes exclusions que ci-dessus).
- Dividendes versés : mouvement débit du compte 465, à l'exclusion des mouvements ne traduisant pas un flux réel (paiement de dividendes en actions, par exemple).

*Flux des capitaux étrangers.* Variation des comptes 16 (hors intérêts courus) et 18. Les dettes de location-acquisition (compte 17) sont exclues à l'entrée, faute d'encaissement ; leur remboursement (débit du 17), lui, compte comme un remboursement de dette financière.

*Trésorerie de fin d'exercice.* Trésorerie-actif de N (corrigée du compte 472) moins trésorerie-passif de N.

**Tracé.** Plan comptable général OHADA, Titre IX chapitre 5.

## 5. Notes annexes

**Justification** (art. 29). Les Notes complètent et précisent l'information des trois autres états. Elles ont la même valeur que le Bilan, le Compte de résultat et le TFT — ce n'est pas un appendice.

**Contenu** (art. 33). Descriptions narratives, décompositions d'éléments déjà présentés ailleurs, informations sur des éléments qui ne répondent pas aux critères de comptabilisation propres aux trois autres états. Toute information déjà portée ailleurs dans les états financiers n'a pas à être répétée dans les Notes. Chaque élément des états de synthèse doit renvoyer, par référence croisée, à l'information qui lui correspond dans les Notes.

Les Notes doivent comporter une déclaration explicite de conformité au Plan Comptable OHADA. Les états financiers ne peuvent être déclarés conformes au SYSCOHADA que s'ils respectent l'intégralité des dispositions du Système comptable OHADA et de l'Acte uniforme — pas seulement certaines d'entre elles.

**Tracé.** Trente-six modèles de Notes, Plan comptable général OHADA, Titre IX chapitre 6. Les modèles non applicables à l'entité (cf. Fiche R4 de l'Application 127) ne sont pas joints ; leur contenu, en revanche, peut être enrichi par l'entité qui les utilise.

## Ce que ce fichier apporte au module

Avec ce fichier, la Partie 3 du Guide (« Présentation des états financiers annuels ») est couverte pour ses deux chapitres : la logique des masses et rubriques (ici) et l'exemple chiffré (Application 127, dans l'autre fichier de ce même dossier `references/`). La mise à jour correspondante du `SKILL.md` retire la mention « chapitre 1 non encodé ».

Ce fichier reste un résumé structuré de la logique de construction des états — il ne remplace pas `maquette.tsv` pour l'affectation compte par rubrique, ni les règles d'évaluation qui relèvent de l'AUDCIF proprement dit.
