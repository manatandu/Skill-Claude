# Guide d'application du SYSCOHADA révisé — écritures et cas pratiques

Ce module contient les **écritures-types** et les **cas pratiques** (Applications numérotées) du Guide d'application SYSCOHADA. Il répond à *comment* comptabiliser une opération courante, pas à *quel numéro* de compte (→ `syscohada-comptes`) ni à *quel article/critère* d'évaluation (→ `audcif-acte-uniforme`). Les trois se lisent ensemble.

## Règle d'usage

Ne jamais reconstituer une écriture, un schéma de régularisation ou le résultat d'une Application de mémoire. Toujours ouvrir le fichier `references/` concerné et recopier le sens des comptes, les montants et le libellé. En cas de doute sur un numéro de compte, vérifier dans `syscohada-comptes` ; en cas de doute sur la règle d'évaluation, vérifier dans `audcif-acte-uniforme`.

**Montants et taux = illustrations pédagogiques.** Les nombres des Applications (TVA 10 %, 18 %, 20 %, taux d'amortissement, cours de change, etc.) illustrent le mécanisme et ne sont pas les taux réels. Pour les taux effectifs en RDC (TVA **16 %**, barèmes, taux d'amortissement de l'AM n° 013/2025, échéances) → `fiscalite-rdc-socle` et les skills `fiscalite-rdc-is` / `fiscalite-rdc-irpp`.

**Présentation des écritures.** Toute écriture se présente en tableau à 5 colonnes avec en-tête nommé : `Débit | Crédit | Date et libellé | Montant débit | Montant crédit`. Colonne 1 = n° du compte débité ; colonne 2 = n° du compte crédité ; colonne 3 = date/libellé ; colonnes 4-5 = montants.

**Anomalies du texte officiel.** Les incohérences de dates, de libellés ou de montants du guide sont signalées inline par un marqueur `[texte officiel]` et jamais corrigées silencieusement.

## Position dans la famille SYSCOHADA

| Question | Skill |
|---|---|
| Quelle **écriture** passer pour cette opération ? | **`syscohada-ecritures`** (ce module) |
| Quel **numéro / intitulé** de compte ? | `syscohada-comptes` |
| Quel **article** ou critère d'évaluation ? | `audcif-acte-uniforme` |
| Dans quelle **rubrique** du bilan / CR ? | `syscohada-etats-financiers` |
| Monter une **balance en liasse** ? | `syscohada-liasse` |

## Table des matières

### Partie 1 — Opérations courantes

| Fichier | Contenu | Applications |
|---|---|---|
| `references/partie-1-ch1-plan-comptes-subdivisions.md` | Plan de comptes : classes de situation/gestion, comptes principaux et divisionnaires, constantes (chiffres 8 et 9), parallélismes, subdivision en sous-comptes (nature/fonction), nomenclatures. **Cadre**, pas d'écriture. | — |
| `references/partie-1-ch2-achats-ventes-facture.md` | Achats (60-63) et ventes (70) bruts ; stocks (inventaire intermittent/permanent, 603/73, 476/605) ; éléments soustractifs (retours, RRR, escompte) ; éléments additifs (ports/emballages 7071, consignés 4194/4094/7074/6224, TCA 446, TVA 443/445). | 1 à 6 |
| `references/partie-1-ch3-autres-operations-exploitation.md` | Conception (flux amont/aval) ; impôts et taxes (droits de douane, centralisation TVA 443/445/444, impôt sur les bénéfices 891/441) ; subventions d'exploitation et d'équilibre (71/718/88) ; charges de personnel (bulletin de paie, avantages en nature 6617/781, personnel extérieur 637/667) ; frais financiers (67) et revenus financiers (77). | 7 à 10 |
| `references/partie-1-ch4-operations-tresorerie.md` | Espèces (57), chèque (513/514), carte (515/6315), virement ; effets de commerce (402/412, à encaisser 512, à l'escompte 415/565, impayés 4131) ; monnaie électronique (55) ; délais de règlement (escompte 673/773, retard 6318/413) ; synthèse. | 11, 12 |
| `references/partie-1-ch5-investissement-desinvestissement.md` | Notion d'immobilisation ; comptabilisation (achat, production, gratuit) ; valeur d'entrée (coût d'acquisition/production, coûts d'emprunt) ; amortissement (linéaire, dégressif SOFTY, unités d'œuvre) ; décomptabilisation (rebut, destruction, vente, échange, 81/82 vs 654/754) ; plus-value à réinvestir (152/851/861). | 13 à 16 |
| `references/partie-1-ch6-regularisations-periodiques.md` | Régularisation des stocks (intermittent/permanent, CCA 476) ; amortissements (681/852, dérogatoires 151/851/861) ; dépréciations (dotations 691/697/853, charges 659/679/839, reprises 79/759) ; provisions pour risques et charges (19 vs 499/599) ; CCA/PCA ; charges à payer (408, 4281, 166) ; produits à recevoir (4098, 4181, 4858). | 17 à 24 |

### Partie 2 — Opérations et problèmes spécifiques

| Fichier | Contenu | Applications |
|---|---|---|
| `references/partie-2-ch1-frais-recherche-developpement.md` | Frais de recherche et développement : recherche fondamentale/appliquée en charges, développement activable (211/721), brevet (2121), amortissement (6812/2812). | 25 |
| `references/partie-2-ch2-immobilisations-incorporelles.md` | Brevets réglés par redevances (2121, valeur actualisée vs 634), marques (interne en charges vs 214 acquise/2814), logiciels créés en interne (2131/2193/721), sites internet e-commerce (2132), coût d'obtention du contrat (2182), fonds commercial (215, écart d'acquisition). | 26 à 31 |
| `references/partie-2-ch3-5-prospection-composants-revisions.md` | Frais de prospection/évaluation des ressources minérales (2181, avant droits en charges) ; approche par composants (structure vs composant, renouvellement) ; révisions majeures/inspections comme composant amorti sur la périodicité. | 32 à 34 |
| `references/partie-2-ch6-7-demantelement-cout-emprunts.md` | Démantèlement/remise en état (actif de démantèlement + provision 1984, désactualisation 6971, reprise 7911/7971) ; coût d'emprunts incorporable à l'actif éligible (net des placements). | 35, 36 |
| `references/partie-2-ch8-contrats-location.md` | Location acquisition/crédit-bail chez le preneur (173, 623, 672, taux implicite, levée/non-levée) ; location financement chez le bailleur (2714, 775, tableau créance). | 37, 38 |
| `references/partie-2-ch9-reserve-propriete.md` | Réserve de propriété acheteur (24116/4816 + engagement 9183/9083) et vendeur (4116/9043, revendication, revente, provisions). | 39, 40 |
| `references/partie-2-ch10-11-placement-sol-autrui-rentes.md` | Immeubles de placement (2315 vs 2313) ; constructions sur sol d'autrui (232, indemnité d'éviction) ; rentes viagères (1681, bouquet, décès du crédirentier). | 41 à 43 |
| `references/partie-2-ch12-depreciations-immobilisations.md` | Dépréciation et reprise plafonnée (plan révisé) ; groupe d'actifs (fonds commercial d'abord, prorata VNC) ; perte après réévaluation (1062) ; immobilisation subventionnée (2 méthodes). | 44 à 47 |
| `references/partie-2-ch13-portefeuille-titres.md` | Acquisition titres (placement 502x/frais 5026, participation 261, TIAP 2741, immobilisés 2746) ; titres non libérés (472) ; cession de participation (816/826/797) ; cession de placement (PEPS vs CMP). | 48 à 51 |
| `references/partie-2-ch14-15-stocks-abandons-affacturage.md` | Stocks : imputation rationnelle (coût de chômage), VNR et contrat ferme, matières premières en continuité ; abandons de créances (836/846), affacturage classique/inversé (4716), titrisation (FCTC). | 52 à 57 |
| `references/partie-2-ch16-capitaux-propres.md` | Libération intégrale/fractionnée, augmentation en numéraire (prime 1051), incorporation de réserves, réduction par imputation des pertes / par remboursement, amortissement du capital (1014), affectation du résultat. | 58 à 65 |
| `references/partie-2-ch17-subventions.md` | Subventions d'investissement (1411/1412, reprise 799 au rythme d'amortissement) ; d'exploitation (71) ; d'équilibre (88) ; avances remboursables (163) ; immobilisation subventionnée dépréciée. | 66 à 70 |
| `references/partie-2-ch18-19-provisions-actions-gratuites.md` | Provisions : constitution/estimation (garanties 192, restructuration 194, litiges 191), passifs éventuels ; attribution gratuite d'actions par rachat (5021/6772) ou prélèvement sur résultat. | 71 à 77 |
| `references/partie-2-ch20-emprunt-obligataire.md` | Emprunt obligataire : amortissements constants avec prime (6714/1661), remboursement in fine (prorata intérêts courus), convertible en actions (1612, provision de prime, prime de conversion 1054). | 78 à 80 |
| `references/partie-2-ch21-engagements-retraite.md` | Engagements de retraite (unités de crédit projetées, provision 1961) ; écart actuariel (gain/perte) ; régimes couverts par des actifs (police d'assurance, 4731). | 81 à 83 |
| `references/partie-2-ch22-devises-couverture.md` | Opérations en devises et couverture (art. 51-58) : écarts de conversion 478/479, provision pour perte de change 194/499, position globale (art. 57), étalement de la perte sur emprunt pluri-exercices (art. 56), couverture fixant le cours (art. 58-3), opération symétrique (4788), transactions futures (54, 6784, 4786/4797). | 84 à 91 |
| `references/partie-2-ch23-24-contrats-pluri-exercices-abonnement.md` | Contrats pluri-exercices : méthode à l'avancement (4181/7051/4435) vs à l'achèvement, contrat déficitaire (provision 193) ; abonnement des charges et produits (4746). | 92 à 94 |
| `references/partie-2-ch25-concession-service-public.md` | Concession de service public : PPP phase construction (2734) et post-construction (411/706/77), droits de passage (4731) ; biens « de retour » (hors bilan) vs biens « de remise » (au patrimoine, amortis). | 95 |
| `references/partie-2-ch26-27-gie-personnel-interimaire.md` | GIE : participation aux résultats (4631/772/621/706, dépréciation 4963), participation financière (266/277) ; personnel intérimaire/détaché (637/667, 6371/6372, 6327). | 96 à 98 |
| `references/partie-2-ch28-reevaluation-bilans.md` | Réévaluation légale (écart 1061 ou provision spéciale 154/861) et libre (1062, 2 méthodes) ; valeur retenue = min(indiciaire, actuelle). | 99, 100 |
| `references/partie-2-ch29-inventaire-permanent.md` | Inventaire permanent : CMUP recalculé après chaque entrée, sorties 6031/311, escomptes 673/773, emballages 4094, écart d'inventaire. | 101 |
| `references/partie-2-ch30-31-engagements-evenements-posterieurs.md` | Engagements hors bilan (donnés 906/916, reçus 902/912) ; événements postérieurs à la clôture (ajustement vs Notes annexes vs rapport de gestion). | 102, 103 |
| `references/partie-2-ch32-operations-compte-tiers.md` | Commissionnaire (marge, tout au résultat) vs mandataire (4731, 4711/4712, rémunération 706/7072) ; débours et remboursements. | 104, 105 |
| `references/partie-2-ch33-operations-faites-en-commun.md` | Société en participation : comptabilité autonome (188) vs intégrée (06/07), chez gérant (4631/182/752/781) et non-gérant (2773), répartition du résultat. | 106, 107 |
| `references/partie-2-ch34-comptabilite-autonome-etablissement.md` | Comptabilité par établissement : comptes de liaison bloqués (184) et non bloqués (1851/1852), cessions internes (185/186/187), balance et CR de succursale, intégration au siège. | 108 à 111 |
| `references/partie-2-ch35-contrat-franchise.md` | Franchise : droit d'entrée chez le franchisé (2184/235, amortissements) et le franchiseur (706), redevance annuelle (634/4181). | 112 |
| `references/partie-2-ch36-37-pluri-monetaire-entites-agricoles.md` | Comptabilité pluri monétaire : intégration directe (cours du jour/fixe), différée (184), mixte (partie simple + partie double) ; entités agricoles (2245, 2465/2496/2846, cheptel 2462, autoconsommation 1047/724, cessions courantes 654/754). | 113 à 115 |
| `references/partie-2-ch38-fusions-operations-assimilees.md` | Fusions et opérations assimilées : évaluation des apports (valeur réelle vs comptable), parité d'échange, comptabilisation chez l'absorbante (4614/1013/1053) et l'absorbée (4718/1381/4618) ; fusion-renonciation et boni de fusion ; participations réciproques (système à deux inconnues) ; apport partiel d'actif (1052). | 116 à 120 |
| `references/partie-2-ch39-40-comptes-intermediaires-liquidation.md` | Comptes intermédiaires : périodes comparatives (N vs N-1). Liquidation : comptes 837/847/1384 [texte officiel : le guide définit 1374 mais utilise 1384], deux méthodes (directe vs via charges/produits H.A.O.), écritures de partage (4619). | 121, 122 |
| `references/partie-2-ch41-premiere-application-syscohada-revise.md` | Première application du SYSCOHADA révisé : compte transitoire 4751, étalement des frais d'établissement et des primes de remboursement des obligations (206/1611/6714), approche par composants (réallocation des VNC, sans impact sur les capitaux propres), engagement de retraite (196/1961), changement de méthode pour un contrat à long terme (achèvement → avancement, 475/34-35/4181). | 123 à 126 |

### Partie 4 — Comptes consolidés et combinés

| Fichier | Contenu | Applications |
|---|---|---|
| `references/partie-4-consolidation-combinaison.md` | Ch. 1 Périmètre et méthodes : pourcentage de contrôle vs pourcentage d'intérêt, actions à vote double/sans droit de vote, droits de vote potentiels substantifs, participations circulaires (résolution directe et par système d'équations), entité ad hoc (3 critères de contrôle). Ch. 2 Mise en œuvre : intégration globale, intégration proportionnelle, mise en équivalence — un même couple mère/filiale traité sous les trois méthodes. Ch. 3 Écart de consolidation : écart d'évaluation (imposition différée), écart d'acquisition positif (goodwill, amortissement, dépréciation) et négatif (badwill), en intégration globale et en mise en équivalence. Ch. 4 Conversion des états financiers en devises : méthode temporelle (écart de change en résultat financier) vs méthode du cours de clôture (écart de conversion en réserves consolidées, réparti avec les minoritaires). Ch. 5 Retraitements (écarts de conversion, provision pour retraite non comptabilisée, amortissements dérogatoires, subventions) et élimination des opérations intragroupe (dividendes, marge sur stock). Ch. 6 Variations du périmètre sans changement de méthode (montée en participation, écart d'acquisition figé à la prise de contrôle initiale). Ch. 7 Comptes combinés (entité mère hors espace OHADA, filiales combinées entre elles indépendamment de la mère). | 128 à 142 |

## État d'encodage

- **Partie 1 (Opérations courantes)** : chapitres 1 à 6 encodés (Applications 1 à 24).
- **Partie 2 (Problèmes spécifiques)** : chapitres 1 à 41 encodés (Applications 25 à 126). Guide_2 couvrait les App. 26 à 83 ; Guide_3 couvre les App. 84 à 115 (chapitres 22 à 37) ; Guide_4 couvre les App. 116 à 126 (chapitres 38 à 41 : fusions, comptes intermédiaires, liquidation, première application du SYSCOHADA révisé).
- **Partie 4 (Comptes consolidés et combinés)** : chapitres 1 à 7 encodés (Applications 128 à 142). Guide_5 couvre l'intégralité de cette partie.
- **Hors périmètre** : Guide_4 enchaîne sur une « Troisième partie : Présentation des états financiers annuels » (chapitre 1, sections Bilan/Compte de résultat/TFT/Notes annexes — logique des postes, masses, rubriques) et Guide_5 ouvre sur l'Application 127 (modèle type d'un jeu complet d'états financiers, chapitre 2 de cette même Troisième partie). Ni l'une ni l'autre ne comportent d'écritures ; elles relèvent de `syscohada-etats-financiers`, pas de ce skill, et n'ont pas été encodées ici.

## Déploiement

Les fichiers de ce zip sont une copie de travail. Seul Manasse peut téléverser le skill via Réglages → Compétences. Ne jamais affirmer que le skill est « intégré » ou « déployé ».
