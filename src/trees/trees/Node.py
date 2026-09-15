"""Módulo del modelo de dominio: Node (Satélites y Sondas Espaciales).

Define la entidad `Node` que representa un satélite, sonda o estación espacial.
Incluye coordenadas tridimensionales en el espacio (x, y, z en km respecto al centro de la Tierra)
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import total_ordering
import math
import typing


@dataclass(frozen=True)
@total_ordering
class Node:
    """Entidad inmutable que representa un satélite, estación o sonda espacial.

    Al estar decorada con `@total_ordering`, implementar `__eq__` y `__lt__`
    proporciona automáticamente el resto de operadores relacionales (`<=`, `>`, `>=`),
    permitiendo ordenar e indexar los satélites en el Árbol Binario de Búsqueda y AVL
    por su identificador o nombre.

    Attributes:
        name (str): Nombre o identificador del satélite (clave de ordenación en el árbol).
        agency (str): Agencia espacial operadora (ej: NASA, ESA, JAXA, SpaceX).
        orbit_type (str): Tipo de órbita (LEO, MEO, GEO, HEO, Lagrange L2, etc.).
        launch_year (int): Año en que fue puesto en órbita.
        x (float): Coordenada espacial X en kilómetros (km) respecto al geocentro.
        y (float): Coordenada espacial Y en kilómetros (km) respecto al geocentro.
        z (float): Coordenada espacial Z en kilómetros (km) respecto al geocentro.
        transmitter_power_w (float): Potencia de emisión en vatios (relevante para alcance en grafos).
        status (str): Estado operativo actual ('Active', 'In transit', 'Retired').
        description (str): Breve resumen del propósito u objetivos científicos de la misión.
    """

    name: str
    agency: str
    orbit_type: str
    launch_year: int
    x: float
    y: float
    z: float
    transmitter_power_w: float
    status: str
    description: str

    def distance(self: typing.Self, other: Node) -> float:
        """Calcula la distancia euclidiana en 3D en kilómetros hacia otro satélite.

        Args:
            other (Node): Otro satélite con coordenadas x, y, z.

        Returns:
            float: Distancia en kilómetros en el espacio tridimensional.
        """
        dx = self.x - other.x
        dy = self.y - other.y
        dz = self.z - other.z
        return math.sqrt(dx * dx + dy * dy + dz * dz)

    def __eq__(self: typing.Self, other: object) -> bool:
        """Determina la igualdad entre este satélite y otro objeto (Node o str de nombre)."""
        if isinstance(other, Node):
            return self.name == other.name
        elif isinstance(other, str):
            return self.name == other
        return False

    def __lt__(self: typing.Self, other: Node | str) -> bool:
        """Determina el orden alfabético por nombre para mantener la invariante en el árbol AVL."""
        if isinstance(other, Node):
            return self.name < other.name
        elif isinstance(other, str):
            return self.name < other
        return NotImplemented
