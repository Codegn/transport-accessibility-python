from dataclasses import dataclass
from src.domain.oportunities.entities.oportunity import Oportunity
from src.domain.zone import Zone

@dataclass
class OportunitiesByZone:
    data: dict[Zone, Oportunity]
