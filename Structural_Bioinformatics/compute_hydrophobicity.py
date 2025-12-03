import sys
import matplotlib.pyplot as plt
import os

STUDENT_SURNAME = "Kamalan_kumaraguruparan"

def get_residues(pdb_file):

    atom_lines =[]
    residues = []
    protein_pdb = open(pdb_file)
    Protein_read = protein_pdb.readlines()
    for lines in Protein_read:
        if lines.startswith("ATOM"):
           line = lines.replace("\n","").rstrip()
           atom_lines.append(line)
    
    for line in atom_lines:
          lines = line.split()
          for val in lines:
             if val == "CA":
                trim = str(line[17:20])
                residues.append(trim)
    return residues
    

def compute_hydrophobicity(residues, window_size):
        
    Kyte_Doolittle_scale = { 'ALA': 1.8,'ARG':-4.5,'ASN':-3.5,'ASP':-3.5,'CYS': 2.5,
        'GLN':-3.5,'GLU':-3.5,'GLY':-0.4,'HIS':-3.2,'ILE': 4.5,
        'LEU': 3.8,'LYS':-3.9,'MET': 1.9,'PHE': 2.8,'PRO':-1.6,
        'SER':-0.8,'THR':-0.7,'TRP':-0.9,'TYR':-1.3,'VAL': 4.2 }

    average_values = []
    kyte_Doolittle_scale_values = []
    
    for codon in residues:
        if codon in Kyte_Doolittle_scale:
            values = Kyte_Doolittle_scale.get(codon)
            kyte_Doolittle_scale_values.append(values)
    print(kyte_Doolittle_scale_values)

    x = 0
    m = 0
    n = window_size
    while x < len(kyte_Doolittle_scale_values):
        value = kyte_Doolittle_scale_values[m:n]
        sum = 0
        if len(value) == window_size:
          final = 0
          for x1 in value:
              sum += x1
              m += 1
              n += 1
          final = sum/window_size
          #final1 = round(final,2)
          average_values.append(final)
        x += 1     

    try: 
        plt.plot(average_values, marker = 'o',color = 'black', ms = 10, mfc ='r')
        plt.title("Hydrophobicity plot")
        plt.xlabel("AA position")
        plt.ylabel("Hydrophobicity")
        plt.savefig(f"./{STUDENT_SURNAME}_hydrophobicity_plot_{window_size}.png")
        plt.clf()
        return 1        
    except Exception as e:
        print(f"Error in plotting: {e}")
        return 0

#Nothing to do here
if __name__ == "__main__":
    if STUDENT_SURNAME == None:
        print(f"Update your surname")
        sys.exit()
    residues = get_residues(sys.argv[1])
    print(f"Length of residues: {len(residues)}")
    window_sizes = [5, 9]
    for window_size in window_sizes:
        compute_hydrophobicity(residues, window_size)
        plt.clf()

    for window_size in [3, 7]:
        compute_hydrophobicity(residues, window_size)
    os.remove(f"./{STUDENT_SURNAME}_hydrophobicity_plot_3.png")

