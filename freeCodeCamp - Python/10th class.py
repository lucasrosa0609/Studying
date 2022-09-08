# loop idioms: what we do in loops
# note: even though these examples are simple, the pattens apply to all king of loops

# making smats loops
# the trick is "knowing" something abotu the whole loop whe nyou are stuck writing
# code that only sees one entry at a time

# set some variables to initial values
# "for thing in data:
# look for something or do something to each entry separately, updating a variable
# look at the variables

print('Before')
for thing in [9, 41, 12, 3, 74, 15]:
    print(thing)
print('After')
print()

# what is the largest number?
# how did your brain organize to know what is the largest number
# computers do NOT do like your brain, he scans and keep the biggest untill
# find another bigger than the one that he kept

largest_so_far = -1
print('Before:', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)

# we make a variable that contains the largest value we have seen so far. If the
# current number we are looking at is larger, it is the new largest value we have
# seen so far

print('After:', largest_so_far)
print()

# more loops patterns
# 