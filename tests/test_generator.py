
import unittest
import os
from nvram_tool.memory_block import MemoryBlock
from nvram_tool.generator import ConfGenerator

class TestConfGenerator(unittest.TestCase):

    def test_generate_conf_h(self):
        blocks = [
            MemoryBlock(
                name="TestBlock",
                variables=["var1", "var2"],
                data_types=["uint8", "boolean"],
                store_timing="ONFLY",
                reset_safe=True,
                onfly_functions=["func1", "func2"],
                reset_safe_schedules=["10ms", "20ms"]
            )
        ]
        output_path = 'output/test_conf.h'
        ConfGenerator.generate_conf_h(blocks, output_path)
        self.assertTrue(os.path.exists(output_path))

if __name__ == '__main__':
    unittest.main()
