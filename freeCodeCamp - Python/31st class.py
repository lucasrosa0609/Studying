# what is web scraping?
# whe na program or script pretends to be a browser and retrieves web pages,
# looks at those web pages, extracts information, and then looks at more web
# pages. Search engines scrape web pages - we call this "spidering the web" or
# "web crawling"

# why scrape?
# pull data - particularly social data - who links to who?
# Get your own data back out of some system that has no "export capability".
# Monitor a site for new information. Spider the web to make a database for
# a search engine


# there is some controversy about web page scraping and some sites are a bit
# snippy about it. Republishing copyrighted information is not allowed.
# Violating terms of service is not allowed


# the easy way - beautiful soup
# you could do string searches the hard way
# or use the free software library called BeautifulSoup from www.crummy.com

# to run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# or download the file:
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))