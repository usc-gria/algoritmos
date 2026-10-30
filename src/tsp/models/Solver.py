"""Algoritmos que debe completar o alumnado. Non modificar as sinaturas."""
from __future__ import annotations
from .Problem import Problem

Result = tuple[int, tuple[str, ...]]


class Solver:
    def __init__(self, problem: Problem):
        self.problem = problem

    def brute_force(self, origin: str) -> Result:
        """Devolve (custo, ruta pechada) explorando todas as permutacións.

        A orixe xa foi validada polo comando TSP. Visitar todos os outros
        nodos unha vez e incluír o regreso. En empate, escoller a tupla de
        nomes lexicograficamente menor. Un único nodo: (0, (origin, origin)).
        """
        # TODO: [Práctica Alumno] Enumerar e avaliar os ciclos posibles.
        raise NotImplementedError("Implement Solver.brute_force")

    def dynamic(self, origin: str) -> Result:
        """Mesmo contrato que brute_force, mediante programación dinámica.

        Definir estados por nodo e subconxunto, gardar os custos dos
        subproblemas e reconstruír a ruta óptima co desempate especificado.
        As táboas deben ser locais a cada chamada.
        """
        # TODO: [Práctica Alumno] Implementar Held–Karp e reconstruír a ruta.
        raise NotImplementedError("Implement Solver.dynamic")
