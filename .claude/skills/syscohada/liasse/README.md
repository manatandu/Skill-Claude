# Montage de la liasse SYSCOHADA — Système normal ET Système minimal de trésorerie

## Workflow impératif avant tout montage

Quand une balance est fournie, **ne jamais générer d'états sans avoir posé
deux questions** (sauf si la réponse est déjà explicite dans la demande) :

1. **Quel référentiel ?** SYSCOHADA (entités commerciales) ou SYCEBNL
   (entités à but non lucratif — skill `sycebnl`). Une balance d'EBNL ne se
   monte jamais avec ce module, malgré la ressemblance des numéros.
2. **Quel système ?** Pour le SYSCOHADA :
   - **Système normal** → `scripts/monter_liasse.py` (bilan, compte de
     résultat, TFT, notes 1 à 36) ;
   - **Système minimal de trésorerie (SMT)** → `scripts/monter_smt.py`
     (bilan SMT, compte de résultat SMT, notes 1 à 4 + journaux). Seuils
     d'assujettissement : CA HT ≤ 60 M FCFA (négoce), 40 M (artisanat),
     30 M (services) — AUDCIF art. 13, sauf option pour le Système normal.

Ensuite seulement : analyser la balance, signaler les anomalies, générer la
liasse du système retenu. Chaque système a **son propre jeu d'états et ses
propres notes annexes** — ne jamais servir les états de l'un à l'autre.

## Sources et vérification

- **Système normal** : correspondance compte → poste et liste des notes
  recoupées contre l'**AUDCIF, Titre IX, chapitres 6 et 7** (source
  officielle unique) ; gabarit officiel `assets/gabarit-liasse.xlsx`.
  Corrections documentées dans `references/correspondance.tsv` (colonne
  note) et `references/anomalies.md`.
- **SMT** : états et notes transcrits de l'**AUDCIF, Titre X, chapitres
  1 à 3** (voir le skill `audcif-acte-uniforme`,
  `references/titre-10-systeme-minimal-tresorerie.md`). Pas de table de
  correspondance officielle : celle du moteur
  (`references/correspondance-smt.tsv`) est une construction documentée,
  chaque compte vérifié au plan (`comptes/references/plan-comptes.tsv`).
- **TFT** : formules de `references/tft-formules-praticien.md` (recoupées
  AUDCIF Titre IX §598-620). v3 : correction d'une inversion de signe sur
  FB/FC/FD — les libellés du gabarit portent « − Variation … » et ZB est
  une somme simple, la cellule doit donc porter l'OPPOSÉ de la variation.
  Vérifié sur balance synthétique : ZB recoupe le calcul manuel.

## Ce que le moteur produit (v3)

### Système normal (`monter_liasse.py`)

```bash
python3 monter_liasse.py balance_N.xlsx [balance_N-1.xlsx] \
    --sortie liasse.xlsx --entite "..." --identifiant "..." \
    --exercice "31/12/N" --duree 12
```

Un classeur unique, une feuille par état :

- **GARDE** (page de garde), **FICHES R1-R4** (identification, gabarit) ;
- **ACTIF** et **PASSIF** (feuilles séparées), **Compte de Résultat**,
  **TFT** ;
- **NOTES 1 à 36** (toutes les feuilles du gabarit officiel) — les notes
  de soldes (4 à 30 hors déclaratives) sont **entièrement alimentées en
  formules** ; les notes de mouvements (3A, 3C, 3D, 28) reçoivent
  l'ouverture (balance N-1), la clôture (formule du gabarit) et les flux
  (colonnes de mouvement de la balance si présentes, sinon variation nette
  posée en formule `MAX(0, N−(N-1))`) ; la NOTE 34 (fiche de synthèse) est
  câblée en formules croisées vers les états ; les notes déclaratives
  (1, 2, 3B, 3E, 8A/3F, 13, 16B, 16C, 27B, 31, 32, 33, 35, 36) restent des
  gabarits à compléter, en-tête d'identification pré-rempli partout ;
- **BALANCE** (avec préfixes, mouvements et colonne « poste(s)
  d'affectation » pour l'audit), **BALANCE_N1**, **CONTROLES** (équilibres
  et une batterie de recoupements notes ↔ postes, tous en formules),
  **ANOMALIES**.

**Traçabilité** : chaque poste des états et chaque ligne calculée des notes
porte une **formule Excel** (`SUMIF` sur BALANCE/BALANCE_N1) — l'origine de
tout chiffre se remonte au compte près, directement dans le classeur.

