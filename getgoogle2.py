# pip install google
import os
import sys
import time
import random
import pprint
from googlesearch import search

for url in search(query='"index of / - OneIndex"',stop=400):
	pprint.pprint(url)
time.sleep(random.randint(5, 10))
