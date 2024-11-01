def parse_pdb(file_path):
    # Initialize a list to store atom details
    atoms = []
    
    # Open the file in read mode
    with open(file_path, 'r') as file:
        for line in file:
            # Check if the line represents an ATOM or HETATM record
            if line.startswith("ATOM") or line.startswith("HETATM"):
                # Parse and store relevant atom information in a dictionary
                atom = {
                    "atom_name": line[12:16].strip(),       # Atom name (columns 13-16)
                    "residue_name": line[17:20].strip(),    # Residue name (columns 18-20)
                    "chain_id": line[21].strip(),           # Chain identifier (column 22)
                    "residue_seq_num": int(line[22:26].strip()),  # Residue sequence number (columns 23-26)
                    "x": float(line[30:38].strip()),        # X coordinate (columns 31-38)
                    "y": float(line[38:46].strip()),        # Y coordinate (columns 39-46)
                    "z": float(line[46:54].strip()),        # Z coordinate (columns 47-54)
                }
                # Append the atom dictionary to the atoms list
                atoms.append(atom)
    
    # Return the list of atoms, each represented as a dictionary with details
    return atoms

# Example usage of the function
pdb_data = parse_pdb("sample.pdb")
print(pdb_data)

