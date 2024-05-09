from dataclasses import dataclass
from src.infraestructure.data_models.orides_data import ProcessedOridesData

@dataclass(kw_only=True)
class SVMatrixData:
    hour_column: str = "H"
    mode_column: str = "MODO "
    origin_zone_column: str = ' "ZO"'
    destination_zone_column: str = ' "ZD"'
    walk_time_column: str = "T_CAMI"
    wait_time_column: str = "T_ESPE"
    travel_time_column: str = "T_VIAJ"
    trips_column: str = "VIAJES"

@dataclass(kw_only=True)
class ProcessedSVMatrixData(SVMatrixData):
    hout_column: str = "hour"
    mode_column: str = "mode"
    origin_zone_column: str = "origin_zone"
    destination_zone_column: str = "destination_zone"
    walk_time_column: str = "walk_time"
    wait_time_column: str = "wait_time"
    travel_time_column: str = "travel_time"
    trips_column: str = "trips"
    total_time_column: str = "total_time"
    destination_trips_column: str = ProcessedOridesData.destination_trips_column