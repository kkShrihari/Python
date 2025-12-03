import sys
from Bio.Align import AlignInfo
from Bio.Align import MultipleSeqAlignment
import logomaker
from Bio import AlignIO
import csv
import os
import pandas as pd

#TODO write your surname here to name file in compute_hydrophobicity function
STUDENT_SURNAME = None

script_dir = os.path.dirname(__file__)


def calculate_sequence_profiles(consensus_file):

    """
        Function to calculate sequence profiles

        Parameters
        ----------
        consensus_file : str
            path to consensus file (clustal omega fasta output)

        Return
        ----------
        pssm : pssm file
            # Hint check imports

    """

    pssm = None

    #TODO
    
    return pssm


def sequence_logo_creator(sequence_profile_csv):

    """
        Function to read sequence profile csv file, plot sequence logo and saves as png

        Parameters
        ----------
        sequence_profile_csv : str
            path to sequence profile csv

        Return
        ----------
        None

    """

    #Hint: You can use pandas dataframe

    logo = None

    #TODO read csv file and create sequence logo

    logo.fig.savefig(f"./{STUDENT_SURNAME}_sequence_logo.png")


def csv_writer(pssm, output_file):

    """
        Function to write probabilities to csv file

        Parameters
        ----------
        pssm : pssm file
            returned pssm from calculate_sequence_profiles

        output_file : str
            path for output file
            
        Return
        ----------
        None

    """


# Nothing to do here
if __name__ == "__main__":

    if STUDENT_SURNAME == None:
        print(f"Update your surname")
        sys.exit()
        
    seq_profiles = calculate_sequence_profiles(sys.argv[1])  
    csv_writer(seq_profiles, f"{script_dir}/{STUDENT_SURNAME}_sequence_profile.csv")
    sequence_logo_creator(f"{script_dir}/{STUDENT_SURNAME}_sequence_profile.csv")