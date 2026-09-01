---
name: syscohada
description: Référentiel SYSCOHADA révisé (Système normal ET Système minimal de trésorerie), quatre sous-dossiers pour quatre questions distinctes. `comptes/` : plan de comptes intégral (1403 comptes, classes 1-9) — quel numéro, quel intitulé. `ecritures/` : guide d'application, écritures-types et cas pratiques (App. 1-142) — quelle écriture passer. `etats-financiers/` : maquette bilan/compte de résultat, correspondance compte-rubrique, exemple chiffré complet — dans quelle ligne un compte se range. `liasse/` : moteurs qui transforment une balance générale en liasse OHADA complète — Système normal (bilan, compte de résultat, TFT, notes annexes 1 à 36 alimentées en formules Excel traçables) et SMT (bilan, compte de résultat, notes 1 à 4), chaque système avec son propre classeur. Devant une balance : demander d'abord le référentiel (SYSCOHADA ou SYCEBNL), puis le système (normal ou SMT), avant de générer. À utiliser pour tout numéro de compte SYSCOHADA/OHADA, toute écriture comptable, toute rubrique de bilan/CR, ou pour monter/contrôler une liasse depuis une balance. Renvoie à audcif-acte-uniforme pour les règles d'évaluation. Ne jamais citer un numéro de compte, une écriture ou une rubrique de mémoire.
---

# SYSCOHADA révisé — plan de comptes, écritures, états financiers, liasse

Quatre facettes du même référentiel, quatre sous-dossiers. Un numéro de compte, une écriture, une rubrique de bilan et un montage de liasse ne répondent pas à la même question — les confondre produit des réponses fausses avec assurance. Chaque sous-dossier a son README détaillé ; celui-ci sert seulement d'aiguillage.

## Devant une balance : le workflow en deux questions

Quand l'utilisateur fournit une balance générale et demande des états
financiers, **poser deux questions avant tout montage** (sauf réponse déjà
explicite dans la demande) :

1. **Quel référentiel ?**
   - **SYSCOHADA** (entité commerciale) → ce skill ;
   - **SYCEBNL** (association, ordre professionnel, fondation, projet de
     développement) → skill `sycebnl`, jeux d'états entièrement distincts.
2. **Quel système ?** (pour le SYSCOHADA)
   - **Système normal** → `liasse/scripts/monter_liasse.py` — bilan
     (actif/passif sur feuilles séparées), compte de résultat, TFT et
     notes annexes 1 à 36 dans un classeur unique ;
   - **Système minimal de trésorerie (SMT)** → `liasse/scripts/monter_smt.py`
     — bilan SMT, compte de résultat SMT, notes 1 à 4 + journaux.
     Seuils AUDCIF art. 13 : CA HT ≤ 60 M FCFA (négoce), 40 M (artisanat),
     30 M (services).

C'est en fonction de ces deux réponses que la balance s'analyse et que le
bon jeu d'états (avec ses notes annexes propres) se génère. Détail du
processus dans `liasse/README.md`.

## Quelle question, quel dossier

| Question | Dossier |
|---|---|
| Quel **numéro / intitulé** de compte ? | `comptes/` |
| Quelle **écriture** passer pour cette opération ? | `ecritures/` |
| Dans quelle **rubrique** du bilan / compte de résultat ? | `etats-financiers/` |
| Monter une **liasse** depuis une balance générale ? | `liasse/` (SN ou SMT) |
| Quel **article** ou critère d'évaluation ? | skill `audcif-acte-uniforme` (hors de ce module) |
| Retraiter le bilan, **diagnostiquer** FR / BFR / trésorerie, ratios ? | skill `analyse-financiere-diagnostic-rdc` (hors de ce module) |

## `comptes/`

Plan de comptes intégral, `comptes/references/plan-comptes.tsv` (1403 lignes) et `comptes/references/regles-et-notes.md` (codification, notes officielles). Se consulte par `grep`, jamais de mémoire — les numéros SYSCOHADA ressemblent trop à ceux du PCG français pour être devinés sans risque. Détail complet dans `comptes/README.md`.

## `ecritures/`

Guide d'application : écritures-types et cas pratiques numérotés (App. 1 à 142), répartis en Partie 1 (opérations courantes), Partie 2 (opérations spécifiques : location, provisions, devises, fusions...) et Partie 4 (comptes consolidés/combinés). Présentation systématique en tableau à 5 colonnes (Débit | Crédit | Date et libellé | Montant débit | Montant crédit). Table des matières complète et règles d'usage dans `ecritures/README.md`.

## `etats-financiers/`

Maquette bilan/compte de résultat : correspondance entre les codes de rubrique (AJ, BQ, XC...) et les comptes qui les alimentent, avec les conventions d'englobement. Distingue explicitement ce qui est vérifié (affectation des comptes) de ce qui ne l'est pas (les codes de rubrique eux-mêmes, transcrits et non lus dans l'annexe officielle). Inclut un exemple chiffré complet (Application 127) et un script de contrôle de partition. Détail dans `etats-financiers/README.md`.

## `liasse/`

Deux moteurs, un par système, chacun produisant un classeur professionnel
complet (une feuille par état, bilan actif et passif séparés, notes
annexes, page de garde, feuilles d'audit BALANCE/CONTROLES/ANOMALIES) :

- **Système normal** (`liasse/scripts/monter_liasse.py`) : gabarit officiel
  OHADA (`liasse/assets/gabarit-liasse.xlsx`), notes 1 à 36 alimentées.
- **SMT** (`liasse/scripts/monter_smt.py`) : AUDCIF Titre X, classeur
  construit, notes 1 à 4 + journaux de suivi.

Tous les montants sont écrits en **formules Excel** (`SUMIF` sur la feuille
BALANCE injectée) : chaque chiffre de la liasse est retraçable jusqu'aux
comptes de la balance. Les anomalies de balance sont détectées et signalées
plutôt que corrigées en silence. Détail dans `liasse/README.md`.

## Frontière commune

Aucun des quatre sous-dossiers ne dit *pourquoi* une opération se traite ainsi : les critères d'évaluation, de qualification (location simple vs acquisition, par exemple) relèvent du skill `audcif-acte-uniforme`. Ce skill dit le *comment* (compte, écriture, rubrique, liasse), pas le *pourquoi*.

Frontière aval : ce skill s'arrête aux **états financiers produits**. Dès qu'il s'agit de les retraiter pour l'analyse (passage du bilan comptable au bilan financier, déflation en francs constants, fonds de roulement, besoin de financement, trésorerie nette, ratios de liquidité, de solvabilité et d'endettement, effet de levier), le relais est pris par `analyse-financiere-diagnostic-rdc`, qui porte la doctrine CPCC appliquée en RDC.
