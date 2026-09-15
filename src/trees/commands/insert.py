"""Comando del intérprete para insertar un nuevo valor en el árbol."""

from __future__ import annotations

import typing

from trees import AVLTree

T = typing.TypeVar("T")


def insert(tree: AVLTree[T], value: str) -> AVLTree[T]:
    """Inserta una nueva entidad en el árbol AVL manteniendo la propiedad de balanceo.

    Nota pedagógica de implementación:
        El argumento `value` se recibe como una cadena de texto en formato JSON.
        Debe deserializarse al objeto definido en `model.py` (usando `utils.parse_json_to_character(value)`)
        antes de invocar el método `tree.insert(...)`.

    Sintaxis en el script:
        INSERT '{"nome": "Yoda", "especie": "Desconocida", ...}'

    Args:
        tree (AVLTree[T]): Árbol actual en memoria sobre el cual insertar.
        value (str): Cadena en formato JSON que representa la entidad a insertar.

    Returns:
        AVLTree[T]: La nueva raíz del árbol tras la inserción y las posibles rotaciones AVL.

    Raises:
        json.JSONDecodeError: Si la cadena `value` no es un JSON válido.
        TypeError: Si la estructura de campos no coincide con la del modelo.

    Complejidad temporal: O(log n).
    Complejidad espacial: O(log n) por la recursión.
    """
    # TODO: [Práctica Alumno]
    # 1. Parsear el string JSON 'value' a un objeto del modelo (ej: obj = utils.parse_json_to_character(value))
    # 2. Insertar el objeto en el árbol: tree = tree.insert(obj)
    # 3. Retornar la nueva raíz
    ...

