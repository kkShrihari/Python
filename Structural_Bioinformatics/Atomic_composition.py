import sys
import math


"""
PDB Parser Script Template for Structural Bioinformatics Assignments

Created by Alper Yurtseven on 12 May 2023
"""

Kyte_Doolittle_scale = { 'ALA': 1.8,'ARG':-4.5,'ASN':-3.5,'ASP':-3.5,'CYS': 2.5,
       'GLN':-3.5,'GLU':-3.5,'GLY':-0.4,'HIS':-3.2,'ILE': 4.5,
       'LEU': 3.8,'LYS':-3.9,'MET': 1.9,'PHE': 2.8,'PRO':-1.6,
       'SER':-0.8,'THR':-0.7,'TRP':-0.9,'TYR':-1.3,'VAL': 4.2 }

set_path = (r"C:\Users\ASUS\Downloads\Protein_1fcn.pdb")

def pdb_file_reader(pdb_file):
    atom_lines = []
    protein_pdb = open(pdb_file)
    Protein_read = protein_pdb.readlines()
    for lines in Protein_read:
        if lines.startswith("ATOM"):
           line = lines.replace("\n","").rstrip()
           atom_lines.append(line)
    return atom_lines

pdb_list = pdb_file_reader(set_path)
print(pdb_list)

def amino_acid_composition_calculator(atom_lines):
    amino_acid_composition = {}
    aminoacid_list1 = []
    aminoacid_list2 = []
    counts_list = []
    for line in atom_lines:
        if line.startswith("ATOM"):
          lines = line.split()
          for val in lines:
             if val == "CA":
                trim = str(line[17:20])
                aminoacid_list1.append(trim)
    for codons in aminoacid_list1:
        if codons not in aminoacid_list2:
            count = aminoacid_list1.count(codons)
            counts_list.append(count)
            aminoacid_list2.append(codons)
        else:
            continue
    
    zipping = zip(aminoacid_list2,counts_list)
    amino_acid_composition = dict(list(zipping))
    return amino_acid_composition

amino_acid_composition0 = amino_acid_composition_calculator(pdb_list)
print(amino_acid_composition0)


def amino_acid_composition_percentage_calculator(atom_lines):
    aminoacid_list1 = []
    aminoacid_list2 = []
    counts_list = []
    for datas in atom_lines:
      if datas.startswith("ATOM"):
        datas1 = datas.split()
        for val in datas1:
          if val == "CA":
            trim = str(datas[17:20])
            aminoacid_list1.append(trim)
            aminoacid_list1.sort()
    for codons in aminoacid_list1:
        if codons not in aminoacid_list2:
            count = aminoacid_list1.count(codons)
            counts_list.append(count)
            aminoacid_list2.append(codons)
        else:
            continue
        
    total =0
    final_list = []
    for number in counts_list:
        total += number 
    for value in counts_list:
        final_value0 = (value/total)*100
        final_value1 = round(final_value0, 2)
        final_list.append(final_value1)

    zipping2 = zip(aminoacid_list2,final_list)
    amino_acid_composition_percentage = dict(list(zipping2))
        
    
    return amino_acid_composition_percentage

amino_acid_composition_percentage0 = amino_acid_composition_percentage_calculator(pdb_list)
print(amino_acid_composition_percentage0)


def atomic_composition_calculator(atom_lines):

    atomic_composition = {}
    atom_lines_1 = atom_lines.copy()
    aminoacid_list1 = []
    aminoacid_list2 = []
    counts_list = []
    for datas in atom_lines_1:
        trim = str(datas[77])
        aminoacid_list1.append(trim)
    for codons in aminoacid_list1:
        if codons not in aminoacid_list2:
            count = aminoacid_list1.count(codons)
            counts_list.append(count)
            aminoacid_list2.append(codons)
        else:
            continue
    zipping2 = zip(aminoacid_list2,counts_list)
    atomic_composition = dict(list(zipping2))
    
    return atomic_composition

atomic_composition_calculator0 = atomic_composition_calculator(pdb_list)
print(atomic_composition_calculator0)


def atomic_composition_percentage_calculator(atom_lines):

    atomic_composition_percentage = {}
    aminoacid_list1 = []
    aminoacid_list2 = []
    counts_list = []
    for datas in atom_lines:
        trim = str(datas[77])
        aminoacid_list1.append(trim)
    for codons in aminoacid_list1:
        if codons not in aminoacid_list2:
            count = aminoacid_list1.count(codons)
            counts_list.append(count)
            aminoacid_list2.append(codons)
        else:
            continue
        
    total =0
    final_list = []
    for number in counts_list:
        total += number 
    for value in counts_list:
        final_value = (value/total)*100
        final_value1 = round(final_value,2)
        final_list.append(final_value1)

    zipping2 = zip(aminoacid_list2,final_list)
    atomic_composition_percentage = dict(list(zipping2))
        
    
    return atomic_composition_percentage