Conditions du TFT : ZA et FB-FE exigent la balance N-1 ; FF-FQ exigent en
plus les colonnes de mouvement. À défaut, postes vides + anomalie INFO —
jamais un chiffre approximé en silence.

### Système minimal de trésorerie (`monter_smt.py`)

```bash
python3 monter_smt.py balance_N.xlsx [balance_N-1.xlsx] \
    --sortie etats-smt.xlsx --entite "..." --exercice "31/12/N"
```

Classeur dédié : GARDE, **BILAN ACTIF**, **BILAN PASSIF**, **COMPTE DE
RESULTAT** (G = C − D + E − F), **NOTES 1 à 4** + journaux de suivi,
BALANCE(_N1), CONTROLES, ANOMALIES. Détail dans
`references/notes-smt.md`. Pas de TFT au SMT (propre au Système normal).

## Conventions de lecture des comptes

Deux premiers chiffres = compte principal, troisième = sous-compte,
quatrième = divisionnaire : `24421000` se lit `24 / 244 / 2442`. Un jeton
de 2 chiffres englobe ses divisionnaires ; 3-4 chiffres valent pour
eux-mêmes et leurs subdivisions. Clause `sauf` = retranchement. Les
formules SUMIF générées appliquent la même convention (critère jocker
`"24*"` sur la colonne des comptes, jetons imbriqués dédoublonnés).


## Présentation : charte graphique « ETAFI »

Les classeurs produits reprennent la présentation d'une liasse fiscale
professionnelle réelle (logiciel ETAFI, dépôt DGI), portée par
`scripts/theme_etafi.py` :

- **cartouche d'identification** en tête de chaque page (numéro « - n - »,
  référence de page en haut à droite, dénomination sociale, adresse, sigle,
  NCC, exercice clos, durée, NTD) — options CLI `--adresse`, `--sigle`,
  `--ntd` en plus de `--entite`, `--identifiant`, `--exercice`, `--duree` ;
- **palette exacte du modèle** : en-têtes de colonnes `CCFFFF`, rubriques
  `FFFFCC`, totaux intermédiaires gris `C0C0C0`, totaux de section verts
  `008000` (texte blanc), TOTAL GENERAL bleu nuit `000080`, titres d'états
  en Arial Black vert, titres de notes en Arial Black `003366`, lignes
  clefs du TFT sur `003366` ; corps Arial 9, filets fins, format comptable
  `_-* #,##0 ...` (zéro affiché « - ») ;
- **pages du modèle** : `Couverture` (bandeau violet « LIASSE ... »),
  `Garde` (bandeau du référentiel, désignation de l'entité, documents
  déposés, zone réservée à l'administration), `Fiche 1` (identification à
  cases codes ZA...), `Fiche 2` (équipe/dirigeants), `CONTROLE BALANCE`
  (équilibre soldes et mouvements, verdicts « Equilibre / Déséquilibre »),
  `Bilan paysage` (actif et passif côte à côte, en liens vers les feuilles
  du bilan), fiche récapitulative `NOTES ANNEXES` et `TABLE COMMENTAIRE`
  (zone de commentaire libre par note) ;
- **ordre des feuilles du modèle** : BALANCE N, BALANCE N-1, CONTROLE
  BALANCE, Couverture, Garde, fiches, Bilan paysage, états, NOTES ANNEXES,
  notes, TABLE COMMENTAIRE, puis CONTROLES et ANOMALIES (audit interne).

## Feuilles de balance

`BALANCE N` et `BALANCE N-1` portent huit colonnes, comptes classés par
numéro croissant :

| A | B | C - D | E - F | G - H |
|---|---|---|---|---|
| Compte | Intitulé | Solde d'ouverture débit / crédit | Mouvement débit / crédit | Solde de clôture débit / crédit |

Un **TOTAL GENERAL** ferme la feuille (un total par solde, en débit et en
crédit) suivi d'une ligne de contrôle d'équilibre (débit - crédit, doit être
0) ; la feuille `CONTROLE BALANCE` reprend les trois blocs avec leur verdict.

Le solde d'ouverture ne porte que les **comptes de bilan (classes 1 à 5)**.
La comptabilité financière se scinde en comptes de bilan (classes 1 à 5) et
comptes de gestion (classes 6 à 8), la classe 9 étant réservée aux
engagements hors bilan et à la comptabilité analytique (AUDCIF art. 18 et
Titre VII, ch. 1 ; même partage au SYCEBNL, Partie 2, ch. 1). À la clôture,
le compte 13 est débité des charges « par le crédit des comptes de la classe
6 et des comptes débiteurs de la classe 8, **pour solde** » et crédité des
produits « par le débit des comptes de la classe 7 et des comptes créditeurs
de la classe 8, **pour solde** » : les comptes de gestion sont soldés et
n'ont donc aucun solde d'ouverture. Le bloc d'ouverture reprend uniquement
le **bilan d'ouverture**. Un solde d'ouverture porté par un compte de classe
6 à 9 dans le fichier source est ramené à zéro et signalé dans `ANOMALIES`.

