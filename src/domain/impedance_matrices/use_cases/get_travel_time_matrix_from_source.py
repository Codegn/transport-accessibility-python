from src.domain.impedance_matrices.entities.travel_time_matrix import TravelTimeMatrix
from src.domain.impedance_matrices.repository.impedance_matrices_repository import ImpedanceMatricesRepository

class GetTravelTimeMatrixFromSource:

    def __init__(self, impedance_matrices_repository: ImpedanceMatricesRepository):
        self.impedance_matrices_repository = impedance_matrices_repository

    def get_from_file(self, file_path: str) -> TravelTimeMatrix:

        travel_time_matrix: TravelTimeMatrix = self.impedance_matrices_repository.get_travel_time_matrix_from_file(file_path)

        return travel_time_matrix
