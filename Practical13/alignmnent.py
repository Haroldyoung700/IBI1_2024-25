from Bio import SeqIO
from Bio.Align import substitution_matrices
import os
import sys
import random

# ================= Configuration Section =================
FASTA_DIR = r"/Users/harold_young/Library/Mobile Documents/com~apple~CloudDocs/GitHub/IBI1_2024-25/Practical13"
HUMAN_FILE = os.path.join(FASTA_DIR, "P04179.fasta")
MOUSE_FILE = os.path.join(FASTA_DIR, "P09671.fasta")

# ================= Core Functions =================
def load_sequence(filepath):
    """Load and validate protein sequence from FASTA"""
    try:
        with open(filepath, 'r') as f:
            record = SeqIO.read(f, "fasta")
            seq = str(record.seq).upper()
            
            # Validate amino acid composition
            valid_aa = set("ARNDCQEGHILKMFPSTWYVX*")  # Including rare/reserved chars
            seq_chars = set(seq)
            if not seq_chars <= valid_aa:
                invalid = seq_chars - valid_aa
                raise ValueError(f"Invalid characters: {invalid}")
                
            return seq
            
    except Exception as e:
        print(f"Error loading {os.path.basename(filepath)}: {str(e)}")
        sys.exit(1)

def generate_random(reference_seq):
    """Generate random sequence preserving amino acid distribution"""
    aa_counts = {aa: reference_seq.count(aa) for aa in set(reference_seq)}
    population = [aa for aa, count in aa_counts.items() for _ in range(count)]
    return ''.join(random.sample(population, len(population)))

def calculate_alignment(seq1, seq2, matrix):
    """Enhanced alignment scorer with sanity checks"""
    if len(seq1) != len(seq2):
        raise ValueError(f"Length mismatch: {len(seq1)} vs {len(seq2)}")
    
    score = 0
    identical = 0
    
    for a, b in zip(seq1, seq2):
        try:
            score += matrix[(a, b)]
        except KeyError:
            # Handle non-standard residues gracefully
            score += matrix.get((a, b), -4)  # Default penalty for unknown pairs
            
        identical += (a == b)
    
    return {
        'blosum_score': score,
        'identity_pct': (identical / len(seq1)) * 100,
        'alignment_length': len(seq1)
    }

# ================= Main Workflow =================
if __name__ == "__main__":
    # 1. Load and validate sequences
    try:
        human_seq = load_sequence(HUMAN_FILE)
        mouse_seq = load_sequence(MOUSE_FILE)
    except Exception as e:
        sys.exit(1)

    # 2. Generate composition-preserving random sequence
    random_seq = generate_random(human_seq)

    # 3. Load and validate substitution matrix
    try:
        matrix = substitution_matrices.load("BLOSUM62")
        # Add missing entries for non-standard residues
        matrix.update({('X', 'X'): -1, ('*', '*'): 1, ('X', '*'): -4})
    except Exception as e:
        print(f"Matrix error: {str(e)}")
        sys.exit(1)

    # 4. Perform alignments
    comparisons = {
        "Human vs Mouse": (human_seq, mouse_seq),
        "Human vs Random": (human_seq, random_seq),
        "Mouse vs Random": (mouse_seq, random_seq)
    }

    results = {}
    for name, (seq_a, seq_b) in comparisons.items():
        try:
            results[name] = calculate_alignment(seq_a, seq_b, matrix)
        except ValueError as e:
            print(f"Alignment failed for {name}: {str(e)}")
            results[name] = None

    # 5. Generate report
    print("\n=== Sequence Summary ===")
    print(f"Human (P04179): {human_seq[:50]}... (Length: {len(human_seq)})")
    print(f"Mouse (P09671): {mouse_seq[:50]}... (Length: {len(mouse_seq)})")
    print(f"Random Sequence: {random_seq[:50]}... (Length: {len(random_seq)})")

    print("\n=== Alignment Results ===")
    for name, data in results.items():
        if data:
            print(f"{name}:")
            print(f"  BLOSUM62 Score: {data['blosum_score']}")
            print(f"  Percent Identity: {data['identity_pct']:.2f}%")
            print(f"  Compared Positions: {data['alignment_length']}\n")
        else:
            print(f"{name}: Comparison failed\n")

    # 6. Quality control check
    human_mouse_identity = results["Human vs Mouse"]['identity_pct']
    if human_mouse_identity < 20:
        print("\nWARNING: Unexpected low identity between human and mouse sequences.")
        print("Possible issues:\n- Incorrect sequences\n- Species mismatch\n- Sequence corruption")