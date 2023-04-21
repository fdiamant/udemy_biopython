# Extracting the AT/CG content
# Write a function that extracts the proportion (%) of a specific base in a DNA sequence.
# The function must have two parameters:
# 1. Sequence, i.e. the sequence to be analysed
# 2. The base, i.e. A, T, C, G to be analysed

def base_proportion(seq, base):
    # Calculate the proportion
    # Count the occurences of the specified base and divide them by the string (sequence) length
    proportion = seq.count(base) / len(seq)
    # Format the output.
    # The calculated proportion is turned into percentage format with two decimals
    return'The proportion of the base {} in the given sequence is {:.2%}'.format(base, proportion)


test_seq = 'ATCGTC'
test_base = 'A'

print(base_proportion(test_seq, test_base))
