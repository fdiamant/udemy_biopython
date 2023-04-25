
OPTIONS = {1: 'Return the RNA sequence and write it to a file.',
           2: 'Return the complementary sequence and write it to a file.',
           3: 'Show the A-T content.',
           4: 'Show the C-G content.',
           5: 'Exit'}

print(f'The {OPTIONS[3].replace("Show the ", "").replace(".", "")} is 3\n')

text = OPTIONS[3].replace('Show the ', '').replace('.', '')

print(text)