# Contrôle qualité du catalogue et du graphe — v3.0-candidate

## 1. Résultats des contrôles

| Contrôle | Résultat | Décision |
|---|---|---|
| Identifiants du catalogue | Les identifiants du catalogue et de l’addendum sont uniques | Validé pour cette version |
| Références du graphe | Les références utilisées correspondent aux familles et identifiants déclarés, y compris les quatre ajouts | Validé sur la liste de dépendances |
| Dépendances sans définition | Aucune référence inconnue repérée dans le graphe présenté | Validé |
| Cohérence type / niveau | Le type de PROB-09 a été corrigé : SIT est son type ; approfondissement est son niveau | Corrigé |
| Couverture des cinq domaines régionaux | Toutes les grandes compétences décrites dans les éléments régionaux fournis sont représentées | Couverture thématique validée |
| Couverture du domaine 2 du CléA | Nombres, opérations, dénombrement, ordre de grandeur, proportionnalité, pourcentages, temps, mesures, données, géométrie, espace et communication sont représentés | Couverture thématique validée |
| Mesures et géométrie | Longueurs, masses, capacités, durées, aires, périmètres, volumes et instruments sont représentés | Complété, dont aire du disque et volume de la sphère |
| Espaces verts | Espacement sur ligne ouverte, contour fermé, retrait aux extrémités, densité, surfaces et implantation sont séparés | Validé sur les notions explicitement demandées |
| Calculatrice | Règle de décision prévue exercice par exercice | À renseigner à la rédaction des fiches |
| RECTEC+ | Prévu à l’échelle de l’exercice avec justification | À renseigner à la rédaction des fiches |
| Traçabilité officielle exhaustive | La correspondance notion par notion avec chaque libellé officiel n’a pas été reprise ici à partir de l’intégralité de chaque texte source | À distinguer de la couverture thématique |
| Migration des anciens identifiants | Les versions antérieures n’ont pas encore de table de correspondance individuelle complète | Ne pas effectuer de renommage automatique |

## 2. Matrice de couverture des référentiels

Cette matrice indique où les exigences sont principalement traitées. Elle ne signifie pas que chaque compétence officielle est déjà validée par une fiche rédigée et testée.

| Référentiel ou domaine | Familles principales | État de couverture |
|---|---|---|
| Régional — Domaine 1 : nombres, calcul, proportionnalité | NUM, DEC, REL, DIV, CAL, FRA, PROP, PCT | Représenté |
| Régional — Domaine 2 : problèmes et opérations | PROB, CAL, REL, FRA, PCT, COMM | Représenté |
| Régional — Domaine 3 : unités, temps, données et géométrie | MES, UNIT, TEM, DATA, GEO, TRA, PER, AIR, VOL | Représenté |
| Régional — Domaine 4 : espace, cartes et plans | ESP, UNIT, TRA, AGR | Représenté |
| Régional — Domaine 5 : restitution du raisonnement | COMM, PROB, ACT, SIT | Représenté |
| CléA — Se repérer dans l’univers des nombres | NUM, DEC, REL, DIV, CAL, FRA | Représenté |
| CléA — Résoudre des problèmes et utiliser des pourcentages | PROB, CAL, PROP, PCT, FRA | Représenté |
| CléA — Unités, temps, mesures, instruments et données | MES, UNIT, TEM, DATA | Représenté |
| CléA — Périmètres, surfaces et volumes | PER, AIR, VOL | Représenté, sous réserve du contrôle final des formules et des unités |
| CléA — Plans, cartes et diagrammes | ESP, DATA | Représenté |
| CléA — Raisonnement oral | COMM, ACT, SIT | Représenté |
| Programmes du collège | Familles de nombres, calcul, fractions, proportionnalité, géométrie, données, algèbre et résolution de problèmes | Couverture large ; correspondance précise aux attendus de chaque cycle à contrôler séparément |
| Programmes de CAP | Compétences mathématiques mobilisables dans les différentes situations de formation | Couverture transversale ; les exigences propres à chaque groupement de CAP ne sont pas réputées vérifiées par cette seule matrice |
| Référentiels agricoles et paysagers | AGR, GEST, SIT, ESP, MES, UNIT, TEM, PROP, PCT, PER, AIR, VOL | Contextes professionnels représentés ; vérifier chaque application par rapport au diplôme visé |

## 3. Contrôle particulier : implantation et espacements

Les erreurs de comptage des plants ou arbres ne doivent pas être traitées comme un seul exercice indifférencié.

### Ligne ouverte : plantation le long d’un chemin
Si les deux extrémités sont occupées et si l’écart entre plants est constant :

\[
\text{nombre de plants}=\text{nombre d’intervalles}+1
\]

Pour une longueur exactement divisible par l’espacement, le nombre d’intervalles est égal à la longueur divisée par l’espacement.

### Contour fermé : plantation autour d’un lac
Si le dernier intervalle rejoint le premier plant et que la disposition est régulière, le nombre de plants est égal au nombre d’intervalles. Il ne faut pas ajouter un plant pour « fermer » le contour.

### Extrémités avec retrait
Si une distance est imposée entre chaque extrémité et le premier ou le dernier plant, la longueur disponible pour répartir les intervalles doit être calculée avant le dénombrement.

