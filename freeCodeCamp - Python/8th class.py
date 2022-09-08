# Loops and iteration
# repeated steps

n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff')
print(n)

# loops (repeated steps) have iteration variables that change each time throug a loop
# often these iteration variables go through a sequence of numbers


# infinite loop
# n1 = 5
# while n1 > 0:
#     print('Lather')
#     print('Rinse')
# print('Dry off')

# another loop
# n2 = 0
# while n2 > 0:
#     print('Lather')
#     print('Rinse')
# print('Dry off')

# Breaking out of a loop
# the "BREAK" statement ends the current loop and jumps to the statement immediately
# following the loop
# it is like a loop test that can happen anywhere in the body of the loop

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

# continue statement ends the current iteration and jumps to the top of the loop
# and starts the next iteration

# while True:
#     line = input('> ')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

# indefinite loops
# while loops are called "indefinite loops" because they keep going until a logica
# condition becomes False
# the loops we have seen so far are pretty easy to examine to see if they will
# be "infinite loops"
# sometimes it is a little harder to be sure if a loop will terminate

