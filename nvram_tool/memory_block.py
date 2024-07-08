import re

class MemoryBlock:
    """
    Classe représentant un bloc mémoire.
    """

    def __init__(self, name, variables, data_types, store_timing, reset_safe, onfly_functions=None,
                 reset_safe_schedules=None):
        """
        Initialise un bloc mémoire.

        :param name: Nom du bloc
        :param variables: Liste des variables
        :param data_types: Liste des types de données des variables
        :param store_timing: Méthode d'écriture des variables
        :param reset_safe: Indique si le bloc est RESET_SAFE
        :param onfly_functions: Liste des fonctions C-Code pour ONFLY
        :param reset_safe_schedules: Liste des informations de planification pour RESET_SAFE
        """
        self.name = name
        self.variables = variables
        self.data_types = data_types
        self.store_timing = store_timing
        self.reset_safe = reset_safe
        self.onfly_functions = onfly_functions or []
        self.reset_safe_schedules = reset_safe_schedules or []

    def __repr__(self):
        return (f"MemoryBlock(name={self.name}, variables={self.variables}, data_types={self.data_types}, "
                f"store_timing={self.store_timing}, reset_safe={self.reset_safe}, "
                f"onfly_functions={self.onfly_functions}, reset_safe_schedules={self.reset_safe_schedules})")

    def is_valid(self):
        """
        Vérifie la validité du bloc mémoire selon les critères spécifiés.

        :return: True si le bloc est valide, False sinon
        """
        # Calculer la taille totale des variables
        total_size = sum([self.get_size(dtype) for dtype in self.data_types])
        if total_size > 600:
            return False

        # Vérifier le nombre de variables
        if len(set(self.variables)) < 2:
            return False
        print(len(self.variables) != len(set(self.onfly_functions)))
        # Vérifier les spécificités des blocs ONFLY
        if self.store_timing == 'ONFLY':
            if len(self.variables) != len(self.onfly_functions):
                return False
            # Vérifier les spécificités des blocs RESET_SAFE (y compris POST_RUN)
            elif len(self.variables) != len(self.reset_safe_schedules) and not all(self.is_valid_schedule(schedule) for schedule in self.reset_safe_schedules):
                return False


        # Vérifier les spécificités des blocs POWER_LATCH_MODE
        if self.store_timing == 'POWER_LATCH_MODE' or self.store_timing == 'POST_RUN_MODE':
            if self.reset_safe:
                if len(self.variables) != len(self.reset_safe_schedules) and not all(self.is_valid_schedule(schedule) for schedule in self.reset_safe_schedules):
                    return False



        return True

    @staticmethod
    def get_size(data_type):
        """
        Retourne la taille en octets d'un type de donnée.

        :param data_type: Type de donnée
        :return: Taille en octets du type de donnée
        """
        sizes = {'uint8': 1, 'bool': 1, 'single': 4}
        return sizes.get(data_type, 0)

    @staticmethod
    def is_valid_schedule(schedule):
        """
        Vérifie si le format de la périodicité est valide.

        :param schedule: Périodicité à vérifier
        :return: True si le format est valide, False sinon
        """
        return bool(re.match(r'^\d+ms$', schedule))

    def to_c_struct(self):
        """
        Génère la représentation C du bloc mémoire.

        :return: Représentation C du bloc mémoire
        """
        struct = f"// Block: {self.name}\nstruct {self.name} {{\n"
        if self.store_timing == "POWER_LATCH_MODE":
            struct += "    uint8_t Crc8_u8;\n"
        for var, dtype in zip(self.variables, self.data_types):
            struct += f"    {dtype} {var};\n"
        struct += "};\n\n"
        return struct
