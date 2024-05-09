import typer
import logging
from src.main import generate_container

container = generate_container()
app = typer.Typer()
logger = logging.getLogger(__name__)

@app.command()
def calculate_acc(
    sv_matrix_path: str,
    orides_path: str,
    output_folder: str,
    accessibility_type: AccessibilityType = AccessibilityType.umbral
    ):
    raise NotImplementedError

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app()