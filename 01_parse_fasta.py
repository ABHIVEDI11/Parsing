def parse_fasta(file_path):
    # Open the FASTA file in read mode
    with open(file_path, 'r') as file:
        sequences = {}        # Dictionary to store sequences with headers as keys
        current_sequence = ''  # Temporary variable to accumulate the current sequence
        current_header = None  # Variable to store the current header

        # Read the file line by line
        for line in file:
            line = line.strip()  # Remove any leading/trailing whitespace
            
            # Check if the line is a header (starts with '>')
            if line.startswith(">"):
                # If there's a current header, save the accumulated sequence to the dictionary
                if current_header:
                    sequences[current_header] = current_sequence
                # Update the current header (remove the '>' symbol) and reset the sequence
                current_header = line[1:]
                current_sequence = ''
            else:
                # Accumulate sequence lines under the current header
                current_sequence += line
        
        # After the loop, add the last sequence to the dictionary if there's a remaining header
        if current_header:
            sequences[current_header] = current_sequence

    # Return the dictionary with headers as keys and sequences as values
    return sequences

# Example usage of the function
fasta_data = parse_fasta("sample.fasta")
print(fasta_data)
