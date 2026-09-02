sample_name = "  patient_07  "
raw_sequence = " acgt-gcaa-ttgc "

# Project Requirements

# Your program should:

# Remove the spaces from the beginning and end of sample_name.
clean_sample_name = sample_name.strip()

# Convert sample_name to uppercase.
clean_sample_name = clean_sample_name.upper()

# Remove the spaces and hyphens (-) from raw_sequence.
clean_raw_sequence = raw_sequence.strip().replace("-", "")

# Convert the DNA sequence to uppercase.
clean_raw_sequence = clean_raw_sequence.upper()

# Calculate the length of the cleaned DNA sequence.
sequence_length = len(clean_raw_sequence)   
# Store the first four bases in a variable.
first_four_bases = clean_raw_sequence[:4]
# Store the last four bases in another variable.
last_four_bases = clean_raw_sequence[-4:]
# Reverse the cleaned DNA sequence.
reversed_sequence = clean_raw_sequence[::-1]

# Count the number of A, T, G, and C bases.

# Print all the results in a clear report.
print("Sample Name:", {sample_name})
print(f"Cleaned Sample Name: {clean_sample_name}")
print(f"Reversed Sequence: {reversed_sequence}")
print(f"Sequence Length: {sequence_length}")
print(f"First Four Bases: {first_four_bases}")
print(f"Last Four Bases: {last_four_bases}")
print("DNA Sample Report")
print("A count : "+ str(clean_raw_sequence.count("A")))
print("T count : "+ str(clean_raw_sequence.count("T")))
print("G count : "+ str(clean_raw_sequence.count("G")))
print("C count : "+ str(clean_raw_sequence.count("C")))