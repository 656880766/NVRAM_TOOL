import pandas as pd

def generate_test_data():
    data1 = {
        'BLOCK': ['Block1', 'Block2'],
        'STORE TIMING': ['ONFLY', 'POST_RUN_MODE','POWER_LATCH_MODE'],
        'Variable Name': ['var1', 'var2', 'Crc8_u8_var3'],
        'DataType': ['uint8', 'single', 'boolean'],
        'RESET SAFE MECANISM': ['RESET_SAFE', 'NO_RESET_SAFE','RESET_SAFE'],
        'ONFLY C-Code Function': ['function', '', ''],
        'RESETSAFE Scheduling Information': ['10ms', 'dix milliseconde', '10ms']
    }

    data2 = {
        'BLOCK': ['Block1', 'Block2'],
        'STORE TIMING': ['ONFLY', 'ONFLY', 'POST_RUN_MODE'],
        'Variable Name': ['var1', 'var2', 'var3'],
        'DataType': ['uint8', 'single', 'boolean'],
        'RESET SAFE MECANISM': ['RESET_SAFE', 'NO_RESET_SAFE', 'NO_RESET_SAFE'],
        'ONFLY C-Code Function': ['function', 'function2', ''],
        'RESETSAFE Scheduling Information': ['10ms', 'dix milliseconde', '10ms']
    }


    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)
    df1.to_excel('../data_test/Test_Spec_NVRAM_1.0.xlsx', index=False)
    df2.to_excel('../data_test/Test_Spec_NVRAM_2.0.xlsx', index=False)

if __name__ == "__main__":
    generate_test_data()
