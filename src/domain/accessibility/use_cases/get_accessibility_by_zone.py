from src.domain.accessibility.entities.accessibility_by_zone import AccessibilityByZone
from src.domain.accessibility.repository.accessibility_repository import AccessibilityRepository
from src.domain.impedance_matrices.entities.impedance_matrix import ImpedanceMatrix
from src.domain.accessibility_types import AccessibilityType
from src.domain.transport_modes import TransportMode

class GetAccessibilityByZone:

    def __init__(self, accessibility_repository: AccessibilityRepository):
        self.accessibility_repository = accessibility_repository

    def get(
            self, 
            impedance_matrix: ImpedanceMatrix, 
            AccessibilityType: AccessibilityType,
            transport_mode: TransportMode
            ) -> AccessibilityByZone:

        self.accessibility_repository.get_accessibility_by_zone(
            AccessibilityType, 
            transport_mode,
            impedance_matrix
        )
