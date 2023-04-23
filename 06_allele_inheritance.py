# Allele inheritance
#
# Write code that simulates the reproduction between two parents (AA, Aa, aa) 
# and show their offspring based on the probability of inheritance of each allele.
# The program must also show the percentage of each genotype in the offspring.


import random
from collections import Counter
from tabulate import tabulate

VALID = ('AA', 'Aa', 'aa')


def reproduction_sim():
    genotype1 = input('Enter the genotype of the first parent:')
    genotype2 = input('Enter the genotype of the second parent:')
    offspring_number = int(input('Enter the number of offsprings:'))
    # Check if the given genotypes are valid
    valid = ('AA', 'Aa', 'aa')
    if genotype1 not in valid or genotype2 not in valid:
        raise ValueError(f'results: genotype must be one of: {VALID}')
    else:
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
