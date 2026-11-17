"""Matriz completa de custos enteiros construída a partir dos satélites."""
from __future__ import annotations
import math
from .Node import Node


class Problem:
    def __init__(self, nodes: list[Node]):
        self.nodes = tuple(sorted(nodes, key=lambda node: node.name))
        self.names = tuple(node.name for node in self.nodes)
        self.costs = tuple(
            tuple(0 if i == j else math.ceil(a.distance(b))
                  for j, b in enumerate(self.nodes))
            for i, a in enumerate(self.nodes)
        )

    def index(self, name: str) -> int:
        return self.names.index(name)
