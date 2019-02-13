#!/usr/bin/python

import sys
import re

previous = None
totsum = 0

for line in sys.stdin: # read the each line in the file from command prompt
	key, value = line.split('\t') # separate keys and values by using \t to separate
	if key != previous: # if the key is different, then put this key as previous and set the totsum to zero
		if previous is not None: # if the previous has a key (diffrent key), then print it
			print (previous + '\t' + str(totsum))
		previous = key
		totsum = 0
	totsum = totsum + int(value) # if the keys are same, then increase the total sum by 1
print (previous + '\t' + str(totsum)) # print the previous key, the total sum for the last case (after it traverse through the line)
