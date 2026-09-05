# Où se trouve le guide sectoriel, et dans quel état il est

Relevé le 5 septembre 2026. Les URL viennent de résultats de recherche ; l'accès direct à
`ifrs.org` était bloqué depuis la session qui a produit ce fichier. Rien n'a donc été ouvert.
Vérifier au premier téléchargement, et corriger ce fichier si une adresse a bougé.

## 1. Le guide complet, en un seul PDF

```
https://www.ifrs.org/content/dam/ifrs/publications/pdf-standards-issb/english/2023/issued/part-b/ifrs-s2-ibg.pdf?bypass=on
```

C'est le fichier qui porte les 68 volumes. Le suffixe `?bypass=on` compte : sans lui, la Fondation
IFRS renvoie vers la page d'inscription. C'est la réponse à la question « quel est le vrai lien ».

## 2. Un volume à la fois

Le schéma d'URL est régulier :

```
https://www.ifrs.org/content/dam/ifrs/publications/pdf-standards-issb/english/2023/issued/part-b/ifrs-s2-ibg-volume-<N>-<nom-en-minuscules-avec-tirets>-part-b.pdf?bypass=on
```

Quatre adresses relevées telles quelles, donc sûres quant à la forme :

| Volume | Industrie | Fin d'URL |
| --- | --- | --- |
| 7 | Coal Operations | `ifrs-s2-ibg-volume-7-coal-operations-part-b.pdf` |
| 10 | Metals & Mining | `ifrs-s2-ibg-volume-10-metals-and-mining-part-b.pdf` |
| 11 | Oil & Gas, Exploration & Production | `ifrs-s2-ibg-volume-11-oil-and-gas-exploration-and-production-part-b.pdf` |
| 61 | Airlines | `ifrs-s2-ibg-volume-61-airlines-part-b.pdf` |

Noter la règle de nommage : l'esperluette devient `and`, la virgule disparaît, les espaces
deviennent des tirets.

Numérotation du secteur *Extractives & Minerals Processing*, à vérifier avant usage (elle vient
d'une synthèse de recherche, pas d'une page ouverte) : 7 Coal Operations, 8 Construction Materials,
9 Iron & Steel Producers, 10 Metals & Mining, 11 à 14 les quatre volumes Oil & Gas (Exploration &
Production, Midstream, Refining & Marketing, Services).

Pour le contexte congolais, le volume 10 est le premier à encoder. Le 7 et les 11 à 14 ensuite.

## 3. Savoir dans quel volume on tombe

Liste officielle des industries SICS, mise à jour du 10 octobre 2025 :

```
https://www.ifrs.org/content/dam/ifrs/sasb/general/sics-industry-list-10102025.pdf
```

Note de fond de l'ISSB sur l'origine et la maintenance du SICS (mai 2024) :

```
https://www.ifrs.org/content/dam/ifrs/meetings/2024/may/issb/ap6a-sics-background.pdf
```

Une entité intégrée horizontalement ou verticalement applique plusieurs volumes (IB9).

## 4. Autour du guide

| Document | Adresse |
| --- | --- |
| Documentation d'accompagnement d'IFRS S2, partie B, juin 2023 (déjà encodée dans `issb-durabilite`) | `.../part-b/issb-2023-b-ifrs-s2-climate-related-disclosures-accompanying-guidance-part-b.pdf?bypass=on` |
| Matériel pédagogique « Using ISSB Industry-based Guidance when applying ISSB Standards », juillet 2025 | `https://www.ifrs.org/content/dam/ifrs/supporting-implementation/issb-standards/issb-industry-based-guidance-applying-issb-standards.pdf` |
| Orientations ESRS-ISSB sur l'interopérabilité, version anglaise | `https://www.ifrs.org/content/dam/ifrs/supporting-implementation/issb-standards/esrs-issb-standards-interoperability-guidance.pdf` |
| Guide sectoriel TPT Metals & Mining, avril 2024 (plans de transition, hors ISSB) | `https://www.ifrs.org/content/dam/ifrs/knowledge-hub/resources/tpt/metals-mining-sector-guidance-apr-2024.pdf` |

## 5. Ce qui a bougé depuis juin 2023

Le texte encodé dans `issb-durabilite` est celui de juin 2023. Il n'est plus à jour sur un point.

**Amendements à IFRS S2, 11 décembre 2025.** Amendements ciblés sur les émissions de gaz à effet de
serre, en réponse aux difficultés d'application signalées. Quatre assouplissements :

1. l'entité peut limiter la mesure et la publication des émissions de scope 3 catégorie 15 aux
   émissions financées au sens d'IFRS S2 ;
2. elle peut utiliser un système de classification autre que le GICS pour ventiler ces émissions
   financées ;
3. clarification de la dispense juridictionnelle d'utiliser le GHG Protocol quand une partie
   seulement de l'entité est soumise à une autre méthode ;
4. nouvelle dispense juridictionnelle sur les potentiels de réchauffement global du dernier rapport
   d'évaluation du GIEC.

Entrée en vigueur : exercices ouverts à compter du 1er janvier 2027, application anticipée permise.

```
https://www.ifrs.org/content/dam/ifrs/publications/amendments/english/2025/issb-2025-1-amendments-ifrs-s2.pdf
https://www.ifrs.org/projects/completed-projects/2025/amendments-to-disclosure-of-greenhouse-gas-emissions-s2/
```

**Le guide sectoriel lui-même est en révision.** Deux exposés-sondages successifs, dans le cadre du
projet d'amélioration des normes SASB :

- juillet 2025, neuf normes SASB et le guide sectoriel, commentaires clos le 30 novembre 2025 ;
- 26 mars 2026, trois normes SASB de plus et le guide sectoriel, en cours de redélibération à la
  date de ce relevé.

```
https://www.ifrs.org/projects/work-plan/amendments-to-the-ifrs-s2-industry-based-guidance/
https://www.ifrs.org/content/dam/ifrs/project/enhancing-sasb-standards-cont/sasb-ifrs-s2-ibg-ed-2026-1-proposed-amends.pdf
https://www.ifrs.org/content/dam/ifrs/project/enhancing-the-sasb-standards/sasb-ed-2025-1-bc-proposed-amends.pdf
```

Conséquence pour l'encodage : le texte de juin 2023 reste le texte en vigueur, donc c'est lui qu'on
encode. Mais toute réponse sur une métrique sectorielle doit signaler qu'un projet d'amendement est
ouvert. Ne pas encoder un exposé-sondage comme s'il était en vigueur.

## 6. La base des conclusions

Toujours absente de `issb-durabilite`. Elle est diffusée dans la partie C des publications ISSB. Ne
pas reconstruire l'intention du normalisateur sans elle.
