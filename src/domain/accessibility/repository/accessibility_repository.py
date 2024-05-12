from abc import ABC, abstractmethod
from datetime import timedelta
from pathlib import Path

from src.domain.accessibility.entities.accessibility_by_zone import AccessibilityByZone
from src.domain.accessibility_types import AccessibilityType
from src.domain.impedance_matrices.entities.distance import Distance
from src.domain.impedance_matrices.entities.impedance_matrix import ImpedanceMatrix
from src.domain.oportunities.entities.oportunities_by_zone import OportunitiesByZone


class AccessibilityRepository(ABC):

    @abstractmethod
    def get_accessibility_by_zone(
        self,
        accessibility_type: AccessibilityType,
        impedance_matrix: ImpedanceMatrix,
        oportunities_by_zone: OportunitiesByZone,
        umbral: timedelta | Distance | None = None,
    ) -> AccessibilityByZone:
        pass

    @abstractmethod
    def save_accessibility_by_zone_to_file(self, accessibility_by_zone: AccessibilityByZone, output_path: Path):
        pass
