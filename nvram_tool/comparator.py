# nvram_tool/comparator.py
class SpecComparator:
    """
    Classe pour comparer les spécifications N et N+1.
    """

    def __init__(self, spec_n, spec_n_plus_1):
        """
        Initialise le comparateur avec les deux DataFrames des spécifications.

        :param spec_n: DataFrame des spécifications N
        :param spec_n_plus_1: DataFrame des spécifications N+1
        """
        self.spec_n = spec_n
        self.spec_n_plus_1 = spec_n_plus_1

    def compare_specs(self):
        """
        Compare les spécifications et retourne les différences.

        :return: Dictionnaire des différences par colonne
        """
        differences = {}
        for col in self.spec_n.columns:
            if col in self.spec_n_plus_1.columns:
                diff = self.spec_n[self.spec_n[col] != self.spec_n_plus_1[col]]
                if not diff.empty:
                    differences[col] = diff
        return differences
