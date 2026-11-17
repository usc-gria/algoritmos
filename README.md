# GrIA — Algoritmos — Práctica 4

Ramificación e poda: asignación de satélites a centros con capacidade limitada. O enunciado completo está en [description.html](description.html).

## Execución

Desde esta carpeta, con Python ≥ 3.12 e uv:

```bash
uv sync --locked
uv run assignment examples/TEST1.input
uv run assignment --time examples/TEST1.input > actual.output 2> tempos.txt
```

Completar os tres TODO de `src/assignment/models/Solver.py`: cotas inferiores, cotas superiores e busca LC-FIFO. O resto da infraestrutura xa está implementado. O esqueleto falla explicitamente cando se invoca un método pendente.

Proporciónanse os datos JSON, o modelo Node, a matriz de custos e o intérprete. O comando LOAD substitúe o problema; ASSIGN escolle os centros e o conxunto de cotas. As expansións imprímense en stderr e --time engade os tempos; stdout contén a asignación e o custo para a comparación automática.

