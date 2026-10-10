# Référentiel maître des fiches de mathématiques — Prépa Clé - v3.1

**Version documentaire : 3.1**  
**Date : 10 octobre 2026**  
**Statut :** gel éditorial du périmètre et des règles de gestion ; catalogue et graphe à maintenir selon les contrôles ci-dessous.  
**Source de vérité :** 
- ce référentiel pour les règles de gestion, le périmètre documentaire, les décisions et le registre de contrôle ;
- la matrice de traçabilité pour les correspondances détaillées avec les référentiels ;
- le catalogue maître pour les identifiants et les objectifs des fiches ;
- le graphe des prérequis pour les dépendances entre fiches.

Les listes d’identifiants et de dépendances reproduites dans ce référentiel sont des éléments de migration ou de contrôle. Elles ne constituent pas une seconde version du catalogue ou du graphe.

---

# Document A — Politique de versionnage et règles de référence

## A1. Statut des versions

| Version | Statut | Usage |
|---|---|---|
| 1.1 | Archive historique | Référence pour retrouver les objectifs et anciens identifiants |
| 2.1 | Archive de travail | Ne pas utiliser comme source de vérité |
| 2.2 | Brouillon remplacé | Références incomplètes ou incohérentes |
| 2.3 | Brouillon remplacé | Références croisées non fiables |
| 3.0-candidate | Base du catalogue et du graphe | Catalogue principal et dépendances détaillées |
| 3.1 | Version documentaire de référence | Règles de gestion, compléments de couverture et statut des contrôles |

**Attention :** la version 3.1 ne signifie pas que chaque ancienne fiche a déjà été comparée individuellement à son équivalent actuel. Le gel éditorial des règles n’efface pas le travail de migration historique restant.

## A2. Règles d’identification

1. Chaque fiche possède un identifiant unique et permanent.
2. Un identifiant n’est jamais réattribué à un autre objectif.
3. Un changement mineur de formulation ne nécessite pas de nouvel identifiant.
4. Une scission d’objectif produit plusieurs nouvelles fiches et une entrée de migration.
5. Une fusion d’objectifs conserve la trace des anciens identifiants concernés.
6. Un objectif retiré est marqué « retiré » ; il n’est pas supprimé de l’historique.
7. Une fiche ajoutée au catalogue doit être inscrite avant d’être citée dans le graphe, la matrice ou un parcours.
8. Les identifiants des versions précédentes ne sont pas remappés automatiquement.

## A3. Typologie canonique

- **PR** : fiche principale.
- **REN** : renforcement ciblé.
- **PRO-R** : réinvestissement professionnel d’acquis.
- **PRO-N** : introduction d’une notion nouvelle en contexte professionnel.
- **SIT** : situation intégrée mobilisant plusieurs acquis.
- **ACT** : activité de manipulation, d’observation, de verbalisation ou de comparaison.
- **PLURI** : ressource transversale de vocabulaire, de compréhension des consignes ou d’accessibilité.

Une fiche peut comporter des aménagements plurilingues sans être classée PLURI. Une fiche professionnelle peut être de type SIT si sa fonction principale est l’intégration de plusieurs compétences.

## A4. Difficulté et politique de calculatrice

Les niveaux sont indépendants du type de fiche :

- 🟢 **Socle** : tâche essentielle, procédure guidée ou contexte familier.
- 🟠 **Renforcement** : plusieurs étapes, choix de procédure, autonomie ou contrôle.
- 🔵 **Approfondissement** : transfert, stratégie moins évidente, justification ou modélisation.

Chaque exercice précise la politique de calculatrice :
- interdite ;
- autorisée ;
- recommandée.

La politique est décidée selon l’objectif évalué. Si l’objectif est la technique opératoire, la calculatrice peut être interdite ; si l’objectif est la modélisation ou l’interprétation, elle peut être autorisée.

## A5. Principes pédagogiques

