from abc import ABC, abstractmethod
from pathlib import Path

from src.domain.oportunities.entities.oportunities_by_zone import OportunitiesByZone
from src.domain.oportunities.entities.oportunities_source_type import OportunitiesSourceType

class OportunitiesRepository(ABC):

    @abstractmethod
    def get_oportunities_from_file(self, file_path: Path, oportunities_source: OportunitiesSourceType) -> OportunitiesByZone:
        pass

    @abstractmethod
    def save_oportunities_to_file(self, output_path: Path, oportunities_zone: OportunitiesByZone) -> None:
        pass
