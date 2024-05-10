from pathlib import Path
from src.domain.oportunities.entities.oportunities_by_zone import OportunitiesByZone
from src.domain.oportunities.entities.oportunities_source_type import OportunitiesSourceType
from src.domain.oportunities.repository.oportunities_repository import OportunitiesRepository


class GetOportunitiesFromSource:

    def __init__(self, oportunities_repository: OportunitiesRepository):
        self.oportunities_repository = oportunities_repository

    def get_from_file(self, file_path: Path, oportunities_source: OportunitiesSourceType) -> OportunitiesByZone:

        oportunities_by_zone: OportunitiesByZone = self.oportunities_repository.get_oportunities_from_file(
            file_path, oportunities_source
        )

        return oportunities_by_zone

    def get_from_api(self, api_url: Path) -> OportunitiesByZone:
        raise NotImplementedError
