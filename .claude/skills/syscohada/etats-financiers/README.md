# États financiers SYSCOHADA révisé — Système normal

Ce module donne la correspondance entre les rubriques du bilan et du compte de résultat et les comptes qui les alimentent. Il travaille avec le module `syscohada-comptes`, qui détient le plan de comptes : les deux se lisent ensemble.

## Ce qui est garanti, et ce qui ne l'est pas

Cette distinction commande tout usage du module.

**Vérifié.** Chaque compte cité dans `references/maquette.tsv` existe au plan de comptes. Aucun compte des classes 1 à 8 n'échappe à une rubrique. Aucun compte n'est capté deux fois. Les formules de totalisation sont cohérentes entre elles et avec les codes qu'elles appellent. Les soldes intermédiaires renvoient aux comptes 132 à 138 conformément au plan.

**Non vérifié.** Les codes de rubrique eux-mêmes — que « Terrains » porte le code AJ, que « Titres de placement » porte BQ. Ils proviennent d'une transcription, non de l'annexe officielle de l'AUDCIF. Cette transcription comportait un décalage d'une cellule sur les soldes intermédiaires ; rien ne prouve qu'elle n'ait pas glissé ailleurs.

Conséquence pratique : employer les affectations de comptes sans réserve, mais signaler la réserve chaque fois qu'un **code de rubrique** est cité dans un travail destiné à être publié, remis ou opposé à un tiers. Pour un usage interne, la maquette est utilisable telle quelle.

**Deux inférences signalées.** Le renvoi immeubles de placement de AJ (`2281 - 2928p`) et les comptes `585, 588` en BS sont déduits de la structure du plan, non lus dans un texte. Ils portent la mention `[inféré]`.

**Hors périmètre.** Le Système minimal de trésorerie n'est pas couvert. La colonne exercice N-1, obligatoire, ne figure pas dans la maquette elle-même (elle figure en revanche dans l'exemple chiffré de `references/app-127-modele-jeu-complet-etats-financiers.md`). Le TFT et les notes annexes sont couverts pour leur structure, leurs codes de rubrique et la logique de leurs retraitements (chapitre 1) — mais pas pour le détail des règles d'évaluation sous-jacentes, qui relèvent de l'AUDCIF proprement dit.

## Conventions de lecture

Elles ne sont pas décoratives : sans elles, la maquette est ambiguë et tout contrôle de couverture produit des centaines de faux positifs.

Un numéro à **deux chiffres** désigne le compte principal et englobe l'intégralité de ses divisionnaires et sous-comptes. `24` en AM couvre 241 à 249 et toutes leurs subdivisions.

La mention **`sauf XXX`** retranche les comptes cités, qui sont alors captés ailleurs. `24 (sauf 245, 2495)` en AM implique que 245 et 2495 figurent en AN.

Un numéro à **trois ou quatre chiffres** ne vaut que pour lui-même et ses subdivisions propres.

Le suffixe **`p`** signale une reprise partielle : seule la fraction du compte se rapportant à la rubrique y est portée. `2949p` figure en AM et en AN, chacune n'en prenant que sa part.

La colonne **`comptes_amort_deprec`** agrège amortissements (28x) et dépréciations (29x, 39, 49x, 59x) du poste. Le bilan actif se lit en trois colonnes : brut, amortissements et dépréciations, net.

## Consulter la maquette

`references/maquette.tsv` — 99 lignes, colonnes `etat`, `ref`, `rubrique`, `comptes_brut`, `comptes_amort_deprec`, `formule`, `note`.

```bash
grep -P '^BILAN-ACTIF\tAJ\t' references/maquette.tsv       # une rubrique
grep -P '^COMPTE-DE-RESULTAT' references/maquette.tsv      # un état entier
grep -i 'location acquisition' references/maquette.tsv     # par libellé
```

Trouver la rubrique d'un compte demande de tenir compte de l'englobement : le compte 2453 n'apparaît nulle part littéralement, il est capté par le `24` de AM. Chercher du plus précis au plus général — le sous-compte, puis le divisionnaire, puis le compte principal — et vérifier à chaque niveau qu'aucune clause `sauf` ne l'exclut.

```bash
for p in 2453 245 24; do grep -nP "\b$p\b" references/maquette.tsv; done
```

## Logique des postes et des masses — chapitre 1

`references/chapitre-1-logique-postes-masses.md` couvre le chapitre 1 de la Partie 3 (« Présentation des états financiers annuels ») : pourquoi les postes sont lettrés plutôt que numérotés, comment ils se regroupent en rubriques puis en masses, et surtout les aménagements qui écartent le Bilan, le Compte de résultat et le TFT d'une simple sommation comptable — sens des amortissements/dépréciations à l'actif, place du report à nouveau, décalage des écarts de conversion en pied de bilan, cascade des soldes intermédiaires de gestion, construction du TFT en trois étapes (variation comptable → flux potentiel → flux réel) avec le détail des retraitements par catégorie de flux. À consulter avant d'expliquer *pourquoi* une rubrique se calcule ainsi, ou pour justifier une formule du TFT (CAFG, variation du BFE) devant un tiers.

## Exemple travaillé complet — Application 127

`references/app-127-modele-jeu-complet-etats-financiers.md` reproduit un jeu complet d'états financiers rempli pour une entité fictive (Guide d'application SYSCOHADA, Partie 3, chapitre 2) : page de garde, fiches R1 à R4, bilan et compte de résultat chiffrés avec leurs codes de rubrique, tableau des flux de trésorerie, et une table de correspondance des 36 notes annexes avec leur contenu type. Utile pour vérifier qu'un code de rubrique cité dans `maquette.tsv` correspond bien à un usage réel, pour la structure de la Note 34 (fiche de synthèse des indicateurs financiers, avec les formules de fonds de roulement/BFE/BFHAO/trésorerie nette), et pour la Note 36 (tables de codes forme juridique / régime fiscal / pays / activités, utilisées en Fiche R2).

Les deux chapitres de la Partie 3 sont désormais couverts : la logique (chapitre 1, ci-dessus) et l'exemple chiffré (chapitre 2, ce fichier).

## Frontières du module

La maquette dit **dans quelle ligne un solde se range**. Elle ne dit pas :

- comment ce solde a été obtenu — l'évaluation relève de l'AUDCIF ;
- si le solde d'un compte de tiers est débiteur ou créditeur — plusieurs rubriques (BJ, DK, DM, BS, DR) sont conditionnées par le sens du solde, qui se lit dans la balance, pas dans la maquette ;
- ce que contiennent les notes annexes, alors qu'elles font partie intégrante des états financiers.

Quand la question porte sur l'un de ces terrains, répondre sur la rubrique et signaler la limite plutôt que d'extrapoler.

## Contrôle de partition

`scripts/controle_partition.py` rejoue les vérifications qui ont validé cette maquette : existence de chaque compte cité, couverture intégrale des classes 1 à 8, absence de double captation. Le lancer après toute modification de `maquette.tsv`, et avant de tenir un résultat pour fiable.

```bash
python scripts/controle_partition.py
```

Ce contrôle a une propriété qui justifie son existence : une rubrique qui oublie un compte, ou qui en capte un deux fois, ne déséquilibre pas le bilan. L'actif reste égal au passif. Seul ce test le voit.
