from dataclasses import dataclass
from src.domain.orides.entities.orides import Orides

@dataclass(kw_only=True)
class OridesData(Orides):
    zone_column: str = "zone"
    trip_type_column: str = "trip_type"
    trips_column: str = "trips"
    destination_trips_column: str = "destination_trips"
    destination_type_id: int = 1

class ProcessedOridesData(OridesData):
    pass