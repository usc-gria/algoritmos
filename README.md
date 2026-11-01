# GrIA — Algoritmos — Práctica 3

Programación dinámica e TSP sobre ConstellationNet. Véxase [description.html](description.html) para o enunciado completo.

## Execución

Desde esta carpeta, con Python ≥ 3.12 e uv:

```bash
uv sync --locked
uv run tsp examples/TEST1.input
uv run tsp --time examples/TEST1.input > actual.output 2> tempos.txt
```

Completar os dous TODO de `src/tsp/models/Solver.py`. O intérprete, os comandos e a entrada/saída xa están implementados. O esqueleto falla explicitamente se intenta executar un algoritmo pendente.

`data.json` contén os satélites e `Node.py` define o seu modelo. Cada LOAD substitúe o problema; o parámetro opcional limita o número de satélites.

