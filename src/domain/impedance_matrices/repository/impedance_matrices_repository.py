from abc import ABC, abstractmethod
from pathlib import Path

from src.domain.impedance_matrices.entities.impedance_matrix import ImpedanceMatrix
from src.domain.impedance_matrices.entities.impedance_matrix_source_type import (
    ImpedanceMatrixSourceType,
)
from src.domain.impedance_matrices.entities.impedance_type import ImpedanceType
from src.domain.transport_modes import TransportMode


class ImpedanceMatricesRepository(ABC):

    @abstractmethod
    def get_impedance_matrix_from_file(
        self,
        file_path: Path,
        impedance_matrix_source: ImpedanceMatrixSourceType,
        impedance_type: ImpedanceType,
        transport_mode: TransportMode,
    ) -> ImpedanceMatrix:
        pass
