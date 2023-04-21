# Extracting the AT/CG content
# Write a function that extracts the proportion (%) of a specific base in a DNA sequence.
# The function must have two parameters:
# 1. Sequence, i.e. the sequence to be analysed
# 2. The base, i.e. A, T, C, G to be analysed

def base_proportion(seq, base):
    # Calculate the proportion
    # Count the occurences of the specified base
    first_base_count = seq.count(base)
    # Find the second base of the AT/CG pair
    pairing = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    second_base = pairing[base]
    # Count the occurences of the second base
    second_base_count = seq.count(second_base)
    # Calculate the total count
    total_count = first_base_count + second_base_count
    # Calculate the proportion
    proportion = total_count / len(seq)
    # Format the output.
    # The calculated proportion is turned into percentage format with two decimals
    return'The proportion of the base {} in the given sequence is {:.2%}'.format(base, proportion)


test_seq = 'ATCCAGCCTGAGAGATGGGAGAATTGATACGGGACTCTACGTACGTAACTCTCGGTTCGTAGACACCCGACAGCCCGTCTCGCACAGGAGCTATTTATGG'
test_base = 'G'

print(base_proportion(test_seq, test_base))
