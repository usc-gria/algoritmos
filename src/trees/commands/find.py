"""Comando del intérprete para buscar un valor en el árbol e imprimirlo."""

from __future__ import annotations

from ..trees import AVLTree, Comparable


def find[T: Comparable](tree: AVLTree[T], key: str) -> AVLTree[T]:
    """Busca un valor o entidad en el árbol AVL e imprime el resultado por consola.

    Si se encuentra un dato para la clave indicada debe imprimir el mensaje FOUND VALUE <value>
    FOR KEY <key>. Ejemplo: 
        FOUND VALUE {"name": "Hubble", "agency": "NASA/ESA", "orbit_type": "LEO", "launch_year": 1990,
        "x": 4800.0, "y": -3200.0, "z": 3600.0, "transmitter_power_w": 200.0, "status": "Active",
        "description": "Pioneering optical and ultraviolet space telescope exploring the deep universe."}
        FOR KEY Hubble
    
    Si no encuentra, debe imprimir un mensaje con el patron KEY <key> NOT FOUND IN TREE. Ejemplo:
        KEY Hubble NOT FOUND IN TREE

    Importante: Siempre retorna el árbol intacto para preservar su estado en el intérprete.
    
    Nota pedagógica de implementación:
        El parámetro `key` se recibe como una clave textual (ej: `"Hubble"`)

    Sintaxis en el script:
        FIND "Hubble"

    Args:
        tree (AVLTree[T]): Árbol actual en memoria.
        key (str): Clave identificadora del objeto a buscar.

    Returns:
        AVLTree[T]: La misma referencia al árbol recibida.

    Complejidad temporal: O(log n).
    """
    # TODO: [Práctica Alumno]
    # 1. Localizar el nodo objetivo: result = tree.find(...)
    # 2. Imprimir en consola la información del nodo encontrado o mensaje de no hallado
    # 3. Retornar 'tree' intacto
    ...
