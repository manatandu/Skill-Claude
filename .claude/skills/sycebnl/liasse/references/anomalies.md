# Anomalies de balance — catalogue et solutions (SYCEBNL, associations)

Même logique que le moteur `syscohada/liasse` : le script inspecte la balance et sort une feuille `ANOMALIES` triée par gravité, sans jamais corriger un compte en silence.

## Gravités

- **BLOQUANT** : les états ne peuvent pas boucler. À régler avant tout.
- **A_TRAITER** : la présentation sera fausse ou l'équilibre fuira. À régler avant remise.
- **A_VERIFIER** : plausible mais suspect. À confirmer.
- **MINEUR** : sans effet réel (arrondi).
- **INFO** : information de cadrage.

## Anomalies couvertes

**Balance déséquilibrée** (BLOQUANT). Total des soldes débiteurs ≠ total des soldes créditeurs. *Solution :* reprendre la saisie avant montage.

**Écart d'arrondi** (MINEUR). Déséquilibre inférieur au centime. Sans effet.

**Compte non affecté** (A_TRAITER). Solde des classes 1 à 8 qu'aucune rubrique de la maquette ne capte. Il fait fuir l'équilibre de son montant net. *Solution :* vérifier le préfixe SYCEBNL du numéro, ou compléter `correspondance-associations.tsv`.

**Compte non conforme** (A_TRAITER). Classe hors 1-9 ou numéro trop court. *Solution :* se référer au libellé, réaffecter au compte SYCEBNL équivalent avant montage.

**Compte de classe 9** (INFO). Contributions volontaires en nature ou comptabilité analytique. La classe 9 est hors bilan et hors compte de résultat par construction de l'Acte uniforme (Partie 2, ch. 1, section 9) : normal qu'aucune rubrique de bilan/CR ne la capte. Ne pas la confondre avec un compte non affecté.

**Charge (classe 6) au solde créditeur** (A_VERIFIER). Transfert de charge, RRR obtenus ou erreur d'imputation.

**Produit (classe 7) au solde débiteur** (A_VERIFIER). RRR accordés, annulation de produit ou erreur d'imputation.

**Immobilisation (classe 2 hors 28/29) au solde créditeur** (A_VERIFIER). Cession non soldée, avoir sur immobilisation ou mauvaise ventilation.

**Résultat logé à deux endroits** (A_VERIFIER). Classes 6/7/8 ouvertes ET compte 13 mouvementé : risque de double comptage. *Solution :* fournir soit une balance avant clôture (6/7/8 ouverts, 13 vide), soit après (13 seul).

**Résultat nul** (INFO). Classes 6/7/8 non mouvementées : le compte de résultat ressortira à zéro même si le bilan porte un résultat en compte 13. C'est le cas normal d'une balance fournie après affectation — voir la feuille `CONTROLES`, ligne « écart résultat CR / bilan ».

## Corrections apportées à la maquette officielle

La maquette `correspondance-associations.tsv` a été recoupée contre la Partie 4, chapitre 2, du Journal officiel OHADA n° spécial du 22 février 2023 (section 6, tableaux de correspondance). Quatre écarts ont été corrigés pour que les états bouclent, sur le même principe que les trois corrections documentées dans `syscohada/liasse` :

