def parse_pdbsum(file_path):
    # Initialize an empty dictionary to store parsed data by sections
    summary = {}
    
    # Open the file in read mode
    with open(file_path, 'r') as file:
        section = None  # Variable to track the current section
        for line in file:
            # Remove leading and trailing whitespace from the line
            line = line.strip()
            
            # Identify a new section if the line starts with "######"
            if line.startswith("######"):
                # Extract the section name, remove the # symbols, convert to lowercase
                section = line.strip("# ").lower()
                # Initialize an empty list for this section in the summary dictionary
                summary[section] = []
            # If a section is currently being processed, add lines to it
            elif section:
                summary[section].append(line)
    
    # Return the dictionary with parsed sections and their contents
    return summary

# Example usage of the function
pdbsum_data = parse_pdbsum("sample.pdbsum")
print(pdbsum_data)