- Un objectif principal nouveau par fiche PR ou PRO-N.
- Une fiche SIT peut combiner plusieurs notions déjà étudiées.
- Les erreurs sont analysées à partir de la procédure observée ; elles ne sont pas attribuées automatiquement à une cause supposée.
- Les supports d’accessibilité sont proposés sans stigmatisation.
- Les corrections expliquent les étapes du raisonnement.
- Les critères RECTEC+ sont associés à un exercice précis et justifiés ; ils ne remplacent pas les niveaux de difficulté.
- Aucune durée obligatoire n’est assignée à une fiche.
- La validation peut reposer sur plusieurs réussites à des variantes, sans imposer une autoévaluation systématique.
- La mise en page indicative est de deux feuilles recto-verso, avec une page supplémentaire uniquement si elle apporte une ressource nécessaire.
- Le parcours est déterminé par le diagnostic et les besoins constatés, non par un ordre unique de fiches.

---

# Documents B et C — Périmètre des compléments intégrés

Les familles complémentaires PUI, FONC, STAT, GEO3 et ALGO ont été intégrées au catalogue maître et leurs dépendances au graphe des prérequis.

Le référentiel conserve la justification de leur présence et les règles de priorité :

- les notions de collège élargissent la couverture de la bibliothèque ;
- leur présence ne signifie pas qu’elles sont prioritaires pour tous les apprenants ;
- la priorité dépend du diagnostic, du diplôme visé et de la trajectoire de formation ;
- les applications professionnelles doivent rester distinguées des exigences explicites des référentiels scolaires ou professionnels.

Les identifiants et dépendances canoniques sont ceux du catalogue et du graphe. Toute modification future doit être effectuée dans ces fichiers, puis consignée dans le registre de contrôle.


# Document B — Compléments obligatoires au catalogue

## B1. PUI — Puissances et notation scientifique

| ID | Objectif principal | Type |
|---|---|---|
| PUI-01 | Comprendre une puissance comme produit de facteurs identiques | PR |
| PUI-02 | Calculer des puissances d’exposants entiers positifs dans des cas simples | PR |
| PUI-03 | Utiliser les puissances de 10 pour écrire des grands nombres | PR |
| PUI-04 | Utiliser les puissances de 10 pour écrire de petits nombres | PR |
| PUI-05 | Lire et écrire une notation scientifique dans des cas accessibles | PR |
| PUI-06 | Comparer des ordres de grandeur exprimés avec des puissances de 10 | REN |

**Prérequis directs indicatifs :**
- PUI-01 : CAL-03.
- PUI-02 : PUI-01, CAL-03.
- PUI-03 : NUM-03, CAL-10.
- PUI-04 : DEC-02, CAL-10.
- PUI-05 : PUI-03, PUI-04, DEC-04.
- PUI-06 : PUI-05, CAL-12.

**Règle de périmètre :** les puissances sont intégrées au catalogue, mais la priorité donnée à chaque fiche dépend du besoin de formation et du diplôme visé.

## B2. FONC — Fonctions et relations entre grandeurs

| ID | Objectif principal | Type |
|---|---|---|
| FONC-01 | Comprendre qu’une grandeur dépend d’une autre dans une situation concrète | PR |
| FONC-02 | Lire un tableau de valeurs associant deux grandeurs | PR |
| FONC-03 | Lire un graphique représentant une relation entre deux grandeurs | PR |
| FONC-04 | Calculer une valeur à partir d’une règle de calcul donnée | PR |
| FONC-05 | Comparer deux évolutions représentées dans un tableau ou un graphique | REN |
| FONC-06 | Distinguer une situation proportionnelle d’une relation non proportionnelle | PR |

**Prérequis directs indicatifs :**
- FONC-01 : PROP-01, DATA-01.
- FONC-02 : DATA-01, DATA-02.
- FONC-03 : DATA-04.
- FONC-04 : ALG-03, ALG-04.
- FONC-05 : DATA-05, FONC-02 ou FONC-03.
- FONC-06 : PROP-01, PROP-07.

Les fonctions ne sont pas un préalable général aux fiches professionnelles. Elles sont proposées lorsque leur étude est pertinente pour la trajectoire de formation.

