class RNA_Splicing:
    """
    A class to perform RNA splicing: remove introns from a DNA sequence
    and translate the remaining exon sequence into a protein.
    """

    def __init__(self, sequence):
        """
        Initializes the object with a FASTA-formatted sequence.

        Parameters:
        sequence (str): Multi-line FASTA input containing one DNA string
                        followed by one or more introns.
        """
        self.sequence = sequence
    
    def Splicing(self):
        """
        Removes introns from the main DNA sequence, converts the resulting
        exon sequence into RNA, and translates it into a protein sequence
        using the provided codon table.
        """
        codon_table = {
    # Phenylalanine & Leucine
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    # Serine
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    # Tyrosine & Stop
    "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop",
    # Cysteine, Tryptophan, Stop
    "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W",

    # Leucine
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    # Proline
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    # Histidine, Glutamine
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    # Arginine
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",

    # Isoleucine & Methionine (Start)
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    # Threonine
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    # Asparagine, Lysine
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    # Serine, Arginine
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",

    # Valine
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    # Alanine
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    # Aspartic acid, Glutamic acid
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    # Glycine
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
    }
        filtered_list = []
        lines = list(self.sequence.strip().splitlines())
        for i in lines:
            if not i.startswith(">"):
                filtered_list.append(i)
        print(filtered_list)
    
        DNA = filtered_list[0]
        filtered_list.pop(0)
        filtered_list.sort(key=len, reverse=True)

        for i1 in range(len(filtered_list)):
            DNA = DNA.replace(filtered_list[i1],"")
        final_DNA = DNA
        print(final_DNA)

        for i in range(len(final_DNA)):
            if final_DNA[i] == "T":
                final_DNA = final_DNA.replace(final_DNA[i],"U")
        print(final_DNA)

        
        m,n = 0,3
        p_seq = ""
        for i in range(0,len(final_DNA),3):
            if codon_table[final_DNA[m:n]] != "Stop":
                p_seq = p_seq + codon_table[final_DNA[m:n]]
                m +=3
                n+=3
        print(p_seq)
     




fasta_input ="""
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT
"""
RS = RNA_Splicing(fasta_input)
RS.Splicing()