atomic_composition_percentage_calculator0 = atomic_composition_percentage_calculator(pdb_list)
print(atomic_composition_percentage_calculator0)

def amino_acid_hydrophobicity_composition_calculator(amino_acid_composition, Kyte_Doolittle_scale):
    amino_acid_hydrophobicity_composition = {"Hydrophobic" : 0, "Hydrophilic" : 0}
    Hydrophobic = 0
    Hydrophilic = 0
    for codons in amino_acid_composition:
        value = amino_acid_composition.get(codons)
        if codons in Kyte_Doolittle_scale:
            values = Kyte_Doolittle_scale.get(codons)
            if values > 0:
                Hydrophobic += value 
            else:
                Hydrophilic += value
    amino_acid_hydrophobicity_composition.update({"Hydrophobic": Hydrophobic})
    amino_acid_hydrophobicity_composition.update({"Hydrophilic": Hydrophilic})
    
    return amino_acid_hydrophobicity_composition

amino_acid_hydrophobicity_composition0 = amino_acid_hydrophobicity_composition_calculator(amino_acid_composition0, Kyte_Doolittle_scale)
print(amino_acid_hydrophobicity_composition0)

def amino_acid_hydrophobicity_composition_percentage_calculator(amino_acid_composition, Kyte_Doolittle_scale):

    amino_acid_hydrophobicity_composition_percentage = {"Hydrophobic" : 0, "Hydrophilic" : 0}
    Hydrophobic = 0
    Hydrophilic = 0
    for codons in amino_acid_composition:
        value = amino_acid_composition.get(codons)
        if codons in Kyte_Doolittle_scale:
            values = Kyte_Doolittle_scale.get(codons)
            if values > 0:
                Hydrophobic += value 
            else:
                Hydrophilic += value 
    total_counts = Hydrophilic + Hydrophobic
    Hydrophobic_percentage = (Hydrophobic/total_counts)*100
    Hydrophobic_percentage1 = round(Hydrophobic_percentage,2)
    Hydrophilic_percentage = (Hydrophilic/total_counts)*100
    Hydrophilic_percentage1 = round(Hydrophilic_percentage,2)
    amino_acid_hydrophobicity_composition_percentage.update({"Hydrophobic": Hydrophobic_percentage1})
    amino_acid_hydrophobicity_composition_percentage.update({"Hydrophilic": Hydrophilic_percentage1})

    return amino_acid_hydrophobicity_composition_percentage

amino_acid_hydrophobicity_composition_percentage0 = amino_acid_hydrophobicity_composition_percentage_calculator(amino_acid_composition0, Kyte_Doolittle_scale)
print(amino_acid_hydrophobicity_composition_percentage0)

def amino_acid_charge_composition_calculator(amino_acid_composition):

    amino_acid_charge_composition = {"Positive": 0, "Negative": 0}
    Positive_list = ['ARG','LYS',"HIS"]
    Negative_list = ['ASP','GLU']
    Positive = 0
    Negative = 0
    for codons in amino_acid_composition:
        value = amino_acid_composition.get(codons)
        if codons in Positive_list:
            Positive += value 
        elif codons in Negative_list:
            Negative += value 
        else:
            continue

    amino_acid_charge_composition.update({"Positive": Positive})
    amino_acid_charge_composition.update({"Negative": Negative})
    
    return amino_acid_charge_composition

amino_acid_charge_composition_calculator0 = amino_acid_charge_composition_calculator(amino_acid_composition0)
print(amino_acid_charge_composition_calculator0)


def hetero_atom_pdb_reader(pdb_file):
    
    heteroatom_lines = []
    protein_pdb = open(pdb_file)
    protein_read = protein_pdb.readlines()
    for lines in protein_read:
        if lines.startswith("HETATM"):
            line = lines.replace("\n","")
            heteroatom_lines.append(line)

    return heteroatom_lines

hetero_atom_pdb_reader0 = hetero_atom_pdb_reader(set_path)
print(hetero_atom_pdb_reader0)

def hetero_atom_residue_counter(heteroatom_lines):

    hetero_atom_composition = {}
    aminoacid_list1 = []
    aminoacid_list2 = []
    counts_list = []
    for datas in heteroatom_lines:
        trim = str(datas[17:20])
        aminoacid_list1.append(trim)
        #if trim == "HOH":     
    for codons in aminoacid_list1:
        if codons not in aminoacid_list2:
            count = aminoacid_list1.count(codons)
            counts_list.append(count)
            aminoacid_list2.append(codons)
        else:
            continue
    
    zipping = zip(aminoacid_list2,counts_list)
    hetero_atom_composition = dict(list(zipping))
    return hetero_atom_composition
