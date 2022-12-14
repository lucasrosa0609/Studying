# using urllib in Python
# since HTTP is so common, we have a library that does all the socket work for us and makes web pages look like a file

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

# like a file

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
print()

# reading webpages

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

for line in fhand:
    print(line.decode().strip())

# parsing HTML ( a.k.a Web Scraping)

