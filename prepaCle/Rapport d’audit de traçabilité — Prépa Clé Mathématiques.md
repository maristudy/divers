# Rapport d’audit de traçabilité — Prépa Clé Mathématiques

**Version :** 1.0  
**Date :** 10 octobre 2026  
**Périmètre :** matrice de traçabilité, catalogue maître et sources de référentiels  
**Statut :** audit documentaire intermédiaire — gel définitif non prononcé

## 1. Objet de l’audit

Le présent rapport définit et consigne les contrôles nécessaires pour fiabiliser la matrice de traçabilité de Prépa Clé Mathématiques.

L’audit porte sur quatre dimensions :

1. la validité documentaire des sources ;
2. l’exactitude des correspondances entre critères et fiches ;
3. la cohérence des identifiants et des libellés ;
4. la qualité structurelle du Markdown.

Ce rapport ne prétend pas valider des correspondances dont le référentiel primaire n’a pas encore été retrouvé.

## 2. État documentaire

### 2.1. Référentiel régional

La Région Bretagne confirme l’existence du domaine relatif aux règles de base du calcul et au raisonnement mathématique dans PRÉPA Clés.

La documentation institutionnelle consultée ne suffit cependant pas à établir le texte exact de tous les critères régionaux utilisés dans la matrice.

**Conclusion :** validation régionale détaillée suspendue à l’identification de la source primaire.

### 2.2. Référentiel CléA

Les documents nationaux consultés comportent des critères numérotés relatifs aux opérations, aux problèmes, aux pourcentages, aux grandeurs et mesures, ainsi qu’à la restitution orale du raisonnement mathématique.

La matrice doit citer une version déterminée et conserver les libellés correspondants à cette version.

**Conclusion :** contrôle de la section CléA réalisable à partir d’une version identifiée, à condition de vérifier chaque libellé dans le document original retenu.

## 3. Anomalies et points de contrôle

Les éléments ci-dessous constituent des points d’audit à résoudre. Ils ne doivent pas être interprétés comme la preuve que chaque anomalie est encore présente dans la version locale la plus récente.

### 3.1. Intégrité des tableaux Markdown

Des extraits de la matrice examinée présentent des lignes de tableau séparées de leur en-tête par des lignes vides, ainsi que des barres verticales isolées.

Risques :

- tableaux rendus en plusieurs blocs ;
- données interprétées comme du texte courant ;
- association incorrecte entre critères et identifiants ;
- perte de lisibilité et difficultés de maintenance.

**Action :** remettre chaque tableau en un bloc continu, avec une ligne d’en-tête, une ligne de séparation Markdown et toutes les lignes de données consécutives.

Exemple de structure attendue :

| Critère | Attendu | Fiches associées | Couverture | Justification |
|---|---|---|---|---|
| Identifiant vérifié | Libellé exact de la source | Identifiants existants | D, P, C ou V | Justification concise |

Supprimer les lignes contenant uniquement `|` et vérifier les cellules contenant des barres verticales dans le texte.

### 3.2. Couverture de la lecture et de l’écriture des nombres

Le rattachement de la lecture et de l’écriture des nombres entiers à des fiches consacrées à la valeur de position ou aux classes de nombres doit être justifié.

Un contenu consacré aux unités, dizaines, centaines ou classes de nombres peut constituer un prérequis. Il ne démontre pas automatiquement l’ensemble de la compétence de lecture et d’écriture.

**Action :**

- distinguer la lecture et l’écriture proprement dites ;
- identifier séparément la valeur de position ;
- identifier la lecture des grands nombres en contexte ;
- distinguer l’écriture en chiffres et en lettres si le catalogue les traite séparément ;
- classer en couverture directe uniquement les fiches qui travaillent réellement l’attendu.

### 3.3. Arrondis, estimation et contrôle de plausibilité

Les compétences d’arrondi, d’estimation et de contrôle de plausibilité sont liées, mais ne sont pas interchangeables.

**Action :**

- rattacher l’arrondi au rang demandé à la fiche qui le travaille explicitement ;
- rattacher l’estimation au contenu qui demande d’anticiper un ordre de grandeur ;
- rattacher le contrôle de plausibilité aux activités où le résultat est comparé à une estimation, à une situation ou à une autre méthode ;
- ne pas utiliser un identifiant portant sur l’estimation pour couvrir automatiquement toutes les techniques d’arrondi.

### 3.4. Opérations sur les fractions

Les opérations effectivement couvertes par les fiches doivent être distinguées des opérations qui ne figurent pas dans le catalogue.

**Action :**

- vérifier la présence des additions et soustractions de fractions ;
- distinguer les cas à dénominateurs identiques et différents ;
- vérifier le traitement des fractions équivalentes et de la simplification ;
- ne pas attribuer une couverture directe de la multiplication ou de la division de fractions si le catalogue ne contient pas de fiche correspondante ;
- signaler explicitement les lacunes au lieu de les masquer par des fiches voisines.

### 3.5. Périmètres, aires et volumes

Les notions de contour, d’aire, de volume et les formules associées doivent être distinguées.

**Action :**

- contrôler séparément les périmètres des polygones et la circonférence du cercle ;
- contrôler séparément les aires des figures planes ;
- vérifier les conversions d’unités d’aire et de volume ;
- distinguer les formules de volume des solides et les relations entre volume et capacité ;
- ne déclarer la couverture d’une formule que si son utilisation est réellement travaillée dans la fiche.

La présence d’un identifiant relatif à un solide ne prouve pas, à elle seule, que tous les calculs de volume attendus sont couverts.

### 3.6. Exploitation d’une échelle

Un même attendu relatif à l’échelle peut apparaître plusieurs fois dans les tableaux.

**Action :**

