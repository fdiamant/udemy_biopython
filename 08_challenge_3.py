"""
Manipulating a genetic sequence from a database

Write a python script that reads a genetic sequence from a database.
The program must display a menu to the user, allowing her/him to choose from the following options:

1. Return the RNA sequence and write it to a file.
2. Return the complementary sequence and write it to a file.
3. Show the A-T content.
4. Show the C-G content.

Make an error treatment code, so that the program warns the user about an invalid option.
"""

import os

VALID = (1, 2, 3, 4, 5)
OPTIONS = ['Return the RNA sequence and write it to a file.', 'Return the complementary sequence and write it to a '
                                                              'file.', 'Show the A-T content.', 'Show the C-G content.',
           'Exit']
TEMP_PATH = '/Users/fdiamant/PycharmProjects/udemy_biopython/sars.fasta'


def choose_file():
    while True:
        try:
            filepath = TEMP_PATH  # input("Please enter the path to a FASTA file: ")
            if not filepath.endswith('.fasta'):
                raise ValueError("Invalid file extension. Please enter a path to a FASTA file.")
            if not os.path.isfile(filepath):
                raise FileNotFoundError("File not found. Please enter a valid path to a FASTA file.")
            return filepath
        except (ValueError, FileNotFoundError) as e:
            print(e)


def get_input(prompt="Choose an option: ", input_type=int, valid_options=None):
    # Outputs a prompt and loops until a valid input is
    # entered by the user of the specified type and
    # from the specified set of valid options, at which
    # point that value is returned and the function terminates.

    while True:
        # print("Please choose an option from the list below:")

        for idx, element in enumerate(OPTIONS):
            print(f"[{idx + 1}]:{element}")

        try:
            user_input = input_type(input(prompt))
            if valid_options is not None and user_input not in valid_options:
                raise ValueError(f"Invalid option. Please choose from {valid_options}")
            return user_input
        except ValueError as e:
            if input_type == int:
                print(f"Invalid option. Please choose from {valid_options}")
            else:
                print(e)


def open_file():
    with open(str(choose_file()), 'r') as gen_seq:
        # Skip the first line
        gen_seq.readline()
        # Create a list with the rest of the lines
        seq_list = gen_seq.readlines()
        # Return a string from the created list
        dna_seq = ''.join(seq_list)
        return dna_seq


def transcribe_dna():
    dna_seq = open_file()
    dna_to_rna = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}
    rna_seq = ''
    for base in dna_seq:
        if base in dna_to_rna.keys():
            rna_seq += dna_to_rna[base]
    return rna_seq


def complement_dna():
    dna_seq = open_file()
    dna_complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    comp_seq = ''
    for base in dna_seq:
        if base in dna_complement_dict.keys():
            comp_seq += dna_complement_dict[base]
    return comp_seq


def calc_content(choice):
    dna_seq = open_file()
    percentage = ''
    if choice == 3:
        percentage = dna_seq.count('AT') / len(dna_seq)
    elif choice == 4:
        percentage = dna_seq.count('CG') / len(dna_seq)
    else:
        pass
    return percentage


def write_file(choice):
    if choice == 1:
        rna_seq = transcribe_dna()
        with open('transcribed_dna.txt', 'w') as transcribed_dna:
            # Write the rna_seq into the file
            transcribed_dna.write(rna_seq)
    elif choice == 2:
        seq = complement_dna()
        with open('cDNA.txt', 'w') as c_dna:
            # Write the seq into the file
            c_dna.write(seq)
    else:
        pass


def main():
    # filepath = choose_file()
    #
    # print(filepath)
    while True:
        input_option = get_input(prompt='Please choose an option: ', valid_options=VALID)
        if input_option == 1:
            print(transcribe_dna())
            write_file(input_option)
        elif input_option == 2:
            print(complement_dna())
            write_file(input_option)
        elif input_option == 3 or input_option == 4:
            print(calc_content(input_option))
        elif input_option == 5:
            print('Thank you!')
            exit()


# example
main()
