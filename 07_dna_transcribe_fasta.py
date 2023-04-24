"""Transcribing a DNA sequence from a FASTA file
1. Go to some gene/genome repository and download some FASTA file of a DNA sequence.
2. Import the file.
3. Generate a .txt file containing the transcribed sequence."""


# Download Staphylococcus aureus subsp. aureus NCTC 8325 chromosome, complete genome
# NCBI Reference Sequence: NC_007795.1
# from NCBI db

def open_seq():
    with open('sequence.fasta', 'r') as gen_seq:
        # Skip the first line
        gen_seq.readline()
        # Create a list with the rest of the lines
        seq_list = gen_seq.readlines()
        # Return a string from the created list
        return ''.join(seq_list)


def write_file():
    # Create a new file with write permission
    with open('transcribed_seq.txt', 'w') as transcribed_seq:
        # Write the output of the open_seq function into the file
        transcribed_seq.write(open_seq())

# Example
write_file()