### Rangées et densité
Le nombre de plants sur une rangée et le nombre de rangées sont deux calculs distincts. Une densité exprimée par unité de surface relève d’une autre relation encore. Les fiches AGR-01 à AGR-08 et SIT-05/SIT-09 doivent conserver cette distinction.

## 4. Contrôle des dépendances et parcours

Le graphe est destiné à générer des parcours individualisés, pas un cursus linéaire unique.

### Parcours « nombres et calcul »
NUM → DEC → CAL → contrôle du résultat → PROB

### Parcours « fractions et proportionnalité »
FRA → équivalences et dénominateurs communs → opérations sur les fractions → PROP → PCT

### Parcours « temps de travail »
Lecture de l’heure → conversion en durée → calcul d’une heure de fin ou d’une durée → multiplication par une cadence → planning professionnel

### Parcours « mesure et géométrie »
Mesure avec instrument → unités → propriétés géométriques → tracés → périmètre/aire/volume → problème appliqué

### Parcours « plan et implantation »
Lecture de plan → échelle et unités → coordonnées ou repères → espacement des plants → surface ou contour → quantités et contrôle

### Parcours « gestion »
Opérations et unités → lecture de facture → prix unitaire et total → pourcentages → contrôle des montants → situations de gestion

Ces parcours sont des exemples d’utilisation. Le point d’entrée réel doit être décidé à partir des acquis constatés, et non à partir du seul nombre de séances suivies.

## 5. Migration depuis les versions précédentes

### Règle générale
Les versions 1.1, 2.1, 2.2 et 2.3 restent archivées. Elles ne doivent plus être modifiées comme si elles étaient la source courante.

### Règle de correspondance
- **Correspondance exacte :** un ancien identifiant peut pointer vers un identifiant v3.0 si l’objectif est strictement identique.
- **Scission :** si une ancienne fiche couvrait plusieurs notions désormais séparées, l’ancien identifiant doit pointer vers plusieurs nouvelles fiches, sans prétendre qu’il existe une équivalence univoque.
- **Fusion :** si plusieurs anciennes fiches deviennent une seule fiche, chaque ancien identifiant doit être mentionné dans la table de migration.
- **Remplacement :** si l’objectif a changé, l’ancien identifiant est marqué comme remplacé et ne doit pas être réutilisé silencieusement.
- **Non vérifié :** tant que le contenu précis de l’ancienne fiche n’a pas été comparé, la correspondance reste « à vérifier ».

### Table de migration à maintenir
| Ancien ID | Ancien objectif | Nouvel ID | Opération | Vérifié par |
|---|---|---|---|---|
| À renseigner | À reprendre de la version archivée | À renseigner | Conservation / scission / fusion / remplacement | À renseigner |

Cette table doit être remplie par comparaison des anciens intitulés et contenus, pas en déduisant une équivalence du seul préfixe.

## 6. Règles de gel du graphe

Le graphe v3.0 peut servir de **référence de conception**. Pour le considérer comme gelé au sens strict, appliquer les règles suivantes :

1. Tout nouvel identifiant doit être créé dans le catalogue avant d’être utilisé dans le graphe.
2. Toute suppression ou modification d’objectif doit être accompagnée d’une entrée dans le journal des changements.
3. Les dépendances doivent rester directes : éviter d’ajouter tous les prérequis lointains d’une fiche lorsque les prérequis intermédiaires suffisent.
4. Une dépendance n’est pas une obligation de parcours ; le diagnostic et les variantes de fiche restent possibles.
5. Les fiches SIT ne doivent pas être introduites automatiquement dans les prérequis des notions fondamentales.
6. Les supports PLURI ne sont jamais imposés comme prérequis mathématiques.
7. Toute nouvelle fiche doit être vérifiée contre le graphe afin de détecter une dépendance circulaire.
8. Les parcours issus du graphe doivent pouvoir être raccourcis ou adaptés selon les résultats observés en séance.

## 7. Journal des changements de cette consolidation

- Abandon des versions 2.2 et 2.3 comme références canoniques en raison d’identifiants non définis ou incohérents.
- Création d’une base candidate v3.0 structurée par familles.
- Décomposition explicite des notions identifiées comme sources de difficultés : décomposition des entiers, zéros des décimaux, signes des relatifs, dénominateurs communs, calculs de durées et utilisation des instruments.
- Ajout des notions de divisibilité, facteurs, calcul de pourcentages appliqués et gestion.
- Décomposition des espacements en espaces verts selon les configurations géométriques.
- Ajout de l’aire du disque, du volume de la sphère et de la lecture des régions et départements.
- Établissement d’une liste de dépendances directes pour construire les parcours.
- Maintien explicite du statut « à vérifier » pour la correspondance individuelle entre les anciens identifiants et les nouveaux.

## 8. Statut final à enregistrer dans le dépôt

- **Catalogue v3.0-candidate :** base de référence pour la rédaction des prochaines fiches.
- **Graphe v3.0-candidate :** base de référence pour les parcours, sous réserve de maintenir le contrôle des dépendances à chaque évolution.
- **Matrice de couverture :** validée au niveau thématique ; elle ne remplace pas une vérification ligne par ligne de chaque texte officiel.
- **Migration des anciennes versions :** non finalisée au niveau individuel ; aucun ancien identifiant ne doit être remappé automatiquement.
- **Validation terrain :** à effectuer au fur et à mesure de l’utilisation des fiches, avec journal de révision.

