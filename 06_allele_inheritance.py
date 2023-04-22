# Allele inheritance
#
# Write code that simulates the reproduction between two parents (AA, Aa, aa) 
# and show their offspring based on the probability of inheritance of each allele.
# The program must also show the percentage of each genotype in the offspring.


import random

def reproduction_sim(genotype1, genotype2, offspring_number):
    valid = {'AA', 'Aa', 'aa'}
    if genotype1 not in valid or genotype2 not in valid:
        raise ValueError("results: genotype must be one of %r." % valid)
    else:
        offsprings = []
        for allele in range(offspring_number):
            offspring = random.choice(genotype1) + random.choice(genotype2)
            offsprings.append(offspring)
        return offsprings

print(reproduction_sim('aa', 'aa', 10))

# mylist = ["apple", "banana", "cherry"]
# print(random.choices(mylist, weights = [10, 1, 1], k = 14))