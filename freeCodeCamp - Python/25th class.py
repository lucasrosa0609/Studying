# string parsin examples

data = 'From stephen.marquard@uct.ac.za Sat Jan 05 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)
print()


import re
y = re.findall('@([^ ]*)', data)
y1 = re.findall('^From .*@([^ ]*)', data)  # more precise, we will not verify
# lines that dont start with FROM
print(y)
print(y1)


# simple program
import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))
