from pathlib import Path
from src.domain.oportunities.entities.oportunities_by_zone import OportunitiesByZone
from src.domain.oportunities.entities.oportunities_source_type import OportunitiesSourceType
from src.domain.oportunities.repository.oportunities_repository import OportunitiesRepository
from src.infrastructure.components.oportunities_reader import OportunitiesReader


class OportunitiesRepositoryImpl(OportunitiesRepository):

    def __init__(self, oportunities_reader: OportunitiesReader):
        self.oportunities_reader = oportunities_reader

    def get_oportunities_from_file(self, file_path: Path, oportunities_source: OportunitiesSourceType) -> OportunitiesByZone:
        return self.oportunities_reader.read_oportunities(file_path, oportunities_source)

    def save_oportunities_to_file(self, output_path: Path, oportunities_by_zone: OportunitiesByZone) -> None:
        raise NotImplementedError
