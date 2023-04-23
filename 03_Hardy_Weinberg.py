# A hypothetical population has 2500 individuals.
# Scientists are investigating two alleles, P and Q.
# The number of individuals with each genotype is as follows:
#   PP: 1200
#   PQ: 745
#   QQ: 555
# With the numbers above, calculate the frequency of each allele (0 to 1) and the chi-square for this population.
#
# Steps:
# Calculate the frequency of each allele.
# Calculate the expected number for each genotype.
# Calculate the chi-square based on the number of observed and expected individuals



# Retrieve the observed genotype numbers of the population
pp_obs = int(input('Please input the count of entities possessing the PP genotype: '))
pq_obs = int(input('Please input the count of entities possessing the PQ genotype: '))
qq_obs = int(input('Please input the count of entities possessing the QQ genotype: '))

# Calculate the population number
n = pp_obs + pq_obs + qq_obs

print(
    '\nThe population is {0}.\nThe number of individuals with PP genotype are {1}.\nThe number of individuals with PQ '
    'genotype are {2}.\nThe number of individuals with QQ genotype are {3}.\n'.format(
        n, pp_obs, pq_obs, qq_obs))


# Calculate the frequencies of P and Q in the population
# Allele frequency = (2 x homozigotes + heterozigotes)/2 x population
def allele_freq(homozigotes, heterozigotes, population):
    return (2 * homozigotes + heterozigotes) / (2 * population)


p_freq = allele_freq(pp_obs, pq_obs, n)
q_freq = allele_freq(qq_obs, pq_obs, n)

print('The allele P frequency is {}.\nThe allele Q frequency is {}'.format(p_freq, q_freq))


# Calculate the expected number of individuals for each genotype
# Expected number of each genotype:
# ExpPP = freqP^2 x N
# ExpPQ = freqP x freqQ x N x 2
# ExpQQ = freqQ^2 x N
def genotype_exp(freq_a, population, freq_b=None):
    if freq_b is not None:
        result = int(round((freq_a * freq_b * population * 2), 0))
    else:
        result = int(round(population * (freq_a ** 2), 0))
    return result


pp_exp = genotype_exp(p_freq, n)
pq_exp = genotype_exp(p_freq, n, q_freq)
qq_exp = genotype_exp(q_freq, n)

print(
    '\nThe expected number of individuals with PP genotype are {0}.\nThe expected number of individuals with PQ '
    'genotype are {1}.\nThe expected number of individuals with QQ genotype are {2}.\n'.format(
        pp_exp, pq_exp, qq_exp))

# Calculate the chi-squared
# Chi-squared:
# x^2 = Σ[(Ο-Ε)^2/Ε]

n_obs = [pp_obs, pq_obs, qq_obs]
n_exp = [pp_exp, pq_exp, qq_exp]


def chi_sq(obs, exp):
    result = 0
    i = 0
    while i < len(obs):
        delta = (obs[i] - exp[i]) ** 2 / (exp[i])
        result += delta
        i += 1
    return result


chi_squared = chi_sq(n_obs, n_exp)

print('\nThe χ\u00B2 is {}'.format(chi_squared))

# The degrees of freedom are the number of categories minus 1.
# There are two categories in this example (P and Q). Thus, the degrees of freedom are 1
# From the chi squared distribution table, for degrees of freedom 1 and critical value 0.005
# the chi squared value is 7.879
deg_of_freedom = 1
p = 0.005
chi = 7.879
certainty = 1 - p

print('\nFor {0} degree of freedom and p = {1} the χ\u00B2 equals {2}.\nSince the calculated χ\u00B2 ({3}) is greater '
      'than {2}, the null hypothesis is rejected'.format(deg_of_freedom, p, chi, chi_squared))
print('\nConsequently, there is a {:.2%} certainty that an evolutionary process is taking place in the specific '
      'population for the oberved time period'.format(certainty))
