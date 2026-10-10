# Graphe des prérequis — v3.0-candidate
**Statut :** graphe de travail consolidé ; les identifiants pointent vers le catalogue maître v3.0-candidate et son addendum.

Le graphe est exprimé sous forme de liste d’adjacence pour rester lisible, diffable dans Git et exploitable pour construire des parcours individualisés. Une fiche indiquée comme « entrée possible » peut être proposée sans prérequis formel, notamment pour un diagnostic.

## 1. Numération, décimaux et calcul

### NUM — Nombres entiers
- NUM-01 : entrée possible.
- NUM-02 : NUM-01.
- NUM-03 : NUM-02.
- NUM-04 : NUM-02.
- NUM-05 : NUM-02, NUM-04.
- NUM-06 : NUM-04 ou NUM-05.
- NUM-07 : NUM-01.
- NUM-08 : NUM-07.
- NUM-09 : NUM-07.
- NUM-10 : entrée possible.
- NUM-11 : NUM-03.

### DEC — Nombres décimaux
- DEC-01 : NUM-01, NUM-02.
- DEC-02 : DEC-01.
- DEC-03 : DEC-02.
- DEC-04 : DEC-02.
- DEC-05 : DEC-04.
- DEC-06 : DEC-04.
- DEC-07 : DEC-01.
- DEC-08 : DEC-01, DEC-02.
- DEC-09 : DEC-04.
- DEC-10 : CAL-09 ou CAL-12.
- DEC-11 : DEC-01, UNIT-01 ou UNIT-02, CAL-05.

### REL — Nombres relatifs
- REL-01 : NUM-07.
- REL-02 : REL-01.
- REL-03 : REL-02.
- REL-04 : REL-02.
- REL-05 : REL-01.
- REL-06 : REL-01, CAL-01, CAL-02.
- REL-07 : REL-03, REL-05.
- REL-08 : REL-03, REL-05, CAL-02.
- REL-09 : REL-03, CAL-03, CAL-04.
- REL-10 : REL-07, REL-08 ; REL-09 si la situation comporte multiplication ou division.

### DIV — Divisibilité et facteurs
- DIV-01 : NUM-07, CAL-03.
- DIV-02 : DIV-01.
- DIV-03 : DIV-01, CAL-03.
- DIV-04 : DIV-01, DIV-02.
- DIV-05 : DIV-01, DIV-03 ; DIV-04 si l’on travaille la décomposition en facteurs premiers.

### CAL — Techniques opératoires
- CAL-01 : NUM-01.
- CAL-02 : NUM-01.
- CAL-03 : NUM-02, NUM-04.
- CAL-04 : CAL-03, NUM-07.
- CAL-05 : DEC-01, CAL-01, CAL-02.
- CAL-06 : DEC-01, CAL-03.
- CAL-07 : DEC-01, CAL-04.
- CAL-08 : CAL-01 à CAL-07, selon les opérations visées.
- CAL-09 : NUM-01, CAL-01, CAL-03.
- CAL-10 : NUM-02, DEC-02.
- CAL-11 : NUM-02, CAL-09.
- CAL-12 : NUM-07, DEC-04, CAL-09.
- CAL-13 : opération initiale correspondante parmi CAL-01 à CAL-07.
- CAL-14 : CAL-01, CAL-03 ; utiliser CAL-04 si l’expression comporte une division.

### FRA — Fractions
- FRA-01 : NUM-10 ; partage concret possible sans autre prérequis.
- FRA-02 : FRA-01.
- FRA-03 : FRA-01, FRA-02.
- FRA-04 : FRA-02, NUM-09.
- FRA-05 : FRA-01, FRA-03.
- FRA-06 : FRA-02, FRA-03.
- FRA-07 : FRA-02, DIV-01.
- FRA-08 : FRA-02, CAL-03, CAL-04.
- FRA-09 : FRA-02, FRA-06.
- FRA-10 : FRA-08, CAL-04.
- FRA-11 : FRA-02, FRA-06.
- FRA-12 : FRA-08, CAL-01, CAL-02.
- FRA-13 : FRA-02, DEC-01.
- FRA-14 : FRA-01, FRA-05 ; ajouter FRA-11 ou FRA-12 selon les opérations nécessaires.

### PROP — Proportionnalité
- PROP-01 : CAL-03, CAL-04 ; tableaux simples possibles à partir de données concrètes.
- PROP-02 : PROP-01.
- PROP-03 : CAL-04, PROP-01.
- PROP-04 : CAL-03, PROP-02.
- PROP-05 : PROP-02, PROP-03.
- PROP-06 : PROP-02, PROP-04 ou PROP-05.
- PROP-07 : PROP-02, PROP-06.
- PROP-08 : PROP-03, PROP-05 ou PROP-06 ; unités selon la situation.
- PROP-09 : PROP-03 ou PROP-04, UNIT-01 ; relier à ESP-07 pour les plans.

