"""Comando del intérprete para insertar un nuevo valor en el árbol."""

from __future__ import annotations

from trees import AVLTree


def insert[T](tree: AVLTree[T], value: str) -> AVLTree[T]:
    """Inserta una nueva entidad en el árbol AVL manteniendo la propiedad de balanceo.

    Nota pedagógica de implementación:
        El argumento `value` se recibe como una cadena de texto en formato JSON.
        Debe deserializarse al objeto definido en `model.py` (usando `utils.parse_json_to_character(value)`)
        antes de invocar el método `tree.insert(...)`.
        Si ya existe un dato con la misma clave en el arbol debe imprimirse un mensaje con el patron
        VALUE FOR KEY <key> ALREADY EXISTS. Ejemplo:
            VALUE FOR KEY Hubble ALREADY EXISTS
        Si se hace la inserción correctamente debe imprimir un mensaje con el patron VALUE <value>
        INSERTED SUCCESSFULLY. Ejemplo:
            VALUE {"name": "Hubble", "agency": "NASA/ESA", "orbit_type": "LEO", "launch_year": 1990,
            "x": 4800.0, "y": -3200.0, "z": 3600.0, "transmitter_power_w": 200.0, "status": "Active",
            "description": "Pioneering optical and ultraviolet space telescope exploring the deep
            universe."} SUCCESSFULLY INSERTED

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
