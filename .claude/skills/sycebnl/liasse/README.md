# Montage des états financiers SYCEBNL — trois systèmes, trois moteurs

## Workflow impératif avant tout montage

Quand une balance est fournie, **ne jamais générer d'états sans avoir posé
deux questions** (sauf si la réponse est déjà explicite dans la demande) :

1. **Quel référentiel ?** SYCEBNL (entité à but non lucratif) ou SYSCOHADA
   (entité commerciale — skill `syscohada`). Les nomenclatures se
   ressemblent mais les jeux d'états sont entièrement distincts.
2. **Quel système / type d'entité ?** Le SYCEBNL en prévoit trois, chacun
   avec **ses propres états financiers et ses propres notes annexes** :
   - **Système normal — associations et ordres professionnels** (Partie 4,
     ch. 2) → `scripts/monter_etats_sycebnl.py` : Bilan, Compte de
     résultat, TFT, notes 1 à 35 ;
   - **Projets de développement et assimilés** (Partie 4, ch. 3) →
     `scripts/monter_projets.py` : Tableau emplois-ressources, Tableau
     d'exécution budgétaire, Tableau de réconciliation de trésorerie,
     Bilan, Compte d'exploitation, notes 1 à 24 ;
   - **Système minimal de trésorerie** (Partie 4, ch. 4 ; ressources
     annuelles ≤ 30 M FCFA, art. 5-6 de l'Acte uniforme) →
     `scripts/monter_smt_sycebnl.py` : Bilan GA→HZ, Compte de résultat
     KA→KZC, notes 1 à 5.

Ensuite seulement : analyser la balance, signaler les anomalies, générer le
jeu d'états du système retenu. Ne jamais appliquer la maquette d'un système
à un autre.

## Sources et vérification

Les trois jeux sont recoupés contre le **Journal officiel OHADA n° spécial
du 22 février 2023** (Partie 4, ch. 2, 3 et 4) :

- `references/correspondance-associations.tsv` — tableau officiel du ch. 2
  section 6, corrections documentées ligne à ligne (41 retiré de BE,
  qualificatifs de sens sur BE/DI, CJ numéroté 15, RH inclus dans XA,
  **compte 46 ajouté à BE/DI** — omis du tableau officiel alors que les
  notes 10 et 21 l'exigent) ;
- `references/correspondance-projets.tsv` — tableau officiel du ch. 3
  section 4, corrections documentées (présentation du bilan **en net**
  faute de colonne amortissements, exclusion 479 au lieu de 478 sur DH,
  DI servi par 499/599, ligne RC réintégrée au compte d'exploitation,
  dotations 68 ajoutées à TJ², doublons officiels TJ/TK signalés
  `[texte officiel]`) ;
- `references/correspondance-smt-sycebnl.tsv` — construction du moteur
  (le ch. 4 ne publie pas de table), chaque compte vérifié au plan
  (`../references/partie2-ch2-plan-comptes.md`).

Il n'existe pas de gabarit Excel officiel du SYCEBNL : les classeurs sont
**construits** par les moteurs, strictement sur les libellés et codes REF
officiels. `scripts/build_gabarit_sycebnl.py` régénère le gabarit vierge
des associations (`assets/gabarit-etats-associations.xlsx`).

## Ce que les moteurs produisent (v3)

```bash
# Associations et ordres professionnels (Système normal)
python3 monter_etats_sycebnl.py balance_N.xlsx [balance_N-1.xlsx] \
    --sortie etats.xlsx --entite "..." --identifiant "..." \
    --exercice "31/12/N" --duree 12

# Projets de développement et assimilés
python3 monter_projets.py balance_N.xlsx [balance_N-1.xlsx] --sortie etats.xlsx ...

# Système minimal de trésorerie
python3 monter_smt_sycebnl.py balance_N.xlsx [balance_N-1.xlsx] --sortie etats.xlsx ...
```

Chaque moteur produit **un classeur complet, une feuille par état** (bilan
actif et passif sur des feuilles séparées), avec page de **GARDE**, les
**notes annexes officielles du système** (une note par feuille, dans leur
présentation du Journal officiel), et les feuilles d'audit **BALANCE /
BALANCE_N1 / CONTROLES / ANOMALIES**.

**Traçabilité** : chaque poste des états et chaque ligne calculée des notes
porte une **formule Excel** (`SUMIF` sur BALANCE/BALANCE_N1) — l'origine de
tout chiffre se remonte au compte près, directement dans le classeur. La
feuille CONTROLES recoupe les totaux de notes avec leurs postes (écarts
« doit être 0 », en formules).

### Notes annexes

- **Associations** : les 45 feuilles de notes (1 à 35 avec subdivisions
  5A-5H, 17A/B, 18A/B, 29A/B) — couverture détaillée dans
  `references/notes-sycebnl.md` ;
- **Projets** : les 26 feuilles (1 à 24 avec 3A/3B et 20A/20B) —
  `references/notes-projets.md` ;
- **SMT** : les 5 notes — `references/notes-smt-sycebnl.md`.

Notes de soldes : entièrement en formules. Notes de mouvements (5A-5F, 30,
3A/3B et 22 des projets) : ouverture depuis N-1, clôture en formule, flux
posés en variation nette `MAX(0, N−(N-1))` — à ajuster depuis l'inventaire.
Notes déclaratives : gabarits pré-identifiés (en-tête rempli). Rappel de
l'Acte uniforme reproduit en GARDE : ne pas joindre les notes non
documentées, supprimer les lignes non chiffrées avant remise.

### TFT (associations) et tableaux propres aux projets

- **TFT** : ZA, ZC, ZD, ZE, ZF, ZG calculés en formules dès que la balance
  N-1 est fournie ; **ZB en résidu garanti par construction**
  (ZB = ZF − ZC − ZD − ZE) — le TFT boucle toujours avec la trésorerie du
  bilan (contrôle dans CONTROLES). Ses lignes FA à FH (ventilation par
  nature) se saisissent depuis le journal de trésorerie : une balance de
  clôture ne porte pas cette information.
- **Tableau emplois-ressources** : immobilisations (cumul = classe 2
  brute), charges de l'exercice (classe 6) et fonds reçus (variation des
  soldes 16x/46x + quote-part 702 consommée — approximation signalée sur
  la feuille) calculés ; cumuls de début de projet et ventilation des
  fonds disponibles à compléter.
- **Réconciliation de trésorerie** : lignes A, B, C, D, F et G en
  formules ; ligne de rappel « trésorerie balance » et écart à expliquer.
- **Exécution budgétaire** : budget/engagements à saisir (nomenclature du
  projet), réalisations, crédits disponibles et % en formules.

## Conventions

Mêmes règles de lecture des comptes que `syscohada/liasse` (préfixes 2/3/4,
englobement, clause « sauf », qualificatifs « soldes débiteurs/créditeurs »
jeton par jeton). Au compte de résultat, chaque poste est stocké **signé**
(net créditeur) : les totaux sont de simples additions, les charges
apparaissent en négatif. Classe 9 (contributions volontaires en nature) :
hors bilan et hors résultat par construction — reprise seulement dans la
NOTE 1 des associations, signalée en `INFO` ailleurs.

## Anomalies

Voir `references/anomalies.md` : balance déséquilibrée, comptes non
affectés ou non conformes, sens anormaux, double résultat… signalés avec
gravité et solution, jamais corrigés en silence.

## Après montage

Ouvrir le classeur dans Excel/LibreOffice pour recalculer les formules,
vérifier la feuille CONTROLES (écarts à zéro), compléter les notes
déclaratives, purger les notes non documentées avant remise.

## Exemples livrés

`exemples/` : balances synthétiques équilibrées (association N et N-1,
projet de développement N et N-1, SMT) et les classeurs produits
correspondants — à ouvrir pour voir la présentation attendue, ou à passer
aux moteurs pour vérifier l'installation.
