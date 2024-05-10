import pandas as pd

from src.domain.orides.entities.orides import ProcessedOrides
from src.domain.sv_matrix.repository.sv_matrix_repository import SvMatrixRepository


class SvMatrixRepositoryImpl(SvMatrixRepository):

    def get_from_file(self):
        raise NotImplementedError

    def process(self, processed_orides: ProcessedOrides):
        raise NotImplementedError

    def get_data(self) -> pd.DataFrame:
        raise NotImplementedError