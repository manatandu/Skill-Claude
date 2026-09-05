---
name: ifrs-s2-guide-sectoriel
description: >
  Chantier d'encodage du guide sectoriel d'IFRS S2 (Industry-based Guidance on Implementing
  IFRS S2, juin 2023, 68 volumes, 11 secteurs SICS, dérivé des normes SASB). Contient les liens
  officiels de téléchargement volume par volume, l'état des amendements en cours, le protocole
  d'extraction des tableaux chiffrés d'un PDF (script testé, tableau Markdown plus capture PNG,
  contrôle des totaux) et une bibliographie de doctrine et de travaux empiriques prêts à encoder.
  Le texte du guide sectoriel lui-même n'est pas ici. À utiliser avant d'encoder un volume
  sectoriel, ou pour répondre à une question sur les métriques sectorielles d'IFRS S2. Complète
  la skill issb-durabilite, qui porte IFRS S1, IFRS S2 et leur documentation d'accompagnement.
---

# Guide sectoriel d'IFRS S2, chantier d'encodage

Cette skill ne contient pas le guide sectoriel. Elle contient de quoi l'encoder correctement,
et de quoi répondre honnêtement en attendant.

## Ce qu'est le guide sectoriel

L'*Industry-based Guidance on Implementing IFRS S2*, publiée en juin 2023 avec la norme. Elle est
organisée en 68 volumes, un par industrie, répartis en 11 secteurs du Sustainable Industry
Classification System (SICS). Elle est dérivée des normes SASB, que l'ISSB maintient depuis 2022.

Chaque volume donne, pour une industrie : la description de l'industrie, les sujets de publication
(disclosure topics), les métriques associées, les protocoles techniques et les métriques d'activité.
Voir les paragraphes IB1 à IB14 de la documentation d'accompagnement, encodés dans
`issb-durabilite/references/ifrs-s2/02-ifrs-s2-accompanying-guidance-en.md`.

## Pourquoi on ne peut pas s'en passer

Le guide accompagne la norme sans en faire partie. Mais l'obligation de s'y reporter, elle, est dans
la norme. Quatre paragraphes d'IFRS S2 l'imposent, et non un seul :

- §12, pour identifier les risques et opportunités climatiques sectoriels ;
- §23, pour préparer les informations des §13 à §22 ;
- §32, pour publier les métriques sectorielles ;
- §37, pour les métriques de suivi des cibles.

S'ajoute IFRS S1 §59(b) : l'entité indique quel ou quels volumes elle a appliqués.

Conséquence pratique. Devant une question sur un secteur précis (mines, pétrole, banque, transport),
ne pas raisonner par analogie à partir des exemples génériques d'IFRS S2. Dire que le volume n'est pas
encodé, donner son lien, et s'arrêter là. Un code de métrique SASB (`EM-MM-110a.1`, `TR-AU-410a.2`)
ne s'invente jamais.

## Les fichiers de références

- `references/01-sources-officielles.md` : où télécharger le guide complet et chaque volume, le
  schéma d'URL, les volumes utiles au contexte congolais, et l'état des amendements (décembre 2025
  pour IFRS S2, exposé-sondage de mars 2026 pour le guide sectoriel lui-même).
- `references/02-protocole-tableaux.md` : comment encoder les tableaux chiffrés sans les dégrader,
  avec le script `scripts/pdf-tableaux.py` et sa démonstration.
- `references/03-litterature-doctrine.md`, `04-litterature-empirique.md` et
  `05-litterature-afrique-extractif.md` : ce qui vaut la peine d'être encodé, et pourquoi. Chaque
  entrée porte son statut de lecture, `abstract lu` ou `référence relevée`.
- `references/06-versions-linguistiques.md` : quand on garde une version française et quand on la
  supprime au profit de l'anglais.

## Réserve à ne pas oublier

Aucun contenu du guide sectoriel n'est reproduit ici. Les liens ont été relevés dans des résultats de
recherche, pas ouverts : l'accès direct à `ifrs.org` était bloqué depuis la session qui a construit
cette skill. Vérifier chaque URL au premier téléchargement.
