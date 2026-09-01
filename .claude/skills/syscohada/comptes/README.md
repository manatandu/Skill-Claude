# Plan de comptes SYSCOHADA révisé

Ce module contient le référentiel de codification. Il ne contient pas de règles d'évaluation ni de traitement comptable : il dit **quel compte existe et comment il s'appelle**, pas **quand le débiter**.

## Pourquoi vérifier plutôt que réciter

Les numéros de comptes SYSCOHADA sont très proches de ceux du PCG français et des anciens plans nationaux. La ressemblance rend l'erreur facile et invisible : un 613 français n'est pas un 613 SYSCOHADA. La révision de 2017 a par ailleurs déplacé ou créé des comptes (notamment toute la logique de *location acquisition* : 17, 623, 672, 775). Un numéro cité de mémoire a donc une probabilité réelle d'être faux tout en paraissant plausible.

Règle : **tout numéro de compte SYSCOHADA figurant dans une réponse doit avoir été lu dans `references/plan-comptes.tsv` pendant la conversation en cours.**

## Consulter le référentiel

`references/plan-comptes.tsv` — 1403 lignes, colonnes `compte`, `libelle`, `classe`. Ne pas le charger en entier : interroger par `grep`.

Chercher par numéro (préfixe) :
```bash
grep -P '^62' references/plan-comptes.tsv          # tout le poste 62
grep -P '^6232\t' references/plan-comptes.tsv      # un compte précis
```

Chercher par libellé :
```bash
grep -i 'location acquisition' references/plan-comptes.tsv
grep -i 'congés' references/plan-comptes.tsv
```

Les libellés sont accentués et encodés en UTF-8. En mode `-P`, le métacaractère `.` matche un **octet**, pas un caractère : `grep -iP 'cong.s'` ne trouve rien alors que le compte 6613 existe. Deux options sûres — taper l'accent directement, ou activer le mode Unicode :
```bash
grep -iP '(*UTF8)d.pr.ciation.*stock' references/plan-comptes.tsv
```

Vérifier qu'un compte existe avant de l'employer :
```bash
grep -cP '^6234\t' references/plan-comptes.tsv     # 0 = le compte n'existe pas
```

Si un compte cherché ne ressort pas : le dire explicitement. Ne pas proposer le voisin le plus proche comme s'il s'agissait du compte demandé, et ne pas inventer un sous-compte à quatre chiffres qui « devrait » exister. Le plan autorise l'entité à créer des sous-comptes (voir notes [3] et [6] dans `references/regles-et-notes.md`) — le préciser plutôt que le faire silencieusement.

## Structure

Neuf classes. Un numéro compte au maximum quatre chiffres, et la longueur porte un sens : deux chiffres = compte principal (10), trois = compte divisionnaire (101), quatre = sous-compte (1011). Le premier chiffre donne la classe.

| Classe | Contenu |
|---|---|
| 1 | Ressources durables |
| 2 | Actif immobilisé |
| 3 | Stocks |
| 4 | Tiers |
| 5 | Trésorerie |
| 6 | Charges des activités ordinaires |
| 7 | Produits des activités ordinaires |
| 8 | Autres charges et autres produits (dont HAO et impôt sur le résultat) |
| 9 | Engagements hors bilan et comptabilité analytique de gestion |

Les règles de codification (rôle des terminaisons 9, 8, 3 et 0) et les dix notes officielles annexées au plan sont dans `references/regles-et-notes.md`. Les lire avant d'expliquer pourquoi un compte porte tel numéro, ou avant de justifier la création d'un sous-compte.

## Frontières du module

Ce module ne dit rien de :

- **l'évaluation et la comptabilisation** — un contrat de location acquisition mobilise les comptes 17, 2416, 623, 672, mais savoir s'il *est* une location acquisition relève des critères de l'AUDCIF, pas du plan de comptes ;
- **la présentation des états financiers** — les postes du bilan et du compte de résultat ne se déduisent pas mécaniquement des numéros ;
- **la fiscalité** — le compte 441 accueille l'impôt sur les bénéfices, son assiette et son taux relèvent du droit national ;
- **les autres référentiels** — SYCEBNL, IFRS, plans sectoriels (bancaire, assurance, microfinance) ont leurs propres nomenclatures.

Quand la question déborde sur l'un de ces terrains, répondre sur le compte et signaler que le reste sort du référentiel encodé ici, plutôt que d'extrapoler.

## Source

Annexe de l'Acte uniforme relatif au droit comptable et à l'information financière (AUDCIF), adopté le 26 janvier 2017. Le TSV est une extraction fidèle de cette annexe : il n'a pas été enrichi, complété ni corrigé. Toute divergence avec le texte officiel est une erreur d'extraction et doit être signalée, non arbitrée.
