class Nucleotides:
    def __init__(self, input_string):
        self.input_string = input_string  

    def DNA_nucleotides(self):
        """
        Counts the number of Adenine (A), Thymine (T), 
        Guanine (G), and Cytosine (C) present in the input string.
        """
        a, t, g, c = 0, 0, 0, 0

        for i in range(len(self.input_string)):
            if self.input_string[i] == "A":
                a += 1
            elif self.input_string[i] == "T":
                t += 1
            elif self.input_string[i] == "G":
                g += 1
            elif self.input_string[i] == "C":
                c += 1
            elif self.input_string[i] not in ["A", "T", "G", "C"]: 
                print("Unexpected character:", self.input_string[i])
        return f"{a} {c} {g} {t}"

    def DNA2RNA(self):
        """
        Transcribes the DNA input sequence into RNA by replacing
        all thymine (T) nucleotides with uracil (U).
        """
        DNA_list = list(self.input_string)
        for i in range(len(self.input_string)):
            if DNA_list[i] == "T":
                DNA_list[i] = "U"
            elif DNA_list[i] == " ":
                DNA_list[i] = ""
        DNA_string = "".join(DNA_list)
        return DNA_string

    def Rev_complement(self):
        """
        Returns the reverse complement of the DNA input sequence by replacing
        each nucleotide with its complementary base (A↔T, G↔C) and reversing the string.
        """
        DNA_list = list(self.input_string)
        for i in range(len(self.input_string)):
            if DNA_list[i] == "A":
                DNA_list[i] = "T"
            elif DNA_list[i] == "G":
                DNA_list[i] = "C"
            elif DNA_list[i] == "T":
                DNA_list[i] = "A"
            elif DNA_list[i] == "C":
                DNA_list[i] = "G"
        DNA_string = "".join(DNA_list)
        rev_comp = DNA_string[::-1]  
        return rev_comp
    
    def GC_content(self):
        """
        Computes the GC content (%) of the input sequence using:
        GC% = (G_count + C_count) * 100 / total_length
        """
        g, c = 0, 0
        for i in range(len(self.input_string)):
            if self.input_string[i] == "G":
                g += 1
            if self.input_string[i] == "C":
                c += 1

        seq_length = len(self.input_string)
        GC_percent = (g + c) * 100 / seq_length
        return round(GC_percent, 3)
    
    def RNA2Protein(self):
        """
        Translates an RNA sequence into a protein sequence using the RNA codon table.
        Translation stops when a STOP codon is encountered.
        """
        RNA_codon_table = {
            "UUU":"F","UUC":"F","UUA":"L","UUG":"L","CUU":"L","CUC":"L","CUA":"L","CUG":"L",
            "AUU":"I","AUC":"I","AUA":"I","AUG":"M",
            "GUU":"V","GUC":"V","GUA":"V","GUG":"V",
            "UCU":"S","UCC":"S","UCA":"S","UCG":"S","AGU":"S","AGC":"S",
            "CCU":"P","CCC":"P","CCA":"P","CCG":"P",
            "ACU":"T","ACC":"T","ACA":"T","ACG":"T",
            "GCU":"A","GCC":"A","GCA":"A","GCG":"A",
            "UAU":"Y","UAC":"Y","CAU":"H","CAC":"H","CAA":"Q","CAG":"Q",
            "AAU":"N","AAC":"N","AAA":"K","AAG":"K",
            "GAU":"D","GAC":"D","GAA":"E","GAG":"E",
            "UGU":"C","UGC":"C","UGG":"W",
            "CGU":"R","CGC":"R","CGA":"R","CGG":"R","AGA":"R","AGG":"R",
            "GGU":"G","GGC":"G","GGA":"G","GGG":"G",
            "UAA":"Stop","UAG":"Stop","UGA":"Stop"
        }
        
        protein = ""    
        for i in range(0, len(self.input_string), 3):
            codon = self.input_string[i:i+3]
            if len(codon) < 3:
                break
            if RNA_codon_table[codon] == "Stop":
                break
            protein += RNA_codon_table[codon]

        return protein

