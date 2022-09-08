# definite loops
# quite often we have a list of items of the lines in a file - effectively
# a finite set of things

# we can write a loop to run the loop once for each of the items in a set using the
# python for construct

# these loops r called "definite loops" because they execute an exact number of times

# we say that "definite loops iterate through the members of a set"

for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff')
print()

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done')

# definite loops (for loops) have explicit iteration variables that change eacah time
# through a loop. These iteration variables move through the sequence or set

# look at in

# the iteration variable "iterates" through the sequence (ordered set)

# the block(body) of code is executed once for each valuer in the sequence

# the iteration variable moves through all of the values in the sequence

