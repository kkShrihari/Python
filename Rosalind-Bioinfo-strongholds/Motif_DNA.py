class Motif_DNA:
    """
    A class to find all positions of a given substring (motif)
    within a DNA sequence.
    """
    def __init__(self, string, substring):
        self.string = string
        self.substring = substring

    def Motif(self):
        """
        Returns all starting positions (1-based index)
        where the substring occurs in the string.
        """
        position = ""
        len_substring = len(self.substring)
        for i in range(len(self.string)):
            if self.substring == self.string[i:i+len_substring]:
                position = position + " " + str(i+1)
        print("\nThe position of motifs in sequence is:")
        return position
    
motif = Motif_DNA("GATATATGCATATACTT","ATAT")
print(motif.Motif())
