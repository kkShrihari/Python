from modeller import *
from modeller.automodel import *
import sys
import os

script_dir = os.path.dirname(__file__)

#-- Prepare the input files

#-- Make sure paths are relative to the script, not absolute paths on your system

def main(template_pdb_path, target_sequence_fasta_path, output_ali_file_path, output_pap_file_path):

    env = Environ()
    aln = Alignment(env)
    mdl = Model(env, file=f'{template_pdb_path}', model_segment=('FIRST:A','LAST:A'))
    aln.append_model(mdl, align_codes='template', atom_files=f'{template_pdb_path}')
    aln.append(file=f'{target_sequence_fasta_path}', align_codes='target_sequence')
    aln.align2d(max_gap_length=50)
    aln.write(file=f'{output_ali_file_path}', alignment_format='PIR')
    aln.write(file=f'{output_pap_file_path}', alignment_format='PAP')

    a = AutoModel(env, alnfile=f'{output_ali_file_path}',
                knowns='template', sequence='target_sequence',
                assess_methods=(assess.DOPE,
                                assess.GA341))
    a.starting_model = 1
    a.ending_model = 5
    a.make()

if __name__ == "__main__":

    template_pdb_path = None

    target_sequence_fasta_path = None # HINT: check Modeller tutorial TvLDH.ali

    output_ali_file_path = None

    output_pap_file_path = None

    ### ALL PATHS SHOULD BE SAME FOLDER AS SCRIPT!!!

    if template_pdb_path == None:
        print(f"Update the template_pdb_path")
        sys.exit()
    
    if target_sequence_fasta_path == None:
        print(f"Update the target_sequence_fasta_path")
        sys.exit()
    
    if output_ali_file_path == None:
        print(f"Update the output_ali_file_path")
        sys.exit()

    if output_pap_file_path == None:
        print(f"Update the output_pap_file_path")
        sys.exit()

    main(template_pdb_path, target_sequence_fasta_path, output_ali_file_path, output_pap_file_path)