from datetime import timedelta
import typer
import logging
from src.domain.accessibility_types import AccessibilityType
from src.domain.impedance_matrices.entities.distance import Distance
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
    ):
    raise NotImplementedError

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app()
    