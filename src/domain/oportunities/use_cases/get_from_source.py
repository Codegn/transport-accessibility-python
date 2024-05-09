from src.domain.oportunities.entities.oportunities_by_zone import OportunitiesByZone
from src.domain.oportunities.repository.oportunities_repository import OportunitiesRepository

class GetOportunitiesFromSource:

    def __init__(self, oportunities_repository: OportunitiesRepository):
        self.oportunities_repository = oportunities_repository

    def get_from_file(self, file_path: str) -> OportunitiesByZone:

        oportunities_by_zone: OportunitiesByZone = self.oportunities_repository.get_oportunities_from_file(file_path)

        return oportunities_by_zone
    
    def get_from_api(self, api_url: str) -> OportunitiesByZone:
        raise NotImplementedError