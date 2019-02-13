#!/usr/bin/python

import sys
import re

for line in sys.stdin: # read the each line in the file from command prompt
	line = re.sub(r'^\W+|\W+$','',line) # remove the leading and trailing spaces
	words = re.split(r"\W+", line) # split the words, store the words list
	for word in words:
		print(word, "\t1") # for each word , we prints the 1 (indicates its occurance)
