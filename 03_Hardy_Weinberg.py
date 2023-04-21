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
# (2 x homozigotes x heterozigotes)/2 x N
# The the function needs to take three parameters.
#
# Expected number of each genotype:
# ExpPP = freqP^2 x N
# ExpPQ = freqP x freqQ x N x 2
# ExpQQ = freqQ^2 x N
#
# Chi-square:
#
# x^2 = Σ[(Ο-Ε)^2/Ε]
#Thus 6 parameters: PPobs, PQobs, QQobs, PPexp, PQexp, QQexp
