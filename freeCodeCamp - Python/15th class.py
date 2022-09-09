# file handle as a sequence

# a file handle open for read can be treated as a sequence of strings
# where each line in the file is a string in the sequence
# we can use the for statement to iterate through a sequence
# remembrer - a sequence is an ordered set

# xfile = open('mbox.txt')
# for cheese in xfile:
#     print(cheese)

# open a file read-only
# use a for loop to read each line
# count the lines and print out the number of files

# fhand = open('mbox.txt')
# count = 0
# for line in fhand:
#     count = count + 1
# print('Line count:', count)
# print()

# reading the whole file
# we can read the whole file (newlines and all) into a single string

# fhand = open('mbox-short.txt')
# inp = fhand.read()
# print(len(inp))
# >> 94626
# print(inp[:20])
# print()

# searching through a file
# we can put an if statement in ou for loop to only print
# lines that meet some criteria

# fhand = open('mbox-short.txt')
# for line in fhand:
#     if line.startswith('From:'):
#         print(line)

# from: stephen.
#
# from: louis
#
# from : zquian

# blank lines
# each line from the file has a newline at the end
# the print statement adds a newline to each line

# searching through a file
# we can strip the whitespace from the right-hand side of the
# string using rstrip() from the string libreary
# the newline is considered "whitespace" and is stripped

# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith('From:'):
#         print(line)

# from: stephen.
# from: louis
# from : zquian

# skipping with continue
# we can conveniently skip a line by using the continue statement

# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From:'):
#         continue
#     print(line)

# using in to select lines
# we can look for a string anywhere in a line as our selection
# criteria

# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not '@uct.ac.za' in line:
#         continue
#     print(line)


# gives us the count of subjects:

# fname = input('Enter the file name: ')
# fhand = open(fname)
# count = 0
# for line in fhand:
#     if line.startswith('Subject:'):
#         count = count + 1
# print('There were', count, 'subject lines in', fname)

# bad filenames

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)


