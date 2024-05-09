import pandas as pd
from src.infraestructure.sources.file_readers.basic_csv_reader import BasicCSVReader
from src.infraestructure.data_models.orides_data import OridesData

class OridesReader(BasicCSVReader):

    def read_csv_file(self):
        self.df = pd.read_csv(
            self.file_path,
            skiprows=0,
            header=None,
            names = [
                OridesData.zone_column, 
                OridesData.trip_type_column, 
                OridesData.trips_column
                ],
            sep='\s+',
            engine='python'
        )

        return self.df

    def filter_destination_rows(self):
        """
        Filters the rows with destination trips.
        """
        self.df = self.df[self.df[OridesData.trip_type_column] == OridesData.destination_type_id].copy()

    def rename_trips_column(self):
        """
        Renames the trips column to destination_trips.
        """
        self.df = self.df.rename(columns={OridesData.trips_column: OridesData.destination_trips_column})

    def process_data(self):
        self._read_csv_file()
        self._filter_destination_rows()
        self._rename_trips_column()
        return self.df
