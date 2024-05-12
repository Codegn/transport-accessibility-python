import pandas as pd

from src.application.accessibility_calculator.accessibility_calculator import MAX_TOTAL_TIME, MIN_TOTAL_TIME
from src.domain.impedance_matrices.entities.travel_time_matrix import TravelTimeMatrix
from src.domain.transport_modes import TransportMode
from src.infrastructure.sources.file_readers.basic_csv_reader import BasicCSVReader

VS_MATRIX_COLUMNS = ["H", "MODO ", ' "ZO"', ' "ZD"', "T_CAMI", "T_ESPE", "T_VIAJ", "VIAJES"]

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
    TRIPS_COLUMN,
]

TOTAL_TIME_COLUMN = "total_time"

TPUB_MODES = ["cam", "busT", "txc", "metro", "metbusT", "mettxc"]

TPRIV_MODES = ["cam", "ach", "aac", "taxi"]

TRANSPORT_MODES_DICT = {TransportMode.PUBLIC: TPUB_MODES, TransportMode.PRIVATE: TPRIV_MODES}

FIRST_PERIOD_HOUR = 1
SECOND_PERIOD_HOUR = 2


class SVMatrixReader(BasicCSVReader):

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
        self.df = (
            self.df.groupby([ORIGIN_ZONE_COLUMN, DESTINATION_ZONE_COLUMN])
            .agg({TOTAL_TIME_COLUMN: "min", TRIPS_COLUMN: "sum"})
            .reset_index()
        )

    def _calculate_total_time(self):
        """
        Calculates the total time of a trip.
        """
        self.df[TOTAL_TIME_COLUMN] = (
            self.df[WAIT_TIME_COLUMN] + self.df[WAIT_TIME_COLUMN] + self.df[TRAVEL_TIME_COLUMN]
        )

    def _total_time_corrections(self):
        """
        Applies corrections to the total time of a trip.
        """
        self.df[TOTAL_TIME_COLUMN] = self.df[TOTAL_TIME_COLUMN].apply(
            lambda x: x if x <= MAX_TOTAL_TIME else MAX_TOTAL_TIME
        )
        self.df[TOTAL_TIME_COLUMN] = self.df[TOTAL_TIME_COLUMN].apply(
            lambda x: x if x >= MIN_TOTAL_TIME else MIN_TOTAL_TIME
        )

    def _from_df_to_travel_time_matrix(self) -> TravelTimeMatrix:
        """
        Converts a pandas DataFrame to a TravelTimeMatrix object.
        """
        travel_time_matrix_dict = {
            (row[ORIGIN_ZONE_COLUMN], row[DESTINATION_ZONE_COLUMN]): row[TOTAL_TIME_COLUMN]
            for _, row in self.df.iterrows()
        }
        return TravelTimeMatrix(travel_time_matrix_dict)

    def read_and_process_travel_time_data(self, transport_mode: TransportMode) -> TravelTimeMatrix:
        """
        Runs the complete process of reading, filtering, renaming, grouping, calculating and correcting the data.
        """
        self._read_csv_file()
        self._filter_columns(VS_MATRIX_COLUMNS)
        self._rename_columns(dict(zip(VS_MATRIX_COLUMNS, VS_MATRIX_COLUMNS_RENAMED)))
        self._filter_by_hour(FIRST_PERIOD_HOUR)
        self._filter_by_transport_mode(transport_mode)
        self._calculate_total_time()
        self._groupby_min_total_time()
        self._total_time_corrections()
        travel_time_matrix = self._from_df_to_travel_time_matrix()
        return travel_time_matrix
