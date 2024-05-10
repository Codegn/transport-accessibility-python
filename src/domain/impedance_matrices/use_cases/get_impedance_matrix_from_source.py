from pathlib import Path
from src.domain.impedance_matrices.entities.distance_matrix import DistanceMatrix
from src.domain.impedance_matrices.entities.impedance_matrix_source_type import ImpedanceMatrixSourceType
from src.domain.impedance_matrices.entities.travel_time_matrix import TravelTimeMatrix
from src.domain.impedance_matrices.repository.impedance_matrices_repository import ImpedanceMatricesRepository


class GetImpedanceMatrixFromSource:

    def __init__(self, impedance_matrices_repository: ImpedanceMatricesRepository):
        self.impedance_matrices_repository = impedance_matrices_repository

    def get_distance_matrix_from_file(
        self, file_path: Path, impedance_matrix_source: ImpedanceMatrixSourceType
    ) -> DistanceMatrix:

        distance_matrix: DistanceMatrix = self.impedance_matrices_repository.get_distance_matrix_from_file(
            file_path, impedance_matrix_source
        )

        return distance_matrix

    def get_travel_time_matrix_from_file(
        self, file_path: Path, impedance_matrix_source: ImpedanceMatrixSourceType
    ) -> TravelTimeMatrix:

        travel_time_matrix: TravelTimeMatrix = self.impedance_matrices_repository.get_travel_time_matrix_from_file(
            file_path, impedance_matrix_source
        )

        return travel_time_matrix
