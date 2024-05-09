from dataclasses import dataclass
from datetime import timedelta

from src.domain.impedance_matrices.entities.impedance_matrix import ImpedanceMatrix
from src.domain.zone import Zone

@dataclass
class TravelTimeMatrix(ImpedanceMatrix):
    data: dict[tuple[Zone, Zone], timedelta]
