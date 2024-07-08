import unittest
import pandas as pd
from nvram_tool.comparator import SpecComparator

class TestSpecComparator(unittest.TestCase):

    def test_compare_specs(self):
        spec_n = pd.read_excel('data_test/Test_Spec_NVRAM_1.0.xlsx', skiprows=[1])
        spec_n1 = pd.read_excel('data_test/Test_Spec_NVRAM_2.0.xlsx', skiprows=[1])
        comparator = SpecComparator(spec_n, spec_n1)
        differences = comparator.compare_specs()
        self.assertIsInstance(differences, dict)

if __name__ == '__main__':
    unittest.main()
