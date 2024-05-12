from datetime import timedelta
from src.domain.accessibility.entities.accessibility_by_zone import AccessibilityByZone
from src.domain.accessibility.repository.accessibility_repository import AccessibilityRepository
from src.domain.impedance_matrices.entities.distance import Distance
from src.domain.impedance_matrices.entities.impedance_matrix import ImpedanceMatrix
from src.domain.accessibility_types import AccessibilityType
from src.domain.oportunities.entities.oportunities_by_zone import OportunitiesByZone
from src.domain.transport_modes import TransportMode


class GetAccessibilityByZone:

    def __init__(self, accessibility_repository: AccessibilityRepository):
        self.accessibility_repository = accessibility_repository

    def get(
        self,
        impedance_matrix: ImpedanceMatrix,
        oportunities_by_zone: OportunitiesByZone,
        accessibility_type: AccessibilityType,
        umbral: timedelta | Distance | None = None,
    ) -> AccessibilityByZone:

        return self.accessibility_repository.get_accessibility_by_zone(
            accessibility_type, impedance_matrix, oportunities_by_zone, umbral
        )
