from src.domain.impedance_matrices.entities.distance_matrix import DistanceMatrix
from src.domain.impedance_matrices.repository.impedance_matrices_repository import ImpedanceMatricesRepository

class GetDistanceMatrixFromSource:

    def __init__(self, impedance_matrices_repository: ImpedanceMatricesRepository):
        self.impedance_matrices_repository = impedance_matrices_repository

    def get_from_file(self, file_path: str) -> DistanceMatrix:

        distance_matrix: DistanceMatrix = self.impedance_matrices_repository.get_distance_matrix_from_file(file_path)

        return distance_matrix
