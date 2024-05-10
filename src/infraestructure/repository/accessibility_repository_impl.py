from src.domain.accessibility.entities.accessibility_by_zone import AccessibilityByZone
from src.domain.accessibility.repository.accessibility_repository import AccessibilityRepository
from src.domain.accessibility_types import AccessibilityType
from src.domain.impedance_matrices.entities.impedance_matrix import ImpedanceMatrix
from src.domain.oportunities.entities.oportunities_by_zone import OportunitiesByZone
from src.domain.transport_modes import TransportMode
from src.infraestructure.components.accessibility_procesor import AccessibilityProcessor


class AccessibilityRepositoryImpl(AccessibilityRepository):

    def __init__(self, accessibility_processor: AccessibilityProcessor):
        self.accessibility_processor = accessibility_processor
    
    def get_accessibility_by_zone(
        self, 
        accessibility_type: AccessibilityType, 
        transport_mode: TransportMode,
        impedance_matrix: ImpedanceMatrix,
        oportunities_by_zone: OportunitiesByZone
        ) -> AccessibilityByZone:

        return self.accessibility_processor.process(accessibility_type, transport_mode, impedance_matrix, oportunities_by_zone)
