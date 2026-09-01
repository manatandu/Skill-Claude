---
name: sycebnl
description: "Système comptable des entités à but non lucratif (SYCEBNL), Acte uniforme OHADA du 22 décembre 2022, applicable au 1er janvier 2024 (associations, ordres professionnels, fondations, projets de développement). Couvre le texte légal (art. 1-28), le cadre conceptuel, le glossaire, le plan des comptes intégral (9 classes) et le fonctionnement compte par compte, les opérations spécifiques (fonds propres, fonds affectés/reportés, dons, cotisations, mécénat) et les états financiers complets (associations, projets de développement, Système Minimal de Trésorerie) avec tableaux de correspondance postes/comptes. Inclut le Guide d'application officiel : 22 cas pratiques corrigés et entièrement chiffrés (écritures-types). `liasse/` : trois moteurs, un par système — associations/Système normal (Bilan, Compte de résultat, TFT + les 35 notes annexes officielles), projets de développement (tableau emplois-ressources, exécution budgétaire, réconciliation de trésorerie, bilan, compte d'exploitation + 24 notes) et SMT (bilan GA→HZ, compte de résultat KA→KZC + 5 notes) — classeurs Excel complets, chaque montant en formule traçable vers la balance. Devant une balance : demander d'abord le référentiel (SYCEBNL ou SYSCOHADA), puis le système/type d'entité, avant de générer. Nomenclature propre au SYCEBNL, distincte du SYSCOHADA."
---

# SYCEBNL — Système comptable des entités à but non lucratif (OHADA)

Ce module encode l'**Acte uniforme relatif au système comptable des entités à but non lucratif**, adopté à Niamey le 22 décembre 2022, publié au Journal Officiel OHADA (numéro spécial du 22 février 2023), **applicable à compter du 1er janvier 2024**.

Le SYCEBNL est un référentiel **distinct** du SYSCOHADA révisé (entités commerciales) et de l'AUDCIF classique. Il s'applique aux **entités à but non lucratif** : associations, ordres professionnels, fondations, fonds de dotation, organisations religieuses, et entités gérant des projets de développement financés par des bailleurs. Ne pas transposer les comptes ou les états financiers du SYSCOHADA à une EBNL : la nomenclature et les états sont propres au SYCEBNL.

## Devant une balance : le workflow en deux questions

Quand l'utilisateur fournit une balance générale et demande des états
financiers, **poser deux questions avant tout montage** (sauf réponse déjà
explicite dans la demande) :

1. **Quel référentiel ?** SYCEBNL (EBNL) ou SYSCOHADA (entité
   commerciale → skill `syscohada`).
