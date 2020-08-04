"""
I/O functions for PDB files
"""
import numpy as np

def open_pdb(f_loc):
    # This function reads in a pdb file and returns the atom names and coordinates.
    with open(f_loc) as f:
        data = f.readlines()

    coords_list = []
    sym = []
    for line in data:
        if 'ATOM' in line[0:6] or 'HETATM' in line[0:6]:
            sym.append(line[76:79].strip())
            coords_entry = [float(x) for x in line[30:55].split()]
            coords_list.append(coords_entry)

    coords = np.array(coords_list)
    return sym, coords

