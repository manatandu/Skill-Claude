# TFT — formules détaillées poste par poste (source secondaire)

**Source :** Kambale Mbahweka Nzanzu (dir.), *Le Praticien Comptable OHADA-SYSCOHADA*, Section 2, « Tableau de correspondance : Tableau des flux de trésorerie », p. 1274-1275. Transcription faite à partir des photos fournies par l'utilisateur, vérifiée image par image (plusieurs pages étaient imprimées tête-bêche).

Ce document ne remplace pas l'AUDCIF. Il **complète** `chapitre-1-logique-postes-masses.md` (qui donne la logique narrative, sourcée AUDCIF Titre IX) par le détail compte-par-compte que l'AUDCIF ne donne pas lui-même. Recoupé avec AUDCIF Titre IX chapitre 5 (`titre-9-ch1-5-bilan-resultat-flux.md`, §598-620) : cohérent sur tous les postes sauf un, signalé ci-dessous.

Convention de lecture : dans les encadrés source, le signe imprimé **avant** une ligne gouverne cette ligne. Absence de signe sur la toute première ligne = terme positif.

## Trésorerie d'ouverture et de clôture

**ZA — Trésorerie nette au 1er janvier**
```
(BQ+BR+BS du bilan actif N-1) − (solde créditeur balance N-1, compte 4726) − (DQ+DR du bilan passif N-1)
```

**ZH — Trésorerie nette au 31 décembre**
```
(BQ+BR+BS du bilan actif N) − (solde créditeur balance N, compte 4726) − (DQ+DR du bilan passif N)
```
Miroir exact de ZA sur l'exercice N. Contrôle de bouclage : ZH doit égaler ZA + B + C + F (somme des trois flux).

## ZB — Flux des activités opérationnelles (FA à FE)

**FA — CAFG**
```
XD (EBE)
+ solde débiteur balance N, compte 654 (VNC cessions courantes d'immobilisations)
− solde créditeur balance N, compte 754 (produits de cessions courantes)
+ XF (résultat financier), sauf dotations (TL), reprises (RN) et correction des intérêts courus sur prêts/dettes financières si significatif
+ TO (autres produits HAO), sauf compte 86
− RP (autres charges HAO), sauf compte 85
− RQ (participation des travailleurs)
− RS (impôts sur le résultat)
```
Conforme à la narrative existante (`chapitre-1-...md` §88). La matrice précise en plus les exclusions sur XF (dotations/reprises/intérêts courus) et sur TO/RP (comptes 86 et 85), non détaillées jusqu'ici — à intégrer.

**FB — Variation de l'actif circulant HAO**
```
BA(N) − BA(N-1) − [485(N) − 485(N-1)] + [écart conversion actif 47818(N) − 47818(N-1)] − [écart conversion passif 47918(N) − 47918(N-1)]
```
Confirmé sur scan net (relecture du 20/08/2026) : le compte 485 est bien **retranché** de ΔBA, conforme à l'AUDCIF (Titre IX, §611-618 et §744, qui exclut du calcul de la variation du BF opérationnel « les variations liées aux dettes et créances sur cession et acquisition ou production d'immobilisations ») et à FI de la même source, qui reprend le mouvement du 485 côté investissement. Codé tel quel dans `monter_liasse.py`.

**FC — Variation des stocks**
```
BB(N) − BB(N-1)
```
Conforme à AUDCIF et à la narrative existante.

**FD — Variation des créances**
```
[BH(N) + BI(N) + BJ(N)] − [BH(N-1) + BI(N-1) + BJ(N-1)]
− [solde débiteur balance N, comptes 414, 4494, 458, 461, 467, 4752]
+ [mêmes comptes, solde débiteur balance N-1]
+ mouvement débit balance N, comptes 2714, 2766
+ [écart conversion actif 47811(N) − 47811(N-1)]
− [écart conversion passif 47911(N) − 47911(N-1)]
```
Cohérent avec la narrative (§89) : les créances rattachées aux immobilisations, aux apporteurs, aux comptes transitoires et aux titres non libérés sont retranchées de la variation brute clients/autres créances. Aucune divergence.

