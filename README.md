# GrIA — Algoritmos — Práctica 3

Programación dinámica e TSP sobre ConstellationNet. Véxase [enunciado.md](enunciado.md) ou [description.html](description.html) para a descrición completa.

## Execución

Desde esta carpeta, con Python ≥ 3.12 e uv:

```bash
uv sync --locked
uv run tsp examples/TEST1.input
uv run tsp --time examples/TEST1.input > actual.output 2> tempos.txt
```

Completar os dous TODO de `src/tsp/models/Solver.py`. O intérprete, os comandos e a entrada/saída xa están implementados. O esqueleto falla explicitamente se intenta executar un algoritmo pendente.

`data.json` e `Node.py` reutilízanse sen cambios de p2; o JSON tamén coincide co de p1. Cada LOAD substitúe o problema; o parámetro opcional limita o número de satélites.

