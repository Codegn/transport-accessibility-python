import pandas as pd
from src.infraestructure.sources.file_readers.basic_csv_reader import BasicCSVReader

ZONE_COLUMN = "zone"
TRIPS_TYPE_COLUMN = "trip_type"
TRIPS_COLUMN = "trips"
DESTINATION_TRIPS_COLUMN = "destination_trips"

ORIDES_COLUMNS = [
    ZONE_COLUMN,
    TRIPS_TYPE_COLUMN,
    TRIPS_COLUMN
]

DESTINATION_TYPE = 1

class OridesReader(BasicCSVReader):

    def _read_csv_file(self):
        self.df = pd.read_csv(
            self.file_path,
            skiprows=0,
            header=None,
            names = ORIDES_COLUMNS,
            sep='\s+',
            engine='python'
        )

    def _filter_destination_rows(self):
        """
        Filters the rows with destination trips.
        """
        self.df = self.df[self.df[TRIPS_TYPE_COLUMN] == DESTINATION_TYPE].copy()

    def _rename_trips_column(self):
        """
        Renames the trips column to destination_trips.
        """
        self.df = self.df.rename(columns={TRIPS_COLUMN: DESTINATION_TRIPS_COLUMN})

    def process_data(self):
        self._read_csv_file()
        self._filter_destination_rows()
        self._rename_trips_column()
        return self.df

    