### PCT — Pourcentages
- PCT-01 : FRA-01, compréhension de « sur 100 ».
- PCT-02 : PCT-01, DEC-01, FRA-02.
- PCT-03 : PCT-01, CAL-09.
- PCT-04 : PCT-02, PROP-03 ou PROP-05.
- PCT-05 : PCT-02, PROP-03.
- PCT-06 : PCT-04, PROP-05 ou PROP-06.
- PCT-07 : PCT-04, CAL-01 ou CAL-02.
- PCT-08 : PCT-04, CAL-01, CAL-02.
- PCT-09 : PCT-08, PCT-04.
- PCT-10 : PCT-04, PCT-07 ; PCT-09 selon les offres.
- PCT-11 : PCT-04, PCT-07, GEST-01.
- PCT-12 : PCT-04, DATA-01 ou DATA-02.
- PCT-13 : PCT-04, PROP-08, UNIT-03 ; suivre les consignes de sécurité propres au produit.
- PCT-14 : PCT-02, PCT-08.

## 2. Mesures, temps et grandeurs

### MES — Instruments
- MES-01 : entrée possible par comparaison d’objets.
- MES-02 : MES-01.
- MES-03 : MES-01.
- MES-04 : MES-01.
- MES-05 : MES-02, MES-03 ou MES-04 selon l’instrument.
- MES-06 : MES-01.
- MES-07 : MES-05, MES-06.

### UNIT — Conversions
- UNIT-01 : NUM-01, DEC-01 ; MES-02 utile.
- UNIT-02 : NUM-01, DEC-01 ; MES-03 utile.
- UNIT-03 : NUM-01, DEC-01 ; MES-04 utile.
- UNIT-04 : UNIT-01 ; comprendre le lien entre longueur et aire.
- UNIT-05 : TEM-03.
- UNIT-06 : UNIT-01 à UNIT-05 selon l’unité visée.
- UNIT-07 : UNIT-03, VOL-01.

### TEM — Temps
- TEM-01 : entrée possible.
- TEM-02 : TEM-01 ; activité de lecture de cadran possible en parallèle.
- TEM-03 : TEM-01 ou TEM-02.
- TEM-04 : TEM-03, CAL-01.
- TEM-05 : TEM-03, CAL-02.
- TEM-06 : TEM-01 ou TEM-02, TEM-03 ; traiter séparément le passage de minuit si nécessaire.
- TEM-07 : TEM-03, CAL-01.
- TEM-08 : TEM-03, CAL-03.
- TEM-09 : TEM-04, TEM-05 ou TEM-06 ; DATA-01 si le planning est présenté en tableau.
- TEM-10 : TEM-01, TEM-03.
- TEM-11 : TEM-08, TEM-09 ; PROP-03 utile pour les cadences.

## 3. Géométrie, tracés, périmètres, aires et volumes

### GEO — Géométrie
- GEO-01 : entrée possible.
- GEO-02 : GEO-01.
- GEO-03 : GEO-01.
- GEO-04 : GEO-01.
- GEO-05 : GEO-04.
- GEO-06 : GEO-04.
- GEO-07 : GEO-01.
- GEO-08 : GEO-02, GEO-03, GEO-04 ou GEO-07 selon la construction.

### TRA — Tracés
- TRA-01 : GEO-01, MES-02.
- TRA-02 : GEO-01, GEO-02.
- TRA-03 : GEO-02, TRA-02.
- TRA-04 : GEO-07, MES-02.
- TRA-05 : TRA-01, GEO-07.
- TRA-06 : GEO-04, TRA-01 ; GEO-08 selon les données.
- TRA-07 : GEO-03.
- TRA-08 : TRA-07.
- TRA-09 : TRA-07, TRA-08.
- TRA-10 : TRA-01 à TRA-09 selon les instruments mobilisés.
- TRA-11 : TRA-01 à TRA-09 selon la construction à contrôler.

### PER — Périmètres
- PER-01 : GEO-01, NUM-10.
- PER-02 : PER-01, GEO-05, CAL-03.
- PER-03 : PER-01, CAL-01.
- PER-04 : PER-01, GEO-07, PROP-04 ; utiliser une formule fournie si nécessaire.
- PER-05 : PER-02 ou PER-03 ou PER-04, UNIT-01.
- PER-06 : PER-01, AIR-01.

