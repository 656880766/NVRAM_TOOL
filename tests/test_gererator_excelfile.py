import pandas as pd

def generate_test_data():
    data1 = {
        'BLOCK': ['','Block1', 'Block2', 'Block3','Block4'],
        'STORE TIMING': ['','ONFLY', 'POST_RUN_MODE','POWER_LATCH_MODE','POWER_LATCH_MODE'],
        'Variable Name': ['','var1', 'var2', 'var3', 'var4'],
        'DataType': ['','uint8', 'single', 'boolean','boolean'],
        'min': ['','0', '0', '0','0'],
        'max': ['','1', '1', '1','1'],
        'Dimension': ['','1*1', '1*1', '1*1', '1*1'],
        'MEM Initialization Value': ['','0', '0', '0','0'],
        'RESET SAFE MECANISM': ['','RESET_SAFE', 'NO_RESET_SAFE','RESET_SAFE','RESET_SAFE'],
        'RESISTANT TO SW CHANGE': ['','RESISTANT_TO_SW_CHANGE', 'RESISTANT_TO_SW_CHANGE', 'RESISTANT_TO_SW_CHANGE','RESISTANT_TO_SW_CHANGE'],
        'ONFLY C-Code Function': ['','function', 'function2', '',''],
        'RESETSAFE Scheduling Information': ['','10ms', '10ms', '10ms','10 miliseconds'],
        'FOTA Keep': ['','Yes', 'No', 'No','Yes'],
        'FOTA MEM Initialization value': ['','Not Applicable', 'Not Applicable', 'Not Applicable','Applicable']
    }

    data2 = {
        'BLOCK': ['','Block1', 'Block1', 'Block2','Block2'],
        'STORE TIMING': ['','ONFLY', 'ONFLY', 'POST_RUN_MODE','POWER_LATCH_MODE'],
        'Variable Name': ['','var1', 'var2', 'var3','var5'],
        'DataType': ['','uint8', 'single', 'boolean','boolean'],
        'min': ['','0', '0', '0','0'],
        'max': ['','1', '1', '1','1'],
        'Dimension': ['','1*1', '1*1', '1*1', '1*1'],
        'MEM Initialization Value': ['','0', '0', '0','0'],
        'RESET SAFE MECANISM': ['','RESET_SAFE', 'NO_RESET_SAFE','RESET_SAFE','RESET_SAFE'],
        'RESISTANT TO SW CHANGE': ['','RESISTANT_TO_SW_CHANGE', 'RESISTANT_TO_SW_CHANGE', 'RESISTANT_TO_SW_CHANGE','RESISTANT_TO_SW_CHANGE'],
        'ONFLY C-Code Function': ['','function', 'function2', '',''],
        'RESETSAFE Scheduling Information': ['','10ms', '10ms', '10ms','10ms'],
        'FOTA Keep': ['','Yes', 'No', 'No','Yes'],
        'FOTA MEM Initialization value': ['','Not Applicable', 'Not Applicable', 'Not Applicable','Not Applicable']
    }

    dataOnflyAndPowerLatchValid = {
        'BLOCK': ['','Block1', 'Block1', 'Block2', 'Block2'],
        'STORE TIMING': ['','ONFLY', 'ONFLY', 'POWER_LATCH_MODE', 'POWER_LATCH_MODE'],
        'Variable Name': ['','var1', 'var2', 'var3', 'var4'],
        'DataType': ['','uint8', 'single', 'boolean', 'boolean'],
        'min': ['','0', '0', '0', '0'],
        'max': ['','1', '1', '1', '1'],
        'Dimension': ['','1*1', '1*1', '1*1', '1*1'],
        'MEM Initialization Value': ['','0', '0', '0', '0'],
        'RESET SAFE MECANISM': ['','RESET_SAFE', 'NO_RESET_SAFE', 'RESET_SAFE', 'RESET_SAFE'],
        'RESISTANT TO SW CHANGE': ['','RESISTANT_TO_SW_CHANGE', 'RESISTANT_TO_SW_CHANGE', 'RESISTANT_TO_SW_CHANGE',
                                   'RESISTANT_TO_SW_CHANGE'],
        'ONFLY C-Code Function': ['','function', 'function2', '', ''],
        'RESETSAFE Scheduling Information': ['','10ms', '10ms', '10ms', '10ms'],
        'FOTA Keep': ['','Yes', 'No', 'No', 'Yes'],
        'FOTA MEM Initialization value': ['','Not Applicable', 'Not Applicable', 'Not Applicable', 'Applicable']
    }

    dataOnflyAndPowerLatchNotValid = {
        'BLOCK': ['','Block1', 'Block2', 'Block3', 'Block4'],
        'STORE TIMING': ['','ONFLY', 'ONFLY', 'POWER_LATCH_MODE', 'POWER_LATCH_MODE'],
        'Variable Name': ['','var1', '', 'var3', 'var4'],
        'DataType': ['','uint8', 'single', 'boolean', 'boolean'],
        'min': ['','0', '0', '0', '0'],
        'max': ['','1', '1', '1', '1'],
        'Dimension': ['','1*1', '1*1', '1*1', '1*1'],
        'MEM Initialization Value': ['','0', '0', '0', '0'],
        'RESET SAFE MECANISM': ['','RESET_SAFE', 'NO_RESET_SAFE', 'RESET_SAFE', 'RESET_SAFE'],
        'RESISTANT TO SW CHANGE': ['','RESISTANT_TO_SW_CHANGE', 'RESISTANT_TO_SW_CHANGE', 'RESISTANT_TO_SW_CHANGE',
                                   'RESISTANT_TO_SW_CHANGE'],
        'ONFLY C-Code Function': ['','function', '', '', ''],
        'RESETSAFE Scheduling Information': ['','10ms', '10ms', '10ms', '10 miliseconds'],
        'FOTA Keep': ['','Yes', 'No', 'No', 'Yes'],
        'FOTA MEM Initialization value': ['','Not Applicable', 'Not Applicable', 'Not Applicable', 'Applicable']
    }

    dataOnflyValid = {
        'BLOCK': ['', 'Block1', 'Block1'],
        'STORE TIMING': ['', 'ONFLY', 'ONFLY'],
        'Variable Name': ['', 'var1', 'var2'],
        'DataType': ['', 'uint8', 'single'],
        'min': ['', '0', '0'],
        'max': ['', '1', '1'],
        'Dimension': ['', '1*1', '1*1'],
        'MEM Initialization Value': ['', '0', '0', '0', '0'],
        'RESET SAFE MECANISM': ['', 'RESET_SAFE', 'NO_RESET_SAFE', 'RESET_SAFE', 'RESET_SAFE'],
        'RESISTANT TO SW CHANGE': ['', 'RESISTANT_TO_SW_CHANGE', 'RESISTANT_TO_SW_CHANGE', 'RESISTANT_TO_SW_CHANGE',
                                   'RESISTANT_TO_SW_CHANGE'],
        'ONFLY C-Code Function': ['', 'function', 'function2', '', ''],
        'RESETSAFE Scheduling Information': ['', '10ms', '10ms', '10ms', '10ms'],
        'FOTA Keep': ['', 'Yes', 'No', 'No', 'Yes'],
        'FOTA MEM Initialization value': ['', 'Not Applicable', 'Not Applicable', 'Not Applicable', 'Applicable']
    }

    dataOnflyNotValid = {
        'BLOCK': ['', 'Block1', 'Block1'],
        'STORE TIMING': ['', 'ONFLY', 'ONFLY'],
        'Variable Name': ['', '', 'var2'],
        'DataType': ['', 'uint8', 'single'],
        'min': ['', '0', '0'],
        'max': ['', '1', '1'],
        'Dimension': ['', '1*1', '1*1'],
        'MEM Initialization Value': ['', '0', '0', '0', '0'],
        'RESET SAFE MECANISM': ['', 'RESET_SAFE', 'NO_RESET_SAFE', 'RESET_SAFE', 'RESET_SAFE'],
        'RESISTANT TO SW CHANGE': ['', 'RESISTANT_TO_SW_CHANGE', 'RESISTANT_TO_SW_CHANGE', 'RESISTANT_TO_SW_CHANGE',
                                   'RESISTANT_TO_SW_CHANGE'],
        'ONFLY C-Code Function': ['', 'function', 'function2', '', ''],
        'RESETSAFE Scheduling Information': ['', '10ms', '10ms', '10ms', '10ms'],
        'FOTA Keep': ['', 'Yes', 'No', 'No', 'Yes'],
        'FOTA MEM Initialization value': ['', 'Not Applicable', 'Not Applicable', 'Not Applicable', 'Applicable']
    }



    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)
    dfValid = pd.DataFrame(dataOnflyAndPowerLatchValid)
    dfNotValid = pd.DataFrame(dataOnflyAndPowerLatchNotValid)
    df1.to_excel('data_test/TestData1.xlsx', index=False)
    df2.to_excel('data_test/TestData2.xlsx', index=False)
    dfValid.to_excel('data_test/TestValid.xlsx', index=False)
    dfNotValid.to_excel('data_test/TestNotValid.xlsx', index=False)

if __name__ == "__main__":
    generate_test_data()
