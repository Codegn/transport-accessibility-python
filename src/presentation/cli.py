from datetime import timedelta
from pathlib import Path
import typer
import logging
from src.domain.accessibility_types import AccessibilityType
from src.domain.impedance_matrices.entities.distance import Distance
from src.domain.impedance_matrices.entities.impedance_matrix_source_type import ImpedanceMatrixSourceType
from src.domain.impedance_matrices.entities.impedance_type import ImpedanceType
from src.domain.transport_modes import TransportMode
from src.main import generate_container

container = generate_container()
app = typer.Typer()
logger = logging.getLogger(__name__)

@app.command()
def calculate_acc_from_orides_and_sv_matrix(
    sv_matrix_path: str,
    orides_path: str,
    output_folder: str,
    accessibility_type: AccessibilityType = AccessibilityType.UMBRAL,
    umbral: timedelta | Distance | None = None,
    impedance_type: ImpedanceType = ImpedanceType.TIME,
    transport_mode: TransportMode = TransportMode.PUBLIC,
    ):
    logger.info("Calculating accessibility")

    impedance_matrix_file_path = Path(sv_matrix_path)
    oportunities_file_path = Path(orides_path)

    accessibility = container.accessibility_calculator().calculate_accessibility(
        impedance_type,
        impedance_matrix_file_path,
        oportunities_file_path,
        ImpedanceMatrixSourceType.SV_MATRIX,
        accessibility_type,
        transport_mode,
        umbral,
    )

    print(accessibility)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app()
    