# Timing algorithm execution
# Use the previous random sequence generation function and the time module to
# evaluate how many seconds the algorithm takes to generate a sequence with a thousand, ten thousand,
# one hundred thousand and one million nucleotides (1,000, 10,000, 100,000, 1,000,000).

import time
import random
from tabulate import tabulate


def execution_timing():
    global interval
    dna_seq_lengths = [1000, 10000, 100000, 1000000]
    times = {}
    for length in dna_seq_lengths:
        start = time.time()
        random_dna_seq(length)
        end = time.time()
        interval = end - start
        times[length] = interval
    table = [(k, v) for k, v in times.items()]
    print(tabulate(table, headers=['DNA length', 'Execution time'], tablefmt='grid'))


def random_dna_seq(length):
    # Define a list with the dna bases
    base_list = ['A', 'T', 'C', 'G']
    # Initialise an empty dna sequence and a counter
    dna_seq = ''
    i = 0
    while i < length:
        # Choose a random base from the base list
        dna_seq += random.choice(base_list)
        i += 1
    return dna_seq


# Example
execution_timing()
