# strings

# string data type
# a string is a sequence of characters, a string literal uses quotes
# 'Hello' or "hello". For strings, + means "concatenate". When a string contains
# numbers, it is still a string. we can convert numbers in a string into a number
# using int()

# str1 = "hello"
# str2 = 'there'
# bob = str1 + str2
# print(bob)
# str3 = '123'
# str3 = str3 + 1

# x = int(str3) + 1
# print(x)

# looking inside strings

# we can  get any single character in a string using an index
# specified in squade brackets. The index value must be an integer and
# starts at zero, the  index value can be n expression that is computed

fruit = 'banana'
letter = fruit[1]
print(letter)
x = 3
w = fruit[x - 1]
print(w)
print()

# a character too far
# you will get a python error if you attempt to index beyond the end of a string
# so be careful when constructing index values and slices

# strings have lenght

#the built-in function len gives us the lenght of a string

fruit = 'banana'
print(len(fruit))
print()

# len function

fruit = 'banana'
x = len(fruit)
print(x)
print()

# a function is some stores code that we use. A function takes some
# input and procuces and output

# looping through strings
# using a while statement and a iteration variable, and the len function, we can
# construct a loop to look at each of the letters in a string individually

fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1
print()

# a defininte loop using a for statement is much more elegant
# the iteration variable is completely taken care of by the for loop

count = 0
fruit = 'banana'
for letter in fruit:
    count += 1
    print(count, letter)
print()

# this is a simple loop that loops through each letter in a string and counts the
# number of times the loop encounters the 'a' character

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count+1
    print(count)

# looking deeper into 'IN'

# the iteration variable "iterates" through the sequence (ordered set)
# the block (body) of code is executed once for each value in the sequence
# the iteration variable moves through all of the values in the sequence

for letter in 'banana':
    print(letter)

    # the iteration variable "iterates" through the string and the block (body)
    # of code if executed once for each value in sequence

# more strings operations

