# AMR-enhanced-alignments
A release of models and data related to alignments between AMR and English text for better parsing and probing of many different linguistic phenomena.

## Data (Planned to be Released)

- `<corpus>.spans.json`: spans for each sentence, grouping tokens which are either named entities or multiword expressions
- `<corpus>.subgraph_alignments.json`: alignments of connected DAG-shaped subgraphs to a single span
- `<corpus>.rel_alignments.json`: alignments of single relations to tokens cueing that relation, such as prepositions or relativizers
- `<corpus>.coref_alignments.json`: alignments of reentrancy edges to spans cueing coreference, such as pronouns or repeated named entity names.
- `<corpus>.control_alignments.json`: alignments of reentrancy edges to spans cueing control, such as control verbs or purpose clauses.
- `<corpus>.dupl_alignments.json`: alignments of connected DAG-shaped subgraphs to a span, where the semantic content is a duplicate of another subgraph (This is usually the result of some linguistic mechanism, such as coordination or ellipsis.)
