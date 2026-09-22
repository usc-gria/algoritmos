"""Módulo del modelo de dominio: Node (Satélites y Sondas Espaciales).

Define la entidad `Node` que representa un satélite, sonda o estación espacial.
Incluye coordenadas tridimensionales en el espacio (x, y, z en km respecto al centro de la Tierra)
"""

from __future__ import annotations

import math
import typing
from dataclasses import dataclass, field

from . import Comparable


@dataclass(frozen=True, order=True)
class Node(Comparable):
    """Entidad inmutable que representa un satélite, estación o sonda espacial.

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

    name: str = field(compare=True)
    agency: str = field(compare=False)
    orbit_type: str = field(compare=False)
    launch_year: int = field(compare=False)
    x: float = field(compare=False)
    y: float = field(compare=False)
    z: float = field(compare=False)
    transmitter_power_w: float = field(compare=False)
    status: str = field(compare=False)
    description: str = field(compare=False)

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
