# The function of recombination frequency
# Write a function that estimates the recombination frequency based on the
# number of recombinant and non-recombinant genotypes.
# The function should take 4 parameters.
# Two for the recombinant and two for the non-recombinant genotypes.


def get_genotype_num(prompt="Enter number: "):

    # (str) -> num (int)
    # Outputs a prompt and loops until a valid number is
    # entered by the user, at which point that value is
    # returned and the function terminates

    while True:
        num = input(prompt)
        try:
            num = int(num)
            return num
        except:
            print("Please enter a valid number (e.g., 1, 134, 56, 79).")

def recombination_freq():
    rec1 = get_genotype_num('Number of recombinant genotype 1:')
    rec2 = get_genotype_num('Number of recombinant genotype 2:')
    nonrec1 = get_genotype_num('Number of non-recombinant genotype 1:')
    nonrec2 = get_genotype_num('Number of non-recombinant genotype 2:')
    # freq = sum of recombinant / sum of all
    percentage = (rec1 + rec2) / (rec1 + rec2 + nonrec1 + nonrec2)
    return 'The recombination frequency is {:.5%}'.format(percentage)


print(recombination_freq())
