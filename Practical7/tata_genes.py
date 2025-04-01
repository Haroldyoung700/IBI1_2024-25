import re
# This script processes a FASTA file to extract sequences of genes that contain the TATA box pattern.
def extract_gene_name(header):
    return header.split()[0][1:] 
# assessing the TATA box pattern, which is a common promoter element in eukaryotic genes.
def process_fasta(input_file, output_file):
    tata_pattern = re.compile(r'TATA[AT]A[AT]') 
    current_gene = None
    current_seq_lines = []
    current_seq = ""
# read the input FASTA file and write to the output file
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.startswith('>'):# assess the header line
                if current_gene is not None:# examine the previous gene
                    if tata_pattern.search(current_seq): #write the gene to the output file if it contains the TATA box pattern
                        outfile.write(f'>{current_gene}\n')
                        outfile.writelines(current_seq_lines)
                # initialize for the next gene
                current_gene = extract_gene_name(line.strip())
                current_seq_lines = []
                current_seq = ""
            else:
                # accumulate the sequence lines
                current_seq += line.strip().upper()  # convert to uppercase
                current_seq_lines.append(line)  # add the current line to the sequence list

        # check the last gene after the loop
        if current_gene is not None and tata_pattern.search(current_seq):
            outfile.write(f'>{current_gene}\n')
            outfile.writelines(current_seq_lines)

# use the function to process the input FASTA file and write the output
process_fasta(
    'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa',
    'tata_genes.fa'
)