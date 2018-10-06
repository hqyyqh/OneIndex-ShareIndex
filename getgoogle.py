# 順調に働くため、まず：pip install MagicGoogle
# ４０３エイラが起こえるから、getgoogle2.pyを使ってください。

import os
import sys
import time
import random
import pprint
from MagicGoogle import MagicGoogle

mg = MagicGoogle()

for i in range(1,5):
	for url in mg.search_url(query='"index of / - OneIndex"',start=i*100+1,num=100):
		pprint.pprint(url)
	time.sleep(random.randint(5, 10))


