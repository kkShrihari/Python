class Mendel_inheritance:
    """
    Calculates the probability of producing an offspring with a dominant phenotype
    given counts of homozygous dominant (AA), heterozygous (Aa), and homozygous recessive (aa) individuals.
    """
    def __init__(self, AA, Aa, aa):
        self.AA = AA
        self.Aa = Aa
        self.aa = aa

    def MI_prob(self):
        """
        Computes the probability of an offspring having a dominant allele
        using Mendelian genetics and random mating probabilities.
        """
        population = self.AA + self.Aa + self.aa
        Aa_Aa, Aa_aa, aa_aa = 0.25, 0.50, 1    # Recessive probability
        Aa_Aa_prop = (self.Aa/population)*((self.Aa-1)/(population-1))*Aa_Aa
        Aa_aa_prop = (self.Aa/population)*((self.aa)/(population-1))*Aa_aa
        aa_Aa_prop = (self.aa/population) * (self.Aa/(population-1)) * Aa_aa
        aa_aa_prop = (self.aa/population)*((self.aa-1)/(population-1))*aa_aa
        recessive_sum = Aa_Aa_prop + Aa_aa_prop + aa_Aa_prop + aa_aa_prop
        Dominant_prop = 1 - recessive_sum
        print("\nThe Dominant probability is:")
        return Dominant_prop
    
MI = Mendel_inheritance(2,2,2)
print(MI.MI_prob())
