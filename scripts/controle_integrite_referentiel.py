
#!/usr/bin/env python3
"""Contrôle d'intégrité du catalogue maître et du graphe des prérequis.

Dépendances : bibliothèque standard Python uniquement.
Le rapport généré est un diagnostic technique, pas une validation pédagogique.
"""

from collections import Counter
from datetime import datetime
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parent.parent
CATALOGUE = ROOT / (
    "Catalogue maître des fiches — Prépa Clé Mathématiques - v3.0.md"
)
GRAPHE = ROOT / "Graphe des prérequis — v3.0.md"
RAPPORT = ROOT / "rapport_controle_integrite.md"

ID_PATTERN = re.compile(r"\b[A-Z][A-Z0-9]*-\d{2}\b")
CATALOGUE_ROW = re.compile(
    r"^\s*\|\s*([A-Z][A-Z0-9]*-\d{2})\s*\|"
)
GRAPH_ROW = re.compile(
    r"^\s*-\s+([A-Z][A-Z0-9]*-\d{2})\s*:\s*(.*?)\s*$"
)
RANGE_PATTERN = re.compile(
    r"\b([A-Z][A-Z0-9]*)-(\d{2})\s+à\s+"
    r"([A-Z][A-Z0-9]*)-(\d{2})\b",
    re.IGNORECASE,
)


def read_file(path):
    if not path.is_file():
        raise FileNotFoundError(f"Fichier introuvable : {path}")
    return path.read_text(encoding="utf-8")


def extract_catalogue_ids(text):
    ids = []
    for line in text.splitlines():
        match = CATALOGUE_ROW.match(line)
        if match:
            ids.append(match.group(1))
    return ids


def extract_graph(text):
    definitions = []
    prerequisites = {}

    for line_number, line in enumerate(text.splitlines(), start=1):
        match = GRAPH_ROW.match(line)
        if not match:
            continue

        target, body = match.groups()
        definitions.append((target, line_number))
        prerequisites.setdefault(target, []).extend(
            extract_references(body)
        )

    return definitions, prerequisites


def extract_references(text):
    """Extrait les identifiants et développe les plages de type CAL-01 à CAL-07."""
    references = []

    def expand_range(match):
        prefix_start, start, prefix_end, end = match.groups()

        if prefix_start != prefix_end:
            return match.group(0)

        first, last = int(start), int(end)
        if first > last:
            return match.group(0)

        references.extend(
            f"{prefix_start}-{number:02d}"
            for number in range(first, last + 1)
        )
        return " "

    remaining = RANGE_PATTERN.sub(expand_range, text)
    references.extend(ID_PATTERN.findall(remaining))
    return list(dict.fromkeys(references))


def find_one_cycle(edges, known_ids):
    """Renvoie un premier cycle potentiel dans les dépendances extraites."""
    state = {}
    stack = []
    stack_positions = {}

    def visit(node):
        state[node] = 1
        stack_positions[node] = len(stack)
        stack.append(node)

        for neighbour in edges.get(node, []):
            if neighbour not in known_ids:
                continue

            if state.get(neighbour, 0) == 0:
                cycle = visit(neighbour)
                if cycle:
                    return cycle
            elif state.get(neighbour) == 1:
                start = stack_positions[neighbour]
                return stack[start:] + [neighbour]

        stack.pop()
        stack_positions.pop(node, None)
        state[node] = 2
        return None

    for node in sorted(known_ids):
        if state.get(node, 0) == 0:
            cycle = visit(node)
            if cycle:
                return cycle

    return None


def markdown_list(items):
    if not items:
        return "- Aucun élément détecté."
    return "\n".join(f"- `{item}`" for item in items)


def main():
    try:
        catalogue_text = read_file(CATALOGUE)
        graphe_text = read_file(GRAPHE)
    except (OSError, UnicodeError) as error:
        print(f"ERREUR : {error}", file=sys.stderr)
        return 2

    catalogue_ids = extract_catalogue_ids(catalogue_text)
    graph_definitions, graph_edges = extract_graph(graphe_text)

    catalogue_counts = Counter(catalogue_ids)
    graph_counts = Counter(
        target for target, _ in graph_definitions
    )

    catalogue_set = set(catalogue_ids)
    graph_set = set(graph_counts)

    duplicate_catalogue = sorted(
        item for item, count in catalogue_counts.items() if count > 1
    )
    duplicate_graph = sorted(
        item for item, count in graph_counts.items() if count > 1
    )

    graph_targets_missing_from_catalogue = sorted(
        graph_set - catalogue_set
    )
    catalogue_ids_missing_from_graph = sorted(
        catalogue_set - graph_set
    )

    unknown_references = sorted({
        reference
        for references in graph_edges.values()
        for reference in references
        if reference not in catalogue_set
    })

    cycle = find_one_cycle(graph_edges, graph_set)

    report = f"""# Rapport de contrôle d'intégrité

- Date du contrôle : {datetime.now().astimezone().isoformat(timespec="seconds")}
- Catalogue contrôlé : `{CATALOGUE.name}`
- Graphe contrôlé : `{GRAPHE.name}`
- Identifiants distincts du catalogue : {len(catalogue_set)}
- Définitions distinctes du graphe : {len(graph_set)}

## 1. Unicité des identifiants du catalogue

{"ÉCHEC : identifiants dupliqués détectés." if duplicate_catalogue else "Aucun doublon détecté dans les lignes d'identifiants du catalogue."}

{markdown_list(duplicate_catalogue)}

## 2. Unicité des définitions du graphe

{"ÉCHEC : fiches définies plusieurs fois dans le graphe." if duplicate_graph else "Aucune définition répétée détectée dans le graphe."}

{markdown_list(duplicate_graph)}

## 3. Cohérence des identifiants

### Identifiants définis dans le graphe mais absents du catalogue

{markdown_list(graph_targets_missing_from_catalogue)}

### Identifiants du catalogue absents du graphe

{markdown_list(catalogue_ids_missing_from_graph)}

### Références extraites du graphe absentes du catalogue

{markdown_list(unknown_references)}

## 4. Recherche de cycles potentiels

"""

    if cycle:
        report += (
            "CYCLE POTENTIEL DÉTECTÉ : `"
            + " → ".join(cycle)
            + "`\n\n"
            "Ce résultat doit être examiné manuellement : le script "
            "regroupe les références extraites et peut traiter une "
            "alternative « ou » comme une arête supplémentaire.\n"
        )
    else:
        report += (
            "Aucun cycle détecté dans le graphe extrait. "
            "Cela ne dispense pas de vérifier manuellement les "
            "alternatives, les dépendances conditionnelles et les "
            "formulations descriptives.\n"
        )

    report += """
## 5. Limites du contrôle

Ce rapport vérifie la structure et les références détectables dans les
fichiers. Il ne valide pas la pertinence pédagogique des prérequis,
la couverture effective des critères CléA, ni la conformité au
référentiel régional.

Les mentions descriptives d'identifiants peuvent être interprétées
comme des références. Tout cycle signalé doit donc être examiné avant
de modifier le graphe.

## 6. Décision

Ne pas prononcer le gel définitif sur la seule base de ce rapport.
Examiner les anomalies, corriger si nécessaire, puis relancer le script.
"""

    RAPPORT.write_text(report, encoding="utf-8")
    print(report)
    print(f"\nRapport écrit dans : {RAPPORT}")

    hard_errors = (
        duplicate_catalogue
        or duplicate_graph
        or graph_targets_missing_from_catalogue
        or catalogue_ids_missing_from_graph
        or unknown_references
        or cycle
    )
    return 1 if hard_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
