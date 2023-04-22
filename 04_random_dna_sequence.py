# Generating a random DNA sequence.
# Write a function that generates a random DNA sequence.
# This function must receive the sequence length as the only parameter.

import random
from colorama import init, Fore, Style


def random_dna_seq(length):
    # Define a tuple with the dna bases
    base_list = ('A', 'T', 'C', 'G')
    # Initialise an empty dna sequence and a counter
    dna_seq = ''
    for base in range(length):
        # Choose a random base from the base list
        dna_seq += random.choice(base_list)
    # Initialize colorama
    init()
    # Set the colours for each base
    base_colors = {'A': Fore.RED, 'T': Fore.GREEN, 'C': Fore.YELLOW, 'G': Fore.BLUE}
    # Color each base and define the colorama style as bright
    # The end='' eliminates the space between the characters
    for base in dna_seq:
        color = base_colors.get(base, Fore.WHITE)
        print(color + base + Style.BRIGHT, end='')
    # Reset colorama styles
    print(Style.RESET_ALL)

# Example
random_dna_seq(97)
