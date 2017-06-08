#!/usr/bin/env python

import pafy 
import re
import urllib
#import urllib2
from bs4 import BeautifulSoup

term = input("What u wont m8?: ")
search = urllib.quote(term)
url ="https://www.youtube.com/results?search_query=" + search
response = urllib.urlopen(url)
html = response.read()
soup = BeautifulSoup(html)
link = soup.find(attrs={'class':'yt-uix-tile-link'})

print (link)


#https://stackoverflow.com/questions/2792650/python3-error-import-error-no-module-name-urllib2
