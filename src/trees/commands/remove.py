"""Comando del intérprete para eliminar un valor del árbol."""

from __future__ import annotations

import typing

from trees import AVLTree

T = typing.TypeVar("T")


def remove(tree: AVLTree[T], value: str) -> AVLTree[T]:
    """Elimina una entidad del árbol AVL y rebalancea la estructura si es necesario.

    Nota pedagógica de implementación:
        El argumento `value` puede recibirse como una clave directa (p. ej. el nombre de un personaje)
        o como un objeto JSON completo. Si es un JSON, se deserializa con `utils.parse_json_to_character(value)`;
        si no es JSON, se busca directamente por clave gracias al método `__eq__` del modelo.

    Sintaxis en el script:
        REMOVE '{"nome": "Darth Vader", ...}'
        REMOVE "Darth Vader"

    Args:
        tree (AVLTree[T]): Árbol actual en memoria.
        value (str): Cadena identificativa o JSON de la entidad a eliminar.

    Returns:
        AVLTree[T]: La nueva raíz del árbol tras la eliminación.

    Complejidad temporal: O(log n).
    """
    # TODO: [Práctica Alumno]
    # 1. Intentar parsear como JSON si procede o utilizar el valor/clave directamente
    # 2. Invocar tree.remove(...)
    # 3. Retornar la nueva raíz del árbol
    ...

