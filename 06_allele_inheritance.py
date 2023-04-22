# Allele inheritance
#
# Write code that simulates the reproduction between two parents (AA, Aa, aa) 
# and show their offspring based on the probability of inheritance of each allele.
# The program must also show the percentage of each genotype in the offspring.


import random

def reproduction_sim(genotype1, genotype2, offspring_number):
    # Check if the given genotypes are valid
    valid = {'AA', 'Aa', 'aa'}
    if genotype1 not in valid or genotype2 not in valid:
        raise ValueError("results: genotype must be one of %r." % valid)
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
        percentages[offspring] = percentage


    return percentages



print(reproduction_sim('Aa', 'Aa', 10))

