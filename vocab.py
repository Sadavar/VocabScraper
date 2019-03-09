#!/usr/bin/env python

from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys


urls = {}
defs = {}

x = 1

for word in range(5):
	urls[x] = "https://www.merriam-webster.com/dictionary/" + sys.argv[x]
	x = x + 1


x = 1

for url in urls:
	page = urlopen(urls.get(x))
	soup = BeautifulSoup(page, features="lxml")

	result = soup.select_one("span[class*=dtText]").text

	result = result.split(":")[1]
	result = result.split('\n')[0]

	defs[sys.argv[x]] = result

	x = x + 1

for key,val in defs.items():
    print(key, "=", val)