## B3. STAT — Probabilités et hasard

| ID | Objectif principal | Type |
|---|---|---|
| STAT-01 | Identifier une expérience aléatoire dans une situation simple | PR |
| STAT-02 | Distinguer les issues possibles d’une expérience aléatoire | PR |
| STAT-03 | Comprendre une probabilité comme mesure de chance dans un cas simple | PR |
| STAT-04 | Calculer une probabilité dans une situation équiprobable simple | PR |
| STAT-05 | Interpréter une fréquence à partir de données observées | PR |
| STAT-06 | Distinguer fréquence observée et probabilité théorique | REN |

**Prérequis directs indicatifs :**
- STAT-01 : PROB-01.
- STAT-02 : STAT-01, NUM-10.
- STAT-03 : STAT-02, FRA-01.
- STAT-04 : STAT-03, CAL-04.
- STAT-05 : DATA-01, DATA-02.
- STAT-06 : STAT-04, STAT-05.

Ces fiches sont intégrées pour la couverture du programme du collège. Elles ne doivent pas être présentées comme des prérequis à la numératie professionnelle courante.

## B4. GEO3 — Géométrie dans l’espace

| ID | Objectif principal | Type |
|---|---|---|
| GEO3-01 | Reconnaître cube, pavé droit, prisme, cylindre, cône et sphère | PR |
| GEO3-02 | Identifier faces, arêtes et sommets d’un solide | PR |
| GEO3-03 | Relier un solide à une représentation plane simple | PR |
| GEO3-04 | Lire ou compléter un patron de cube ou de pavé droit | PR |
| GEO3-05 | Identifier les dimensions utiles au calcul d’un volume | PR |

**Prérequis directs indicatifs :**
- GEO3-01 : GEO-04, GEO-07.
- GEO3-02 : GEO3-01.
- GEO3-03 : GEO3-01, DATA-01 utile selon la représentation.
- GEO3-04 : GEO3-01, GEO3-02.
- GEO3-05 : GEO3-01, VOL-01.

Les solides et volumes sont distingués : reconnaître un solide n’implique pas de savoir calculer son volume.

## B5. ALGO — Algorithmique et procédures

| ID | Objectif principal | Type |
|---|---|---|
| ALGO-01 | Décrire une procédure sous forme d’étapes ordonnées | ACT |
| ALGO-02 | Identifier une répétition dans une procédure simple | PR |
| ALGO-03 | Comprendre une variable dans une procédure ou un programme simple | PR |
| ALGO-04 | Suivre un algorithme court et déterminer son résultat | PR |
| ALGO-05 | Repérer une erreur dans une procédure séquentielle simple | REN |

**Prérequis directs indicatifs :**
- ALGO-01 : COMM-03.
- ALGO-02 : ALGO-01.
- ALGO-03 : NUM-01, ALG-01.
- ALGO-04 : ALGO-01, CAL-01 à CAL-04 selon la procédure.
- ALGO-05 : ALGO-04, ACT-06.

L’algorithmique est une famille de couverture du programme scolaire ; elle ne doit être priorisée en Prépa Clé que selon les besoins identifiés.

---

# Document C — Graphe des dépendances : règles et compléments

## C1. Dépendances PUI
- PUI-01 dépend de CAL-03.
- PUI-02 dépend de PUI-01 et CAL-03.
- PUI-03 dépend de NUM-03 et CAL-10.
- PUI-04 dépend de DEC-02 et CAL-10.
- PUI-05 dépend de PUI-03, PUI-04 et DEC-04.
- PUI-06 dépend de PUI-05 et CAL-12.

## C2. Dépendances FONC
- FONC-01 dépend de PROP-01 et DATA-01.
- FONC-02 dépend de DATA-01 et DATA-02.
- FONC-03 dépend de DATA-04.
- FONC-04 dépend de ALG-03 et ALG-04.
- FONC-05 dépend de DATA-05 et de FONC-02 ou FONC-03.
- FONC-06 dépend de PROP-01 et PROP-07.

