from src.domain.orides.entities.orides import Orides, ProcessedOrides
from src.domain.orides.repository.orides_repository import OridesRepository

class GetProcessedOrides:
    def __init__(self, orides_repository: OridesRepository):
        self.orides_repository = orides_repository

    def get_from_file(self, file_path: str) -> ProcessedOrides:
        """
        Get orides from file and process it to remove unnecessary data
        """
        orides: Orides = self.orides_repository.get_from_file(file_path)
        processed_orides: ProcessedOrides = self.orides_repository.process(orides)
        return processed_orides