# Prépa Clé — Bloc 5 - registre de validation et décisions avant production des fiches - v2.3

**Version : 2.3 — registre qualité**  
**Rôle : suivre les corrections, les vérifications documentaires et les décisions restant à prendre.**

## 1. Registre des corrections issues de l’audit

| ID | Point contrôlé | Décision | Statut |
|---|---|---|---|
| AUD-01 | Décomposition additive des entiers | Entrée explicite NUM-07 | Intégré à V2.2 |
| AUD-02 | Décomposition multiplicative des entiers | Entrée explicite NUM-08 | Intégré à V2.2 |
| AUD-03 | Zéros terminaux et internes dans les décimaux | Entrée explicite DEC-06 | Intégré à V2.2 |
| AUD-04 | Distance à zéro et opposés | REL-03 et REL-04 séparés | Intégré à V2.2 |
| AUD-05 | Signe d’un nombre et signe d’une opération | REL-06 | Intégré à V2.2 |
| AUD-06 | Critères de divisibilité | DIV-02 et DIV-03 | Intégré à V2.2 |
| AUD-07 | Décomposition en facteurs premiers | DIV-04 | Intégré à V2.2 |
| AUD-08 | Simplification des fractions | FRA-07 et DIV-05 | Intégré à V2.2 |
| AUD-09 | Dénominateur commun par plusieurs méthodes | FRA-08 et FRA-09 | Intégré à V2.2 |
| AUD-10 | Calcul d’une durée entre deux horaires | TEM-03 | Intégré à V2.2 |
| AUD-11 | Calcul de l’heure de fin | TEM-04 | Intégré à V2.2 |
| AUD-12 | Calcul de l’heure de départ | TEM-05 | Intégré à V2.2 |
| AUD-13 | Multiplication d’une durée répétée | TEM-07 | Intégré à V2.2 |
| AUD-14 | Instruments de géométrie | TRA-01 à TRA-09 | Intégré à V2.2 |
| AUD-15 | Volume de la sphère | VOL-06 | Entrée ajoutée ; niveau à vérifier |
| AUD-16 | Repérage des régions et départements français | ESP-11 | Intégré à V2.2 |
| AUD-17 | Espacement sur ligne ouverte | AGR-08 | Intégré à V2.2 |
| AUD-18 | Espacement sur boucle fermée | AGR-09 | Intégré à V2.2 |
| AUD-19 | Plantation en rangées | AGR-10 | Intégré à V2.2 |
| AUD-20 | Densité de plantation et de semis | AGR-11 | Intégré à V2.2 |
| AUD-21 | Retraits et espacement irrégulier | AGR-13 | Intégré à V2.2 |
| AUD-22 | Pourcentages dans les situations professionnelles | PCT-01 à PCT-12 | Famille renforcée |
| AUD-23 | Applications de gestion et comptabilité | GEST-01 à GEST-07 | Famille conditionnelle selon le parcours |
| AUD-24 | Stabilité des identifiants | Plan de migration distinct | Non clos |
| AUD-25 | Correspondance exacte avec chaque critère source | Matrice de traçabilité préparée | À valider sur les textes complets |
| AUD-26 | Validation de terrain | Prévue après production de prototypes | À réaliser |

## 2. Contrôle qualité d’une fiche avant publication

Une fiche ne devrait être considérée comme prête à tester que si les points suivants ont été examinés.

### A. Objectif et rattachement

- [ ] L’objectif principal est formulé en une phrase observable.
- [ ] L’identifiant de catalogue correspond réellement à cet objectif.
- [ ] Le type de fiche est indiqué : PR, REN, PRO-R, PRO-N, SIT, ACT ou PLURI.
- [ ] Les critères régionaux ou CléA concernés sont référencés.
- [ ] Les liens aux programmes scolaires ou professionnels sont qualifiés : exigence explicite, prérequis, approfondissement ou application.

### B. Conception pédagogique

- [ ] La fiche n’introduit pas plusieurs notions nouvelles sans justification.
- [ ] Les prérequis nécessaires sont identifiés.
- [ ] Les exercices progressent de façon lisible.
- [ ] Les consignes ne reposent pas uniquement sur des mots-clés.
- [ ] Les erreurs fréquentes sont anticipées sans attribuer une cause à l’apprenant.
- [ ] Une procédure ou une justification peut être observée.

### C. Accessibilité

- [ ] La mise en page est suffisamment aérée.
- [ ] Les consignes peuvent être reformulées ou lues si nécessaire.
- [ ] Les symboles, unités et termes techniques sont explicités lorsque cela aide.
- [ ] Les supports visuels contribuent au raisonnement et ne sont pas purement décoratifs.
- [ ] Les aides sont proposées à tous, sans assigner un profil à l’apprenant.

### D. Calculatrice et contrôle

- [ ] L’usage de la calculatrice est précisé pour chaque exercice.
- [ ] Les unités attendues sont explicites.
- [ ] Les ordres de grandeur sont mobilisés quand ils sont pertinents.
- [ ] Les réponses attendues ont été vérifiées.
- [ ] Les variantes ont été contrôlées pour éviter les résultats ambigus.