## C3. Dépendances STAT
- STAT-01 dépend de PROB-01.
- STAT-02 dépend de STAT-01 et NUM-10.
- STAT-03 dépend de STAT-02 et FRA-01.
- STAT-04 dépend de STAT-03 et CAL-04.
- STAT-05 dépend de DATA-01 et DATA-02.
- STAT-06 dépend de STAT-04 et STAT-05.

## C4. Dépendances GEO3
- GEO3-01 dépend de GEO-04 et GEO-07.
- GEO3-02 dépend de GEO3-01.
- GEO3-03 dépend de GEO3-01.
- GEO3-04 dépend de GEO3-01 et GEO3-02.
- GEO3-05 dépend de GEO3-01 et VOL-01.

## C5. Dépendances ALGO
- ALGO-01 dépend de COMM-03.
- ALGO-02 dépend de ALGO-01.
- ALGO-03 dépend de NUM-01 et ALG-01.
- ALGO-04 dépend de ALGO-01 et des opérations utilisées.
- ALGO-05 dépend de ALGO-04 et ACT-06.

## C6. Contrôle des cycles

À chaque changement du catalogue ou du graphe :
1. vérifier que chaque prérequis existe ;
2. vérifier qu’aucun identifiant n’est dupliqué ;
3. rechercher les cycles dans le graphe orienté ;
4. vérifier qu’une fiche SIT ne devient pas un prérequis universel ;
5. vérifier que les supports PLURI ne deviennent pas des prérequis mathématiques ;
6. vérifier que les prérequis sont nécessaires ou utiles et ne sont pas seulement des associations thématiques.

Une dépendance circulaire indique soit une erreur de modélisation, soit une notion qui doit être décomposée en étapes plus élémentaires.

---

# Document D — Matrice de couverture et traçabilité

## D1. Sources de référence

| Code | Source | Usage |
|---|---|---|
| REG | Référentiel régional Prépa Clé transmis dans le projet | Périmètre principal et compétences visées |
| CLEA21 | Référentiel CléA 2021, domaine 2 | Socle de numératie et critères d’évaluation |
| C2-2024 | Programme officiel de mathématiques du cycle 2 | Consolidation des fondamentaux |
| C3-2025 | Programme officiel de mathématiques du cycle 3 | Nombres, calcul, proportionnalité, mesures, espace, données |
| C4-2026 | Programme officiel de mathématiques du cycle 4 | Approfondissement collège ; application progressive |
| CAP-2019 | Programme de mathématiques du CAP et groupements applicables | Compétences communes et exigences du diplôme |
| AGR-JP | Référentiel professionnel du CAPa Jardinier-paysagiste | Contextes professionnels de plantation, implantation et entretien |
| RECTEC+ | Référentiel de compétences transversales mobilisé dans le projet | Repérage justifié des compétences par exercice |

## D2. Matrice de couverture thématique

| Domaine de compétence | Familles principales | Usage prioritaire |
|---|---|---|
| Nombres entiers, décimaux et relatifs | NUM, DEC, REL | REG, CLEA21, collège |
| Opérations et contrôle du résultat | CAL, PROB | REG, CLEA21, CAP |
| Divisibilité, facteurs et fractions | DIV, FRA | REG, collège, selon besoins |
| Proportionnalité et pourcentages | PROP, PCT | REG, CLEA21, CAP, métiers |
| Mesures, instruments et conversions | MES, UNIT | REG, CLEA21, CAP |
| Temps et plannings | TEM | REG, CLEA21, CAP, métiers |
| Géométrie plane et tracés | GEO, TRA | REG, collège, CAP selon spécialité |
| Périmètres et aires | PER, AIR | REG, CLEA21, CAP, espaces verts |
| Volumes et solides | VOL, GEO3 | REG, CLEA21, CAP selon spécialité |
| Plans, échelles et orientation | ESP | REG, CAP, agriculture et paysage |
| Tableaux, graphiques et données | DATA | REG, CLEA21, collège, CAP |
| Calcul littéral et équations | ALG | Collège et parcours de formation pertinents |
| Puissances et notation scientifique | PUI | Collège ; priorité à déterminer selon le parcours |
| Fonctions | FONC | Collège ; priorité à déterminer selon le parcours |
| Probabilités | STAT | Collège ; priorité à déterminer selon le parcours |
| Algorithmique | ALGO | Collège ; priorité à déterminer selon le parcours |
| Résolution de problèmes | PROB, SIT | Tous les domaines |
| Communication du raisonnement | COMM, ACT | REG, CLEA21 |
| Gestion et comptabilité | GEST | Réinvestissement professionnel ciblé |
| Agriculture et espaces verts | AGR | Réinvestissement professionnel ciblé |
| Langue et accessibilité | PLURI | Transversal à toutes les familles |

