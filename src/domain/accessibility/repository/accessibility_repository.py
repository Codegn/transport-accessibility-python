from abc import ABC, abstractmethod

from src.domain.accessibility.entities.accessibility_by_zone import AccessibilityByZone
from src.domain.accessibility_types import AccessibilityType
from src.domain.impedance_matrices.entities.impedance_matrix import ImpedanceMatrix
from src.domain.transport_modes import TransportMode

class AccessibilityRepository(ABC):
    
    @abstractmethod
    def get_accessibility_by_zone(
        self, 
        accessibility_type: AccessibilityType, 
        transport_mode: TransportMode,
        impedance_matrix: ImpedanceMatrix
        ) -> AccessibilityByZone:
        pass
