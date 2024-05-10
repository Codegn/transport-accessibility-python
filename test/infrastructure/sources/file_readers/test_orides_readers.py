from pathlib import Path
import unittest
from unittest.mock import patch

import pandas as pd

from src.infrastructure.sources.file_readers.orides_reader import TRIP_TYPE_COLUMN, OridesReader


class TestOridesReader(unittest.TestCase):
    def setUp(self):
        self.reader = OridesReader(Path("test.csv"))

    @patch("src.infrastructure.sources.file_readers.orides_reader.pd")
    def test_filter_destination_rows(self, mock_pd):
        mock_df = pd.DataFrame()
        mock_pd.read_csv.return_value = mock_df
        self.reader._read_csv_file()

        mock_df[TRIP_TYPE_COLUMN] = [1, 1, 1, 2, 2]
        expected_filtered_df = pd.DataFrame([1, 1, 1], columns=[TRIP_TYPE_COLUMN])

        self.reader._filter_destination_rows()

        pd.testing.assert_frame_equal(self.reader.df, expected_filtered_df)


if __name__ == "__main__":
    unittest.main()
