from pymol import cmd, stored


@cmd.extend
def hydrophobicity(selection="all", palette='blue_red', window=1, _self=cmd):

    """
        Function to compute hydrophobicity with window size

        Parameters
        ----------
        selection : str
            selected residues, default = "all"

        palette : pymol palette
            selected palette, default = "blue_red"
        
        window : int
            integer value of averaging window size 

        Return
        ----------
        None

    """

    assert window % 2 == 1
    
    Kyte_Doolittle_scale = { 'ALA': 1.8,'ARG':-4.5,'ASN':-3.5,'ASP':-3.5,'CYS': 2.5,
        'GLN':-3.5,'GLU':-3.5,'GLY':-0.4,'HIS':-3.2,'ILE': 4.5,
        'LEU': 3.8,'LYS':-3.9,'MET': 1.9,'PHE': 2.8,'PRO':-1.6,
        'SER':-0.8,'THR':-0.7,'TRP':-0.9,'TYR':-1.3,'VAL': 4.2 }

    #TODO Write a PyMOL extension that will colour each residue in a given PyMOL selection according to the Kyte-Doolittle scale. The extension has to be imported
    # into PyMOL with run script.py from the PyMOL command line, and has to be
    # launchable with the hydrophobicity [, selection [, palette]] from inside PyMOL. Refer to the PyMOL wiki and provided code snippet for guidance

