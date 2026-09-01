# Notes annexes SYCEBNL — Système minimal de trésorerie : couverture du moteur

**Source : Journal officiel OHADA n° spécial du 22 février 2023, Partie 4,
chapitre 4** (transcrit dans `../../references/partie4-ch4-etats-smt.md`).
Entités visées : petites EBNL sous le seuil de **30 M FCFA** de ressources
annuelles (Acte uniforme, art. 5-6), tenant une comptabilité de trésorerie.

Jeu d'états : **Bilan (GA→HZ) + Compte de résultat (KA→KZC) + 5 notes** —
pas de TFT, pas de tableau emplois-ressources.

| Note | Intitulé officiel | Couverture (`monter_smt_sycebnl.py`) |
|---|---|---|
| 1 | Tableau d'acquisition et de suivi du matériel, du mobilier et des cautions | Pré-alimentée : une ligne par compte de classe 2 (formules), total brut, cumul 28/29, valeur nette recoupant le poste GA. Dates/durées/sorties à compléter. |
| 2 | État des stocks | Lignes par compte de classe 3 (formules), stock final (classe 3 N), stock initial (classe 3 N-1 si fournie). Détail article/quantité/PU à saisir. |
| 3 | État des créances et des dettes non échues | Gabarit de saisie (l'inventaire extra-comptable fait foi) + rappels balance en formules (classe 4 débiteurs/créditeurs). Alimente VB/VC du compte de résultat. |
| 4 | Journal unique de trésorerie | Gabarit avec les ventilations officielles (recettes : cotisations/subventions/autres/matériel ; dépenses : achats liés à l'activité/autres achats/transport/services extérieurs/salaires/autres), soldes en formules de cumul. Un journal par banque + un pour la caisse ; regroupement mensuel possible. |
| 5 | Dotation | Table des membres (à saisir) + rappels balance en formules : dotation non consomptible (101/102), droit d'entrée (103), dotation consomptible (104). |

## Correspondance compte → poste

Le chapitre 4 ne publie **pas de table de correspondance** : celle du
moteur (`correspondance-smt-sycebnl.tsv`) est une construction documentée,
chaque compte vérifié au plan SYCEBNL. Points d'attention :

- classe 2 en **net** (pas de colonne amortissements au bilan SMT) ;
- « Banque (en + ou en –) » : un découvert vient en moins de l'actif — pas
  de poste banques créditrices au passif ;
- dépréciations de tiers (49) et de titres (590/591) en moins des créances
  (GC), jamais en dettes ; 599 en créditeurs (HD) ;
- « Autres fonds propres » (HC) regroupe réserves, report à nouveau,
  subventions, fonds affectés/reportés, **emprunts et provisions** (11, 12,
  14 à 19) — le modèle officiel ne les distingue pas ;
- 603 et 73 reclassés vers la ligne VA (variations des stocks) pour éviter
  le double compte avec l'état des stocks ;
- résultat : `KZC = KZ + VA + VB − VC − JG` (signes officiels du modèle) ;
- VB/VC : cellules de saisie depuis la Note 3, jamais calculées depuis la
  balance ; si la balance porte une classe 4 mouvementée (base
  engagement), les laisser à zéro — anomalie `INFO` le rappelle.
