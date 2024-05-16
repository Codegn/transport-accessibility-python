from dataclasses import dataclass
from typing import Dict

from src.domain.oportunities.entities.oportunity import Oportunity
from src.domain.zone import Zone


@dataclass
class OportunitiesByZone:
    data: Dict[Zone, Oportunity]
