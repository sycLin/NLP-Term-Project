#!/usr/bin/python
# -*- coding: utf-8 -*-

#################### Import Modules ####################
import os
import sys

#################### Class Definitions ####################

class NGRAM:

	def __init__(self, n):
		self.N = n
		self.gramList = []
		self.gramCount = 0
	
	# build up the n-gram model from taglist
	def build(self, tagList):

		# add start symbols and end symbols
		for i in range(self.N - 1):
			tagList.insert(0, "^")
			tagList.append("$")

		# process the taglist to get tuple
		length = len(tagList)
		tmp = []
		for i in range(length - self.N + 1):
			tmp.append(tagList[i])
		gramTuple = tuple(tmp)

		# add this tuple to NGRAM
		self.addGram(gramTuple)

	# count total occurences of all gram instances
	def countAll(self):
		total = 0
		for i in self.gramList:
			total = total + i.Count
		self.gramCount = total
		return total

	# check if the tuple already exists in gramList
	# 1) return the GRAM instance if found.
	# 2) return False if not found.
	def hasGram(self, gramTuple):
		for i in self.gramList:
			if i.content == gramTuple:
				return i
		return False

	# add a gram instance of the tuple
	# 1) if didn't exist, creat and insert.
	# 2) if already exists, count += 1
	def addGram(self, gramTuple):
		tmp = self.hasGram(gramTuple)
		if tmp == False: # does not exist, yet.
			# create a GRAM instance, and insert.
			newGRAMInstance = GRAM(gramTuple)
			self.gramList.append(newGRAMInstance)
		else: # already exists
			tmp.Count += 1

	# return the count corresponding to the given tuple
	def getGramCount(self, gramTuple):
		tmp = self.hasGram(gramTuple)
		if tmp == False:
			return 0
		return tmp.Count

class GRAM:

	def __init__(self, gramTuple):
		self.Content = gramTuple
		self.Count = 1
	
	def __repr__(self):
		return ("This gram: "+self.Content+" Count = "+self.Count)

pass

#################### Helper Functions ####################

def print_usage():
	sys.stderr.write("Usage: ./main.py [train_file] [test_file]\n")

# return list of POS tags, given rawLine (either Correct or Error)
def process_raw_line(rawLines):
	result = []
	tmp = rawLines.split();
	for i in tmp:
		tmp2 = i.split('#')
		result.append(tmp2[1])
	return result

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

# positive ones
uniGram = NGRAM(1)
biGram = NGRAM(2)
triGram = NGRAM(3)

# negative ones
uniGramNeg = NGRAM(1)
biGramNeg = NGRAM(2)
triGramNeg = NGRAM(3)

########################
# process the raw data #
########################

i = 0
while True:

	# get lines from p2.*.tagged.txt two by two
	rawErrorLine = trainFile.readline()
	if rawErrorLine == "": # EOF reached
		break
	rawCorrectLine = trainFile.readline()

	# process the line, to get the POS tags sequence only
	negList = process_raw_line(rawErrorLine)
	posList = process_raw_line(rawCorrectLine)

	# build the NGRAMs
	uniGram.build(posList)
	biGram.build(posList)
	triGram.build(posList)

	uniGramNeg.build(negList)
	biGramNeg.build(negList)
	triGramNeg.build(negList)

	i += 1
	if i == 10:
		break



###############
# close files #
###############
trainFile.close()
testFile.close()

pass
