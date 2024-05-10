from dataclasses import dataclass
from typing import Dict

from src.domain.accessibility.entities.accessibility import Accessibility
from src.domain.zone import Zone

@dataclass
class AccessibilityByZone:
    data: Dict[Zone, Accessibility]
