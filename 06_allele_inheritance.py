# Allele inheritance
#
# Write code that simulates the reproduction between two parents (AA, Aa, aa) 
# and show their offspring based on the probability of inheritance of each allele.
# The program must also show the percentage of each genotype in the offspring.


import random
from collections import Counter
from tabulate import tabulate

VALID = ('AA', 'Aa', 'aa')


def get_input(prompt="Enter input: ", input_type=str, valid_options=None):
    # (str, type, set) -> any
    # Outputs a prompt and loops until a valid input is
    # entered by the user of the specified type and (optionally)
    # from the specified set of valid options, at which
    # point that value is returned and the function terminates.

    while True:
        try:
            user_input = input_type(input(prompt))
            if valid_options is not None and user_input not in valid_options:
                raise ValueError(f"Invalid option. Please choose from {valid_options}")
            return user_input
        except ValueError as e:
            if input_type == int:
                print("Please enter an integer (e.g. 1, 34, 67, 1593)")
            else:
                print(e)


def reproduction_sim():
    genotype1 = get_input(prompt='Enter the genotype of the first parent: ', valid_options=VALID)
    genotype2 = get_input(prompt='Enter the genotype of the second parent: ', valid_options=VALID)
    offspring_number = get_input(prompt='Enter the number of offsprings: ', input_type=int)

    # Create an empty list to store the offsprings
    offsprings = []
    # Repeat for the wanted number of offsprings
    for _ in range(offspring_number):
        # Choose a random allele from the first parent and a random allele from the second parent
        # Join them to create the offspring and store the new offspring in the offsprings list
        # aA and Aa are the same
        allele1 = random.choice(genotype1)
        allele2 = random.choice(genotype2)
        if allele1 == 'a' and allele2 == 'A':
            offspring = 'Aa'
        elif allele1 == 'A' and allele2 == 'a':
            offspring = 'Aa'
        else:
            offspring = allele1 + allele2
        offsprings.append(offspring)

    # Calculate percentages
    percentages = {}
    for offspring in offsprings:
        percentage = offsprings.count(offspring) / len(offsprings)
        percentages[offspring] = round(100 * percentage, 2)
    # Store the offsprings in a dict with values as keys and their respective frequency as value
    offsprings_dict = dict(Counter(offsprings))

    # Formulate the result in a table
    # Create two tables from the results dictionaries
    offsprings_freq_table = [(k, v) for k, v in offsprings_dict.items()]
    offsprings_percentage_table = [(k, v) for k, v in percentages.items()]
    # Join the two tables in one per genotype
    joined_table = [(k, v1, v2) for (k, v1), (k2, v2) in zip(offsprings_freq_table, offsprings_percentage_table) if
                    k == k2]
    # Print the result in a tabular format
    print(tabulate(joined_table, headers=['Genotype', 'Frequency', 'Percentage'], tablefmt='grid'))


# Example
reproduction_sim()
