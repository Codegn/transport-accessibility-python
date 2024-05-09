from dataclasses import dataclass
import pandas as pd

@dataclass
class SVMatrix:
    data: pd.DataFrame

class ProcessedSVMatrix(SVMatrix):
    pass