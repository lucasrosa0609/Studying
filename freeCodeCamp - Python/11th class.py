# continuing in a loop

zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print('After', zork)
print()

# to count how many times we execute a loop, we introduce a new variable that starts
# at 0 and we add one to it each time through the loop

# summing in a loop
zork1 = 0
print('Before', zork1)
for thing in [9, 41, 12, 3, 74, 15]:
    zork1 = zork1 + thing
    print(zork1, thing)
print('After', zork1)
print()

# to add up a value we encounter in a loop, we introduce a sum
# variable that starts at 0, and we add the value to the sum each time
# through the loop

# finding the average in a loop

count = 0
sum = 0
print('Before:', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After:', count, sum, sum/count)
print()

# an avreage just combines the counting and sum patterns and divides
# when the loop is done

# filtering in a loop

print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if value>20:
        print('Larger number', value)
print('After')
print()

# we use an if statement in the loop to catch / filter the values we are looking for

# search using a boolean variable
found = False
print('before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
print('After', found)
print()

# if we just want to search and know if a value was found, we use a variable
# that starts at false and is set to true as soon as we find what we are looking for

# how to find the smallest value
# smallest_so_far = -1
# print('Before', smallest_so_far)
# for the_num in [9, 41, 12, 3, 74, 15]:
#     if the_num < smallest_so_far:
#         smallest_so_far = the_num
#     print(smallest_so_far, the_num)
# print('After', smallest_so_far)

# how would we change this to make it find the smallest value in the list
smallest_so_far = None
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest_so_far is None:
        smallest_so_far = value
    elif value < smallest_so_far:
        smallest_so_far = value
    print(smallest_so_far, value)
print('After', smallest_so_far)

# we still have a variable that is the smallest so far. The first time through
# the loop smallest is none, so we take the first value to be the smallest
# works for the largest too

# the "is" and "is not" operators

# python has an "is" operator that can be used in logical expressions
# implies "is the same as"
# similar to, but stronger than "=="
# is not also is a logical operator


