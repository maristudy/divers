# Référentiel maître des fiches de mathématiques — Prépa Clé - v3.1

**Version documentaire : 3.1**  
**Date : 10 octobre 2026**  
**Statut :** gel de structure visé ; périmètre et règles de gestion stabilisés. Les contrôles techniques et la traçabilité exhaustive restent à compléter.

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
| 3.0 — gel de structure | Référence du catalogue et du graphe | Identifiants, familles, objectifs et dépendances stabilisés ; contrôles techniques exhaustifs restant à consigner |
|3.1 | version documentaire de gouvernance | Règles de gestion, périmètre, traçabilité et état global des contrôles| 3.1 | Référence de gouvernance | Règles de gestion, périmètre, compléments de couverture, traçabilité et état des contrôles |

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

# Documents B et C — Périmètre des compléments et gouvernance du graphe

## B. Périmètre des compléments intégrés

Les familles complémentaires PUI, FONC, STAT, GEO3 et ALGO sont intégrées au catalogue maître et leurs dépendances au graphe des prérequis.

Leur présence élargit la couverture de la bibliothèque ; elle ne signifie pas qu’elles sont prioritaires pour tous les apprenants. La priorité dépend du diagnostic, du diplôme visé et de la trajectoire de formation.

Les applications professionnelles doivent rester distinguées des exigences explicites des référentiels scolaires ou professionnels.

Les identifiants, objectifs et types canoniques sont définis dans le catalogue. Les dépendances canoniques sont définies dans le graphe. Le présent référentiel conserve la justification de ces choix et les règles de gouvernance, sans reproduire les listes détaillées.

## C. Gouvernance du graphe des prérequis

Le graphe des prérequis est la référence unique pour les dépendances entre les fiches du catalogue maître.

À chaque modification du catalogue ou du graphe, les contrôles suivants doivent être réalisés :

1. vérifier que chaque prérequis correspond à un identifiant existant ;
2. vérifier l’unicité des identifiants du catalogue ;
3. rechercher les cycles dans le graphe orienté ;
4. vérifier qu’une fiche SIT ne devient pas un prérequis universel ;
5. vérifier que les supports PLURI ne deviennent pas des prérequis mathématiques ;
6. vérifier que les dépendances sont pédagogiquement justifiées et ne correspondent pas à de simples associations thématiques.

Une dépendance circulaire doit être examinée : elle peut signaler une erreur de modélisation ou la nécessité de décomposer une notion en étapes plus élémentaires.

Les résultats des contrôles sont consignés dans le Document F. Le présent référentiel ne constitue pas une seconde version du catalogue ou du graphe.


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

### État des contrôles avant gel de structure

| Contrôle | État | Suite prévue |
|---|---|---|
| Unicité des identifiants du catalogue | Contrôle automatique non exécuté | À exécuter lors de la phase de validation technique |
| Validité des références du graphe | Contrôle automatique non exécuté | À exécuter lors de la phase de validation technique |
| Détection des cycles du graphe | Contrôle non exécuté | À exécuter lors de la phase de validation technique |
| Cohérence catalogue–graphe | Cohérence documentaire examinée, contrôle exhaustif non exécuté | À confirmer lors des contrôles techniques |
| Matrice de traçabilité | Examen partiel | Poursuivre la vérification des correspondances |
| Migration des anciennes versions | Non finalisée | Traiter séparément, sans présumer d’équivalences historiques |
| Validation pédagogique en situation réelle | À réaliser | Tester les fiches avec les apprenants |

Le gel de structure porte sur l’organisation du référentiel et la stabilisation de ses documents de référence. Il ne vaut ni validation technique des contrôles non exécutés, ni validation exhaustive de la traçabilité, ni validation pédagogique.
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
### Décision de gel de structure

Le périmètre documentaire, les familles, les identifiants, les objectifs principaux et les dépendances du catalogue Prépa Clé sont stabilisés pour la phase de validation technique et pédagogique.

Les documents canoniques sont :
- le référentiel maître pour la gouvernance et l’état global des contrôles ;
- le catalogue maître pour les identifiants, les familles et les objectifs ;
- le graphe des prérequis pour les dépendances ;
- la matrice de traçabilité v0.2 pour les correspondances avec les référentiels sources.

La matrice maîtresse v1.0 et les autres documents historiques sont conservés pour la traçabilité, sans constituer des sources concurrentes.

Ce gel de structure ne vaut pas validation technique : les contrôles automatiques d’unicité des identifiants, de validité des références et d’absence de cycles restent à exécuter. La vérification exhaustive de la matrice, la migration historique et la validation pédagogique demeurent des travaux distincts.

