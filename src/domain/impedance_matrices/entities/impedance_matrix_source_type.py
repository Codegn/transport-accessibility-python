from enum import Enum

class ImpedanceMatrixSourceType(Enum):
    SV_MATRIX = "sv_matrix_file"

class TravelTimeMatrixSourceType(ImpedanceMatrixSourceType, Enum):
    # TODO: Averiguar si esto está bien
    pass

class DistanceMatrixSourceType(ImpedanceMatrixSourceType, Enum):
    pass
