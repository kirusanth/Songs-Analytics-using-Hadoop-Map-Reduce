#!/usr/bin/python
import sys
import re


# create (word, song_ids) pair
def word_plus_ids(song_ids, previous):
	to_print = ''
	for i in range(len(song_ids)):
		# if it's the last song_id
		if i == (len(song_ids) - 1):
			to_print += song_ids[i]
			to_print = to_print.replace("\n", "") # all song_ids come with \n, remove them
			print (previous + '\t' + to_print) # print word result
		else:
			to_print += song_ids[i] + ', ' # add song_id to to_print

previous = None
song_ids = ()

for line in sys.stdin:
	key, value = line.split('\t')
	if key != previous:
		if previous is not None:
			word_plus_ids(song_ids, previous) # print result
		previous = key
		song_ids = () # reset tuple
	song_ids += (value,) # add song id to tuple
word_plus_ids(song_ids,  previous) # print result
