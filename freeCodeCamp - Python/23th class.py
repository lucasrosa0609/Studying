# regular expressions
# in computing, a regular expression, also referred to as "regex" or "regexp",
# provides a concise and flexible menas for matching string of text,
# such as particular characters, words, or patterns of characters.
# A regular expression is written in a formal language that can be interpreted by
# a regular expression processor

# really clever "wild card" expression for matching and parsing strings
# SMART FIND OR SMART SEARCH

# understanding regular expressions
# very powerful and quite cryptic
# fun once you understand them. Regular expressions are a language unto themselves.
# A language of "markers characters" - programming with characters.
# Its kind of and "old school" language = compact

# regular expressions quick guide:
# ^ matches the beginning of a line
# $ matches the end of the line
# . matches any character
# \s matches whitespace
# \S matches any non-whitespace character
# * Repeats a character zero or more times
# *? Repeats a character zero or more times
# + Repeats a character zero or more times
# +? Repeats a character zero or more times
# [aeiou] Matches a single character in the listed set
# [^XYZ] Matches a single character not in the listed set
# [a-z0-9] The set of characters can include a range
# ( Indicates where string extraction is to start
# ) Indicates where string extraction is to end

# the regular expression module:
# before you can use regular expressions in your program, you must import the
# library using "import re".
# You can use re.search() to see if a string matches a regular expression,
# similar to using the find() method for strings.
# You can use re.findall() to extract portions of a string that match your regular
# expression, similar to a combination of find() and slicing: var[5:10]

# using re.search() like (find)

# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if line.find('From:') >= 0:
#         print(line)

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)
print()

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
print()

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)
print()

# wild-card characters
# the dot character matches any character.
# If you add the asterisk character, the character is "any number of times"


# ^X.*:  -> it says if something (^) startswith X and have any (.) character
# (*) many times

# ^X-\S+:  -> it says if something (^) startswith X-, match any (\S) non-whitespace
# character, (+) one or more times, :
# this will give us something like: X-Sieve: blablabla

# From matching to extracting



