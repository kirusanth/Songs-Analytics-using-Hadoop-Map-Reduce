#!/usr/bin/python

import sys
import re

for line in sys.stdin:
	line = re.sub(r'^\W+|\W+$','',line)
	print(line)
	words = re.split(r"\W+",line)
	number_of_words = len(words) - 1
	for i in range(0,number_of_words):
		print(words[i] +" " +words[i+1],"\t1")
	