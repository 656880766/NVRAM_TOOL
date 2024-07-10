# tests/test_parser.py
import unittest
from nvram_tool.parser import ExcelParser
from nvram_tool.memory_block import MemoryBlock

class TestExcelParser(unittest.TestCase):

    def test_parse_excel(self):
        blocks = ExcelParser.parse_excel('data_test/TestData1.xlsx')
        self.assertGreater(len(blocks), 0)
        for block in blocks:
            self.assertIsInstance(block, MemoryBlock)

if __name__ == '__main__':
    unittest.main()
