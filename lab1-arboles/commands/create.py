"""Comando del intérprete para inicializar un nuevo Árbol AVL."""

from __future__ import annotations

import typing

from trees import AVLTree

T = typing.TypeVar("T")


def create(tree: AVLTree[T] | None, value: str) -> AVLTree[T]:
    """Crea e inicializa un nuevo Árbol AVL con el objeto deserializado como raíz.

    Descarta cualquier árbol previo y retorna una nueva instancia de `AVLTree`.

    Nota pedagógica de implementación:
        El argumento `value` se recibe como una cadena de texto en formato JSON.
        Antes de instanciar el árbol, debe parsearse dicha cadena al tipo de objeto
        definido en `model.py` (por ejemplo, utilizando las funciones de `utils.py`).

    Sintaxis en el script:
        CREATE '{"nome": "Luke", "especie": "Humano", ...}'

    Args:
        tree (AVLTree[T] | None): Instancia previa del árbol en memoria (se descarta).
        value (str): Cadena en formato JSON que representa la entidad del modelo
            que se asignará como raíz del nuevo árbol.

    Returns:
        AVLTree[T]: Nueva instancia de Árbol AVL inicializada con el objeto parseado.

    Raises:
        json.JSONDecodeError: Si `value` no es un JSON válido.
        TypeError: Si los campos del JSON no coinciden con la clase del modelo.

    Complejidad temporal: O(1).
    Complejidad espacial: O(1).
    """
    # TODO: [Práctica Alumno]
    # 1. Parsear la cadena JSON 'value' a una instancia del objeto del modelo (ej: utils.parse_json_to_character(value))
    # 2. Crear y retornar un nuevo AVLTree con dicha instancia como raíz
    ...