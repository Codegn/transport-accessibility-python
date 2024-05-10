from src.domain.accessibility.entities.accessibility_by_zone import AccessibilityByZone
from src.domain.accessibility_types import AccessibilityType
from src.domain.impedance_matrices.entities.impedance_matrix import ImpedanceMatrix
from src.domain.oportunities.entities.oportunities_by_zone import OportunitiesByZone
from src.domain.transport_modes import TransportMode


class AccessibilityProcessor:
    
    def process(
            self,
            accessibility_type: AccessibilityType, 
            transport_mode: TransportMode,
            impedance_matrix: ImpedanceMatrix,
            oportunities_by_zone: OportunitiesByZone
            ) -> AccessibilityByZone:
        raise NotImplementedError