**FE — Variation du passif circulant**
```
DP(N) − DP(N-1)
− [solde créditeur balance N, comptes 404, 461, 465, 4726, 481, 482]
+ [mêmes comptes, solde créditeur balance N-1]
+ [écart conversion 4793(N) − 4793(N-1)]
− [écart conversion 4783(N) − 4783(N-1)]
+ mouvement débit balance N, compte 4752
− mouvement crédit balance N, compte 4752
```
Cohérent avec la narrative (§89). Aucune divergence.

## ZC — Flux des activités d'investissement (FF à FJ)

**FF — Décaissements liés aux acquisitions d'immobilisations incorporelles**
```
AD(N) − AD(N-1)
+ mouvement débit balance N, compte 251
− mouvement crédit balance N, compte 251
+ mouvement débit balance N, comptes 4041, 4046, 4811, 48161, 48171, 48181, 4821, 281
− mouvement crédit balance N, comptes 4041, 4046, 4811, 48161, 48171, 48181, 4821
+ solde débiteur balance N, comptes 6541, 811
```

**FG — Décaissements liés aux acquisitions d'immobilisations corporelles**
```
AI(N) − AI(N-1)
+ mouvement débit balance N, compte 252
− mouvement crédit balance N, compte 252
+ mouvement débit balance N, comptes 4042, 4047, 4812, 48162, 48172, 48182, 4822, 282, 283, 284
− mouvement crédit balance N, comptes 17, 19842, 4042, 4047, 4812, 48162, 48172, 48182, 4822
− mouvement crédit balance N, comptes 106, 154 (réévaluation, part relative aux immobilisations corporelles)
+ solde débiteur balance N, comptes 6542, 812
```
Le crédit du compte 17 (dette de location-acquisition) en déduction confirme l'exclusion des acquisitions financées par crédit-bail, décrite dans la narrative.

