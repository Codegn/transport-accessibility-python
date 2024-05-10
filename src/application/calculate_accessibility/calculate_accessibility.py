from pathlib import Path
from src.application.calculate_accessibility.models.impedance_type import ImpedanceType
from src.domain.accessibility.use_cases.get_accessibility_by_zone import GetAccessibilityByZone
from src.domain.impedance_matrices.use_cases.get_distance_matrix_from_source import GetDistanceMatrixFromSource
from src.domain.impedance_matrices.use_cases.get_travel_time_matrix_from_source import GetTravelTimeMatrixFromSource
from src.domain.oportunities.use_cases.get_from_source import GetOportunitiesFromSource

MIN_TOTAL_TIME = 5
MAX_TOTAL_TIME = 180


class CalculateAccessibility:

    def __init__(
        self,
        get_accessibility_by_zone: GetAccessibilityByZone,
        get_distance_matrix_from_source: GetDistanceMatrixFromSource,
        get_travel_time_matrix_from_source: GetTravelTimeMatrixFromSource,
        get_oportunities_from_source: GetOportunitiesFromSource,
    ):
        self.get_accessibility_by_zone = get_accessibility_by_zone
        self.get_distance_matrix_from_source = get_distance_matrix_from_source
        self.get_travel_time_matrix_from_source = get_travel_time_matrix_from_source
        self.get_oportunities_from_source = get_oportunities_from_source

    def _get_impedance_matrix(self, impedance_type: ImpedanceType, file_path: Path):
        if impedance_type == ImpedanceType.DISTANCE:
            impedance_matrix = self.get_distance_matrix_from_source.get_from_file(file_path)
        elif impedance_type == ImpedanceType.TIME:
            impedance_matrix = self.get_travel_time_matrix_from_source.get_from_file(file_path)
        else:
            raise ValueError(f"Invalid impedance type: {impedance_type}")
        return impedance_matrix

    def calculate_accessibility(
        self, impedance_type: ImpedanceType, impedance_matrix_file_path: Path, oportunities_file_path: Path
    ):
        impedance_matrix = self._get_impedance_matrix(impedance_type, impedance_matrix_file_path)
        oportunities_by_zone = self.get_oportunities_from_source.get_from_file(oportunities_file_path)
        accessibility = self.get_accessibility_by_zone.get(
            impedance_matrix, oportunities_by_zone, MIN_TOTAL_TIME, MAX_TOTAL_TIME
        )
