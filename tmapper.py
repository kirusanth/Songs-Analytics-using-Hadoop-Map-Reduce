#!/usr/bin/python


import sys
import re

for line in sys.stdin: # read the each line in the file from command prompt
	line = re.sub(r'^\W+|\W+$','',line) # remove the leading and trailing spaces
	words = re.split(r"\W+", line) # split the words, store the words list
	number_of_words = len(words) - 2 # in order to avoid index out of bounds exception
	for i in range(0, number_of_words):
		print(words[i] + " " + words[i + 1] + " " + words[i + 2], "\t1") # prints word i, i+1, and i+2 index word (represents trigrams)
