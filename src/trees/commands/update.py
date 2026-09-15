"""Comando del intérprete para actualizar el valor asociado a un nodo."""

from __future__ import annotations

import typing

from trees import AVLTree

V = typing.TypeVar("V")


def update(tree: AVLTree[V], key: str, value: str) -> AVLTree[V]:
    """Actualiza la entidad identificada por `key` reemplazándola por el nuevo objeto deserializado de `value`.

    Nota pedagógica de implementación:
        - `key` identifica el nodo actual a actualizar (ej: `"Luke Skywalker"`).
        - `value` es una cadena en formato JSON que representa la nueva versión de la entidad
          (o los nuevos datos a actualizar). Debe deserializarse con `utils.parse_json_to_character(value)`.
        - Si la nueva versión modifica la clave que determina el orden relativo en el árbol,
          el alumno debe considerar si procede actualizar el valor in-situ o eliminar y reinsertar
          para mantener la invariante de orden del ABB y el balanceo AVL.

    Sintaxis en el script:
        UPDATE "Luke Skywalker" '{"nome": "Luke Skywalker", "arma_principal": "Sable verde", ...}'

    Args:
        tree (AVLTree[V]): Árbol actual en memoria.
        key (str): Clave o identificador del nodo a buscar y actualizar.
        value (str): Cadena en formato JSON con la nueva información de la entidad.

    Returns:
        AVLTree[V]: La referencia a la raíz del árbol tras la actualización.

    Raises:
        KeyError: Si no existe ningún nodo con la clave `key` en el árbol.
        json.JSONDecodeError: Si `value` no es un JSON válido.
    """
    # TODO: [Práctica Alumno]
    # 1. Parsear el string JSON 'value' a un objeto del modelo (ej: new_obj = utils.parse_json_to_character(value))
    # 2. Localizar el nodo con clave 'key'
    # 3. Actualizar el contenido garantizando que se preserve la invariante AVL
    # 4. Retornar la raíz del árbol
    ...