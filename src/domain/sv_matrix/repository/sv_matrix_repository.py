from abc import ABC, abstractmethod

from src.domain.orides.entities.orides import ProcessedOrides

class SvMatrixRepository(ABC):

    @abstractmethod
    def get_from_file(self):
        pass

    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def append_processed_orides_data(self, processed_orides: ProcessedOrides):
        pass