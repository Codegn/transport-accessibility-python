import numpy as np
import pandas as pd

from src.domain.acc_model.entities.acc_results import AccessibilityResults
from src.domain.acc_model.repository.acc_model_repository import AccModelRepository
from src.domain.sv_matrix.entities.sv_matrix import ProcessedSVMatrix
from src.infrastructure.data_models.sv_matrix_data import ProcessedSVMatrixData

class AccModelRepositoryImpl(AccModelRepository):
    
    def calculate_with_loglog_method(self, processed_sv_matrix: ProcessedSVMatrix):
        raise NotImplementedError

    def calculate_with_umbral_method(
            self, 
            processed_sv_matrix: ProcessedSVMatrix, 
            umbral: int = 30
        ) -> AccessibilityResults:

        """
        Calculate the accessibility with the umbral method
        """

        df = processed_sv_matrix.get_data()

        df['dummy_'+str(umbral)] = np.where(df[ProcessedSVMatrix.total_time_column] <= umbral, 1, 0)

        df_acc = df[df['dummy_'+str(umbral)] == 1].groupby(
            ProcessedSVMatrixData.origin_zone_column
        ).agg(
            {ProcessedSVMatrix.destination_trips_column:'sum'}
        ).reset_index().rename(
            columns={
                ProcessedSVMatrix.destination_trips_column:ProcessedSVMatrix.destination_trips_column + '_' + str(umbral)
                }
        )

        return AccessibilityResults(df_acc)