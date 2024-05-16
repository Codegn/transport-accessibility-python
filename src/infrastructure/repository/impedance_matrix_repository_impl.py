from pathlib import Path

from src.domain.impedance_matrices.entities.impedance_matrix import ImpedanceMatrix
from src.domain.impedance_matrices.entities.impedance_matrix_source_type import (
    ImpedanceMatrixSourceType,
)
from src.domain.impedance_matrices.entities.impedance_type import ImpedanceType
from src.domain.impedance_matrices.repository.impedance_matrices_repository import (
    ImpedanceMatricesRepository,
)
from src.domain.transport_modes import TransportMode
from src.infrastructure.components.impedance_matrix_reader import ImpedanceMatrixReader


class ImpedanceMatricesRepositoryImpl(ImpedanceMatricesRepository):

    def __init__(self, impedance_matrix_reader: ImpedanceMatrixReader):
        self.impedance_matrix_reader = impedance_matrix_reader

    def get_impedance_matrix_from_file(
        self,
        file_path: Path,
        impedance_matrix_source: ImpedanceMatrixSourceType,
        impedance_type: ImpedanceType,
        transport_mode: TransportMode,
    ) -> ImpedanceMatrix:
        return self.impedance_matrix_reader.read_impedance_matrix(
            file_path, impedance_matrix_source, impedance_type, transport_mode
        )
