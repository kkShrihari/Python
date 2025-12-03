class Distance_Matrix:
    """
    A class to compute the pairwise p-distance matrix for a set of DNA sequences
    provided in FASTA format.
    """
    print("\n")

    def __init__(self, input):
        """
        Parameters:
        input (str): FASTA-formatted multi-sequence input.
        """
        self.input  = input
    
    def Distance_phylogeny(self):
        """
        Computes the p-distance (proportion of differing nucleotides)
        between each pair of sequences and outputs a formatted distance matrix.

        Returns:
        str: A matrix of p-distances with 5 decimal precision.
        """
        str_list = self.input.strip().splitlines()

        final_list = []
        for line in str_list:
            if not line.startswith(">"): 
                final_list.append(line)
       
        match, matrix = 0, ""
        for i in range(len(final_list)):
            for i1 in range(len(final_list)):
                match = 0
                for i2 in range(len(final_list[i])):
                    if final_list[i][i2] != final_list[i1][i2]:
                        match += 1
                total = match / len(final_list[0])
                matrix += str(total) + " "
            matrix += "\n"

        matrix = matrix.split(" ")
        for i in range(len(matrix)):
            matrix[i] = matrix[i].replace("\n", "")

        matrix.pop(-1)

        final = ""
        for i in range(len(matrix)):
            final += f"{float(matrix[i]):.5f} "
            if ((i+1) % 4 == 0):
                final += "\n"
        r
