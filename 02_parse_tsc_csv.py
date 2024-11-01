def parse_csv_tsv(file_path, delimiter=','):
    # Open the CSV/TSV file in read mode
    with open(file_path, 'r') as file:
        data = []  # List to store each row's data as a dictionary
        # Read the first line to extract headers
        headers = file.readline().strip().split(delimiter)
        
        # Iterate through the remaining lines in the file
        for line in file:
            # Split each line into values based on the specified delimiter
            values = line.strip().split(delimiter)
            # Create a dictionary for each row by pairing headers with corresponding values
            row = dict(zip(headers, values))
            # Append the row dictionary to the data list
            data.append(row)
    
    # Return the list of rows, where each row is a dictionary with headers as keys
    return data

# Example usage of the function for a CSV file
csv_data = parse_csv_tsv("sample.csv", delimiter=',')
print(csv_data)

# Example usage of the function for a TSV file
tsv_data = parse_csv_tsv("sample.tsv", delimiter='\t')
print(tsv_data)