1. **Poste BE (Autres créances)** : le tableau officiel liste le compte 41 parmi les comptes de BE, alors que 41 est déjà entièrement affecté à BD (Adhérents, Clients-usagers). Laissé tel quel, ce doublon casserait l'équilibre du bilan. Le compte 41 a été retiré de BE.
2. **Postes BE et DI (Autres créances / Autres dettes)** : le tableau officiel liste les comptes 42, 43, 44, 45, 47 sans réserve de sens sur les deux postes à la fois (actif ET passif), ce qui les ferait capter deux fois un même solde selon son signe. Un qualificatif « solde débiteurs » a été ajouté côté BE et « solde créditeurs » côté DI — exactement le traitement que la maquette SYSCOHADA applique déjà à ces mêmes comptes de tiers polyvalents.
3. **Poste CJ (Provisions réglementées)** : la fiche sommaire de la classe 1 (Partie 2, ch. 1) numérote ce poste 16, mais la fiche détaillée par compte et le tableau de correspondance du bilan (Partie 4, ch. 2) le numérotent 15. Le numéro 15 a été retenu, cohérent avec le tableau de correspondance qui gouverne le montage.
4. **Poste XA (Revenus des activités ordinaires)** : le libellé officiel indique « Somme RA à RG », ce qui exclurait RH (reprises de provisions, dépréciations, subventions et autres reprises) de la formule. RH est pourtant un produit ordinaire ; l'exclure romprait l'égalité entre le résultat du compte de résultat et le résultat logé au bilan (poste CH) dès qu'une entité a des reprises. Le moteur inclut RH dans XA.

Ces quatre corrections sont documentées ligne par ligne dans la colonne `note` de la maquette. Rien n'est corrigé ailleurs : toute autre bizarrerie de numérotation observée dans le texte officiel (ex. le renvoi de note illisible sur AG) est transcrite telle quelle et signalée `[texte officiel]`, sans être devinée.

## Limite du calcul du TFT (v2)

Le Tableau des flux de trésorerie n'est calculé que si `balance_N1` est fournie. La section « activités opérationnelles » (ZB) est un résidu comptable garanti par construction (`ZB = variation totale de trésorerie − investissement − fonds propres − fonds étrangers`) : le total boucle toujours, mais les lignes de détail FA à FH ne sont pas calculées individuellement — cette ventilation par nature d'encaissement/décaissement exige des données de mouvement (journal de trésorerie) qu'une balance de clôture, même sur deux exercices, ne porte pas. Ne pas confondre l'absence de calcul du détail avec une anomalie : le moteur ne signale rien sur ce point, il documente la limite dans la feuille `TFT` elle-même (libellé de la ligne ZB) et dans `README.md`.

## À enrichir

Pistes pour les versions suivantes, sur le même modèle que `syscohada/liasse/references/anomalies.md` : compte d'amortissement (28x/29x) sans immobilisation brute correspondante ; fonds affectés (16/17) mouvementés sans solde de trésorerie ou de créance en contrepartie ; dons en nature (classe 3, comptes 33-34) sans écriture miroir en produit (classe 7, compte 704) ; capitaux propres négatifs (alerte de continuité, particulièrement sensible pour une EBNL sans actionnaire de dernier recours).

## Évolutions v3

- **Cinquième correction de maquette (associations)** : le compte **46**
  (Bailleurs, État et autres organismes, fonds d'administration) est absent
  des deux côtés du tableau de correspondance officiel du bilan, alors que
  la NOTE 10 (ligne « Bailleurs, fonds d'administration ») et la NOTE 21
  (« Fonds d'administration des projets », ventilée 462/463/464) l'exigent.
  Ajouté à BE (soldes débiteurs — 469 fonds à recevoir) et DI (soldes
  créditeurs — 462-464), documenté dans la colonne note de la maquette.
- Les trois systèmes ont désormais chacun leur moteur et leur catalogue :
  ce fichier vaut pour les associations ; `monter_projets.py` applique les
  mêmes règles sur `correspondance-projets.tsv` (corrections documentées
  dans la maquette : bilan en net, 479/478, DI=499/599, ligne RC, TJ²=68+69,
  doublons TJ/TK officiels signalés) ; `monter_smt_sycebnl.py` porte un
  catalogue allégé (équilibre, conformité, classe 9, garde-fou VB/VC,
  rappel du seuil de 30 M FCFA).
- Les postes et les notes étant écrits en **formules Excel** (SUMIF sur
  BALANCE), toute affectation se vérifie en remontant la formule ; la
  feuille CONTROLES recoupe notes et postes (écarts « doit être 0 »).
