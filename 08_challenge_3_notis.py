import os
import sys

OPTIONS = {
    1: "Return the RNA sequence and write it to a file.",
    2: "Return the complementary sequence and write it to a file.",
    3: "Show the A-T content.",
    4: "Show the C-G content.",
    5: "Exit",
}

VALID_OPTIONS = set(OPTIONS.keys())


def main():
    fasta_file = choose_file()
    seq = read_sequence(fasta_file)

    while True:
        option = get_option()

        if option == 1:
            rna_seq = transcribe_dna(seq)
            print(f"The RNA sequence is:\n\n{rna_seq}\n")
            write_to_file("rna.txt", rna_seq)
        elif option == 2:
            comp_seq = complement_dna(seq)
            print(f"The complementary sequence is:\n\n{comp_seq}\n")
            write_to_file("cDNA.txt", comp_seq)
        elif option == 3:
            print(f"The A-T content is {calc_content(seq, 'A', 'T')}%")
        elif option == 4:
            print(f"The C-G content is {calc_content(seq, 'C', 'G')}%")
        elif option == 5:
            print("Thank you!")
            sys.exit()


def choose_file():
    while True:
        filepath = input("\nPlease enter the path to a FASTA file: ")
        if not filepath.endswith(".fasta"):
            print("Invalid file extension. Please enter a path to a FASTA file.")
        elif not os.path.isfile(filepath):
            print("File not found. Please enter a valid path to a FASTA file.")
        else:
            return filepath


def read_sequence(fasta_file):
    with open(fasta_file, "r") as seq_file:
        seq_file.readline()
        seq = seq_file.read().replace("\n", "")
    return seq


def get_option():
    while True:
        print("\nWhat would you like to do with the given sequence?\n")
        for key, value in OPTIONS.items():
            print(f"[{key}]:{value}")

        try:
            user_input = int(input("\nChoose an option: "))
            if user_input not in VALID_OPTIONS:
                raise ValueError(f"Invalid option. Please choose from {VALID_OPTIONS}")
            return user_input
        except ValueError as e:
            print(e)


def transcribe_dna(seq):
    dna_to_rna = {"A": "U", "T": "A", "C": "G", "G": "C"}
    return "".join([dna_to_rna.get(base, base) for base in seq])


def complement_dna(seq):
    dna_complement_dict = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join([dna_complement_dict.get(base, base) for base in seq])


def calc_content(seq, base1, base2):
    count1 = seq.count(base1)
    count2 = seq.count(base2)
    total = len(seq)
    percentage = (count1 + count2) / total * 100
    return round(percentage, 2)


def write_to_file(filename, content):
    with open(filename, "w") as output_file:
        output_file.write(content)


if __name__ == "__main__":
    main()
