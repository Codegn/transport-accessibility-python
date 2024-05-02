import os
import typer
import logging
from transport_accessibility.core.models.acc_model import AccessibilityModel
from transport_accessibility.core.acc_types import AccessibilityType
from transport_accessibility.core.readers.vs_matrix_reader import VSMatrixReader
from transport_accessibility.core.readers.orides_reader import OridesReader
from transport_accessibility.core.data_mergers.vs_matrix_orides_merger import VSMatrixOridesMerger
from transport_accessibility.utils import save_df_to_csv
import time

app = typer.Typer()
logger = logging.getLogger(__name__)

@app.command()
def process_vs_matrix_and_orides(
    vs_matrix_path: str,
    orides_path: str,
    output_folder: str
    ):
    start_time = time.time()

    logger.info("Processing VS Matrix and Orides data")
    vs_matrix_reader = VSMatrixReader(vs_matrix_path)
    vs_matrix_df = vs_matrix_reader.process_data()
    orides_reader = OridesReader(orides_path)
    orides_df = orides_reader.process_data()
    data_merger = VSMatrixOridesMerger(vs_matrix_df, orides_df)
    vs_matrix_df = data_merger.merge()
    save_df_to_csv(vs_matrix_df, os.path.join(output_folder, "vs_matrix_orides.csv"))

    end_time = time.time()
    execution_time = end_time - start_time
    logger.info("Execution time: {:.2f} seconds".format(execution_time))

@app.command()
def calculate_acc_from_vs_matrix(
    vs_matrix_path: str,
    orides_path: str,
    output_folder: str,
    accessibility_type: AccessibilityType = AccessibilityType.umbral
    ):
    start_time = time.time()

    logger.info("Calculating accessibility with " + str(accessibility_type) + " method")
    vs_matrix_reader = VSMatrixReader(vs_matrix_path)
    vs_matrix_df = vs_matrix_reader.process_data()
    orides_reader = OridesReader(orides_path)
    orides_df = orides_reader.process_data()
    data_merger = VSMatrixOridesMerger(vs_matrix_df, orides_df)
    vs_matrix_df = data_merger.merge()
    acc_model = AccessibilityModel(vs_matrix_df)
    result = acc_model.calculate(accessibility_type)
    save_df_to_csv(result, os.path.join(output_folder, "acc_result.csv"))

    end_time = time.time()
    execution_time = end_time - start_time
    logger.info("Execution time: {:.2f} seconds".format(execution_time))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app()
