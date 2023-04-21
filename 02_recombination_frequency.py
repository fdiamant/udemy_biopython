# The function of recombination frequency
# Write a function that estimates the recombination frequency based on the
# number of recombinant and non-recombinant genotypes.
# The function should take 4 parameters.
# Two for the recombinant and two for the non-recombinant genotypes.

def recombination_freq(rec1, rec2, nonrec1, nonrec2):
    # freq = sum of recombinant / sum of all
    percentage = (rec1 + rec2) / (rec1 + rec2 + nonrec1 + nonrec2)
    return 'The recombination frequency is {:.2%}'.format(percentage)


print(recombination_freq(4, 8, 54, 67))