Pour ces comptes de bilan, l'ouverture vient des colonnes du fichier fourni
quand elles existent (en-têtes reconnus : « solde initial », « à nouveau »,
« SI », « ouverture »…), sinon elle est reconstituée par *clôture -
mouvements* quand la balance porte ses mouvements. Sans l'une ni l'autre
source, la colonne reste à zéro : rien n'est inventé. Les formules des états
et des notes visent toujours les colonnes de clôture (G/H) et de mouvement
(E/F).

### Enchaînement des deux exercices

`BALANCE N-1` est une balance générale complète, pas un extrait de la balance
N : elle porte son propre solde d'ouverture, ses propres mouvements et sa
clôture, **comptes de gestion compris** — ce sont eux qui alimentent les
colonnes N-1 du compte de résultat et des notes. Les deux exercices
s'enchaînent ainsi :

1. à la clôture de N-1, les comptes de gestion sont soldés par le compte 13,
   qui porte alors le résultat de l'exercice ;
2. ce résultat figure au **bilan d'ouverture de N**, au compte 13 des
   capitaux propres — c'est la seule façon dont l'ouverture de N boucle ;
3. au cours de N, il est affecté par les organes compétents — réserves (11), report à nouveau (12),
   associés (465), et le compte
   13 est soldé.

Les balances d'exemple livrées suivent cet enchaînement de bout en bout : la
liasse se lit sur deux exercices réels, pas sur un exercice dupliqué.

Cas particulier du **Système normal** : les feuilles viennent du gabarit
officiel OHADA et gardent leurs noms (`ACTIF`, `PASSIF`, `Compte de
Résultat`, `TFT`, `NOTE x`, `FICHE R1` à `R4` qui tiennent lieu de Fiche 1
/ Fiche 2 / fiche récapitulative) ; le moteur les **repeint** aux couleurs
de la charte (`reskin_etafi`) sans toucher ni aux textes ni aux formules.
Le SMT, construit de toutes pièces, applique la charte nativement
(`Bilan-Actif`, `Bilan-Passif`, `Résultat`).


## Filigrane des notes non renseignées

Chaque feuille de note porte un filigrane (grand texte gris clair incliné,
sous le corps de la note) :

- **note chiffrable** : le filigrane est une **formule** qui n'affiche
  « NÉANT » que si la somme des colonnes de montants de la note est nulle.
  Il disparaît de lui-même au recalcul dès qu'un montant apparaît — pas
  d'entretien manuel ;
- **note déclarative** (aucune colonne de montant : informations
  obligatoires, événements postérieurs, changements de méthodes...) :
  mention fixe « NOTE À COMPLÉTER », à servir en texte avant remise.

Toutes les notes du référentiel restent présentes dans le classeur, y
compris vides : la fiche NOTES ANNEXES sert à cocher A / N/A, et l'Acte
uniforme demande de ne pas joindre à la remise les notes non documentées -
le filigrane indique lesquelles.
## Anomalies et numéros non conformes

Voir `references/anomalies.md`. Rien n'est corrigé en silence : balance
déséquilibrée (bloquant), comptes non affectés, non conformes, sens de
solde anormal, résultat logé à deux endroits… chaque anomalie sort avec
gravité et solution proposée. L'arbitrage final revient à l'humain.

## Après montage

Ouvrir le classeur dans Excel ou LibreOffice pour que les formules se
recalculent (ou convertir : `soffice --headless --convert-to xlsx`).
Vérifier la feuille CONTROLES : tous les écarts « doit être 0 » à zéro.
Purger les notes non documentées avant remise (l'OHADA impose de ne pas
joindre les notes vides).

## Frontière

Système normal et SMT **commerciaux** uniquement. Le SYCEBNL (associations,
projets de développement, SMT des EBNL) relève du skill `sycebnl` — autres
postes, autres comptes, autres notes.

## Exemples livrés

`exemples/` : balances synthétiques équilibrées (Système normal N et N-1,
variante à 6 colonnes avec mouvements, SMT) et les classeurs produits
correspondants — à ouvrir pour voir la présentation attendue, ou à passer
aux moteurs pour vérifier l'installation.
