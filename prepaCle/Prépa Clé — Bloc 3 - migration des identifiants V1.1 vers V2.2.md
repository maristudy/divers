# Prépa Clé — Bloc 3 - migration des identifiants V1.1 vers V2.2

**Version : 2.3 — plan de migration conservateur**

## 1. Règle fondamentale

La migration doit préserver la traçabilité historique des fiches déjà créées. Un identifiant ne peut être conservé que si son sens reste identique.

La V2.2 est une consolidation : elle a réduit certaines séries, séparé plusieurs notions auparavant regroupées et renommé au moins une famille. Il serait donc dangereux d’appliquer automatiquement une règle telle que « ancien ID = nouvel ID portant le même numéro ».

Ce bloc fournit une **table de migration par famille et par cas de figure**. Il ne prétend pas être une correspondance exacte de chaque fiche ancienne : pour cela, chaque ancienne ligne doit être comparée à son intitulé et à son objectif précis.

## 2. Statuts de migration

| Code | Signification | Action |
|---|---|---|
| CONSERVÉ | Même objectif principal et même périmètre | Garder l’identifiant si aucune collision n’existe |
| RENOMMÉ | Même objectif, nouvelle convention d’identifiant | Mettre à jour les références |
| SCINDÉ | Une ancienne entrée recouvre plusieurs notions distinctes | Créer plusieurs nouvelles entrées et documenter le lien |
| FUSIONNÉ | Plusieurs anciennes entrées couvrent le même objectif | Choisir une entrée cible et conserver les anciennes références comme alias historiques |
| RECADRÉ | Objectif conservé, mais périmètre ou formulation précisés | Revoir la fiche et sa correspondance |
| À ARBITRER | L’intitulé ancien ne suffit pas à déterminer le lien | Comparer la fiche et son objectif avant de migrer |

## 3. Table de migration par famille

| Famille V1.1 | Série ancienne recensée | Famille(s) V2.2 | Traitement recommandé |
|---|---|---|---|
| NUM | NUM-01 à NUM-20 | NUM | **À arbitrer fiche par fiche** : la V2.2 distingue explicitement valeur positionnelle, décomposition additive et multiplicative |
| DEC | DEC-01 à DEC-18 | DEC | **À arbitrer** : plusieurs anciennes fiches peuvent se regrouper, mais les zéros terminaux et internes doivent être explicitement couverts |
| REL | REL-01 à REL-15 | REL | **À arbitrer** : séparer repérage, distance à zéro, opposés, comparaison et opérations |
| FRA | FRA-01 à FRA-24 | FRA, DIV | **Scission probable** : les contenus de divisibilité et de facteurs doivent être reliés à DIV sans perdre les objectifs propres aux fractions |
| CAL | CAL-01 à CAL-25 | CAL | **À arbitrer** : distinguer sens de l’opération, technique, automatismes, estimation et contrôle |
| PROP | PROP-01 à PROP-12 | PROP | **À arbitrer** : préserver les méthodes distinctes, notamment passage à l’unité, coefficient et situations non proportionnelles |
| PCT | PCT-01 à PCT-15 | PCT | **À arbitrer** : distinguer compréhension du taux, calcul d’une part, détermination d’un taux et recherche du tout |
| MES | MES-01 à MES-16 | MES, UNIT | **Scission possible** entre mesure/instrument et conversion d’unité |
| UNIT | UNIT-01 à UNIT-06 | UNIT, TEM, AIR, VOL | **À arbitrer** selon la grandeur : durée, longueur, aire, volume et capacité |
| TEM | TEM-01 à TEM-17 | TEM, UNIT | **À arbitrer** : lecture de l’heure, durée, heure de fin, heure de départ, durées répétées et planning doivent rester identifiables |
| GEO | GEO-01 à GEO-16 | GEO, TRA | **Scission possible** entre reconnaissance de propriétés et gestes de construction |
| TRA | TRA-01 à TRA-17 | TRA, GEO | **À arbitrer** : conserver les objectifs distincts sur règle, équerre, compas, rapporteur et programme de construction |
| GEO+ | GEO+-01 à GEO+-09 | GEO, TRA, ESP | **À arbitrer** : l’ancien intitulé et le contenu de chaque fiche doivent déterminer la famille cible |
| PER | PER-01 à PER-10 | PER | **À arbitrer** : préserver les formules et les procédures par figure |
| AIR | AIR-01 à AIR-11 | AIR | **À arbitrer** : séparer sens de l’aire, formule, conversion et estimation si ces objectifs étaient fusionnés |
| VOL | VOL-01 à VOL-10 | VOL | **À arbitrer** : conserver les solides/formes séparés ; ajouter VOL-06 pour la sphère si elle n’était pas couverte |
| ESP | ESP-01 à ESP-14 | ESP | **À arbitrer** : repérage, carte, coordonnées, itinéraire et échelle sont des tâches différentes |
| DATA | DATA-01 à DATA-16 | DATA | **À arbitrer** : séparer lecture, comparaison, organisation, représentation et détection d’erreurs |
| ALG | ALG-01 à ALG-12 | ALG | **À arbitrer** : conserver les notions réellement utiles et ne pas imposer tout l’algèbre à tous les parcours |
| PROB | PROB-01 à PROB-16 | PROB, SIT | **À arbitrer** : les méthodes de résolution restent distinctes des situations intégrées |
| SIT | SIT-01 à SIT-08 | SIT | **Réviser les objectifs** : garder une SIT si elle mobilise plusieurs notions déjà travaillées |
| COM | COM-01 à COM-14 | COMM, GEST | **Renommage partiel à contrôler** : COMM pour la communication mathématique ; GEST seulement pour les applications de gestion |
| AGR | AGR-01 à AGR-24 | AGR, ESP, MES, UNIT, PER, AIR, VOL, PROP, PCT | **À arbitrer** : conserver le contexte professionnel et relier chaque notion mathématique aux fiches fondamentales |
| TRANS | TRANS-01 à TRANS-15 | PLURI, COMM, PROB | **Renommage ou réaffectation à contrôler** : aide transversale, communication ou compréhension d’énoncé selon l’objectif réel |