Toute modification ultérieure touchant aux identifiants, aux familles, aux objectifs ou aux dépendances devra être justifiée, tracée et répercutée dans les documents canoniques concernés.

## F3. Contrôles métier et limites de couverture

### Implantation et dénombrement

Les situations d’implantation doivent distinguer :

- **Ligne ouverte avec les deux extrémités occupées :** le nombre de plants est égal au nombre d’intervalles augmenté d’un.
- **Contour fermé :** lorsque le dernier intervalle rejoint le premier plant, le nombre de plants est égal au nombre d’intervalles ; il ne faut pas compter deux fois le point de départ.
- **Retrait aux extrémités :** calculer d’abord la longueur disponible entre les retraits, puis déterminer le nombre d’intervalles et de plants.
- **Rangées et densité :** distinguer le nombre de plants sur une rangée, le nombre de rangées et la quantité calculée à partir d’une densité surfacique.

Les fiches concernées doivent conserver ces distinctions dans leurs objectifs et leurs exercices.

### Parcours et couverture

Le graphe sert à construire des parcours individualisés. Il ne définit pas un cursus linéaire obligatoire. Le point d’entrée doit être déterminé à partir des acquis constatés, du diagnostic, du diplôme visé et des besoins de formation.

La couverture thématique signifie que les familles de notions pertinentes sont représentées. Elle ne prouve pas que chaque critère d’un référentiel officiel est intégralement couvert, ni que les fiches ont été testées en situation réelle.

### Statut des contrôles

Aucun contrôle automatique ne doit être déclaré réussi sans conserver son résultat. Les vérifications d’unicité des identifiants, d’existence des références du graphe et d’absence de cycles doivent être consignées avec la date, la version contrôlée et le résultat obtenu.

La migration historique, la traçabilité officielle et la validation pédagogique en situation réelle restent des chantiers distincts du gel de structure.
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

- **Catalogue maître** : source canonique des identifiants, familles et objectifs des fiches.
- **Graphe des prérequis** : source canonique des dépendances entre les fiches.
- **Matrice de traçabilité v0.2** : source de référence pour les correspondances entre les référentiels sources et les objectifs du catalogue ; correspondances en cours de vérification.
- **Matrice maîtresse v1.0** : document distinct conservé pour comparaison historique jusqu’à vérification de son contenu ; ne pas l’utiliser comme source concurrente du catalogue ou de la matrice v0.2.
- **Archive qualité** : document historique conservé sans modification ; les décisions et statuts courants sont consignés dans le référentiel maître.


## 2. État actuel

| Élément | État documentaire |
|---|---|
| Périmètre pédagogique général | Défini ; la traçabilité exhaustive des référentiels reste à établir |
| Catalogue maître v3.0 | Structure stabilisée ; contrôles techniques restant à exécuter |
| Familles complémentaires PUI, FONC, STAT, GEO3 et ALGO | Intégrées au catalogue maître et au graphe |
| Graphe des prérequis v3.0 | Structure stabilisée ; validité exhaustive des références et absence de cycles restant à vérifier |
| Matrice de traçabilité v0.2 | Document actif de référence pour les correspondances ; examen partiel, vérification à poursuivre |
| Matrice maîtresse v1.0 | Document distinct conservé pour comparaison historique jusqu’à vérification de son contenu ; ne pas utiliser comme source concurrente |
| Contrôles techniques | Non exécutés pour l’unicité des identifiants, les références du graphe et les cycles |
| Archive qualité | Conservée à titre historique ; ne pas modifier ni utiliser comme registre actif |
| Migration des anciennes versions | Non finalisée ; aucune équivalence historique ne doit être présumée sans comparaison |
| Validation pédagogique en situation réelle | À réaliser au fil des tests des fiches |

## 3. Documents historiques et archives

Les documents suivants sont conservés pour préserver la traçabilité historique. Ils ne constituent pas des sources de vérité courantes :

- Matrice maîtresse des référentiels mathématiques v1.0, jusqu’à vérification de son contenu et comparaison avec la matrice v0.2 ;
- Bloc 1 — matrice de traçabilité V2.3 ;
- Bloc 2 — contrôle des programmes et contextes professionnels V2.3 ;
- Bloc 3 — migration des identifiants V1.1 vers V2.2 ;
- Bloc 5 — registre de validation V2.3 ;
- Archive qualité du catalogue et du graphe ;
- Carte des prérequis V2.2.

La matrice des référentiels v0.2 reste le document actif de traçabilité. Sa vérification n’est pas achevée.

L’archivage d’un document ne vaut pas validation de son contenu. Les informations historiques utiles doivent rester consultables et les correspondances entre anciens et nouveaux identifiants ne peuvent être déclarées validées qu’après comparaison.

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