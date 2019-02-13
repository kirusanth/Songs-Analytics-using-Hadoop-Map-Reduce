# Name : Kirusanth Thiruchelvam , Daniel Fortunato
# Course : EECS 4415 - Big Data Systems
# Student No: 212918298 , 216796443
# Program : It preprocess the song lyrics from csv file
import pandas as pd
import nltk as nl
from nltk.corpus import stopwords
from nltk import word_tokenize
import sys
import csv
import re
nl.download('stopwords')
nl.download('punkt')

#function to clean data
def regex_clean(word):
    #lower case all words
    word = word.lower()
    #remove numbers and special characters
    word = re.sub (r'(\d|\W)+'," ", word)
    #remove words with 2 or less length
    word = re.sub(r'\b\w{1,2}\b', '', word)
    return word

def unique_word_in_a_song_lyrics (song):
	# stores the stop words
	nl_stop_words = set(stopwords.words('english'))
	song = regex_clean(song)
	# tokenize the words in song
	words_in_song = word_tokenize(song)

	# remove the duplicates (we store each word in collection if the word appears again then we dont add it to the output string)
	words_collection = set()

	#output string
	unique_song = '' # stores the unique words in a string
 	# traverse the words in the list of tokenized song
	for word in words_in_song:
		if word not in nl_stop_words:
			if word not in words_collection: # in a song, we will not have same word again
				unique_song += " " + word # return string
				words_collection.add(word)
	return unique_song

def main():
	# get the file from system input
	csv_file = sys.stdin
	# read the csv file and separe the song lyrics
	reader  = pd.read_csv(csv_file, delimiter =',')
	# get the text column
	song_collection = reader["text"]
	# file creation
	file = open("input.txt","w+") # if the file does not exist, this will create it
	# traverse through each song
	for song in song_collection: 
		song = unique_word_in_a_song_lyrics(song) # only allow unique word in a song
		file.write(song +'\n') # write a song in a line, then move to newline
	file.close() # close the file


if __name__ == "__main__":
	main()
