# write a program which repeatedly reads numbers until the user enters "done".
# Once "done" is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake
# using try and except and print an error message and skip to the next number

total = 0
count = 0
while True:
    value = input('Write a number: ')
    if value == 'Done':
        break
    try:
        int(value)
    except:
        value = -1
        if value < 0:
            print('Bad data')
            continue

    if int(value) > 0:
        value = int(value)
        count = count + 1
        total = total + value

print(count, total, total / count)

