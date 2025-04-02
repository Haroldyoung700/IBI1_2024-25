# This script finds the length of the largest intron in a given DNA sequence.
# It identifies the positions of 'GT' and 'AG' sequences in the DNA sequence,
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
# The sequence is a string of DNA bases (A, T, C, G).
# It then calculates the length of the largest intron by finding the maximum distance between 'GT' and 'AG' positions.
gt_positions = []
for i in range(len(seq)-1):
    if seq[i] == 'G' and seq[i+1] == 'T':
        gt_positions.append(i)
# The 'GT' sequence is a common splice donor site in eukaryotic genes.
# The 'AG' sequence is a common splice acceptor site.
# The script iterates through the DNA sequence to find all occurrences of 'GT' and 'AG'.
# It stores their positions in separate lists.
ag_positions = []
for j in range(len(seq)-1):
    if seq[j] == 'A' and seq[j+1] == 'G':
        ag_positions.append(j)
# The script then calculates the length of the largest intron by finding the maximum distance between 'GT' and 'AG' positions.
# It ensures that the 'AG' position is at least 2 bases after the 'GT' position.
max_length = 0
for gt in gt_positions:
    for ag in ag_positions:
        if ag >= gt + 2:  
            current_length = ag - gt + 2  
            if current_length > max_length:
                max_length = current_length
# The script prints the length of the largest intron found in the DNA sequence.
print("The length of the largest intron", max_length)