## D3. Règles de traçabilité

Pour chaque critère du référentiel régional ou du CléA, la matrice finale doit contenir :
- le libellé du critère ;
- sa source et, si possible, son numéro ou sa section ;
- les identifiants de fiches qui contribuent à ce critère ;
- la nature de la contribution : enseignement, entraînement, transfert ou évaluation ;
- le statut de la correspondance : vérifiée, partielle ou à vérifier ;
- une remarque lorsqu’une compétence est couverte par plusieurs fiches.

Pour les programmes du collège et du CAP, la traçabilité doit distinguer :
1. la notion explicitement inscrite au programme ;
2. la compétence de résolution de problèmes qui permet de la mobiliser ;
3. le contexte professionnel utilisé pour le réinvestissement ;
4. l’approfondissement optionnel qui n’est pas nécessairement exigé pour tous les parcours.

Une fiche AGR qui mobilise une proportionnalité ne devient pas pour autant une exigence réglementaire propre au diplôme agricole : elle constitue une application professionnelle d’un outil mathématique.

---

# Document E — Registre de migration des anciens identifiants

## E1. Règle de migration

Aucun ancien identifiant ne doit être transformé automatiquement à partir de son seul préfixe. La migration est effectuée en comparant l’ancien objectif, le contenu de la fiche, ses prérequis et sa fonction pédagogique.

## E2. Table à remplir à partir des archives

| Version source | Ancien ID | Ancien objectif | ID cible v3.x | Type de migration | État |
|---|---|---|---|---|---|
| 1.1 | À relever dans l’archive | À comparer | À établir | Conservation / scission / fusion / retrait | À vérifier |
| 2.1 | À relever dans l’archive | À comparer | À établir | Conservation / scission / fusion / retrait | À vérifier |
| 2.2 | À relever dans l’archive | À comparer | À établir | Conservation / scission / fusion / retrait | À vérifier |
| 2.3 | À relever dans l’archive | À comparer | À établir | Conservation / scission / fusion / retrait | À vérifier |

## E2 bis. Migration ciblée des anciennes familles GAV et ESP

**Règle :** les identifiants de la matrice V1.0 ci-dessous sont des identifiants historiques. Ils ne doivent pas être utilisés comme identifiants canoniques du catalogue V3.0.

### Ancienne famille GAV — périmètres, aires et volumes

