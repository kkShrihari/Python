class Expected_Offspring:
    """
    A class to calculate the expected number of dominant phenotype offspring
    given counts of couples with specific genotype pairings.
    """
    def __init__(self, input_, children):
        """
        Parameters:
        input_ (str): Six integers representing the number of couples with genotypes:
                      AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa.
        children (int): Expected number of offspring per couple.
        """
        self.c = children
        self.input_ = input_

    def Exp_off(self):
        """
        Computes the expected number of offspring showing the dominant phenotype
        by multiplying each couple type by its probability of producing a dominant child.
        
        Returns:
        float: Expected number of dominant phenotype offspring.
        """
        sum = 0
        input_list = list(map(int, self.input_.strip().split()))
        AA_AA = 1 * input_list[0] * self.c
        AA_Aa = 1 * input_list[1] * self.c
        AA_aa = 1 * input_list[2] * self.c
        Aa_Aa = 0.75 * input_list[3] * self.c
        Aa_aa = 0.5 * input_list[4] * self.c
        aa_aa = 0 * input_list[5] * self.c
        sum = AA_AA + AA_Aa + AA_aa + Aa_Aa + Aa_aa + aa_aa
        return sum


EO1 = Expected_Offspring("1 0 0 1 0 1", 2)
print(EO1.Exp_off())
