from dataclasses import dataclass
from datetime import timedelta
from typing import Dict, Tuple

from src.domain.impedance_matrices.entities.impedance_matrix import ImpedanceMatrix
from src.domain.zone import Zone

@dataclass
class TravelTimeMatrix(ImpedanceMatrix):
    data: Dict[Tuple[Zone, Zone], timedelta]
