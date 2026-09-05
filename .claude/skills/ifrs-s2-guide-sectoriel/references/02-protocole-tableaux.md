# Les tableaux chiffrés, et pourquoi ils sortaient abîmés

## Le constat

Tout ne se dégrade pas. Dans `issb-durabilite`, les tableaux à filets de la documentation
d'accompagnement d'IFRS S2 sont intacts : la Table 7 (AUM par portefeuille) et la Table 8 (émissions
financées ventilées par classe d'actifs) gardent leurs colonnes. L'extraction en mode `-layout` a
suffi.

Ce qui casse, ce sont les mises en page à colonnes sans filets. Deux exemples vérifiables dans
`issb-durabilite/references/guide-application-ey/01-applying-ifrs-s1-s2-en.md` :

- Figure 3-2, vers la ligne 1930. Deux colonnes, « Relevance » et « Faithful representation ».
  À la lecture du fichier, la seconde colonne suit la première en un seul flux. Les puces de gauche
  et celles de droite se retrouvent bout à bout. Rien ne dit plus à quelle colonne appartient une
  puce donnée.
- Figure 4-1, vers la ligne 3730. Un encadré latéral s'insère au milieu d'un paragraphe courant et
  le coupe en deux.

C'est le même phénomène que sur un tableau chiffré : dès que le PDF n'a pas de filets, l'extraction
rend une colonne unique et les nombres arrivent en file. On lit bien `48,600,415`, mais plus rien ne
dit à quelle colonne il appartient.

## Pourquoi aucune capture n'était gardée

Trois raisons, aucune n'est une fatalité.

1. La chaîne d'encodage était en texte seul. Le PDF entrait, du Markdown sortait, il n'y avait pas
   d'étape image.
2. Une image ne se cherche pas. `grep` ne trouve rien dedans. Un fichier de références sert d'abord
   à être fouillé.
3. Une image que rien n'annonce ne sera pas ouverte. Sans consigne explicite dans le Markdown, la
   capture reste un fichier mort à côté du texte.

La correction tient en une phrase : on garde une capture, mais on la double d'un tableau Markdown
reconstruit, et on écrit dans le fichier quand il faut l'ouvrir.

## La règle, en trois temps

**1. Reconstruire la grille, pas le flux.** L'extraction texte lit la page dans l'ordre de lecture.
La détection de tableaux lit la géométrie : filets, alignements, blocs. Sur le même PDF, le second
retrouve les colonnes que le premier a perdues.

**2. Garder la capture à côté.** Un PNG de la zone du tableau, référencé depuis le Markdown, avec la
consigne. Le tableau reconstruit sert à chercher et à lire vite. La capture sert de preuve quand un
chiffre est repris dans un travail.

**3. Contrôler les totaux.** Quand une ligne s'appelle « Total », sa valeur doit égaler la somme des
lignes numériques au-dessus, colonne par colonne. Un écart signale soit une extraction fausse, soit
une erreur de la source. Les deux méritent d'être écrites dans le fichier.

## Le script

`scripts/pdf-tableaux.py`. Une dépendance, `pymupdf` (`pip install pymupdf`).

```
python3 scripts/pdf-tableaux.py guide-sectoriel.pdf --pages 210-232 --out references/volume-10/
```

Il produit :

- `references/volume-10/tableaux.md`, un tableau Markdown par tableau détecté, chacun suivi du
  renvoi vers sa capture et, s'il y a lieu, de la ligne de contrôle des totaux ;
- `references/volume-10/images/p<N>-t<k>.png`, la capture de la zone, marge de 8 points, 200 dpi par
  défaut.

Les pages se donnent en numérotation du PDF, à partir de 1, sous la forme `210-232,240`. Sans
`--pages`, il traite tout le fichier.

## La démonstration

`exemples/` contient la sortie réelle du script sur un PDF de test qui reproduit les deux cas :
l'encadré à deux colonnes et le tableau chiffré. Le PDF de test se régénère avec
`scripts/demo-pdf.py`.

Sur le tableau chiffré, l'extraction texte donne ceci, colonnes perdues :

```
Scope 1
48,600,415
101,487,332
150,087,747
Scope 2
33,805,025
...
```

Le script donne un tableau Markdown correct, plus `exemples/images/p1-t2.png`. Le contrôle des
totaux passe : 48 600 415 + 33 805 025 + 159 615 008 = 242 020 448. Testé aussi sur un tableau
volontairement faux, où le contrôle signale bien la colonne fautive.

## Les limites, à dire plutôt qu'à découvrir

- La détection échoue sur un tableau sans filets et mal aligné. Dans ce cas, il reste la capture, et
  le Markdown doit le dire.
- Un PDF scanné ne contient pas de texte. Il faut un OCR avant, et l'OCR se relit.
- Une capture coûte de la place et, à la lecture, de l'ordre de mille à deux mille jetons. On en
  garde pour les tableaux qui portent des chiffres, pas pour la décoration.
- Ne pas jeter l'extraction texte d'origine. Elle reste la version cherchable.

## Comment citer un chiffre lu dans une capture

Comme un chiffre lu dans le PDF : source, page, tableau. La capture est un moyen de lecture, pas une
source. Et si le contrôle des totaux a signalé un écart, ce chiffre ne sort pas du fichier sans
vérification humaine.