### AIR — Aires
- AIR-01 : GEO-01 ; comparaison ou pavage de surfaces possible sans formule.
- AIR-02 : AIR-01, GEO-05, CAL-03.
- AIR-03 : AIR-01, GEO-05, CAL-03.
- AIR-04 : AIR-01, GEO-04, CAL-03, CAL-04.
- AIR-05 : AIR-02 ou AIR-03 ; calculs d’addition et de soustraction.
- AIR-06 : AIR-02 ou AIR-03, UNIT-04.
- AIR-07 : AIR-02 ou AIR-03 ou AIR-05, UNIT-04, PROP-03 selon la commande.
- AIR-08 : PER-01, AIR-01.
- AIR-09 : AIR-01, GEO-07, calcul numérique ; formule fournie ou mémorisée selon l’objectif.

### VOL — Volumes
- VOL-01 : UNIT-03 ; manipulation de contenants possible.
- VOL-02 : VOL-01, CAL-03.
- VOL-03 : VOL-01, VOL-02.
- VOL-04 : VOL-01, CAL-03, CAL-04, GEO-07 ; formule du cylindre disponible si nécessaire.
- VOL-05 : VOL-01, UNIT-03.
- VOL-06 : VOL-01, UNIT-03.
- VOL-07 : VOL-02 ou VOL-03 ou VOL-04 ou VOL-06, UNIT-03.
- VOL-08 : AIR-01, VOL-01.
- VOL-09 : VOL-01, calcul numérique ; formule fournie ou mémorisée selon l’objectif.

## 4. Espace, données et algèbre

### ESP — Plans et cartes
- ESP-01 : entrée possible.
- ESP-02 : ESP-01 utile ; un plan avec repères simples peut servir d’entrée diagnostique.
- ESP-03 : NUM-01 ; lecture de grille.
- ESP-04 : ESP-02 ou ESP-06.
- ESP-05 : ESP-04, COMM-01.
- ESP-06 : ESP-02, lecture de légende.
- ESP-07 : UNIT-01, PROP-01.
- ESP-08 : ESP-02, lecture de carte.
- ESP-09 : ESP-02, ESP-06 ou ESP-08.
- ESP-10 : ESP-02, ESP-03.
- ESP-11 : ESP-03, ESP-07 ; TRA-01 utile pour reporter des mesures.
- ESP-12 : ESP-04, ESP-07 ; TEM-04 ou TEM-06 si les horaires comptent.
- ESP-13 : ESP-08, ESP-09.
- ESP-14 : ESP-08, ESP-13 ; ESP-04 si l’itinéraire doit être décrit.

### DATA — Données
- DATA-01 : NUM-01, lecture de titres et d’étiquettes.
- DATA-02 : DATA-01.
- DATA-03 : DATA-01, NUM-07.
- DATA-04 : NUM-07, lecture d’axes et d’échelles.
- DATA-05 : DATA-01 ou DATA-03 ou DATA-04.
- DATA-06 : DATA-01, UNIT-06 ; DATA-03 ou DATA-04 selon le support.
- DATA-07 : DATA-01, classement des informations.
- DATA-08 : DATA-01, DATA-03 ou DATA-04.
- DATA-09 : DATA-01 ou DATA-02, unités adaptées au contexte.

### ALG — Algèbre
- ALG-01 : NUM-01, COMM-04.
- ALG-02 : ALG-01, PROB-01.
- ALG-03 : ALG-01, CAL-01 à CAL-07 selon l’expression.
- ALG-04 : ALG-03, compréhension des unités si la formule en comporte.
- ALG-05 : CAL-01 à CAL-04 ; ALG-01 utile.
- ALG-06 : ALG-01, ALG-02, CAL-01 à CAL-04.
- ALG-07 : ALG-04, ALG-05 ; ne proposer que si utile à la trajectoire de formation.

## 5. Résolution de problèmes et communication

### PROB — Problèmes
- PROB-01 : entrée possible ; lecture accompagnée possible.
- PROB-02 : PROB-01 ; PLURI-05 utile si le vocabulaire bloque.
- PROB-03 : PROB-01, PROB-02, CAL-01 à CAL-04 selon le problème.
- PROB-04 : PROB-03.
- PROB-05 : PROB-03, CAL-01 à CAL-04.
- PROB-06 : PROB-01 ; DATA-01, ESP-03 ou GEO-01 selon la représentation choisie.
- PROB-07 : CAL-12, CAL-13.
- PROB-08 : PROB-01, PROB-02.
- PROB-09 : PROB-01, PROB-03, PROB-06, PROB-07.

### COMM — Communication
- COMM-01 : PROB-01.
- COMM-02 : CAL-01 à CAL-07 selon le calcul expliqué.
- COMM-03 : COMM-02.
- COMM-04 : vocabulaire travaillé dans les familles concernées ; PLURI-01 à PLURI-05 en soutien.
- COMM-05 : COMM-02, UNIT-06 si une unité est attendue.
- COMM-06 : COMM-02, COMM-04.
- COMM-07 : COMM-03, PROB-03, PROB-07.

