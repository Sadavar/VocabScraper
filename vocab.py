#!/usr/bin/env python

from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys


urls = {}
defs = {}



for word in range(5):
	urls[x] = "https://www.merriam-webster.com/dictionary/" + sys.argv[x]




for url in urls:
	page = urlopen(urls.get(x))
	soup = BeautifulSoup(page, features="lxml")

	result = soup.select_one("span[class*=dtText]").text

	result = result.split(":")[1]
	result = result.split('\n')[0]

	defs[sys.argv[x]] = result



for key,val in defs.items():
    print(key, "=", val)
