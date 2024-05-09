from abc import ABC, abstractmethod

from src.domain.impedance_matrices.entities.distance_matrix import DistanceMatrix
from src.domain.impedance_matrices.entities.travel_time_matrix import TravelTimeMatrix

class ImpedanceMatricesRepository(ABC):

    @abstractmethod
    def get_travel_time_matrix_from_file(self, file_path) -> TravelTimeMatrix:
        pass

    @abstractmethod
    def get_distance_matrix_from_file(self, file_path) -> DistanceMatrix:
        pass
