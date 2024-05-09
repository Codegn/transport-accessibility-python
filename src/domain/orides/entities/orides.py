from dataclasses import dataclass
import pandas as pd

@dataclass
class Orides:
    data: pd.DataFrame

class ProcessedOrides(Orides):
    pass