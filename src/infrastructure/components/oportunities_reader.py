from pathlib import Path

from src.domain.oportunities.entities.oportunities_by_zone import OportunitiesByZone
from src.domain.oportunities.entities.oportunities_source_type import OportunitiesSourceType
from src.infrastructure.sources.file_readers.orides_reader import OridesReader

class OportunitiesReader:

    def _read_from_orides(self, file_path: Path) -> OportunitiesByZone:
        orides_reader = OridesReader(file_path)
        return orides_reader.read_and_process_data()

    def read_oportunities(self, file_path: Path, oportunities_source: OportunitiesSourceType) -> OportunitiesByZone:
        if oportunities_source == OportunitiesSourceType.ORIDES:
            return self._read_from_orides(file_path)
        
        raise NotImplementedError