| Ancien ID V1.0 | Objectif ancien | Identifiants cibles proposés | État |
|---|---|---|---|
| GAV-01 | Calculer le périmètre d’un polygone | PER-03 | À vérifier |
| GAV-02 | Calculer le périmètre d’un carré ou d’un rectangle | PER-02 | À vérifier |
| GAV-03 | Calculer la circonférence d’un cercle | PER-04 | À vérifier |
| GAV-04 | Calculer l’aire d’un carré ou d’un rectangle | AIR-02, AIR-03 | À vérifier |
| GAV-05 | Calculer l’aire d’un triangle | AIR-04 | À vérifier |
| GAV-06 | Calculer l’aire d’un disque | AIR-09 | À vérifier |
| GAV-07 | Décomposer une figure complexe en figures simples | AIR-05 | À vérifier |
| GAV-08 | Calculer le volume d’un cube ou d’un pavé droit | VOL-02, VOL-03 | À vérifier |
| GAV-09 | Calculer le volume d’un cylindre | VOL-04 | À vérifier |
| GAV-10 | Comprendre le volume d’une sphère | VOL-09 | À vérifier |
| GAV-11 | Relier volume et capacité | VOL-06, UNIT-07 | À vérifier |
| GAV-12 | Calculer une longueur, une aire ou un volume manquant | ALG-05 ou ALG-07 et famille géométrique concernée | Correspondance à décomposer |
| GAV-13 | Estimer et contrôler un résultat géométrique | CAL-12, CAL-13, PROB-07 | À vérifier |
| GAV-14 | Calculer des surfaces de terrain | AIR-02, AIR-03, AIR-05, AGR-09 | À vérifier |
| GAV-15 | Calculer des volumes de terre, de paillage ou de matériaux | AGR-14 et VOL-02 ou VOL-04 selon la forme | À vérifier |
| GAV-16 | Calculer une longueur de clôture ou de bordure | PER-05, AGR-10 | À vérifier |
| GAV-17 | Déterminer un nombre d’objets à répartir sur une longueur ou une surface | AGR-03 à AGR-08 selon la situation | À vérifier |

### Ancienne famille ESP de la matrice V1.0 — intervalles et implantation

**Attention :** cette famille ESP historique ne correspond pas à la famille `ESP` du catalogue actuel, qui concerne le repérage, les plans et les cartes.

| Ancien ID V1.0 | Objectif ancien | Identifiants cibles proposés | État |
|---|---|---|---|
| ESP-01 | Calculer le nombre d’intervalles sur une ligne | AGR-03 | À vérifier |
| ESP-02 | Déterminer le nombre d’arbres alignés, arbre aux deux extrémités | AGR-04 | À vérifier |
| ESP-03 | Déterminer le nombre d’arbres avec retrait aux extrémités | AGR-06 | À vérifier |
| ESP-04 | Planter autour d’un lac ou d’un contour fermé | AGR-05 | À vérifier |
| ESP-05 | Comparer plusieurs écartements possibles | AGR-07, AGR-19 | Correspondance à confirmer |
| ESP-06 | Répartir des piquets, lampes, bornes ou supports | AGR-03, AGR-04 ou AGR-07 selon la situation | Correspondance à confirmer |
| ESP-07 | Calculer le nombre de rangées sur une parcelle | AGR-02 | À vérifier |
| ESP-08 | Calculer le nombre de plants par rangée puis sur la parcelle | AGR-01, AGR-04 | Correspondance à confirmer |
| ESP-09 | Calculer une densité de plantation | AGR-08 | À vérifier |
| ESP-10 | Calculer une longueur de rangée ou une distance entre plants | AGR-03, AGR-07 | Correspondance à confirmer |
| ESP-11 | Prévoir une quantité de plants avec marge | PCT-04, AGR-19 ou SIT-09 selon la situation | Correspondance à confirmer |
| ESP-12 | Lire un plan de plantation ou d’implantation | AGR-11, AGR-12 | À vérifier |

### Conditions de validation

Une correspondance ne devient « vérifiée » qu’après comparaison de l’objectif ancien avec l’objectif cible et contrôle des éléments suivants :

- la compétence mathématique réellement travaillée ;
- les conditions de la situation, notamment ligne ouverte, boucle fermée et retraits aux extrémités ;
- les prérequis ;
- la fonction pédagogique de la fiche ;
- les éventuelles notions présentes dans l’ancien objectif mais absentes de la fiche cible.

Si une ancienne fiche couvre plusieurs objectifs désormais séparés, la migration doit mentionner une scission. Si plusieurs anciens objectifs sont réunis dans une seule fiche actuelle, la fusion doit être justifiée.

Cette table est une aide à la migration et non une preuve de couverture exhaustive des anciennes matrices.

## E3. Critères d’acceptation d’une migration

