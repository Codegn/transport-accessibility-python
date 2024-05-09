from dataclasses import dataclass

from src.domain.accessibility.entities.accessibility import Accessibility
from src.domain.zone import Zone

@dataclass
class AccessibilityByZone:
    data: dict[Zone, Accessibility]
