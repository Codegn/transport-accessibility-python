from abc import ABC, abstractmethod

from src.domain.oportunities.entities.oportunities_by_zone import Oportunities

class OportunitiesRepository(ABC):

    @abstractmethod
    def get_oportunities_from_file(self, file_path) -> Oportunities:
        pass

    @abstractmethod
    def save_oportunities_to_file(self, output_path, oportunities: Oportunities) -> None:
        pass