## 6. Réinvestissements professionnels et situations intégrées

### GEST — Gestion et comptabilité
- GEST-01 : CAL-01, CAL-03, DATA-01 ; lecture des libellés.
- GEST-02 : GEST-01, CAL-03, CAL-04.
- GEST-03 : GEST-01, PCT-04 ; PCT-07 selon le contexte.
- GEST-04 : GEST-01, CAL-13, CAL-12.
- GEST-05 : DATA-01, DATA-02, CAL-01.
- GEST-06 : TEM-03, CAL-01 ; PROP-03 selon la répartition.
- GEST-07 : GEST-05, PCT-04 si un taux est utilisé ; la règle d’amortissement doit être fournie ou explicitement enseignée.
- GEST-08 : GEST-01, GEST-02, PCT-10.

### AGR — Agriculture et espaces verts
- AGR-01 : CAL-03, CAL-04 ; PROP-03 si le calcul utilise une quantité unitaire.
- AGR-02 : UNIT-01, CAL-04, PROP-03 ; plan ou mesures de terrain selon le cas.
- AGR-03 : CAL-01, CAL-04 ; distinction entre plants et intervalles à enseigner explicitement.
- AGR-04 : AGR-03.
- AGR-05 : AGR-03, GEO-07 ou compréhension d’un contour fermé ; expliquer pourquoi il n’y a pas de plant supplémentaire au point de fermeture.
- AGR-06 : AGR-03, UNIT-01.
- AGR-07 : UNIT-01, CAL-04, PROP-03.
- AGR-08 : AIR-02 ou AIR-03, UNIT-04, PROP-03.
- AGR-09 : AIR-02 ou AIR-03 ou AIR-05, UNIT-04.
- AGR-10 : PER-02 ou PER-03, UNIT-01.
- AGR-11 : ESP-02, ESP-09.
- AGR-12 : ESP-07, UNIT-01.
- AGR-13 : PROP-05 ou PROP-06, UNIT-03 ; PCT-04 si le dosage est exprimé en pourcentage.
- AGR-14 : VOL-02 ou VOL-03 ou VOL-04 selon la forme, UNIT-03 ou UNIT-05 selon les données.
- AGR-15 : TEM-08 ou TEM-11 ; unités de débit à définir selon le contexte.
- AGR-16 : UNIT-01 à UNIT-05 selon les mesures du chantier.
- AGR-17 : MES-05, DATA-01.
- AGR-18 : AGR-11, AGR-16, TEM-09 ; autres fiches selon les contraintes du chantier.
- AGR-19 : AGR-01 ou AGR-08, CAL-12.
- AGR-20 : GEST-02, AGR-09 ou AGR-10 selon les postes de coût.
- AGR-21 : UNIT-01, PROP-01 ; une notion de pente est enseignée si elle n’a pas été vue.
- AGR-22 : ESP-03, ESP-10, TRA-01.
- AGR-23 : DATA-01, DATA-05, PROP-03 selon le calcul de rendement.
- AGR-24 : AGR-11, AGR-16, AGR-18, PROB-05.

### SIT — Situations intégrées
- SIT-01 : PROB-05, CAL-12 ; GEST-02 selon les données.
- SIT-02 : ESP-04, ESP-07, TEM-04 ou TEM-06.
- SIT-03 : GEST-01, GEST-02, PCT-04.
- SIT-04 : AIR-02 ou AIR-03 ou AIR-05, UNIT-04, PROP-03 selon les quantités.
- SIT-05 : AGR-01, AGR-02, AGR-03 ou AGR-05, AGR-11.
- SIT-06 : TEM-08, TEM-09 ou TEM-11.
- SIT-07 : DATA-01, DATA-05 ou DATA-06, COMM-03.
- SIT-08 : PROB-05, COMM-02, COMM-03, COMM-05.
- SIT-09 : AGR-03, AGR-05 ou AGR-06, AGR-08, AGR-11.

### ACT — Activités
- ACT-01 : entrée possible.
- ACT-02 : CAL-01 à CAL-07 selon les procédures comparées.
- ACT-03 : MES-01, MES-05 ou MES-06.
- ACT-04 : PROB-01, PROB-06.
- ACT-05 : COMM-02, COMM-06.
- ACT-06 : CAL-13, DATA-06, PROB-07.

### PLURI — Supports transversaux
- PLURI-01 à PLURI-08 : utilisables à tout moment, en parallèle des fiches mathématiques correspondantes ; aucun n’est un prérequis obligatoire.
