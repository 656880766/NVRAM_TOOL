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
        isvalid, errorMessage = block.is_valid()
        self.assertTrue(block.is_valid(), errorMessage)

    def test_invalid_memory_block_too_large(self):
        block = MemoryBlock(
            name="TestBlock",
            variables=["var1", "var2"],
            data_types=["uint8"] * 700,
            store_timing="ONFLY",
            reset_safe=True,
            onfly_functions=["func1"],
            reset_safe_schedules=["dix-ms"]
        )
        isvalid, errorMessage = block.is_valid()
        self.assertFalse(isvalid, errorMessage)

    def test_invalid_memory_block_missing_onfly_function(self):

        block = MemoryBlock(
            name="TestBlock",
            variables=["var1", "var2"],
            data_types=["uint8", "boolean"],
            store_timing="ONFLY",
            reset_safe=True,
            onfly_functions=["func1"],
            reset_safe_schedules=["10ms", "20ms"]
        )
        isvalid, errorMessage = block.is_valid()
        self.assertFalse(isvalid)

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
        isvalid , errorMessage = block.is_valid()
        self.assertFalse(isvalid)

if __name__ == '__main__':
    unittest.main()
