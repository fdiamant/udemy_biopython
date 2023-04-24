"""Transcribing a DNA sequence from a FASTA file
1. Go to some gene/genome repository and download some FASTA file of a DNA sequence.
2. Import the file.
3. Generate a .txt file containing the transcribed sequence."""


# Download Staphylococcus aureus subsp. aureus NCTC 8325 chromosome, complete genome
# NCBI Reference Sequence: NC_007795.1
# from NCBI db

def transcribe_seq():
    with open('sequence.fasta', 'r') as gen_seq:
        # Skip the first line
        gen_seq.readline()
        # Create a list with the rest of the lines
        seq_list = gen_seq.readlines()
        # Return a string from the created list
        dna_seq = ''.join(seq_list)

    # Transcription dictionary and process
    dna_to_rna = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}
    rna_seq = ''
    for base in dna_seq:
        if base in dna_to_rna.keys():
            rna_seq += dna_to_rna[base]

    # Create a new file with write permission
    with open('transcribed_seq.txt', 'w') as transcribed_seq:
        # Write the rna_seq into the file
        transcribed_seq.write(rna_seq)


# Example
transcribe_seq()