hetero_atom_residue_counter0 = hetero_atom_residue_counter(hetero_atom_pdb_reader0)
print(hetero_atom_residue_counter0)


def most_distant_residue_finder(atom_lines):
    final_list1 = []
    final_list2 = []
    for lines_0 in atom_lines:
        final_list1 = lines_0.rsplit()
        if final_list1[2] == 'CA':
          final_list2.append(final_list1)

        def distance_calculator(x1,y1,z1,x2,y2,z2):
            distance0 = ((float(x2)-float(x1))*(float(x2)-float(x1))) + ((float(y2)-float(y1))*(float(y2)-float(y1))) + ((float(z2)-float(z1))*(float(z2)-float(z1)))
            distance1 = math.sqrt(distance0)
            distance = math.floor(distance1)
            return distance
    
    nested_list = []
    for x in final_list2:
      for y in final_list2:
        max_distance = []
        residue_1 = int(x[5])
        residue_2 = int(y[5])
        max_distance.append(distance_calculator(x[6],x[7],x[8],y[6],y[7],y[8]))
        max_distance.append(residue_2)
        max_distance.append(residue_1)
        nested_list.append(max_distance)

    nested_list.sort()
    for x in nested_list:
      if x[0] == nested_list[-1][0]:
        resid_01 = str(x[2])
        resid_02 = str(x[1])
        distance = int(x[0])
        most_distant_residue = ((resid_01,resid_02),distance)
    return most_distant_residue

most_distant_residue_finder0 = most_distant_residue_finder(pdb_list)
print(most_distant_residue_finder0)


def radius_of_gyration_calculator(atom_lines):
    
    radius_of_gyration = 0.0

    #TODO : Calculate the radius of gyration of protein

    return radius_of_gyration


def print_function(pdb_file):

    atom_lines = pdb_file_reader(pdb_file)
    
    amino_acid_composition = amino_acid_composition_calculator(atom_lines)
    amino_acid_composition_percentage = amino_acid_composition_percentage_calculator(atom_lines)

    amino_acid_hydrophobicity_composition = amino_acid_hydrophobicity_composition_calculator(amino_acid_composition, Kyte_Doolittle_scale)
    amino_acid_hydrophobicity_composition_percentage = amino_acid_hydrophobicity_composition_percentage_calculator(amino_acid_composition, Kyte_Doolittle_scale)

    atomic_composition = atomic_composition_calculator(atom_lines)
    atomic_composition_percentage = atomic_composition_percentage_calculator(atom_lines)

    amino_acid_charge_compostion = amino_acid_charge_composition_calculator(amino_acid_composition)

    hetero_atom_composition = hetero_atom_residue_counter(hetero_atom_pdb_reader(pdb_file))

    most_distant_residues = most_distant_residue_finder(atom_lines)

    radius_of_gyration = radius_of_gyration_calculator(atom_lines)

    print(f"Amino acid composition:")
    for amino_acid in amino_acid_composition.keys():
        print(f"{str(amino_acid)} {str(amino_acid_composition[amino_acid])} {amino_acid_composition_percentage[amino_acid]:.2f}%")
    
    print(f"\nAmino acids composition categorized on the basis of hydrophobicity:")
    for hydrophobicity in amino_acid_hydrophobicity_composition.keys():
        print(f"{str(hydrophobicity)} {str(amino_acid_hydrophobicity_composition[hydrophobicity])} {amino_acid_hydrophobicity_composition_percentage[hydrophobicity]:.2f}%")
    
    print(f"\nAtomic composition:")
    for atom in atomic_composition.keys():
        print(f"{atom} {atomic_composition[atom]} {atomic_composition_percentage[atom]:.2f}%")

    print("\nCharge composition of protein:")
    print(f"Positively Charged Residues: {str(amino_acid_charge_compostion['Positive'])}")
    print(f"Negatively Charged Residues: {str(amino_acid_charge_compostion['Negative'])}")

    
    print(f"\nNumber of heteroatoms: {len(hetero_atom_composition.keys())}")
    for heteroatom in hetero_atom_composition.keys():
        print(f"{heteroatom} : {hetero_atom_composition[heteroatom]}")

    print(f"\nDistance between most distant residues {most_distant_residues[0][0]} and {most_distant_residues[0][1]} is {most_distant_residues[1]:.2f} Angstrom")

    print(f"\nRadius of gyration: {radius_of_gyration:.2f}")


    if __name__ == "__main__":
       print_function(sys.argv[1])
