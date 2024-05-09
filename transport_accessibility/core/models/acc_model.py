from src.domain.accessibility_types import AccessibilityType
from transport_accessibility.core.readers.vs_matrix_reader import ORIGIN_ZONE_COLUMN, TOTAL_TIME_COLUMN
from transport_accessibility.core.readers.orides_reader import DESTINATION_TRIPS_COLUMN
import pandas as pd
import numpy as np

DEFAULT_UMBRAL = 30

class AccessibilityModel:

    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.calculation_methods = {
            AccessibilityType.umbral: lambda self: self.umbral_method(),
            AccessibilityType.loglog: lambda self: self.loglog_method(),
        }

    def calculate(self, method_name: str) -> pd.DataFrame:
        """
        This method calculates the accessibility using the specified method.
        """
        if method_name in self.calculation_methods:
            return self.calculation_methods[method_name](self)
        else:
            raise ValueError(f'Invalid method name: {method_name}')

    def umbral_method(self, umbral: int = DEFAULT_UMBRAL) -> pd.DataFrame:
        """
        This method calculates the accessibility using the umbral method.
        """
        self.data['dummy_'+str(umbral)] = np.where(self.data[TOTAL_TIME_COLUMN] <= umbral, 1, 0)
        df_acc = self.data[self.data['dummy_'+str(umbral)] == 1].groupby(
            ORIGIN_ZONE_COLUMN
        ).agg(
            {DESTINATION_TRIPS_COLUMN:'sum'}
        ).reset_index().rename(
            columns={DESTINATION_TRIPS_COLUMN:DESTINATION_TRIPS_COLUMN + '_' + str(umbral)}
        )
        return df_acc

    def loglog_method(self, loglog_param) -> pd.DataFrame:
        raise NotImplementedError('Method not implemented yet')