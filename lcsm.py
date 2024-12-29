def longest_common_substring(dna_strings):
    if not dna_strings:
        return ""

    reference = dna_strings[0]
    max_length = 0
    longest_substr = ""

    for start in range(len(reference)):
        for end in range(start + 1, len(reference) + 1):
            substr = reference[start:end]
            if all(substr in other for other in dna_strings[1:]):
                if len(substr) > max_length:
                    max_length = len(substr)
                    longest_substr = substr

    return longest_substr

def read_fasta(file_path):
    with open(file_path, 'r') as file:
        sequences = []
        current_sequence = ""
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if current_sequence:
                    sequences.append(current_sequence)
                    current_sequence = ""
            else:
                current_sequence += line
        if current_sequence:  # Add the last sequence
            sequences.append(current_sequence)
    return sequences

# Example usage
file_path = 'dna_sequences.fasta'  # Replace with your actual file path
dna_sequences = read_fasta(file_path)
result = longest_common_substring(dna_sequences)
print("Longest Common Substring:", result)