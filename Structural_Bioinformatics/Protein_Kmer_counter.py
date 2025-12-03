import sys
import math


"""
Assignment 0 Template for Structural Bioinformatics Assignments

Created by Alper Yurtseven on 27 Sep 2024
"""

def protein_counter(fasta_file):

    """
        Function to count proteins in given fasta file

        Parameters
        ----------
        fasta_file : str
            path of fasta file

        Return
        ----------
        protein_count : int
            integer value of number of proteins in the file

    """
    protein_count = 0
    fasta_count = open(fasta_file)
    fasta_read = fasta_count.readlines()
    for line in fasta_read:
        if line[0] == ">":
            protein_count +=1
    return print(protein_count)
result = protein_counter(r"C:\Users\ASUS\Downloads\test_fasta1.fasta")


"""
    Hint : You can use following steps;

        1. Open fasta file
        2. Read line by line
        3. Set a counter to zero to store number of proteins
        4. Iterate over lines and increase counter when new protein begins
        5. Return number

"""

def kmer_counter(fasta_file, kmer_size=2):

    """
        Function to count kmers in given fasta file

        Parameters
        ----------
        fasta_file : str
            path of fasta file

        Return
        ----------
        sorted_kmer_counts : dictionary
            Descending order sorted dictionary of kmer counts
            key: str k-mer
            value: how many times it is observed

    """

    sorted_kmer_counts = {}
    list_kmer = []
    kmer_count = open(fasta_file)
    fasta_read = kmer_count.readlines()
    for x in fasta_read:
        print(x)
    return print(fasta_read[1])
result = kmer_counter(r"C:\Users\ASUS\Downloads\test_fasta1.fasta")


    #return sorted_kmer_counts


def print_function(fasta_files, output_file):

    with open(output_file, "w") as ofile:
        for fasta_file in fasta_files:
            ofile.write(fasta_file.strip().split("/")[-1] + "\n")
            ofile.write("Number of proteins: " + str(protein_counter(fasta_file)) + "\n")
            ofile.write("Kmer counts: " + str(kmer_counter(fasta_file)) + "\n\n")


def main(fasta_file1, fasta_file2, fasta_file3, output_file):

    """
        Function to get fasta file paths and output path as arguments and prints

        Parameters
        ----------
        fasta_file1 : str
            path of first fasta file
        
        fasta_file2 : str
            path of second fasta file
        
        fasta_file3 : str
            path of third fasta file

        output_file : str
            path of output file

        Return
        ----------
        None

    """

    fasta_files = [fasta_file1, fasta_file2, fasta_file3]

    print_function(fasta_files, output_file)

    if __name__ == "__main__":
      main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