2. **Quel système / type d'entité ?** Chaque système du SYCEBNL a **ses
   propres états financiers et ses propres notes annexes** :
   - **Associations et ordres professionnels, Système normal** →
     `liasse/scripts/monter_etats_sycebnl.py` (Bilan actif/passif sur
     feuilles séparées, Compte de résultat, TFT, notes 1 à 35) ;
   - **Projets de développement et assimilés** →
     `liasse/scripts/monter_projets.py` (tableau emplois-ressources,
     exécution budgétaire, réconciliation de trésorerie, bilan, compte
     d'exploitation, notes 1 à 24) ;
   - **Système minimal de trésorerie** (ressources ≤ 30 M FCFA, art. 5-6)
     → `liasse/scripts/monter_smt_sycebnl.py` (bilan GA→HZ, compte de
     résultat KA→KZC, notes 1 à 5).

C'est en fonction de ces deux réponses que la balance s'analyse et que le
bon jeu d'états se génère. Détail du processus dans `liasse/README.md`.

## Contenu encodé

| Fichier | Contenu |
|---|---|
| `references/liste-sigles.md` | Liste des sigles (B.F., B.F.E., B.F.G., EBNL, H.AO., R.A.O., R.H.A.O., SYSCOHADA, SYCEBNL, V.N.C.) |
| `references/acte-uniforme-articles-1-28.md` | **Texte légal** (art. 1 à 28) : champ d'application (art. 2), articles de l'AUDCIF exclus (art. 3), jeux d'états financiers par type d'entité (art. 4), Système normal vs SMT et seuils à 30 M FCFA (art. 5-6), contenu du bilan/compte de résultat/compte d'exploitation/TFT/tableau emplois-ressources/tableau d'exécution budgétaire/tableau de réconciliation de trésorerie (art. 7-13), livre d'inventaire (art. 14), Notes annexes (art. 15), règles de présentation (art. 16), registre des donateurs (art. 17-18), désignation et mission de l'auditeur — seuils 100/200 M FCFA et 20 personnes (art. 19-22), mise à jour du référentiel (art. 23), sanctions pénales (art. 24-27), entrée en vigueur (art. 28) |
| `references/partie1-ch1-definitions.md` | **Glossaire officiel** (Partie 1, ch. 1) : adhérents, association, bailleur de fonds, bénévole, commodat, consomptible, contribution (volontaire en nature), cotisations, déficit/excédent, denier du culte, dîme, donation, don manuel, dotation consomptible/non consomptible, droit d'entrée, EBNL, exercice, fondateurs, fondation, fonds affectés/d'administration/de dotation/dédiés/reportés, générosité, legs, mécénat, mutuelle, ordre professionnel, parrainage, potentiel de service, projet de développement (durable), subventions (équilibre/exploitation/investissement/versées), tiers financeurs, testateur, usagers, waqf, zakat |
| `references/partie1-ch2-cadre-conceptuel.md` | **Cadre conceptuel** (Partie 1, ch. 2) : utilisateurs et besoins d'information, champ d'application, objectif des états financiers, continuité d'exploitation, **5 postulats** (entité, comptabilité d'engagement, spécialisation des exercices, permanence des méthodes, prééminence de la réalité sur l'apparence — 4 applications) et traitement des changements de méthode/estimation/corrections d'erreurs, **5 conventions** (coût historique et réévaluation, prudence, régularité et sincérité, correspondance bilan clôture/ouverture, importance significative), caractéristiques qualitatives (pertinence, fidélité, comparabilité, vérifiabilité, rapidité, compréhensibilité), définitions actif/passif/passif externe/fonds propres/charges/produits, structure du jeu d'états financiers par type d'entité, règles d'évaluation (valeur d'entrée/actuelle/nette), de comptabilisation (cotisations, subventions, ressources affectées, promesses de financement) et de décomptabilisation |
| `references/partie2-ch1-cadre-comptable.md` | **Cadre comptable** (Partie 2, ch. 1) : structure en 9 classes (1-5 bilan, 6-8 gestion, 9 contributions volontaires en nature hors bilan/résultat), structure décimale, **tableau des comptes divisionnaires à deux chiffres, classe par classe** — nomenclature SYCEBNL propre, à ne pas confondre avec celle du SYSCOHADA. ⚠️ Contient une discordance sur la numérotation 16/17/18 de la Classe 1, signalée et non corrigée — voir `partie2-ch2-plan-comptes.md` |
| `references/partie2-ch2-plan-comptes.md` | **Structure du plan des comptes** (Partie 2, ch. 2) : codification et nomenclature (comptes à 2/3/4 chiffres), documents comptables obligatoires (livre-journal, grand-livre, balance, livre d'inventaire, registre des donateurs), et **plan des comptes détaillé** (numéros et intitulés jusqu'à 4-5 chiffres) des neuf classes |
| `references/partie2-ch3-classe1-comptes10-19.md` | **Fonctionnement compte par compte, Classe 1** (Partie 2, ch. 3, section 1) : comptes 10 à 19 — Dotation, Réserves, Report à nouveau, Résultat net, Subventions d'investissement, Provisions réglementées, Fonds affectés, Fonds reportés, Emprunts et dettes assimilées, Provisions pour risques et charges. Pour chaque compte : contenu, subdivisions, commentaires, fonctionnement débit/crédit, exclusions, éléments de contrôle |
| `references/partie2-ch3-classe2-comptes20-29.md` | **Fonctionnement compte par compte, Classe 2** (Partie 2, ch. 3, section 2) : comptes 20 à 29 — immobilisations destinées à la vente/usufruit temporaire, incorporelles, terrains, bâtiments, matériel/mobilier/actifs biologiques, avances sur immobilisations, titres de participation, autres immobilisations financières, amortissements, dépréciations. Même structure de fiche que la Classe 1, plus les règles générales de valeur d'entrée et de décomposition des immobilisations |
| `references/partie2-ch3-classe3-comptes31-39.md` | **Fonctionnement compte par compte, Classe 3 — Stocks** (Partie 2, ch. 3, section 3) : comptes 31 à 39 — biens liés à l'activité, marchandises/matières premières/fournitures liées, autres approvisionnements, dons en nature (courants et H.A.O.), produits finis et services en cours, produits finis/intermédiaires/résiduels, stocks en cours de route/consignation/dépôt, dépréciations des stocks. Plus les règles générales d'évaluation des stocks (coûts d'acquisition/transformation, C.M.P./P.E.P.S., valeur nette de réalisation) |
| `references/partie2-ch3-classe4-comptes40-49.md` | **Fonctionnement compte par compte, Classe 4 — Tiers** (Partie 2, ch. 3, section 4) : comptes 40 à 49 — fournisseurs et comptes rattachés, adhérents/clients-usagers et comptes rattachés, personnel, organismes sociaux, Etat et collectivités publiques, fondateurs/apporteurs et comptes courants, bailleurs et fonds d'administration, débiteurs et créditeurs divers, créances et dettes H.A.O., dépréciations et provisions pour risques à court terme (tiers) |
| `references/partie2-ch3-classe5-comptes50-59.md` | **Fonctionnement compte par compte, Classe 5 — Trésorerie** (Partie 2, ch. 3, section 5) : comptes 50 à 59 — titres de placement, valeurs à encaisser, banques, établissements financiers et assimilés, instruments de monnaie électronique, banques crédits de trésorerie et d'escompte, caisse, virements internes, dépréciations et provisions pour risques à court terme (trésorerie) |
| `references/partie2-ch3-classe6-comptes60-69.md` | **Fonctionnement compte par compte, Classe 6 — Charges des activités ordinaires** (Partie 2, ch. 3, section 6) : comptes 60 à 69 — achats (60), variations de stocks de biens achetés et reçus en dons (603), transports (61), services extérieurs et autres services extérieurs (62-63), impôts et taxes (64), autres charges et dons en nature reçus à distribuer (65), charges pour dépréciations et provisions à court terme d'exploitation (659), charges de personnel (66), frais financiers et charges assimilées (67), dotations aux amortissements (68), dotations aux provisions et aux dépréciations (69) |
| `references/partie2-ch3-classe7-comptes70-79.md` | **Fonctionnement compte par compte, Classe 7 — Produits des activités ordinaires** (Partie 2, ch. 3, section 7) : comptes 70 à 79 — revenus (70 : cotisations, générosité, ventes, manifestations), subventions d'exploitation (71), production immobilisée (72), variations des stocks de biens produits (73), autres produits (75), reprises de charges pour dépréciations et provisions à court terme d'exploitation (759), revenus financiers et produits assimilés (77), transferts de charges (78), reprises de provisions/dépréciations/subventions d'investissement (79) |
| `references/partie2-ch3-classe8-comptes80-89.md` | **Fonctionnement compte par compte, Classe 8 — Autres charges et autres produits (H.A.O.)** (Partie 2, ch. 3, section 8) : valeurs comptables et produits des cessions d'immobilisations (81, 82), charges H.A.O. (83), revenus H.A.O. (84), dotations H.A.O. (85), reprises H.A.O. (86), variations de stocks de dons en nature H.A.O. (87), subventions d'équilibre (88). ⚠️ Anomalie signalée inline sur la numérotation des sous-comptes 8311/8315 |
| `references/partie2-ch3-classe9-comptes90-99.md` | **Contributions volontaires en nature et comptabilité analytique, Classe 9** (Partie 2, ch. 3, section 9) : sous-section 1 — comptes spéciaux 900-904 (débit) / 910-914 (crédit) des contributions en travail, biens, services ; sous-section 2 — comptes 92 à 99 de la comptabilité analytique de gestion (libre usage) |
| `references/partie3-ch1-fonds-propres-associations.md` | **Partie 3, ch. 1 — Fonds propres des associations et ordres professionnels** : définition et contenu (dotation, réserves, report à nouveau, résultat net, subventions d'investissement, provisions réglementées, fonds affectés 17), écritures de souscription/libération des apports, droit d'entrée, réévaluation, affectation du résultat, subventions d'investissement, provisions réglementées |
| `references/partie3-ch2-fonds-affectes-reportes.md` | **Partie 3, ch. 2 — Fonds affectés et reportés** : fonds destinés à un projet spécifique (165), dons et legs d'immobilisations à conserver (167, 4861, 192), donations/legs non encore reçus d'immobilisations destinées à la vente (171, 172), donation temporaire d'usufruit (2011, 171, 280, 7961) |
| `references/partie3-ch3-fonds-propres-projets-developpement.md` | **Partie 3, ch. 3 — Fonds propres, projets de développement et assimilés** : décaissement des bailleurs (162-164, 462-464), engagement des dépenses par nature de charge et d'immobilisation, paiement, décomptabilisation ou reprise des immobilisations en fin de projet (cession, remise gratuite, restitution/vol/destruction) |
| `references/partie3-ch4-dons.md` | **Partie 3, ch. 4 — Dons** : dons en nature à distribuer (récurrents/non récurrents, stock de fin d'exercice), dons en nature à vendre (suivi extra-comptable), dons en numéraire (dons, legs, denier du culte, zakat, dîme, célébrations, mécénat, parrainage — compte 704), frais de recherche de fonds (636) |
| `references/partie3-ch5-cotisations-fondateurs.md` | **Partie 3, ch. 5 — Cotisations des membres et versement des fondateurs** : appel et recouvrement des cotisations (701, dépréciation des créances douteuses), contribution du fondateur pour une fondation (752), subventions et aides financières versées par les EBNL (652) |
| `references/partie3-ch6-autres-operations-specifiques.md` | **Partie 3, ch. 6 — Autres opérations spécifiques** : subventions d'exploitation sur plusieurs exercices (477), abandons de frais des bénévoles (4572, 7583, 846), convention de mécénat (4751, 7046), restitution de subvention non utilisée (4739), contributions volontaires en nature (classe 9), première année d'application du SYCEBNL |
| `references/partie4-ch1-principes-generaux.md` | **Partie 4, ch. 1 — Principes généraux des états financiers** : objectif et structure du jeu d'états financiers par type d'entité, cas des petites entités (Système minimal de trésorerie), règles générales de présentation, bilan, compte de résultat, tableau de flux de trésorerie (méthode directe, formules d'encaissements/décaissements), état des ressources et des emplois, notes annexes |
| `references/partie4-ch2-etats-associations.md` | **Partie 4, ch. 2 — Etats financiers des associations et ordres professionnels** : modèles vierges du bilan (actif/passif, codes REF AA→DZ), du compte de résultat (RA→XE), du tableau de flux de trésorerie (ZA→ZG, méthode directe), fiche récapitulative et **35 notes annexes** (Notes 1 à 35, dont 5A-5H immobilisations, 29B effectifs/masse salariale, 33 indicateurs financiers, 34 informations sociales/environnementales/sociétales, 35 exécution budgétaire), et les deux **tableaux de correspondance** postes/comptes (bilan et compte de résultat) |
| `references/partie4-ch3-etats-projets-developpement.md` | **Partie 4, ch. 3 — Etats financiers des projets de développement et assimilés** : tableau emplois-ressources (FA→GZ), tableau d'exécution budgétaire, tableau de réconciliation de trésorerie (A→I), bilan (AA→DZ), compte d'exploitation (RA→XC), fiche récapitulative et **24 notes annexes** (Notes 1 à 24, dont 3A-3B immobilisations, 9 fonds du bailleur, 20B effectifs), et les **tableaux de correspondance** bilan et compte d'exploitation. ⚠️ Doublon de codes REF « TJ » et « TK » dans le compte d'exploitation signalé `[texte officiel]` |
| `references/partie4-ch4-etats-smt.md` | **Partie 4, ch. 4 — Etats financiers du Système Minimal de Trésorerie** : bilan (GA→HZ), compte de résultat (KA→KZC, comptabilité de trésorerie avec retraitement variations stocks/créances/dettes et dotations aux amortissements), fiche récapitulative et **5 notes annexes** (tableau d'acquisition/suivi des immobilisations, état des stocks, état des créances et dettes non échues, journal unique de trésorerie, dotation) |
| `liasse/README.md` | **Trois moteurs de montage**, un par système : `monter_etats_sycebnl.py` (associations/Système normal — Bilan, Compte de résultat, TFT et **les 35 notes annexes officielles** construites dans leur présentation du Journal officiel), `monter_projets.py` (projets de développement — tableau emplois-ressources, exécution budgétaire, réconciliation de trésorerie, bilan, compte d'exploitation et les 24 notes) et `monter_smt_sycebnl.py` (SMT — bilan GA→HZ, compte de résultat KA→KZC et les 5 notes). Chaque moteur produit un classeur Excel professionnel complet (une feuille par état, bilan actif/passif séparés, page de garde, feuilles BALANCE/BALANCE_N1/CONTROLES/ANOMALIES) où **chaque montant est une formule traçable** (SUMIF) vers la balance. Maquettes de correspondance vérifiées et corrigées contre le Journal officiel (`correspondance-associations.tsv`, `correspondance-projets.tsv`, `correspondance-smt-sycebnl.tsv`), couverture des notes documentée (`notes-sycebnl.md`, `notes-projets.md`, `notes-smt-sycebnl.md`). Le TFT boucle avec la trésorerie du bilan (ZB en résidu) ; sa ventilation FA-FH reste à saisir depuis le journal de trésorerie |
| `references/note-circulaire-003-2013-enregistrement-asbl-eup.md` | Note circulaire n°003/CAB/MIN/PL.SMRM/COFAF/2013 du Ministère du Plan (24/01/2013) : liste des pièces requises pour l'**enregistrement d'une ASBL/EUP** et pour les demandes de **facilités administratives, fiscales et douanières** (arrêté interministériel ponctuel, prévisionnel, renouvellement). Cadre formel de constitution/reconnaissance d'une entité à but non lucratif en RDC, en amont de sa comptabilisation SYCEBNL |
| `references/guide-application-cas-pratiques.md` | **Guide d'application — 22 cas pratiques corrigés et chiffrés** (écritures-types) : ch. 1 fonds propres associations (dotation consomptible/non consomptible, droit d'adhésion, subventions d'investissement) ; ch. 2 fonds affectés/reportés (fonds projet spécifique, dons et legs d'immobilisations, legs destinés à la vente, usufruit temporaire) ; ch. 3 projet de développement (décaissement bailleur, fonds d'administration 462/702, fonds d'investissement 162/165, ajustements) ; ch. 4 dons (nature à distribuer, nature à vendre, numéraire et édifices religieux, frais de recherche de fonds) ; ch. 5 cotisations et fondateurs (appel/recouvrement, créances douteuses, contribution du fondateur, aides versées) ; ch. 6 autres opérations (subvention pluriannuelle, abandon de frais des bénévoles, mécénat, restitution de subvention, contributions volontaires en nature) ; ch. 7 tableaux de correspondance emplois-ressources et exécution budgétaire. Exemples entièrement chiffrés, complémentaires des schémas généraux de la Partie 3. ⚠️ Anomalies du guide signalées `[texte officiel]` (double numérotation de parties/chapitres, sous-titre erroné App. 1, compte d'amortissement 28444 au lieu de 28441 App. 5, écart 2 880 450 / 2 864 880 App. 20) |

## Périmètre encodé

L'ensemble du référentiel SYCEBNL est encodé : texte légal, cadre conceptuel, glossaire, plan et fonctionnement des comptes, opérations spécifiques, présentation des états financiers (Partie 4 complète, ch. 1 à 4). S'y ajoute désormais le **Guide d'application officiel** (`guide-application-cas-pratiques.md`), qui fournit les 22 cas pratiques corrigés et entièrement chiffrés (écritures-types). Les schémas généraux de la Partie 3 (avec `x`) donnent le mécanisme ; le guide donne l'exemple numérique. Pour passer ou vérifier une écriture d'EBNL, croiser les deux.

Les modèles d'états financiers ci-dessus sont des **gabarits officiels vierges** transcrits d'un Journal officiel scanné. Les rubriques, codes REF et numéros de comptes (multi-chiffres des tableaux de correspondance) sont fiables. En revanche, certains **renvois de Notes** (un seul caractère dans la source) apparaissent par endroits incohérents avec la fiche récapitulative, notamment dans les chapitres 3 et 4 : chaque fichier concerné porte un avertissement de transcription et un marqueur `[texte officiel]`. Se fier à la fiche récapitulative pour le titre exact de chaque note et vérifier les renvois sur le PDF officiel avant citation.

## Repères de recherche

Le fichier de l'Acte uniforme porte un en-tête `### Article N` par article :
```bash
grep -n '### Article 19' references/acte-uniforme-articles-1-28.md
```
Le glossaire porte un en-tête `### TERME` par entrée, en capitales :
```bash
grep -ni '### FONDS' references/partie1-ch1-definitions.md
```
Le cadre conceptuel se navigue par en-têtes `## Section` / numérotation `3.3.1.x` :
```bash
grep -n '^#### 3.3.1' references/partie1-ch2-cadre-conceptuel.md
```
Les fichiers de fonctionnement compte par compte portent un en-tête `## COMPTE N : Intitulé` par compte :
```bash
grep -n '^## COMPTE 41' references/partie2-ch3-classe4-comptes40-49.md
```
Les fichiers de la Partie 3 (opérations spécifiques) et de la Partie 4 ch. 1 se naviguent par `## Section N` puis sous-numérotation `### N.N` :
```bash
grep -n '^## Section' references/partie3-ch2-fonds-affectes-reportes.md
```
Les modèles d'états financiers (Partie 4, ch. 2 à 4) portent un en-tête `### NOTE N :` par note et `## Section N :` par état :
```bash
grep -n '^### NOTE' references/partie4-ch2-etats-associations.md
grep -n '^## Section' references/partie4-ch3-etats-projets-developpement.md
```
Le guide d'application se navigue par `## CHAPITRE N :` puis `### APPLICATION N —` :
```bash
grep -n '^### APPLICATION' references/guide-application-cas-pratiques.md
```
Les anomalies du texte officiel sont repérables directement :
```bash
grep -rn '\[texte officiel\]' references/
```

## Règle de transcription

Transcrire fidèlement le texte officiel ; ne jamais combler une lacune à partir de la mémoire ou du SYSCOHADA. Toute anomalie du texte source est signalée par un marqueur `[texte officiel]` inline, sans correction silencieuse. Ce skill ne peut être « déployé » ou « intégré » que par Manasse, manuellement, via Réglages → Compétences.
