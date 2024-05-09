from src.domain.oportunities.entities.oportunities_by_zone import Oportunities
from src.domain.oportunities.repository.oportunities_repository import OportunitiesRepository

class SaveOportunitiesToFile:
    def __init__(self, oportunities_repository: OportunitiesRepository):
        self.oportunities_repository = oportunities_repository

    def save_to_file(self, output_path: str, oportunities: Oportunities) -> None:
        self.oportunities_repository.save_oportunities_to_file(output_path, oportunities)
