seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'

gt_positions = []
for i in range(len(seq)-1):
    if seq[i] == 'G' and seq[i+1] == 'T':
        gt_positions.append(i)

ag_positions = []
for j in range(len(seq)-1):
    if seq[j] == 'A' and seq[j+1] == 'G':
        ag_positions.append(j)

max_length = 0
for gt in gt_positions:
    for ag in ag_positions:
        if ag >= gt + 2:  
            current_length = ag - gt + 2  
            if current_length > max_length:
                max_length = current_length

print("The length of the largest intron", max_length)