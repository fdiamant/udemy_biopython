# Generating a random DNA sequence.
# Write a function that generates a random DNA sequence.
# This function must receive the sequence length as the only parameter.

import random
from termcolor import colored
from colorama import init, Fore, Style

def dna_generator(length):
    base_list = ['A', 'T', 'C', 'G']
    dna_seq = ''
    i = 0
    while i < length:
        dna_seq += random.choice(base_list)
        i+=1
    return dna_seq

def print_colored_dna(sequence):
    init()  # initialize colorama
    base_colors = {'A': Fore.RED, 'T': Fore.GREEN, 'C': Fore.YELLOW, 'G': Fore.BLUE}
    for base in sequence:
        color = base_colors.get(base, Fore.LIGHTBLACK_EX)
        print(color + base, end=' ')
    print(Style.RESET_ALL)  # reset colorama styles

print_colored_dna(dna_generator(100))