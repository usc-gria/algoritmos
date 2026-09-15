"""Comando del intérprete para buscar un valor en el árbol e imprimirlo."""

from __future__ import annotations

import typing

from trees import AVLTree

T = typing.TypeVar("T")


def find(tree: AVLTree[T], value: str) -> AVLTree[T]:
    """Busca un valor o entidad en el árbol AVL e imprime el resultado por consola.

    Importante: Siempre retorna el árbol intacto para preservar su estado en el intérprete.

    Nota pedagógica de implementación:
        El parámetro `value` puede recibirse como una clave textual (ej: `"Yoda"`)
        o como un objeto JSON completo (ej: `'{"nome": "Yoda", ...}'`).
        Si es JSON, puede parsearse con `utils.parse_json_to_character(value)`.
        Dado que `Character` implementa `__eq__` admitiendo comparación directa con `str`,
        la búsqueda por nombre opera directamente.

    Sintaxis en el script:
        FIND "Luke Skywalker"
        FIND '{"nome": "Luke Skywalker", ...}'

    Args:
        tree (AVLTree[T]): Árbol actual en memoria.
        value (str): Clave identificadora o cadena JSON del objeto a buscar.

    Returns:
        AVLTree[T]: La misma referencia al árbol recibida.

    Complejidad temporal: O(log n).
    """
    # TODO: [Práctica Alumno]
    # 1. Localizar el nodo objetivo: result = tree.find(...)
    # 2. Imprimir en consola la información del nodo encontrado o mensaje de no hallado
    # 3. Retornar 'tree' intacto
    ...

