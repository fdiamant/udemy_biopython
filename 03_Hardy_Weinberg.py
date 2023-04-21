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
#
# Allele frequency:
# (2 x homozigotes + heterozigotes)/2 x N
# The function needs to take three parameters.
#
# Expected number of each genotype:
# ExpPP = freqP^2 x N
# ExpPQ = freqP x freqQ x N x 2
# ExpQQ = freqQ^2 x N
#
# Chi-square:
#
# x^2 = Σ[(Ο-Ε)^2/Ε]
# Thus 6 parameters: PPobs, PQobs, QQobs, PPexp, PQexp, QQexp
#
# Explain the degrees of freedom.
# Degrees of freedom: N. of genotypes - N. of alleles
# Compare the measured chi-aquare with the table for the calculated degrees of freedom.

def allele_freq(pp_number, pq_number, qq_number):
    population = pp_number + pq_number + qq_number
    observed_p_freq = (2 * pp_number + pq_number) / (2 * population)
    observed_q_freq = (2 * qq_number + pq_number) / (2 * population)
    expected_pp_freq = pow(observed_p_freq, 2) * population
    expected_pq_freq = 2 * population * observed_q_freq * observed_p_freq
    expected_qq_freq = pow(observed_q_freq, 2) * population

    # return observed_p_freq, observed_q_freq, expected_pq_freq, expected_pp_freq, expected_qq_freq
    return 'The observed allele P frequency is {:.5} and the observed allele Q frequency is {:.5}.\nThe expected PP ' \
           'genotype number is {:.5}, the expected PQ genotype number is {:.5} and the expected QQ genotype number is ' \
           '{:.5}\n'.format(observed_q_freq, observed_q_freq, expected_pp_freq, expected_pq_freq, expected_qq_freq)


print(allele_freq(1200, 745, 555))
