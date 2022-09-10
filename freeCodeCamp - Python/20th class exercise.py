#  Count the frequency of each word in a file & store it in a dictionary.
#  Then, find the most common word.

archive1 = open('clown.txt')
# print(archive1)

count = dict()
for word in archive1:
    word1 = word.split()
    for word2 in word1:
        # print(word2)
        count[word2] = count.get(word2, 0) + 1
# print(count)
# print()

archive2 = open('intro.txt')
count1 = dict()
for value in archive2:
    # print(value)
    value1 = value.split()
    for value2 in value1:
        # print(value2)
        count1[value2] = count1.get(value2, 0) + 1
# print(count1)

for v1 in count:
    if count[v1] > 2:
        print(v1, count[v1])

max_value = max(count, key=count.get)
print(max_value)
print()
print(f'The most common word in intro.txt is:')
print(f'"{max(count, key=count.get)}", that appeard {count.get("the")} times')
print()

for v in count1:
    if count1[v] > 50:
        print(v, count1[v])

print()
print(f'The most common word in intro.txt is:')
print(f'"{max(count1, key=count1.get)}", that appeard {count1.get("the")} times')







