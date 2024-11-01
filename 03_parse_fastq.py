def parse_fastq(file_path):
    # Open the FASTQ file in read mode
    with open(file_path, 'r') as file:
        reads = []  # List to store each read's information
        while True:
            # Read the header line
            header = file.readline().strip()
            # If no header is found, end of file is reached
            if not header:
                break
            # Read the sequence line
            sequence = file.readline().strip()
            # Read the '+' line, which is a separator in FASTQ format
            plus_line = file.readline().strip()
            # Read the quality score line
            quality = file.readline().strip()
            # Store the read's information as a dictionary
            reads.append({
                "header": header[1:],  # Remove the '@' symbol from header
                "sequence": sequence,   # The DNA/RNA sequence
                "quality": quality      # The quality scores as a string
            })
    # Return the list of reads, each represented as a dictionary
    return reads

# Example usage of the function
fastq_data = parse_fastq("sample.fastq")
print(fastq_data)
