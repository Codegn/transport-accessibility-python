from src.domain.sv_matrix.entities.sv_matrix import ProcessedSVMatrix
from src.domain.orides.use_cases.get_processed_orides import GetProcessedOrides


MIN_TOTAL_TIME = 5
MAX_TOTAL_TIME = 180

class CalculateAccessibilityFromProcessedSvMatrix:

    def __init__(self, 
                 get_processed_orides, 
                 get_processed_sv_matrix, 
                 run_acc_model
                 ):
        self.get_processed_orides = get_processed_orides
        self.get_processed_sv_matrix = get_processed_sv_matrix
        self.run_acc_model = run_acc_model

