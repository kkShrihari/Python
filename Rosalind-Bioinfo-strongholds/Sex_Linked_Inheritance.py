class Sex_Linked_Inheritance:
    """
    A class to compute the probability of carrier females in X-linked
    recessive inheritance given male disease frequencies.
    """

    print("\n")
    '''
    q  = frequency of the male affected gene
    normal + normal  = (1 - q)*(1 - q)
    carrier (normal + affected gene) = 2q(1 - q)
    affected + affected = q*q
    '''

    def __init__(self, data_input):
        """
        Parameters:
        data_input (str): Space-separated male-affected frequencies (q values).
        """
        self.data = data_input

    def SLI(self):
        """
        Calculates the proportion of female carriers using:
        carrier = 2q(1 - q)

        Prints:
        List of carrier probabilities rounded to 2 decimals.
        """
        list1 = list(self.data.split())
        final_list = [2 * float(q) * (1 - float(q)) for q in list1]
        final_list = [round(q, 2) for q in final_list]
        print(final_list)


data_input = "0.1 0.5 0.8"
SLI1  = Sex_Linked_Inheritance(data_input)
SLI1.SLI()
