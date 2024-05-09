from dataclasses import dataclass

from src.domain.impedance_matrices.entities.distance import Distance
from src.domain.impedance_matrices.entities.impedance_matrix import ImpedanceMatrix
from src.domain.zone import Zone

@dataclass
class DistanceMatrix(ImpedanceMatrix):
    data: dict[tuple[Zone, Zone], Distance]
