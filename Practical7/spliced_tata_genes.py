import re

def main():
    # input splice donor/acceptor combination from user
    print("Available splice donor/acceptor combinations: GTAG, GCAG, ATAC")
    splice_comb = input("Enter splice donor/acceptor combination (GTAG, GCAG, ATAC): ").upper().strip()
    if splice_comb not in {"GTAG", "GCAG", "ATAC"}:
        print("Invalid input. Exiting.")
        return

    # according to the splice donor/acceptor combination, set the donor and acceptor sequences
    donor = splice_comb[:2]
    acceptor = splice_comb[2:]
    output_file = f"{splice_comb}_spliced_genes.fa"

    # prepare the TATA box pattern
    tata_pattern = re.compile(r'TATA[AT]A[AT]')

    # assess the input FASTA file and write to the output file
    # read the input FASTA file and write to the output file
    with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as infile, \
         open(output_file, 'w') as outfile:
        
        current_gene = None
        current_seq = []
        for line in infile:
            if line.startswith('>'):
                # assess the previous gene
                if current_gene is not None:
                    full_seq = ''.join(current_seq).upper()
                    # examine the TATA box pattern and splice site
                    tata_count = len(tata_pattern.findall(full_seq))
                    if tata_count > 0 and has_splice_site(full_seq, donor, acceptor):
                        outfile.write(f'>{current_gene} TATA:{tata_count}\n{full_seq}\n')
                # initialize for the next gene
                current_gene = line.split()[0][1:]  # extract gene name from header
                current_seq = []
            else:
                current_seq.append(line.strip())
        
        # assess the last gene after the loop
        if current_gene is not None:
            full_seq = ''.join(current_seq).upper()
            tata_count = len(tata_pattern.findall(full_seq))
            if tata_count > 0 and has_splice_site(full_seq, donor, acceptor):
                outfile.write(f'>{current_gene} TATA:{tata_count}\n{full_seq}\n')

def has_splice_site(seq, donor, acceptor):
    donor_len = len(donor)
    acceptor_len = len(acceptor)
    for i in range(len(seq) - donor_len - acceptor_len + 1):
        # pairing donor and acceptor sites
        if seq[i:i+donor_len] == donor:
            # search for acceptor site after donor site
            for j in range(i + donor_len + 1, len(seq) - acceptor_len + 1):
                if seq[j:j+acceptor_len] == acceptor:
                    return True
    return False

if __name__ == "__main__":
    main()