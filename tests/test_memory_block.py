import unittest
from nvram_tool.memory_block import MemoryBlock

class TestMemoryBlock(unittest.TestCase):

    def test_valid_memory_block(self):
        block = MemoryBlock(
            name="TestBlock",
            variables=["var1", "var2"],
            data_types=["uint8", "boolean"],
            store_timing="ONFLY",
            reset_safe=True,
            onfly_functions=["func1", "func2"],
            reset_safe_schedules=["10ms", "20ms"]
        )
        self.assertTrue(block.is_valid())

    def test_invalid_memory_block_too_large(self):
        block = MemoryBlock(
            name="TestBlock",
            variables=["var1", "var2"],
            data_types=["uint8"] * 700,
            store_timing="ONFLY",
            reset_safe=True,
            onfly_functions=["func1"] * 700,
            reset_safe_schedules=["10ms"] * 700
        )
        self.assertFalse(block.is_valid())

    def test_invalid_memory_block_missing_onfly_function(self):
        block = MemoryBlock(
            name="TestBlock",
            variables=["var1", "var2"],
            data_types=["uint8", "boolean"],
            store_timing="ONFLY",
            reset_safe=True,
            onfly_functions=["func1", ""],
            reset_safe_schedules=["10ms", "20ms"]
        )
        self.assertFalse(block.is_valid())

    def test_invalid_memory_block_missing_resetsafe_schedule(self):
        block = MemoryBlock(
            name="TestBlock",
            variables=["var1", "var2"],
            data_types=["uint8", "boolean"],
            store_timing="ONFLY",
            reset_safe=True,
            onfly_functions=["func1", "func2"],
            reset_safe_schedules=["10ms", ""]
        )
        self.assertFalse(block.is_valid())

if __name__ == '__main__':
    unittest.main()
