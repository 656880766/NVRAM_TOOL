import pandas as pd
from nvram_tool.parser import ExcelParser
from nvram_tool.comparator import SpecComparator
from nvram_tool.generator import ConfGenerator


def main():
    spec_n_df = pd.read_excel('../data/Spec_NVRAM_1.0.xlsx', skiprows=[1])
    spec_n1_df = pd.read_excel('../data/Spec_NVRAM_2.0.xlsx', skiprows=[1])

    spec_comparator = SpecComparator(spec_n_df, spec_n1_df)
    differences = spec_comparator.compare_specs()

    with open('../output/diff_log.txt', 'w') as log_file:
        for col, diff in differences.items():
            log_file.write(f"Differences in column {col}:\n")
            log_file.write(diff.to_string())
            log_file.write("\n\n")

 #   blocks_n1 = ExcelParser.parse_excel('../data/Spec_NVRAM_2.0.xlsx')
        blocks_n1 = ExcelParser.parse_excel('../tests/data_test/TestValid.xlsx')
        #blocks_n1 = ExcelParser.parse_excel('../data/Spec_NVRAM_2.0.xlsx')

    # Ecrire dans le fichier de journalisation les blocs memoires et leurs status
    with open('../output/statusBlockLogs.txt', 'w') as log_file:
         log_file.write((str(blocks_n1)))

    print(blocks_n1)  # Print blocks to debug
    ConfGenerator.generate_conf_h(blocks_n1, '../output/conf.h')


if __name__ == "__main__":
    main()