## 4. Traitement des cas sensibles

### 4.1 FRA vers FRA et DIV

Une ancienne fiche de simplification peut comporter :
- la notion de fraction équivalente ;
- l’identification d’un diviseur commun ;
- des critères de divisibilité ;
- une décomposition en facteurs premiers.

Il ne faut pas automatiquement transformer cette fiche en quatre fiches. Il faut examiner son objectif principal et la charge cognitive demandée.

Règle :
- si l’objectif principal est la fraction équivalente ou la simplification, rattacher la fiche à FRA ;
- si l’objectif principal est l’utilisation d’un critère de divisibilité, rattacher à DIV ;
- si la fiche enseigne plusieurs notions nouvelles sans objectif principal clair, la scinder ou la réécrire.

### 4.2 MES et UNIT

La famille MES porte sur le choix et l’usage d’un instrument, la lecture d’une mesure et l’interprétation de la précision. La famille UNIT porte sur les relations entre unités et les conversions.

Une fiche de mesure de longueur peut mobiliser les deux, mais doit préciser lequel de ces apprentissages est l’objectif principal.

### 4.3 GEO et TRA

Reconnaître un triangle rectangle et construire un triangle rectangle ne sont pas le même objectif.

- GEO : reconnaître, nommer et comprendre les propriétés.
- TRA : réaliser le tracé avec les instruments appropriés.

Une fiche ancienne peut contribuer aux deux familles, mais le rattachement doit être documenté.

### 4.4 COM et GEST

L’ancienne famille COM ne doit pas être convertie intégralement en GEST. La communication mathématique devient COMM. Les fiches portant réellement sur factures, montants, tableaux de suivi et amortissement peuvent être rattachées à GEST.

### 4.5 AGR et familles mathématiques fondamentales

Une fiche AGR ne doit pas remplacer les fiches fondamentales auxquelles elle fait appel.

Exemple : une fiche de calcul de plants en rangées peut mobiliser la division, la multiplication et la mesure de longueur. Son rattachement principal peut être AGR-10, mais ses prérequis doivent pointer vers les fiches de calcul et de mesure pertinentes.

## 5. Procédure de migration à appliquer dans le dépôt

Pour chaque ancienne fiche :

1. Copier l’ancien identifiant et l’ancien intitulé sans les modifier.
2. Décrire en une phrase l’objectif principal effectivement enseigné.
3. Identifier les notions secondaires mobilisées.
4. Choisir l’identifiant cible V2.2 correspondant à l’objectif principal.
5. Ajouter d’autres liens si la fiche constitue un prérequis ou un réinvestissement.
6. Si l’ancienne fiche mélange plusieurs notions nouvelles, décider explicitement de la conserver, la scinder ou la réécrire.
7. Vérifier les références croisées dans les fichiers, les corrigés et les index.
8. Conserver une trace de la décision et de sa justification.

## 6. Modèle de table de migration

| Ancien ID | Ancien intitulé | Objectif réel | Nouvel ID principal | Liens secondaires | Décision | Justification |
|---|---|---|---|---|---|---|
| NUM-xx | À reprendre de la V1.1 | À examiner | À attribuer | À attribuer | À arbitrer | À documenter |
| FRA-xx | À reprendre de la V1.1 | À examiner | À attribuer | DIV-xx si nécessaire | À arbitrer | À documenter |
| MES-xx | À reprendre de la V1.1 | À examiner | À attribuer | UNIT-xx si nécessaire | À arbitrer | À documenter |
| GEO-xx | À reprendre de la V1.1 | À examiner | À attribuer | TRA-xx si nécessaire | À arbitrer | À documenter |
| COM-xx | À reprendre de la V1.1 | À examiner | COMM-xx ou GEST-xx | Selon la tâche | À arbitrer | À documenter |
| AGR-xx | À reprendre de la V1.1 | À examiner | AGR-xx ou famille fondamentale | Selon la tâche | À arbitrer | À documenter |

## 7. Critères pour clore la migration

La migration peut être déclarée terminée lorsque :

- chaque fiche existante dispose d’un nouvel identifiant principal ou d’un statut explicite de retrait ;
- aucune fiche n’a perdu son ancien identifiant historique ;
- chaque changement d’identifiant est justifié ;
- chaque fiche scindée possède un lien vers les fiches qui la remplacent ;
- les fiches fusionnées conservent les références historiques ;
- les références vers les corrigés et les index sont à jour ;
- les nouveaux identifiants DIV et les nouvelles entrées de volume et d’implantation ont été contrôlés ;
- les doublons éventuels sont documentés plutôt que supprimés silencieusement.

**Limite :** la table ci-dessus est une procédure de migration et un diagnostic par familles, pas une table de correspondance exhaustive ligne par ligne. Une migration exacte exige de reprendre les intitulés complets et les objectifs de chaque entrée V1.1 ; les seules plages d’identifiants ne suffisent pas à établir un lien fiable.