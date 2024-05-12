from datetime import timedelta
import unittest

from local_paths import example_vs_matrix_path, example_orides_path, output_folder
from src.domain.accessibility_types import AccessibilityType
from src.domain.impedance_matrices.entities.impedance_type import ImpedanceType
from src.domain.transport_modes import TransportMode
from src.presentation.cli import calculate_acc_from_orides_and_sv_matrix


class TestAppExecution(unittest.TestCase):
    def test_app_execution(self):
        calculate_acc_from_orides_and_sv_matrix(
            example_vs_matrix_path,
            example_orides_path,
            output_folder,
            AccessibilityType.UMBRAL,
            timedelta(minutes=30),
            ImpedanceType.TIME,
            TransportMode.PUBLIC,
        )


if __name__ == "__main__":
    unittest.main()
