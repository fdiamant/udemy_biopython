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

# Set the menu options in a dictionary
OPTIONS = {1: 'Return the RNA sequence and write it to a file.',
           2: 'Return the complementary sequence and write it to a file.',
           3: 'Show the A-T content.',
           4: 'Show the C-G content.',
           5: 'Exit'}
# To define the valid input options that a user can select from the previous dictionary,
# we can create a set using the set() function. This set will contain all the keys from
# the dictionary, representing the available options for the user to choose from.
VALID_OPTIONS = set(OPTIONS.keys())
# The TEMP_PATH is for testing purposes
TEMP_PATH = '/Users/fdiamant/PycharmProjects/udemy_biopython/sars.fasta'


# The choose_file function prompts the user to provide a file in the fasta format for analysis.
# The function checks whether the selected file is a valid file and whether it is in the fasta format,
# ensuring that only appropriate files are selected for further analysis.
def choose_file():
    while True:
        try:
            # Comment the TEMP_PATH and uncomment the input("Please enter the path to a FASTA file: ")
            # for a fully working program
            filepath = TEMP_PATH  # input("Please enter the path to a FASTA file: ")
            if not filepath.endswith('.fasta'):
                raise ValueError("Invalid file extension. Please enter a path to a FASTA file.")
            if not os.path.isfile(filepath):
                raise FileNotFoundError("File not found. Please enter a valid path to a FASTA file.")
            return filepath
        except (ValueError, FileNotFoundError) as e:
            print(e)


# The get_input function creates the choices menu and loops until a valid input is
# entered by the user of the specified type and from the specified set of valid options,
# at which point that value is returned and the function terminates.
def get_input(prompt="Choose an option: ", input_type=int, valid_options=None):
    while True:
        print("Please choose an option from the list below:")
        for key, value in OPTIONS.items():
            print(f"[{key}]:{value}")
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


# The function open_file() opens the fasta file, discards the first line
# and returns a string containing the dna sequence (and if present  \n characters)
def open_file():
    with open(str(choose_file()), 'r') as seq:
        # Skip the first line
        seq.readline()
        # Create a list with the rest of the lines
        seq_list = seq.readlines()
        # Return a string from the created list
        dna = ''.join(seq_list)
        return dna


def transcribe_dna():
    dna_seq = open_file()
    dna_to_rna = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}
    rna_seq = ''
    for base in dna_seq:
        if base in dna_to_rna.keys():
            rna_seq += dna_to_rna[base]
        else:
            rna_seq += base
    return rna_seq


def complement_dna():
    dna_seq = open_file()
    dna_complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    comp_seq = ''
    for base in dna_seq:
        if base in dna_complement_dict.keys():
            comp_seq += dna_complement_dict[base]
        else:
            comp_seq += base
    return comp_seq


def calc_content(choice):
    dna_seq = open_file()
    percentage = ''
    if choice == 3:
        percentage = (dna_seq.count('A') + dna_seq.count('T')) / (len(dna_seq)-dna_seq.count('\n'))
    elif choice == 4:
        percentage = (dna_seq.count('C') + dna_seq.count('G')) / (len(dna_seq)-dna_seq.count('\n'))
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
    dna_seq = open_file()
    while True:
        input_option = get_input(prompt='Please choose an option: ', valid_options=VALID_OPTIONS)
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
