# Règles de codification et notes officielles

Transcription de la section « Constantes » et des notes [1] à [10] annexées au plan de comptes SYSCOHADA révisé (AUDCIF, 26 janvier 2017).

## Constantes de codification

Les constantes sont des repères de reconnaissance communs à toutes les classes. Le numéro d'un compte comprend au maximum quatre chiffres, dont la position a une signification.

### 1. Longueur du numéro

Le premier chiffre désigne la classe d'appartenance : 57 appartient à la classe 5.

- deux chiffres → compte principal (ex. 10)
- trois chiffres → compte divisionnaire (ex. 101 Capital social)
- quatre chiffres → sous-compte (ex. 1011 Capital souscrit, non appelé)

### 2. Terminaison 9 des comptes à deux chiffres

Deux cas :

- **Comptes de bilan (classes 1 à 5)** : la terminaison 9 identifie les dépréciations provisionnées de la classe correspondante. Exemples : 19 Provisions pour risques et charges ; 39 Dépréciations des stocks et encours de production.
- **Comptes de gestion (classes 6 et 7)** : rôle analogue, appliqué à l'opération de provision. Exemples : 69 Dotations aux provisions et aux dépréciations ; 79 Reprises de provisions, de dépréciations et autres.

### 3. Terminaison 9 des comptes à trois chiffres et plus

Deux cas à distinguer :

- Le chiffre 9 en troisième ou quatrième position, pour l'ensemble des classes, marque le **solde inversé** des opérations couvertes par le compte de niveau immédiatement supérieur et classées dans les subdivisions se terminant par 1 à 8. Exemple : 6059.
- Il peut aussi marquer la **nature des comptes de catégories**. Exemple : 6049.

Cette logique n'est pas valable pour les comptes de la classe 2.

### 4. Terminaisons 1 à 8 des comptes à trois chiffres et plus

Elles détaillent les opérations subordonnées au niveau immédiatement supérieur.

Dans les comptes de gestion d'activité ordinaire (classes 6 et 7), la terminaison 8 regroupe les opérations autres que celles prévues dans les comptes de même niveau dont la terminaison va de 1 à 7. Exemples : 758 Produits divers ; 668 Autres charges sociales.

### 5. Terminaison 3 dans 603 et 73

Elle identifie les variations de stock : des biens achetés (603) et des biens produits par l'entreprise (73).

### 6. Terminaison 0

La terminaison 0 n'a aucune signification dans le référentiel comptable OHADA.

---

## Notes officielles annexées au plan

Ces renvois apparaissent entre crochets dans les libellés du fichier `plan-comptes.tsv`.

**[1]** — *Compte 2785 Or et métaux précieux.* Pièces, barres, lingots, louis d'or et autres métaux précieux (argent, diamant…) acquis et que l'entité a l'intention de conserver de manière durable.

**[2]** — *Comptes 462, 463, 465.* Le terme « associés » englobe les « actionnaires » et les « membres ».

**[3]** — *Comptes 4816, 4817, 4818.* Créer des sous-comptes distinguant les immobilisations corporelles des incorporelles.

**[4]** — *Compte 545 Avoirs d'or et autres métaux précieux.* Pièces, barres, louis d'or et autres métaux précieux (argent, diamant…) acquis en vue d'une cession à court terme. Ils jouent donc le rôle d'instruments de trésorerie.

**[5]** — *Comptes 6011, 6012, 6021, 6022.* À l'exception des achats effectués avec les entités du groupe.

**[6]** — *Comptes 6015, 6025, 6045, 6085 Frais sur achats.* L'entité peut créer des sous-comptes pour les frais accessoires : douane, fret, assurance sur achats, commissions, courtages sur achats, frais de transit, et autres frais accessoires.

**[7]** — *Comptes 70x1 et 70x2.* À l'exclusion des ventes faites à des entités du groupe.

**[8]** — *Comptes 7072, 7073, 7075, 7076.* À inscrire au compte 706 si ces produits correspondent à une activité principale de l'entité.

**[9]** — *Compte 726 Immobilisations financières.* En cas d'offre publique d'échange (OPE) ou d'achat (OPA) notamment.

**[10]** — *Compte 798 Reprises d'amortissements.* Cas de révision de plan d'amortissement.

---

## Lectures utiles de ces règles

Deux conséquences pratiques méritent d'être retenues, parce qu'elles sont la source la plus fréquente d'erreurs d'imputation.

La première tient à la distinction entre le **compte 622 Locations, charges locatives** et le **compte 623 Redevances de location acquisition**. Le premier accueille les loyers d'une location simple, charge d'exploitation ordinaire. Le second n'existe que pour les contrats qualifiés de location acquisition, et se lit avec la dette 17 et la charge financière 672. Le plan de comptes ne tranche pas la qualification : il offre les deux jeux de comptes et attend qu'elle soit faite ailleurs.

La seconde tient à la terminaison 9 en position trois ou quatre. Un compte comme 6019 Rabais, remises et ristournes obtenus fonctionne en solde inversé du poste 601 : il enregistre au crédit ce que les subdivisions 6011 à 6015 enregistrent au débit. Le traiter comme un compte de charge ordinaire produit un compte de résultat faux, sans que la balance signale quoi que ce soit.
