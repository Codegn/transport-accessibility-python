import unittest

from main import calculate_acc_from_vs_matrix
from local_paths import example_vs_matrix_path, example_orides_path, output_folder

class TestAppExecution(unittest.TestCase):
    def test_app_execution(self):
        calculate_acc_from_vs_matrix(
            example_vs_matrix_path, 
            example_orides_path,
            output_folder
        )

if __name__ == '__main__':
    unittest.main()