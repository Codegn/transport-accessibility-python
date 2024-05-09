import pandas as pd
from src.domain.orides.entities.orides import Orides, ProcessedOrides
from src.domain.orides.repository.orides_repository import OridesRepository
from src.infraestructure.sources.file_readers.orides_reader import OridesReader


class OridesRepositoryImpl(OridesRepository):

    def __init__(self, orides_reader: OridesReader):
        self.orides_reader = orides_reader

    def get_from_file(self, file_path) -> Orides:
        df = self.orides_reader.read_csv_file(file_path)
        return Orides(df)

    def process(self, orides: Orides) -> ProcessedOrides:
        pass

    def get_data(self) -> pd.DataFrame:
        raise NotImplementedError