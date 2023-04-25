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
import sys

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


# The TEMP_PATH is for testing purposes. See the choose_file() function for more
# TEMP_PATH = '/Users/USER/PycharmProjects/udemy_biopython/sars.fasta'


def main():
    fasta_file = choose_file()
    seq = open_file(fasta_file)
    while True:
        input_option = get_input(prompt='Please choose an option: ', valid_options=VALID_OPTIONS)
        print(f'\nThe chosen file is {fasta_file}\nand your option is [{input_option}], to "{OPTIONS[input_option]}"\n')
        if input_option == 1:
            print(f'The RNA sequence is:\n\n{transcribe_dna(seq)}\n')
            write_file(input_option, seq)
        elif input_option == 2:
            print(f'The complementary sequence is:\n\n{complement_dna(seq)}\n')
            write_file(input_option, seq)
        elif input_option == 3 or input_option == 4:
            print(f'The {OPTIONS[3].replace("Show the ", "").replace(".", "")} is {calc_content(input_option, seq)}\n')
        elif input_option == 5:
            print('Thank you!')
            sys.exit()


# The choose_file function prompts the user to provide a file in the fasta format for analysis.
# The function checks whether the selected file is a valid file and whether it is in the fasta format,
# ensuring that only appropriate files are selected for further analysis.
def choose_file():
    while True:
        # Comment the TEMP_PATH and uncomment the input("Please enter the path to a FASTA file: ")
        # for a fully working program
        filepath = input("Please enter the path to a FASTA file: ")  # TEMP_PATH
        try:
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
        print("The available option are:")
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
def open_file(fasta_file):
    with open(str(fasta_file), 'r') as seq:
        # Skip the first line
        seq.readline()
        # Create a list with the rest of the lines
        seq_list = seq.readlines()
        # Return a string from the created list
        dna = ''.join(seq_list)
        return dna


# The transcribe_dna() function accepts a DNA strand as input and converts it to RNA
# based on the dna_to_rna dictionary. The function preserves any other characters,
# such as newline characters (\n), without modification for formatting purposes.
def transcribe_dna(seq):
    dna_to_rna = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}
    rna = ''
    for base in seq:
        if base in dna_to_rna.keys():
            rna += dna_to_rna[base]
        else:
            rna += base
    return rna


# The transcribe_dna() function accepts a DNA strand as input and converts it to complementary dna
# based on the dna_complement_dict dictionary. The function preserves any other characters,
# such as newline characters (\n), without modification for formatting purposes.
def complement_dna(seq):
    dna_complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    comp_seq = ''
    for base in seq:
        if base in dna_complement_dict.keys():
            comp_seq += dna_complement_dict[base]
        else:
            comp_seq += base
    return comp_seq


# The calc_content() function calculates the A-T or C-G content in the provided dna
def calc_content(choice, seq):
    percentage = ''
    # Count the A, T, C, G nucleotides in the dna
    a = seq.count('A')
    t = seq.count('T')
    c = seq.count('C')
    g = seq.count('G')
    # Calculate the total count of nucleotides in the dna
    # The len(dna) would not return an accurate result as it counts the \n characters as well
    # Another option would be len(dna) - dna.count('\n'). However there might be other characters
    # present in the dna strand. Thus, strictly counting the dna nucleotides and getting the total
    # from there seems to be a more accurate way.
    total = a + t + c + g
    if choice == 3:
        percentage = (a + t) / total
    elif choice == 4:
        percentage = (c + g) / total
    else:
        pass
    return f'{round(100 * percentage, 2)}%'


# The write_file() function saves as a .txt file the results
# of the transcription process (choice 1)
# and the complement process (choice 2)
def write_file(choice, seq):
    if choice == 1:
        rna_seq = transcribe_dna(seq)
        with open('rna.txt', 'w') as transcribed_dna:
            # Write the rna_seq into the file
            transcribed_dna.write(rna_seq)
            transcribed_dna.close()
    elif choice == 2:
        seq = complement_dna(seq)
        with open('cDNA.txt', 'w') as c_dna:
            # Write the seq into the file
            c_dna.write(seq)
            c_dna.close()
    else:
        pass


# example
main()
