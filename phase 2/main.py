#!/usr/bin/python
# -*- coding: utf-8 -*-

#################### Import Modules ####################
import os
import sys

#################### Class Definitions ####################

class NGRAM:

	def __init__(self):
		self.gramList = []
		self.gramCount = 0
	
	# build up the n-gram model from lines of data
	def build(self, linesOfData):
		# add start symbols and end symbols
		# process the linesOfData
		pass

	# count total occurences of all gram instances
	def countAll(self):
		total = 0
		for i in self.gramList:
			total = total + i.count
		self.gramCount = total
		return total

	# check if the tuple already exists in gramList
	def hasGram(self, gramTuple):
		pass

	# add a gram instance of the tuple
	def addGram(self, gramTuple):
		pass

	# return the count corresponding to the given tuple
	def getGramCount(self, gramTuple):
		pass

class GRAM:

	def __init__(self, gramTuple):
		self.Content = gramTuple
		self.count = 0
	
	def __repr__(self):
		return ("This gram: "+self.Content+" Count = "+self.Count)

pass

#################### Helper Functions ####################

def print_usage():
	sys.stderr.write("Usage: ./main.py [train_file] [test_file]\n")

pass

#################### Variables Declaration ####################

pass

#################### Main Program ####################

##################
# check argument #
##################

if len(sys.argv) != 3:
	print_usage()
	sys.exit(1)

##############
# open files #
##############
try:
	trainFile = open(sys.argv[1], 'r')
except:
	sys.stderr.write("[Error] training data file: %s does not exist.\n" % sys.argv[1])
	sys.exit(1)
try:
	testFile = open(sys.argv[2], 'r')
except:
	sys.stderr.write("[Error] test data file: %s does not exist.\n" % sys.argv[2])
	sys.exit(1)

print("files both opened successfully!")

###############
# build NGRAM #
###############

uniGram = NGRAM()
biGram = NGRAM()
triGram = NGRAM()

########################
# process the raw data #
########################

i = 0
while True:
	rawErrorLine = trainFile.readline()
	if rawErrorLine == "":
		break
	rawCorrectLine = trainFile.readline()
	print rawErrorLine
	print rawCorrectLine
	i += 1
	if i == 10:
		break



###############
# close files #
###############
trainFile.close()
testFile.close()

pass
