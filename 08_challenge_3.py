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
from tkinter import filedialog

VALID = (1, 2, 3, 4)
OPTIONS = ['Return the RNA sequence and write it to a file.', 'Return the complementary sequence and write it to a '
                                                              'file.', 'Show the A-T content.', 'Show the C-G content.']


def choose_file():
    # Prompts the user to select a fasta file

    # Set the arguments for the filedialog
    options = {
        'title': 'Select a FASTA file',
        'filetypes': [('Text files', '*.fasta')],
        'default extension': '.fasta'
    }
    # Show the file dialog box and get the selected file path
    filepath = filedialog.askopenfilename(**options)
    return filepath

    # print("Selected file:", filepath)


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


def read_file():
    pass


def write_file():
    pass


def transcribe_dna():
    pass


def comp_seq():
    pass


def calc_content():
    pass

# genotype1 = get_input(prompt='Enter the genotype of the first parent: ', valid_options=VALID)
