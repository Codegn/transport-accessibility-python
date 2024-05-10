from pathlib import Path
from src.domain.impedance_matrices.entities.impedance_type import ImpedanceType
from src.domain.accessibility.use_cases.get_accessibility_by_zone import GetAccessibilityByZone
from src.domain.accessibility_types import AccessibilityType
from src.domain.impedance_matrices.entities.impedance_matrix_source_type import ImpedanceMatrixSourceType
from src.domain.impedance_matrices.use_cases.get_impedance_matrix_from_source import GetImpedanceMatrixFromSource
from src.domain.oportunities.entities.oportunities_source_type import OportunitiesSourceType
from src.domain.oportunities.use_cases.get_from_source import GetOportunitiesFromSource
from src.domain.transport_modes import TransportMode

MIN_TOTAL_TIME = 5
MAX_TOTAL_TIME = 180


class AccessibilityCalculator:

    def __init__(
        self,
        get_accessibility_by_zone: GetAccessibilityByZone,
        get_impedance_matrix_from_source: GetImpedanceMatrixFromSource,
        get_oportunities_from_source: GetOportunitiesFromSource,
    ):
        self.get_accessibility_by_zone = get_accessibility_by_zone
        self.get_impedance_matrix_from_source = get_impedance_matrix_from_source
        self.get_oportunities_from_source = get_oportunities_from_source


    def _get_impedance_matrix(
        self, impedance_type: ImpedanceType, impedance_matrix_source: ImpedanceMatrixSourceType, file_path: Path
    ):
        if impedance_type == ImpedanceType.DISTANCE:
            impedance_matrix = self.get_impedance_matrix_from_source.get_distance_matrix_from_file(
                file_path, impedance_matrix_source
            )
        elif impedance_type == ImpedanceType.TIME:
            impedance_matrix = self.get_impedance_matrix_from_source.get_travel_time_matrix_from_file(
                file_path, impedance_matrix_source
            )
        else:
            raise ValueError(f"Invalid impedance type: {impedance_type}")
        return impedance_matrix

    def calculate_accessibility(
        self,
        impedance_type: ImpedanceType,
        impedance_matrix_file_path: Path,
        oportunities_file_path: Path,
        impedance_matrix_source: ImpedanceMatrixSourceType,
        accessibility_type: AccessibilityType = AccessibilityType.UMBRAL,
        transport_mode: TransportMode = TransportMode.PUBLIC,
    ):
        impedance_matrix = self._get_impedance_matrix(
            impedance_type, impedance_matrix_source, impedance_matrix_file_path
        )
        oportunities_by_zone = self.get_oportunities_from_source.get_from_file(
            oportunities_file_path, OportunitiesSourceType.ORIDES
        )
        accessibility = self.get_accessibility_by_zone.get(
            impedance_matrix, oportunities_by_zone, accessibility_type, transport_mode
        )
        return accessibility
