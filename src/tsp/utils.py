"""Lectura dos datos de satélites en formato JSON."""
from __future__ import annotations
import json
import math
from pathlib import Path
from .models.Node import Node


def load_json_file(filepath: str | Path) -> list[Node]:
    with Path(filepath).open(encoding="utf-8") as stream:
        records = json.load(stream)
    if not isinstance(records, list):
        raise ValueError("Expected a JSON array")
    nodes = []
    names = set()
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("Expected a satellite object")
        node = Node(**record)
        if not isinstance(node.name, str) or not node.name.strip():
            raise ValueError("Invalid satellite name")
        if node.name in names:
            raise ValueError("Duplicate satellite name")
        for value in (node.x, node.y, node.z):
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
                raise ValueError("Coordinates must be finite numbers")
        names.add(node.name)
        nodes.append(node)
    return nodes
