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


# Retrieve the observed genotype numbers of the population
pp_obs = int(input('Please input the count of entities possessing the PP genotype: '))
pq_obs = int(input('Please input the count of entities possessing the PQ genotype: '))
qq_obs = int(input('Please input the count of entities possessing the QQ genotype: '))

# Calculate the population number
n = pp_obs + pq_obs + qq_obs
obs = [pp_obs, pq_obs, qq_obs]

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

# def hypothesis_testing():
#
#
#     p_freq = (2 * pp_obs + pq_obs) / (2 * n)
#     q_freq = (2 * qq_obs + pq_obs) / (2 * n)
#
#     # Calculate the expected number of individuals for each genotype
#     pp_exp = pow(p_freq, 2) * n
#     pq_exp = 2 * n * q_freq * p_freq
#     qq_exp = pow(q_freq, 2) * n
#
#     # Assign the observed and expected results in two lists
#     gen_obs = [pp_obs, pq_obs, qq_obs]
#     gen_exp = [pp_exp, pq_exp, qq_exp]
#
#     # Calculate the chisquare
#     chi_sq = 0
#     i=0
#     while i <= len(gen_obs):
#         chi_sq += (pow(gen_obs - gen_exp), 2) / gen_exp
#         i+=1
#
#     chi_square = (pow(pp_obs - pp_exp, 2) / pp_exp) + (
#             pow(pq_obs - pq_exp, 2) / pq_exp) + (
#                          pow(qq_obs - qq_exp, 2) / qq_exp)
#     return chi_square, chi_sq
#
#
# # return 'The observed allele P frequency is {:.5} and the observed allele Q frequency is {:.5}.\nThe expected PP '
# \ #        'genotype number is {:.5}, the expected PQ genotype number is {:.5} and the expected QQ genotype number
# is ' \ #        '{:.5}\nThe chi_square is {:.5} which is larger than {:.5} for significance level 0.001.\nThus the
# ' \ #        'hypothesis stands with 99.9% certainty.'.format( #     p_freq, q_freq, pp_exp, pq_exp, qq_exp,
# chi_square, #     table_chi)
#
#
# print(hypothesis_testing())
