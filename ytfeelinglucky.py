#!/usr/bin/env python

import pafy
import re
import urllib
from bs4 import BeautifulSoup

#Search youtube

term = input("Search term: ")
url ="https://www.youtube.com/results?search_query=" + term
response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, "lxml")

#Find video link

link = soup.find('a', attrs={'href': re.compile("/watch*")})
watchlink = str(link)
startfind = watchlink.find('href="') + 6
endfind = watchlink.find('"><div', startfind)

watchfinal =  (watchlink[startfind:endfind])

#print the video link

print (watchfinal)
