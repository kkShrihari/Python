class Phylogenetic_Ancestors_count:
    """
    A class to compute the minimum number of internal nodes (ancestors)
    in a rooted binary phylogenetic tree given the number of leaves.
    """

    def __init__(self, input):
        """
        Parameters:
        input (int): Number of leaves in the phylogenetic tree.
        """
        self.n = input

    def Pac(self):
        """
        Returns the number of internal nodes in a rooted binary tree.

        Formula:
        Internal nodes = n - 2

        Returns:
        int: Number of ancestors.
        """
        if (self.n <= 3) or (self.n >= 100):
            raise ValueError("Enter no between 3 to 100")
        return self.n - 2


PAC = Phylogenetic_Ancestors_count(4)
print(PAC.Pac())
