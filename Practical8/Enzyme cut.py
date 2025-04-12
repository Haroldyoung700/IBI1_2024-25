def find_restriction_sites(dna_sequence, enzyme_sequence):
    valid_nucleotides = {'A', 'C', 'G', 'T'}
    
    # Validate DNA sequence
    for char in dna_sequence:
        if char not in valid_nucleotides:
            raise ValueError("DNA sequence contains invalid nucleotides.")
    
    # Validate enzyme sequence
    for char in enzyme_sequence:
        if char not in valid_nucleotides:
            raise ValueError("Enzyme sequence contains invalid nucleotides.")
    
    enzyme_length = len(enzyme_sequence)
    dna_length = len(dna_sequence)
    positions = []
    
    # Iterate through possible starting positions
    for i in range(dna_length - enzyme_length + 1):
        if dna_sequence[i:i+enzyme_length] == enzyme_sequence:
            positions.append(i)
    
    return positions

# Example usage:

dna = "ATGTTGAATAGTTCAAGAAAATATGCTTGTCGTTCCCTATTCAGACAAGCGAACGTCTCA"
enzyme = "AATATG"
print(find_restriction_sites(dna, enzyme))  #output: [19]