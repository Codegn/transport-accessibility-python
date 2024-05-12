from datetime import timedelta
from pathlib import Path

import numpy as np
import pandas as pd

from src.domain.accessibility.entities.accessibility import Accessibility
from src.domain.accessibility.entities.accessibility_by_zone import AccessibilityByZone
from src.domain.accessibility_types import AccessibilityType
from src.domain.impedance_matrices.entities.distance import Distance
from src.domain.impedance_matrices.entities.impedance_matrix import ImpedanceMatrix
from src.domain.oportunities.entities.oportunities_by_zone import OportunitiesByZone
from src.domain.zone import Zone

ORIGIN_ZONE_COLUMN = "origin_zone"
DESTINATION_ZONE_COLUMN = "destination_zone"
IMPEDANCE_COLUMN = "impedance"
ZONE_COLUMN = "zone"
OPORTUNITIES_COLUMN = "oportunities"


class AccessibilityProcessor:

    def _impedance_matrix_to_df(self, impedance_matrix: ImpedanceMatrix) -> pd.DataFrame:

        data = [[str(key[0].id), str(key[1].id), value] for key, value in impedance_matrix.data.items()]
        df = pd.DataFrame(data, columns=[ORIGIN_ZONE_COLUMN, DESTINATION_ZONE_COLUMN, IMPEDANCE_COLUMN])
        return df

    def _oportunities_by_zone_to_df(self, oportunities_by_zone: OportunitiesByZone) -> pd.DataFrame:

        data = [[str(key.id), value.value] for key, value in oportunities_by_zone.data.items()]
        df = pd.DataFrame(data, columns=[ZONE_COLUMN, OPORTUNITIES_COLUMN])
        return df

    def _df_to_accessibility_by_zone(self, df: pd.DataFrame) -> AccessibilityByZone:

        accessibility_by_zone_dict = {
            Zone(int(float(row[ORIGIN_ZONE_COLUMN]))): Accessibility(row[OPORTUNITIES_COLUMN])
            for _, row in df.iterrows()
        }
        return AccessibilityByZone(accessibility_by_zone_dict)

    def _process_umbral_accessibility(
        self, impedance_matrix_df: pd.DataFrame, oportunities_by_zone_df: pd.DataFrame, umbral: timedelta | Distance
    ) -> pd.DataFrame:

        df = pd.merge(
            impedance_matrix_df, oportunities_by_zone_df, left_on=DESTINATION_ZONE_COLUMN, right_on=ZONE_COLUMN
        )
        df["dummy_" + str(umbral)] = np.where(df[IMPEDANCE_COLUMN] <= umbral, 1, 0)
        df_acc = (
            df[df["dummy_" + str(umbral)] == 1]
            .groupby(ORIGIN_ZONE_COLUMN)
            .agg({OPORTUNITIES_COLUMN: "sum"})
            .reset_index()
        )
        return df_acc

    def process(
        self,
        accessibility_type: AccessibilityType,
        impedance_matrix: ImpedanceMatrix,
        oportunities_by_zone: OportunitiesByZone,
        umbral: timedelta | Distance | None = None,
    ) -> AccessibilityByZone:

        if accessibility_type == AccessibilityType.UMBRAL:
            if umbral is None:
                raise ValueError("Umbral is required for UMBRAL accessibility type")
            impedance_matrix_df = self._impedance_matrix_to_df(impedance_matrix)
            oportunities_by_zone_df = self._oportunities_by_zone_to_df(oportunities_by_zone)
            accessibility_by_zone_df = self._process_umbral_accessibility(
                impedance_matrix_df, oportunities_by_zone_df, umbral
            )
            accessibility_by_zone = self._df_to_accessibility_by_zone(accessibility_by_zone_df)
            return accessibility_by_zone

        raise NotImplementedError

    def save_accessibility_by_zone_to_file(self, accessibility_by_zone: AccessibilityByZone, output_file: Path):

        with open(output_file, "w") as f:
            f.write("zone_id,accessibility\n")
            for zone, accessibility in accessibility_by_zone.data.items():
                f.write(f"{zone.id},{accessibility.value}\n")