Une ligne est marquée « vérifiée » uniquement si :
- l’ancien identifiant existe bien dans une archive ;
- l’objectif ancien est disponible et lisible ;
- l’objectif cible est défini dans le catalogue actuel ;
- la correspondance est justifiée ;
- une scission ou une fusion est explicitement documentée ;
- les références au graphe, aux matrices et aux fiches sont mises à jour.

Tant que les archives ne sont pas comparées ligne par ligne, la migration historique ne peut pas être déclarée terminée.

---

# Document F — Registre des contrôles et état de gel

## F1. État des contrôles

| Contrôle | État | Preuve attendue |
|---|---|---|
| Unicité des identifiants du catalogue | À vérifier automatiquement sur le fichier consolidé | Liste des doublons, résultat nul attendu |
| Existence de toutes les références du graphe | À vérifier automatiquement | Liste des identifiants inconnus, résultat nul attendu |
| Absence de cycles dans le graphe | À vérifier automatiquement | Rapport de parcours du graphe |
| Correspondance catalogue / matrice | Partielle | Chaque ID de matrice doit exister dans le catalogue |
| Couverture thématique du référentiel régional | Représentée | Relecture des cinq domaines |
| Couverture du CléA 2021 domaine 2 | Représentée | Comparaison critère par critère |
| Couverture des programmes officiels collège | Familles élargies ; correspondance détaillée à vérifier | Tableau de traçabilité par programme et par cycle |
| Couverture des groupements CAP | À préciser selon les diplômes cibles | Matrice par groupement de spécialités |
| Applications agricoles et paysagères | Représentées | Comparaison avec les capacités et modules du référentiel professionnel |
| Calculatrice par exercice | À renseigner lors de la rédaction | Champ obligatoire dans chaque exercice |
| RECTEC+ par exercice | À renseigner lors de la rédaction | Badge accompagné d’une justification |
| Migration des anciens identifiants | Non finalisée | Table E2 remplie et contrôlée |
| Validation par les apprenants | À réaliser sur le terrain | Journal d’observations et versions révisées |

## F2. Critères de gel définitif

Le catalogue et le graphe sont gelés au sens documentaire lorsqu’aucun changement de périmètre ou d’identifiant n’est en cours. Ils ne sont déclarés **entièrement vérifiés** qu’après obtention des preuves suivantes :

1. rapport automatique confirmant l’unicité des identifiants ;
2. rapport confirmant que chaque dépendance pointe vers un identifiant existant ;
3. rapport confirmant l’absence de cycle dans le graphe ;
4. matrice de couverture reliée aux libellés des sources ;
5. table de migration renseignée et contrôlée ;
6. versionnage des fichiers et journal des changements ;
7. validation pédagogique après utilisation des prototypes.

Le statut « à vérifier » ne doit jamais être remplacé par « validé » pour des raisons de présentation.

---

# Document G — Sources officielles et portée de leur usage

1. **CléA 2021 — Référentiel du domaine 2**  
   https://www.certificat-clea.fr/media/2021/07/Referentiel-Clea_2021.pdf  
   Usage : critères de numératie et compétences de base.

2. **Programme officiel de mathématiques du cycle 2 — BO 2024**  
   https://www.education.gouv.fr/bo/2024/Hebdo41/MENE2415135A  
   Usage : consolidation des fondamentaux.

3. **Programme officiel de mathématiques du cycle 3 — BO 2025**  
   https://www.education.gouv.fr/bo/2025/Hebdo16/MENE2504620A  
   Usage : consolidation et extension des notions de numération, calcul, proportionnalité, grandeurs et mesures, espace et données.

4. **Programme officiel de mathématiques du cycle 4 — BO 2026**  
   https://www.education.gouv.fr/bo/2026/Hebdo10/MENE2602912A  
   Usage : notions de collège ; application progressive en 5e, 4e et 3e selon le calendrier réglementaire.

5. **Éduscol — Programmes et ressources de mathématiques en voie professionnelle**  
   https://eduscol.education.gouv.fr/5895/programmes-et-ressources-en-mathematiques-voie-professionnelle  
   Usage : programmes de CAP, groupements de spécialités et ressources associées.