- conserver une ligne par critère source distinct ;
- supprimer les doublons accidentels ;
- si plusieurs contextes sont pédagogiquement distincts, préciser cette différence ;
- vérifier que les identifiants associés existent et correspondent à la lecture, au calcul ou à l’utilisation de l’échelle annoncée.

### 3.7. Critères CléA du domaine mathématique

La section CléA doit être vérifiée à partir d’un document national précisément identifié.

Points à contrôler :

- opérations sur les nombres ;
- résolution de problèmes ;
- pourcentages ;
- périmètres, surfaces et volumes ;
- lecture ou interprétation de données, lorsque le critère source l’exige ;
- restitution orale du raisonnement ;
- reformulation d’un calcul présenté par autrui ;
- transmission claire d’un calcul ;
- vocabulaire mathématique de base.

**Action :** pour chaque critère, enregistrer le numéro exact, le libellé officiel, les attendus d’évaluation pertinents, les fiches associées et la justification du niveau de couverture.

Ne pas fusionner deux critères sous une seule ligne si cette fusion empêche de vérifier leur couverture respective.

### 3.8. Couverture directe et soutien pédagogique

Une fiche de vocabulaire, de communication ou de représentation peut soutenir une compétence mathématique sans suffire à la démontrer.

**Action :**

- réserver la catégorie directe à une correspondance explicite ;
- classer comme partielle une couverture incomplète ;
- classer comme complémentaire les prérequis et supports ;
- classer comme à vérifier les correspondances qui dépendent encore de la source ou du contenu réel de la fiche.

### 3.9. Validité des identifiants

La matrice ne doit contenir aucun identifiant absent du catalogue maître retenu.

**Action :**

- extraire la liste des identifiants du catalogue ;
- extraire la liste des identifiants cités dans la matrice ;
- rechercher les identifiants absents du catalogue ;
- rechercher les identifiants dupliqués ou mal orthographiés ;
- vérifier les libellés des identifiants existants ;
- traiter séparément les codes de référentiel externe et les codes de fiches internes.

Un code externe ne doit jamais être confondu avec un identifiant de fiche.

## 4. Contrôles automatisables

Les contrôles suivants peuvent être automatisés par un script ou une procédure de vérification.

| Contrôle | Résultat attendu |
|---|---|
| Tous les identifiants internes existent dans le catalogue | Aucune référence inconnue |
| Tous les codes cités suivent la convention de nommage | Aucune anomalie de format non expliquée |
| Aucun tableau ne comporte de ligne séparatrice isolée | Aucun tableau cassé |
| Aucun en-tête de tableau n’est séparé de ses données par une ligne vide | Structure Markdown continue |
| Les critères externes ont un libellé et une source | Aucune correspondance sans référence |
| Chaque correspondance a un statut D, P, C, V ou NC | Aucune couverture implicite |
| Les doublons de critères sont justifiés | Aucun doublon accidentel |
| Les versions des référentiels sont explicites | Aucune ambiguïté de version |
| Les lacunes sont consignées | Aucun manque dissimulé |

Ces contrôles automatisés ne peuvent pas décider seuls si une correspondance pédagogique est pertinente. Une vérification humaine du contenu des fiches reste nécessaire.

## 5. Structure minimale attendue pour la matrice

Chaque ligne de correspondance doit comporter, lorsque l’information est disponible :

| Champ | Fonction |
|---|---|
| Référentiel | Identifier la source |
| Version | Identifier l’édition utilisée |
| Code du critère | Permettre la recherche dans la source |
| Libellé officiel | Conserver le texte exact ou une citation clairement signalée |
| Identifiants des fiches | Relier l’attendu au catalogue |
| Statut de couverture | D, P, C, V ou NC |
| Justification | Expliquer le lien entre la fiche et l’attendu |
| Réserve | Documenter les limites éventuelles |

Une ligne sans source identifiée ou sans justification ne doit pas être considérée comme validée.

## 6. Ordre recommandé des opérations

1. Identifier le document primaire régional et sa version.
2. Identifier la version CléA retenue et vérifier ses critères.
3. Contrôler les identifiants du catalogue maître.
4. Contrôler la couverture des critères, fiche par fiche.
5. Corriger les correspondances directes, partielles et complémentaires.
6. Réparer les tableaux Markdown et supprimer les doublons accidentels.
7. Effectuer une lecture croisée entre la matrice, le catalogue et les sources.
8. Mettre à jour les versions et l’historique.
9. Prononcer le gel uniquement après résolution des points bloquants.

## 7. Conditions de gel définitif

La matrice peut être gelée lorsque :

- la source régionale détaillée est identifiée ou que l’absence de grille publique détaillée est explicitement documentée et que la matrice ne prétend pas reproduire des critères introuvables ;
- les sources nationales sont versionnées ;
- les libellés externes sont exacts ;
- tous les identifiants internes sont valides ;
- chaque correspondance est justifiée ;
- les lacunes et couvertures partielles sont visibles ;
- les tableaux Markdown sont corrects ;
- les doublons ont été traités ;
- le contrôle final ne fait apparaître aucune anomalie bloquante.

Si la source régionale détaillée demeure indisponible, le document peut être publié comme matrice de travail contrôlée, mais pas comme traçabilité régionale intégralement vérifiée.

## 8. Conclusion de l’audit

L’audit met en évidence une distinction essentielle : la confirmation institutionnelle du dispositif PRÉPA Clés ne constitue pas une validation des correspondances détaillées de la matrice.

Le référentiel CléA peut être contrôlé séparément à partir d’une version nationale identifiée. Les correspondances régionales détaillées restent conditionnées par l’identification et la vérification du document primaire applicable.

Le statut approprié à ce stade est donc :

**Audit intermédiaire — corrections structurelles et vérifications documentaires à finaliser — gel définitif non prononcé.**
