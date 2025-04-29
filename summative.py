from collections import Counter
from Bio.Seq import Seq
from Bio.Data import CodonTable
import matplotlib.pyplot as plt

# Use the standard codon table
standard_table = CodonTable.unambiguous_rna_by_name["Standard"]

def get_codons(seq):
    """Return a list of codons from a sequence (assumes frame starts at AUG)."""
    start_index = seq.find("AUG")
    if start_index == -1:
        return []
    codons = []
    for i in range(start_index, len(seq) - 2, 3):
        codon = seq[i:i+3]
        if codon in standard_table.stop_codons:
            break
        codons.append(codon)
    return codons

def most_frequent_codon(seq):
    """Return the most frequent codon in a given mRNA sequence."""
    codons = get_codons(seq)
    if not codons:
        return None
    freq = Counter(codons)
    return freq.most_common(1)[0]  # (codon, frequency)

def most_frequent_amino_acid(seq):
    """Return the amino acid corresponding to the most frequent codon."""
    codon, _ = most_frequent_codon(seq)
    if codon:
        return Seq(codon).translate()
    return None

def plot_amino_acid_frequencies(seq):
    """Plot the frequency of amino acids encoded by the given mRNA sequence."""
    codons = get_codons(seq)
    amino_acids = [Seq(codon).translate() for codon in codons]
    freq = Counter(amino_acids)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.bar(freq.keys(), freq.values(), color='skyblue')
    plt.xlabel('Amino Acids')
    plt.ylabel('Frequency')
    plt.title('Amino Acid Frequency Distribution')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

# ICA first trial