6. **ChloroFil — CAPa Jardinier-paysagiste, ressources d’examen**  
   https://chlorofil.fr/diplomes/secondaire/capa/jp/capa-jp-exam  
   Usage : référentiel professionnel et documents complémentaires pour les contextes de paysage.

7. **ChloroFil — Référentiels des diplômes agricoles**  
   https://chlorofil.fr/diplomes/secondaire/ref-rncp  
   Usage : vérification des applications professionnelles en fonction du diplôme visé.

8. **Dépôt de travail du projet**  
   https://github.com/maristudy/divers  
   Contexte : https://github.com/maristudy/divers/blob/master/contexte%20prepa%20cle.txt  
   Référentiel : https://github.com/maristudy/divers/blob/master/referentiel_prepa_cle.txt

Les textes officiels fixent les attendus de leurs périmètres respectifs. Les fiches professionnelles, les aides de langue, les niveaux de difficulté et les parcours individualisés relèvent de la conception pédagogique du dispositif et ne doivent pas être présentés comme des prescriptions officielles lorsqu’ils ne le sont pas.

---

# Décision de gouvernance — état de consolidation

## 1. Documents de référence retenus

À l’issue de la consolidation, les quatre documents actifs seront :

1. **Référentiel maître** : périmètre, sources, matrice de traçabilité et règles de conception.
2. **Catalogue maître des fiches** : identifiants canoniques, objectifs, familles, types et niveaux.
3. **Graphe des prérequis** : dépendances entre les fiches du catalogue et vue fonctionnelle des parcours.
4. **Registre de contrôle et de migration** : résultats des contrôles, anomalies, décisions, historique des identifiants et validation terrain.

Aucun autre document ne doit servir de source de vérité concurrente pour ces informations.

## 2. État actuel

| Élément | État documentaire |
|---|---|
| Périmètre pédagogique général | Défini ; traçabilité exhaustive encore à établir |
| Catalogue V3.0-candidate | Base de travail existante, avec addendum intégré |
| Familles supplémentaires PUI, FONC, STAT, GEO3 et ALGO | Définies dans ce référentiel ; intégration au catalogue à effectuer |
| Graphe des prérequis | Base détaillée existante ; intégration des familles supplémentaires et contrôles complets à effectuer |
| Matrice de traçabilité | Plusieurs versions disponibles ; correspondances à remapper vers les identifiants retenus |
| Migration des anciennes versions | Non finalisée |
| Validation pédagogique en situation réelle | À réaliser au fil des tests des fiches |

## 3. Documents historiques à consolider puis à archiver

Les documents suivants ne doivent plus être entretenus séparément une fois leurs éléments utiles transférés et vérifiés :

- Matrice des référentiels V0.2 ;
- Matrice maîtresse V1.0 ;
- Bloc 1 — matrice de traçabilité V2.3 ;
- Bloc 2 — contrôle des programmes et contextes professionnels V2.3 ;
- Bloc 3 — migration des identifiants V1.1 vers V2.2 ;
- Bloc 5 — registre de validation V2.3 ;
- Contrôle qualité du catalogue et du graphe V3.0-candidate ;
- Carte des prérequis V2.2.

Leur archivage ne vaut pas validation de leur contenu. Les informations transférées doivent être vérifiées, et les anciens identifiants doivent rester consultables pour préserver la traçabilité historique.

## 4. Conditions de validation finale

Le catalogue et le graphe ne pourront être déclarés techniquement vérifiés qu’après :

1. contrôle de l’unicité des identifiants ;
2. vérification de l’existence de chaque identifiant référencé dans le graphe ;
3. recherche de cycles dans les dépendances ;
4. intégration et contrôle des familles supplémentaires ;
5. rapprochement de la matrice avec les identifiants canoniques ;
6. mise à jour du registre de migration ;
7. conservation des résultats des contrôles effectués.

La couverture exhaustive des référentiels et la validation pédagogique sur le terrain constituent des contrôles distincts. Le gel éditorial ne vaut pas preuve de leur achèvement.