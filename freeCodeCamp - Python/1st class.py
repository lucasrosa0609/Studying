# syntax errors - you should find something else to try

# reserved words: False, None, True, and, as, assert, break, class, if, def, del, elif, else, except, return, for
# from, global, try, import, in, is, lambda, while, not, or, pass, raise, finally, continue, nonlocal, with, yield
# simple words that python understands as command

# sentences or lines
x = 2
x = x + 2
print(x)
print()

# python scripts: interactive python is good for experiments and programs of 3-4 lines long
# most programs are much longer, so we type them into a file and tell python to run the commands in the
# file
# in a sense, we are

# conditional steps
# if

x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')

print('Finis')
print()
# repeated steps

n = 5
while n > 0:  # as long as it is bigger then 0, keeps doing
    print(n)
    n = n - 1
print('Blastoff!')

# first program
# a short python "story" about how to count words in a file:

name = input('Enter file: ')
handle = open(name, 'r')

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)

