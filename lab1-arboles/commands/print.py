"""Comando del intérprete para imprimir la estructura del árbol."""

from __future__ import annotations

import typing

from trees import AVLTree

T = typing.TypeVar("T")


def print(tree: AVLTree[T]) -> AVLTree[T]:
    """Imprime por consola la representación del árbol actual.

    Importante: Retorna el árbol intacto para preservar el estado en el intérprete.

    Sintaxis en el script:
        PRINT

    Args:
        tree (AVLTree[T]): Árbol actual en memoria.

    Returns:
        AVLTree[T]: La misma referencia al árbol recibida.
    """
    # TODO: [Práctica Alumno]
    ...