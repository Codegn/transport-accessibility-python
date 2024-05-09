from src.domain.oportunities.entities.oportunities_by_zone import Oportunities
from src.domain.oportunities.repository.oportunities_repository import OportunitiesRepository

class GetOportunitiesFromSource:

    def __init__(self, oportunities_repository: OportunitiesRepository):
        self.oportunities_repository = oportunities_repository

    def get_from_file(self, file_path: str) -> Oportunities:

        oportunities: Oportunities = self.oportunities_repository.get_oportunities_from_file(file_path)

        return oportunities
    
    def get_from_api(self, api_url: str) -> Oportunities:
        raise NotImplementedError