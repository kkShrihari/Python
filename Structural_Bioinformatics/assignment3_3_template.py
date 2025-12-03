import sys
from Bio.Align import AlignInfo
from Bio.Align import MultipleSeqAlignment
from Bio import AlignIO

def calculate_consensus_sequence(clustal_omega_file):

    """
        Function to calculate consensus sequence

        Parameters
        ----------
        clustal_omega_file : str
            path to clustal omega output file

        Return
        ----------
        None

    """

    consensus = None

    MSA_aligned = AlignIO.read(clustal_omega_file, fasta)


    print(consensus)


if __name__ == "__main__":
    calculate_consensus_sequence(sys.argv[1])

