import pandas as pd
from src.domain.oportunities.entities.oportunities_by_zone import OportunitiesByZone
from src.domain.oportunities.entities.oportunity import Oportunity
from src.domain.zone import Zone
from src.infrastructure.sources.file_readers.basic_csv_reader import BasicCSVReader

ZONE_COLUMN = "zone"
TRIP_TYPE_COLUMN = "trip_type"
TRIPS_COLUMN = "trips"
DESTINATION_TRIPS_COLUMN = "destination_trips"
DESTINATION_TYPE_ID = 1

class OridesReader(BasicCSVReader):

    def _read_csv_file(self):
        self.df = pd.read_csv(
            self.file_path,
            skiprows=0,
            header=None,
            names = [
                ZONE_COLUMN, 
                TRIP_TYPE_COLUMN, 
                TRIPS_COLUMN
                ],
            sep='\s+', # type: ignore
            engine='python'
        )

        return self.df

    def _filter_destination_rows(self):
        """
        Filters the rows with destination trips.
        """
        self.df = self.df[self.df[TRIP_TYPE_COLUMN] == DESTINATION_TYPE_ID].copy()

    def _rename_trips_column(self):
        """
        Renames the trips column to destination_trips.
        """
        self.df = self.df.rename(columns={TRIPS_COLUMN: DESTINATION_TRIPS_COLUMN})

    def _from_df_to_oportunities_by_zone(self) -> OportunitiesByZone:
        """
        Converts a pandas DataFrame to an OportunitiesByZone object.
        """
        oportunities_by_zone_dict = {
            Zone(row[ZONE_COLUMN]): Oportunity(row[DESTINATION_TRIPS_COLUMN])
            for _, row in self.df.iterrows()
        }
        return OportunitiesByZone(oportunities_by_zone_dict)
    
    def read_and_process_data(self) -> OportunitiesByZone:
        self._read_csv_file()
        self._filter_destination_rows()
        self._rename_trips_column()
        oportunities_by_zone = self._from_df_to_oportunities_by_zone()
        return oportunities_by_zone
