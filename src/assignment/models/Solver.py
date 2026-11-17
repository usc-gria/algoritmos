"""Completar cotas e busca LC-FIFO. A infraestrutura xa está resolta."""
from __future__ import annotations
from .Problem import Problem

Result = tuple[int, tuple[str, ...], int]


class Solver:
    def __init__(self, problem: Problem, centers: tuple[str, ...]):
        if not centers or len(set(centers)) != len(centers):
            raise ValueError("Expected distinct centers")
        if any(center not in problem.names for center in centers):
            raise ValueError("Unknown center")
        self.problem = problem
        self.centers = tuple(sorted(centers))
        self.points = tuple(name for name in problem.names if name not in self.centers)
        self.capacity = (len(self.points) + len(self.centers) - 1) // len(self.centers)
        self.costs = tuple(tuple(problem.costs[problem.index(point)][problem.index(center)]
                                for center in self.centers) for point in self.points)

    def partial_cost(self, allocation: tuple[int, ...]) -> int:
        """allocation[i] é o índice do centro asignado a points[i]."""
        return sum(self.costs[i][center] for i, center in enumerate(allocation))

    def lower_bound(self, allocation: tuple[int, ...], mode: str) -> int:
        """Cota inferior TRIVIAL ou PRECISE dun prefixo válido, incluído o baleiro."""
        # TODO: [Práctica Alumno] Implementar as dúas cotas inferiores.
        raise NotImplementedError("Implement Solver.lower_bound")

    def upper_bound(self, allocation: tuple[int, ...], mode: str) -> int:
        """Cota superior TRIVIAL ou PRECISE (completado aleatorio válido).

        Nunha folla é o custo exacto."""
        # TODO: [Práctica Alumno] Implementar as dúas cotas superiores.
        raise NotImplementedError("Implement Solver.upper_bound")

    def solve(self, mode: str) -> Result:
        """Devolve (custo, tupla de nomes dos centros, nodos expandidos).

        A posición i da tupla corresponde a self.points[i]. Aplicar LC-FIFO
        e contar os estados que se expanden.
        Reiniciar a cola, cotas globais e contadores en cada chamada.
        """
        # TODO: [Práctica Alumno] Ramificar, podar e devolver a mellor asignación.
        raise NotImplementedError("Implement Solver.solve")