**FH — Décaissements liés aux acquisitions d'immobilisations financières**
```
mouvement débit balance N, comptes 26 et 27 (sauf 2714, 2766, et éventuellement 276 si significatif)
+ mouvement débit balance N, compte 4813
− mouvement crédit balance N, compte 4813
− mouvement crédit balance N, comptes 106 et 154 (part relative aux immobilisations financières)
+ solde débiteur balance N, compte écart de conversion actif, compte 4782
− solde créditeur balance N, compte écart de conversion passif, compte 4792
```
Confirmé sur scan net (20/08/2026) : formule identique à ce qui était déjà codé (les termes 4782/4792 sont des soldes de l'exercice N seul, pas des variations N/N-1). Aucun changement de code nécessaire.

**FI — Encaissements liés aux cessions d'immobilisations incorporelles et corporelles**
```
solde créditeur balance N, comptes 754, 821, 822
− mouvement débit balance N, comptes 414, 485 (sauf 4856)
+ mouvement crédit balance N, comptes 414, 485 (sauf 4856)
```
⚠️ **Corrigé le 20/08/2026.** La première transcription avait les deux derniers termes inversés (+ mouvement débit, − mouvement crédit au lieu de l'inverse). Le scan net confirme le signe ci-dessus, cohérent avec la logique : le mouvement crédit du 414/485 correspond à l'encaissement d'une créance déjà constatée (le client règle, la créance se solde au crédit) — il s'ajoute donc à l'encaissement de l'exercice. Le mouvement débit correspond à une nouvelle créance née d'une cession à crédit non encore encaissée — il s'en retranche.

**FJ — Encaissements liés aux cessions d'immobilisations financières**
```
solde créditeur balance N, compte 826
+ mouvement crédit balance N, compte 27 (sauf 2714, 2766)
− mouvement débit balance N, compte 4856
+ mouvement crédit balance N, compte 4856
```

## ZD/ZE — Flux de financement (FK à FQ)

**FK — Augmentation de capital par apport nouveau**
```
solde créditeur balance N, comptes 101, 102, 1051
− solde créditeur balance N-1, comptes 101, 102, 1051
− solde débiteur balance N, comptes 109, 4613, 467, 4581
− mouvement débit balance N, comptes 11, 12, 130, 131
+ mouvement crédit balance N, comptes 103, 104, 11, 12, 139, 4619, 465
```

**FL — Subventions d'investissement reçues**
```
solde créditeur balance N, compte 14
− solde créditeur balance N-1, compte 14
+ solde créditeur balance N, compte 799
− solde débiteur balance N, comptes 4494, 4582
```

**FM — Prélèvement sur le capital**
```
mouvement débit balance N, compte 4619
+ mouvement débit balance N, comptes 103, 104
```

**FN — Dividendes versés**
```
mouvement débit balance N, compte 465
```
Conforme à la narrative (§100).

**FO — Emprunts**
```
mouvement crédit balance N, comptes 161, 162, 1661, 1662
+ mouvement débit balance N, compte 4713
− solde débiteur balance N, compte écart de conversion actif, compte 4784
```

**FP — Autres dettes financières**
```
mouvement crédit balance N, comptes 163, 164, 165, 166, 167, 168, 181, 182, 183 (sauf 1661, 1662)
− solde débiteur balance N, compte écart de conversion actif, compte 4784
```

**FQ — Remboursements des emprunts et autres dettes financières**
```
mouvement débit balance N, comptes 16, 17, 181, 182, 183
− solde créditeur balance N, compte écart de conversion passif, compte 4794
```
Contrairement à ma première lecture (page pivotée, faible contraste), FQ ne compare pas le 4794 entre N et N-1 : c'est un terme de correction sur le seul exercice N, comme pour FO et FP. Le débit du compte 17 confirme le traitement du remboursement de dette de location-acquisition comme un remboursement financier (narrative §102).

**NB du livre, reporté tel quel :** les intérêts versés peuvent être classés soit en activité opérationnelle, soit en financement — les intérêts courus ont été considérés ici comme opération de financement.

## Statut des formules

Toutes confirmées sur scan net à ce stade (dernière vérification : FH et FI, le 20/08/2026). Codé et testé dans `monter_liasse.py` (`calculer_tft`), avec vérification manuelle de ZA, FA, FB, FD, FE, FG, FK, FO, FP, FQ, FI sur balances synthétiques.

## Prochaine étape

Ce fichier fournit la matière pour coder le TFT dans `scripts/monter_liasse.py` (actuellement non couvert, voir README §« Ce qui reste à alimenter »). Avant codage : lever le doute sur FB (485) et sur FO/FP, idéalement en confrontant un exemple chiffré (le modèle d'application `etats-financiers/references/app-127-modele-jeu-complet-etats-financiers.md` donne un TFT résolu, exercice « SYSTEME COMPTABLE OHADA », qui peut servir de cas de calibrage une fois qu'une balance source est disponible).

## Convention de signe des postes FB, FC, FD (correction v3, 31/08/2026)

Les formules ci-dessus donnent des **variations** (N moins N-1). Or dans le
gabarit officiel, les lignes se libellent « − Variation de l'actif circulant
HAO », « − Variation des stocks », « − Variation des créances »,
« + Variation du passif circulant », et le total ZB est une **somme simple**
(`=H14+H15+H16+H17+H18`). La cellule de FB, FC et FD doit donc porter
l'**opposé** de la variation calculée (une hausse des stocks pèse en négatif
sur le flux) ; FE porte la variation telle quelle. La v2 du moteur écrivait
la variation brute sur FB/FC/FD — inversion corrigée en v3 et vérifiée sur
balance synthétique (ZB recoupe le calcul manuel du flux opérationnel).
