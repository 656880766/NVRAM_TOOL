
import unittest
import os
from nvram_tool.memory_block import MemoryBlock
from nvram_tool.generator import ConfGenerator
from nvram_tool.parser import ExcelParser


class TestConfGenerator(unittest.TestCase):
    #blocks_test = ExcelParser.parse_excel('data/Test_Spec_NVRAM_1.0.xlsx')
    def test_generate_conf_h(self):
        # blocks = [
        #     MemoryBlock(
        #         name="TestBlock",
        #         variables=["var1", "var2"],
        #         data_types=["uint8", "boolean"],
        #         store_timing="ONFLY",
        #         reset_safe=True,
        #         onfly_functions=["func1", "func2"],
        #         reset_safe_schedules=["10ms", "20ms"]
        #     ),
        #
        #     MemoryBlock(
        #         name="TestBlock",
        #         variables=["Crc8_u8var1", "var2"],
        #         data_types=["uint8", "single"],
        #         store_timing="POWER_LATCH_MODE",
        #         reset_safe=True,
        #         onfly_functions=[],
        #         reset_safe_schedules=["10ms", "20ms"]
        #     )
        # ]
#Tester si onfly et post ou power launch sont valident

        blocksValid = ExcelParser.parse_excel('data_test/TestValid.xlsx')
        blocksNotValid = ExcelParser.parse_excel('data_test/TestValid.xlsx')
        output_path_valid = 'output_test/TestValid_conf.h'
        output_path_not_valid = 'output_test/TestNotValid_conf.h'
        ConfGenerator.generate_conf_h(blocksValid, output_path_valid)
        self.assertTrue(os.path.exists(output_path_not_valid))
        ConfGenerator.generate_conf_h(blocksNotValid, output_path_not_valid)
        self.assertFalse(os.path.exists(output_path_not_valid))


if __name__ == '__main__':
    unittest.main()
