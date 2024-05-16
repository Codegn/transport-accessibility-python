import logging
from datetime import timedelta
from pathlib import Path

import typer

from src.domain.accessibility_types import AccessibilityType
from src.domain.impedance_matrices.entities.distance import Distance
from src.domain.impedance_matrices.entities.impedance_matrix_source_type import (
    ImpedanceMatrixSourceType,
)
from src.domain.impedance_matrices.entities.impedance_type import ImpedanceType
from src.domain.transport_modes import TransportMode
from src.main import generate_container

container = generate_container()
app = typer.Typer()
logger = logging.getLogger(__name__)


@app.command()
def placeholder():
    pass


@app.command()
def calculate_acc_from_orides_and_sv_matrix(
    sv_matrix_path: str,
    orides_path: str,
    output_path: str,
    umbral: int = 30,
    accessibility_type: AccessibilityType = AccessibilityType.UMBRAL,
    impedance_type: ImpedanceType = ImpedanceType.TIME,
    transport_mode: TransportMode = TransportMode.PUBLIC,
):

    impedance_matrix_file_path = Path(sv_matrix_path)
    oportunities_file_path = Path(orides_path)

    if accessibility_type == AccessibilityType.UMBRAL:
        logger.info("Calculating accessibility with umbral")

        if umbral is None:
            raise ValueError(f"Invalid impedance type: {impedance_type}")

        if impedance_type == ImpedanceType.TIME:
            typed_umbral = timedelta(minutes=umbral)
        elif impedance_type == ImpedanceType.DISTANCE:
            typed_umbral = Distance(float(umbral))

    else:
        typed_umbral = None

    accessibility = container.accessibility_calculator().calculate_accessibility(
        impedance_type,
        impedance_matrix_file_path,
        oportunities_file_path,
        ImpedanceMatrixSourceType.SV_MATRIX,
        accessibility_type,
        transport_mode,
        typed_umbral,
    )

    container.accessibility_calculator().save_to_file(accessibility, Path(output_path))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app()
