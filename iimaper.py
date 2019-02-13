#!/usr/bin/python

import sys
import re

song_id = 0
for line in sys.stdin: # read the each line in the file from command prompt
    song_id += 1 # To keeps track of the song ( in the collection)
    line = re.sub(r'^\W+|\W+$','',line) # remove the leading and trailing spaces
    words = re.split(r"\W+", line) # split the words, store the words list
    for word in words:
        print(word.lower(), "\t" + str(song_id)) # prints the word and the song it belongs to
