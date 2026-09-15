"""Comando del intérprete para eliminar un valor del árbol."""

from __future__ import annotations

from trees import AVLTree


def remove[T](tree: AVLTree[T], key: str) -> AVLTree[T]:
    """Elimina una entidad del árbol AVL y rebalancea la estructura si es necesario.

    Si el dato no existía debe imprimirse el mensaje KEY <key> NOT PRESENT IN TREE. Por ejemplo:
        KEY Hubble NOT PRESENT IN TREE
    Si el dato existía debe imprimirse el mensaje VALUE <value> SUCCESSFULLY REMOVED. Ejemplo:
        VALUE {"name": "Hubble", "agency": "NASA/ESA", "orbit_type": "LEO", "launch_year": 1990,
        "x": 4800.0, "y": -3200.0, "z": 3600.0, "transmitter_power_w": 200.0, "status": "Active",
        "description": "Pioneering optical and ultraviolet space telescope exploring the deep
        universe."} SUCCESSFULLY REMOVED

    Nota pedagógica de implementación:
        El argumento `key` se recibe como una clave directa (p. ej. el nombre de un satelite)
        
    Sintaxis en el script:
        REMOVE "Darth Vader"

    Args:
        tree (AVLTree[T]): Árbol actual en memoria.
        key (str): Cadena identificativa de la entidad a eliminar.

    Returns:
        AVLTree[T]: La nueva raíz del árbol tras la eliminación.

    Complejidad temporal: O(log n).
    """
    # TODO: [Práctica Alumno]
    # 1. Utilizar la clave directamente
    # 2. Invocar tree.remove(...)
    # 3. Retornar la nueva raíz del árbol
