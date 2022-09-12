# creates a program that tell the most 10 common words
# in the text 'mbox-short.txt'

file = open('mbox-short.txt')
counts = dict()
for line in file:
    line1 = line.split()
    for word in line1:
        counts[word] = counts.get(word, 0) + 1

sequence = list()
for (w, count) in counts.items():
    tuple_for_sequence = (count, w)
    sequence.append(tuple_for_sequence)

sequence = sorted(sequence[:10], reverse=True)
print(sequence)

for value, word1 in sequence:
    print(f'Word: "{word1}", Times: "{value}"')

