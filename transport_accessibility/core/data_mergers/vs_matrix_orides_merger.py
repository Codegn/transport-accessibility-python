import pandas as pd
from transport_accessibility.core.readers.orides_reader import ZONE_COLUMN
from transport_accessibility.core.readers.vs_matrix_reader import DESTINATION_ZONE_COLUMN

class VSMatrixOridesMerger:

    def __init__(self, vs_matrix: pd.DataFrame, orides: pd.DataFrame):
        self.vs_matrix = vs_matrix
        self.orides = orides

    def merge(self):
        merged = pd.merge(self.vs_matrix, self.orides, left_on=DESTINATION_ZONE_COLUMN, right_on=ZONE_COLUMN, how='left')
        return merged
