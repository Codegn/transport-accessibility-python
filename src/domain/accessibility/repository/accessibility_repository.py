from abc import ABC, abstractmethod
from datetime import timedelta

from src.domain.accessibility.entities.accessibility_by_zone import AccessibilityByZone
from src.domain.accessibility_types import AccessibilityType
from src.domain.impedance_matrices.entities.distance import Distance
from src.domain.impedance_matrices.entities.impedance_matrix import ImpedanceMatrix
from src.domain.oportunities.entities.oportunities_by_zone import OportunitiesByZone
from src.domain.transport_modes import TransportMode

class AccessibilityRepository(ABC):
    
    @abstractmethod
    def get_accessibility_by_zone(
        self, 
        accessibility_type: AccessibilityType,
        impedance_matrix: ImpedanceMatrix,
        oportunities_by_zone: OportunitiesByZone,
        umbral: timedelta | Distance | None = None
        ) -> AccessibilityByZone:
        pass
