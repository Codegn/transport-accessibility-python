import pandas as pd

class BasicCSVReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def _read_csv_file(self):
        """
        Reads a CSV file into a pandas DataFrame.
        """
        self.df = pd.read_csv(self.file_path)