from pathlib import Path
from src.domain.impedance_matrices.entities.distance_matrix import DistanceMatrix
from src.domain.impedance_matrices.entities.impedance_matrix import ImpedanceMatrix
from src.domain.impedance_matrices.entities.impedance_matrix_source_type import ImpedanceMatrixSourceType
from src.domain.impedance_matrices.entities.impedance_type import ImpedanceType
from src.domain.impedance_matrices.entities.travel_time_matrix import TravelTimeMatrix
from src.domain.impedance_matrices.repository.impedance_matrices_repository import ImpedanceMatricesRepository
from src.domain.transport_modes import TransportMode


class GetImpedanceMatrixFromSource:

    def __init__(self, impedance_matrices_repository: ImpedanceMatricesRepository):
        self.impedance_matrices_repository = impedance_matrices_repository

    def get_distance_matrix_from_file(
        self, file_path: Path, impedance_matrix_source: ImpedanceMatrixSourceType, transport_mode: TransportMode
    ) -> ImpedanceMatrix:

        distance_matrix: ImpedanceMatrix = self.impedance_matrices_repository.get_impedance_matrix_from_file(
            file_path, impedance_matrix_source, ImpedanceType.DISTANCE, transport_mode,
        )

        return distance_matrix

    def get_travel_time_matrix_from_file(
        self, file_path: Path, impedance_matrix_source: ImpedanceMatrixSourceType, transport_mode: TransportMode
    ) -> ImpedanceMatrix:

        travel_time_matrix: ImpedanceMatrix = self.impedance_matrices_repository.get_impedance_matrix_from_file(
            file_path, impedance_matrix_source, ImpedanceType.TIME, transport_mode
        )

        return travel_time_matrix
