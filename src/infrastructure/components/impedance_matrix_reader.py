from pathlib import Path

from src.domain.impedance_matrices.entities.impedance_matrix import ImpedanceMatrix
from src.domain.impedance_matrices.entities.impedance_matrix_source_type import (
    ImpedanceMatrixSourceType,
)
from src.domain.impedance_matrices.entities.impedance_type import ImpedanceType
from src.domain.impedance_matrices.entities.travel_time_matrix import TravelTimeMatrix
from src.domain.transport_modes import TransportMode
from src.infrastructure.sources.file_readers.sv_matrix_reader import SVMatrixReader


class ImpedanceMatrixReader:

    # TODO check if SVMatrixReader should be injected

    def _read_travel_time_matrix_from_sv_matrix(
        self, file_path: Path, transport_mode: TransportMode
    ) -> TravelTimeMatrix:

        sv_matrix_reader = SVMatrixReader(file_path)
        return sv_matrix_reader.read_and_process_travel_time_data(transport_mode)

    def read_impedance_matrix(
        self,
        file_path: Path,
        impedance_matrix_source: ImpedanceMatrixSourceType,
        impedance_type: ImpedanceType,
        transport_mode: TransportMode,
    ) -> ImpedanceMatrix:

        if impedance_matrix_source == ImpedanceMatrixSourceType.SV_MATRIX:
            if impedance_type == ImpedanceType.TIME:
                return self._read_travel_time_matrix_from_sv_matrix(file_path, transport_mode)

        raise NotImplementedError