### E. Corrigé et évaluation

- [ ] Le corrigé explique les étapes du raisonnement.
- [ ] Les erreurs possibles sont distinguées : compréhension, choix de méthode, calcul, unité, lecture ou interprétation.
- [ ] Les compétences RECTEC+ sont associées aux exercices précis et justifiées.
- [ ] Le niveau indicatif est cohérent avec la tâche réelle.
- [ ] La fiche prévoit un moyen de vérifier le transfert, si nécessaire.

### F. Gestion documentaire

- [ ] La version de la fiche est renseignée.
- [ ] Le corrigé porte la même référence de version.
- [ ] Les anciens identifiants sont conservés dans l’historique si la fiche est migrée.
- [ ] Les liens internes vers le catalogue et les prérequis sont à jour.
- [ ] Les retours de test sont consignés.

---

## 3. Organisation recommandée du dépôt GitHub

La structure suivante permet de maintenir le catalogue et les fiches sans mélanger référentiels, contenus apprenants et corrigés.

```text
divers/
├── contexte prepa cle.txt
├── referentiel_prepa_cle.txt
├── catalogue/
│   ├── catalogue_fiches_v2.2.md
│   ├── matrice_regional_clea_v2.3.md
│   ├── carte_prerequis_v2.3.md
│   ├── migration_v1.1_vers_v2.2.md
│   └── registre_validation_v2.3.md
├── sources/
│   ├── sources_referentiels.md
│   └── decisions_interpretation.md
├── fiches/
│   ├── NUM/
│   ├── DEC/
│   ├── REL/
│   ├── CAL/
│   ├── DIV/
│   ├── FRA/
│   ├── PROP/
│   ├── PCT/
│   ├── MES/
│   ├── UNIT/
│   ├── TEM/
│   ├── GEO/
│   ├── TRA/
│   ├── PER/
│   ├── AIR/
│   ├── VOL/
│   ├── ESP/
│   ├── DATA/
│   ├── ALG/
│   ├── PROB/
│   ├── COMM/
│   ├── GEST/
│   ├── AGR/
│   └── SIT/
└── corriges/
    └── mêmes familles et identifiants que les fiches
```

Cette structure est une proposition. Il n’est pas nécessaire de créer tous les répertoires immédiatement : ils peuvent être ajoutés lorsque les premières fiches de chaque famille existent.

## 4. Décisions documentaires à ne pas masquer

### D-01 — Exhaustivité des référentiels

La matrice ci-dessus couvre les compétences régionales et les critères CléA consignés dans le dossier de travail. Elle ne doit pas être présentée comme une transcription exhaustive de chaque ligne de tous les programmes du collège, de tous les groupements de CAP et de tous les référentiels professionnels.

**Action requise :** conserver les formulations sources exactes et établir, pour chaque entrée, la référence précise du texte et le statut de la correspondance.

### D-02 — Identifiants historiques

Les plages d’identifiants V1.1 et les familles de la V2.2 permettent d’établir un plan de migration, mais pas de prouver une correspondance exacte entre toutes les anciennes fiches et toutes les nouvelles entrées.

**Action requise :** reprendre chaque intitulé et chaque objectif V1.1 avant de clôturer la migration.

### D-03 — Contenus professionnels conditionnels

Les fiches sur la densité, les dosages, l’implantation, les volumes et la comptabilité doivent être adaptées au parcours réel de l’apprenant.

**Action requise :** documenter le contexte métier, les unités, les contraintes réelles et les compétences préalables pour chaque fiche professionnelle.

### D-04 — Volume de la sphère

La présence de `VOL-06` assure la visibilité de cette notion dans le catalogue. Le niveau de formule et le degré d’autonomie attendus doivent toutefois être vérifiés au regard des objectifs effectivement visés.

**Action requise :** décider si la fiche porte sur la reconnaissance de la formule, son application directe ou un approfondissement.

### D-05 — Compétences RECTEC+

Les badges ne doivent pas être assignés par famille entière ni déduits automatiquement du type de fiche.

**Action requise :** associer chaque compétence RECTEC+ à une tâche observable, avec une justification.

---

## 5. Décision de passage à la production

La base est suffisamment structurée pour commencer à produire des prototypes, à condition de ne pas confondre cette étape avec la validation documentaire finale.

Ordre de travail conseillé :

1. Finaliser la correspondance exacte des référentiels.
2. Migrer les fiches V1.1 existantes en conservant l’historique.
3. Sélectionner quelques prototypes de familles différentes : numération, fractions, pourcentages, temps, plan/échelle et implantation en espaces verts.
4. Faire relire les consignes, procédures et corrigés.
5. Tester les fiches avec des apprenants, puis noter les difficultés observées.
6. Réviser et versionner les fiches.
7. Étendre la production aux autres familles à partir des modèles validés.

**Statut global :** catalogue consolidé, matrice de couverture structurée, carte des prérequis organisée et procédure de migration définie. La validation documentaire exhaustive et la migration fiche par fiche restent des étapes distinctes à clore avant de déclarer l’ensemble définitif.