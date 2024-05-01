import pandas as pd
from transport_accessibility.core.transport_modes import TransportMode
from transport_accessibility.core.value_objects import MAX_TOTAL_TIME, MIN_TOTAL_TIME
from transport_accessibility.core.readers.basic_csv_reader import BasicCSVReader
from enum import Enum

VS_MATRIX_COLUMNS = [
    "H",
    "MODO ",
    ' "ZO"',
    ' "ZD"',
    "T_CAMI",
    "T_ESPE",
    "T_VIAJ",
    "VIAJES"
]

HOUR_COLUMN = "hour"
MODE_COLUMN = "mode"
ORIGIN_ZONE_COLUMN = "origin_zone"
DESTINATION_ZONE_COLUMN = "destination_zone"
WALK_TIME_COLUMN = "walk_time"
WAIT_TIME_COLUMN = "wait_time"
TRAVEL_TIME_COLUMN = "travel_time"
TRIPS_COLUMN = "trips"

VS_MATRIX_COLUMNS_RENAMED = [
    HOUR_COLUMN,
    MODE_COLUMN,
    ORIGIN_ZONE_COLUMN,
    DESTINATION_ZONE_COLUMN,
    WALK_TIME_COLUMN,
    WAIT_TIME_COLUMN,
    TRAVEL_TIME_COLUMN,
    TRIPS_COLUMN
]

TOTAL_TIME_COLUMN = "total_time"

TPUB_MODES = [
    'cam', 
    'busT', 
    'txc', 
    'metro', 
    'metbusT', 
    'mettxc'
]

TPRIV_MODES = [
    'cam',
    'ach', 
    'aac', 
    'taxi'
]

TRANSPORT_MODES_DICT = {
    TransportMode.public: TPUB_MODES,
    TransportMode.private: TPRIV_MODES
}

FIRST_PERIOD_HOUR = 1
SECOND_PERIOD_HOUR = 2

class VSMatrixReader(BasicCSVReader):

    def _filter_columns(self, columns: list[str]):
        """
        Filters selected columns from a DataFrame.
        """
        self.df = self.df[columns].copy()
    
    def _rename_columns(self, columns: dict[str, str]):
        """
        Renames columns in a DataFrame.
        """
        self.df.rename(columns=columns, inplace=True)

    def _filter_by_hour(self, hour: int = FIRST_PERIOD_HOUR):
        """
        Filters a DataFrame by hour.
        """
        self.df = self.df[self.df[HOUR_COLUMN] == hour].copy()

    def _filter_by_transport_mode(self, mode: TransportMode):
        """
        Filters a DataFrame by transport mode.
        """
        self.df = self.df[self.df[MODE_COLUMN].isin(TRANSPORT_MODES_DICT[mode])].copy()

    def _groupby_min_total_time(self):
        """
        Groups a DataFrame by origin_zone and destination_zone and calculates the minimum travel time.
        """
        self.df = self.df.groupby([ORIGIN_ZONE_COLUMN, DESTINATION_ZONE_COLUMN]).agg({TOTAL_TIME_COLUMN: "min", TRIPS_COLUMN: "sum"}).reset_index()
    
    def _calculate_total_time(self):
        """
        Calculates the total time of a trip.
        """
        self.df[TOTAL_TIME_COLUMN] = self.df[WAIT_TIME_COLUMN] + self.df[WAIT_TIME_COLUMN] + self.df[TRAVEL_TIME_COLUMN]

    def _total_time_corrections(self):
        """
        Applies corrections to the total time of a trip.
        """
        self.df[TOTAL_TIME_COLUMN] = self.df[TOTAL_TIME_COLUMN].apply(lambda x: x if x <= MAX_TOTAL_TIME else MAX_TOTAL_TIME)
        self.df[TOTAL_TIME_COLUMN] = self.df[TOTAL_TIME_COLUMN].apply(lambda x: x if x >= MIN_TOTAL_TIME else MIN_TOTAL_TIME)

    def process_data(self, mode: TransportMode = TransportMode.public) -> pd.DataFrame:
        """
        Runs the complete process of reading, filtering, renaming, grouping, calculating and correcting the data.
        """
        self._read_csv_file()
        self._filter_columns(VS_MATRIX_COLUMNS)
        self._rename_columns(dict(zip(VS_MATRIX_COLUMNS, VS_MATRIX_COLUMNS_RENAMED)))
        self._filter_by_hour(FIRST_PERIOD_HOUR)
        self._filter_by_transport_mode(mode)
        self._calculate_total_time()
        self._groupby_min_total_time()
        self._total_time_corrections()
        return self.df
    