class NaivePatternSearch:
    """
    Computes the expected number of character comparisons
    for the Naive Pattern Search algorithm.

    Assumes:
    - Independent characters
    - Same probability distribution for pattern and text
    """

    def __init__(self, prob_list: list):
        """
        Initialize nucleotide probabilities.

        Parameters:
        prob_list (list): Probabilities for [A, C, G, T]
        """
        self.nuc_list = ['A', 'C', 'G', 'T']
        self.prob_dict = dict(zip(self.nuc_list, prob_list))

        # Probability that two random characters match
        self.q = sum(p ** 2 for p in prob_list)

    def expected_comparisons(self, m: int) -> float:
        """
        Expected number of comparisons for a pattern of length m.

        Parameters:
        m (int): Pattern length

        Returns:
        float: Expected number of comparisons
        """
        expected = 1 + sum(self.q ** i for i in range(1, m))
        return round(expected, 6)

    def expected_comparisons_infinite(self) -> float:
        """
        Expected number of comparisons as pattern length → ∞.

        Returns:
        float: Expected number of comparisons
        """
        expected_inf = 1 / (1 - self.q)
        return round(expected_inf, 6)
