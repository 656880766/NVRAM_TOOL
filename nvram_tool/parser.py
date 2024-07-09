# nvram_tool/parser.py
import pandas as pd
from collections import defaultdict
from .memory_block import MemoryBlock

class ExcelParser:
    REQUIRED_COLUMNS = [
        'BLOCK', 'STORE TIMING', 'Variable Name', 'DataType', 'min', 'max', 'Dimension', 'MEM Initialization Value',
        'RESET SAFE MECANISM', 'RESISTANT TO SW CHANGE', 'ONFLY C-Code Function',
        'RESETSAFE Scheduling Information', 'FOTA Keep', 'FOTA MEM Initialization value'
    ]

    @staticmethod
    def parse_excel(file_path):
        # Lire le fichier Excel en ignorant la deuxième ligne (types de données)
        df = pd.read_excel(file_path, skiprows=[1])

        # Vérification des colonnes requises
        for column in ExcelParser.REQUIRED_COLUMNS:
            if column not in df.columns:
                raise ValueError(f"Colonne manquante dans le fichier Excel : {column}")

        blocks_dict = defaultdict(lambda: {
            "variables": [], "data_types": [], "store_timing": None, "reset_safe": None,
            "onfly_functions": [], "reset_safe_schedules": []
        })

        for _, row in df.iterrows():
            block_name = row['BLOCK']
           # variable_name = row['Variable Name']
            blocks_dict[block_name]["variables"].append(row['Variable Name'])
            blocks_dict[block_name]["data_types"].append(row['DataType'])
            if blocks_dict[block_name]["store_timing"] is None:
                blocks_dict[block_name]["store_timing"] = row['STORE TIMING']
            if blocks_dict[block_name]["reset_safe"] is None:
                blocks_dict[block_name]["reset_safe"] = row['RESET SAFE MECANISM'] == 'RESET_SAFE'
            if pd.notna(row.get('ONFLY C-Code Function')):
                blocks_dict[block_name]["onfly_functions"].append(row['ONFLY C-Code Function'])
            else: []
            if pd.notna(row.get('RESETSAFE Scheduling Information')):
                blocks_dict[block_name]["reset_safe_schedules"].append(row['RESETSAFE Scheduling Information'])
            else: []

        blocks = []
        for block_name, block_data in blocks_dict.items():
            block = MemoryBlock(
                name=block_name,
                variables=block_data['variables'],
                data_types=block_data['data_types'],
                store_timing=block_data['store_timing'],
                reset_safe=block_data['reset_safe'] == 'RESET_SAFE',
                onfly_functions=block_data.get('onfly_functions', []),
                reset_safe_schedules=block_data.get('reset_safe_schedules', [])
            )
            blocks.append(block)

        # Trier les blocs par leur nom
        blocks = sorted(blocks, key=lambda x: x.name)
        return blocks
