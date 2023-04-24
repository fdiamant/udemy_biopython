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

VALID = (1, 2, 3, 4)
OPTIONS = ['Return the RNA sequence and write it to a file.', 'Return the complementary sequence and write it to a '
                                                              'file.', 'Show the A-T content.', 'Show the C-G content.']
TEMP_PATH = '/Users/fdiamant/PycharmProjects/udemy_biopython/sars.fasta'

def choose_file():
    while True:
        try:
            filepath = TEMP_PATH #input("Please enter the path to a FASTA file: ")
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
        print("Please choose an option from the list below:")

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

def transcribe_dna():
    pass


def write_file():
    pass




def comp_seq():
    pass


def calc_content():
    pass


def main():
    dna_seq = choose_file()
    input_option = get_input(prompt='Please choose an option: ', valid_options=VALID)
    print(f'The selected file is: {dna_seq}\n')
    print(f'The selected option is [{input_option}]: {OPTIONS[input_option-1]}')



main()

