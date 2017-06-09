#!/usr/bin/env python

import pafy 
import re
import urllib
from bs4 import BeautifulSoup

term = input("What u wont m8?: ")
url ="https://www.youtube.com/results?search_query=" + term
response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, "lxml")

link = soup.find('a', href=re.compile("/watch*"))



print (link)
