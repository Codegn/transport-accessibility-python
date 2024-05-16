from dataclasses import dataclass
from typing import Dict, Tuple, Any

from src.domain.zone import Zone

@dataclass
class ImpedanceMatrix():
    data: Dict[Tuple[Zone, Zone], Any]
