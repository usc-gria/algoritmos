"""LOAD <ficheiro_json> [n]: substitúe o problema actual."""
from __future__ import annotations
from ..models import Problem
from ..utils import load_json_file


def load(problem: Problem | None, filepath: str, count: str | None = None) -> Problem:
    nodes = load_json_file(filepath)
    if count is not None:
        n = int(count)
        if not 0 <= n <= len(nodes):
            raise ValueError("n must be between 0 and the number of records")
        nodes = nodes[:n]
    problem = Problem(nodes)
    print(f"PROBLEM LOADED WITH {len(problem.names)} NODES")
    return problem
