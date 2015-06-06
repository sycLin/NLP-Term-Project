#!/usr/bin/python
# -*- coding: utf-8 -*-

#################### Import Modules ####################
import os
import sys

#################### Class Definitions ####################

class NGRAM:

	def __init__(self, n, prefixNGRAM):
		self.N = n
		self.gramList = []
		self.gramCount = 0
		self.prefixNGRAM = prefixNGRAM
	
	# build up the n-gram model from taglist
	def build(self, tagList):

		# don't mess up the tagList
		tagList = list(tagList)
		
		# add start symbols and end symbols
		for i in range(self.N - 1):
			tagList.insert(0, "^")
			tagList.append("$")

		# process the taglist to get tuple
		length = len(tagList)
		for start in range(length - self.N + 1):
			tmp = []
			for index in range(self.N):
				tmp.append(tagList[start+index])
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
			if i.Content == gramTuple:
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

	# Returns the count corresponding to the given tuple
	def getGramCount(self, gramTuple):
		tmp = self.hasGram(gramTuple)
		if tmp == False:
			return 0
		return tmp.Count

	# Return the prefix gram tuple of the given gramTuple
	def getPrefixGram(self, gramTuple):
		tmp = []
		for i in range(len(gramTuple)-2): # exclude the last item in gramTuple
			tmp.append(i)
		return tuple(tmp)

	# Returns a probability indicating how much the tagList fits this NGRAM model
	def getFitness(self, tagList):

		# add start symbols and end symbols
		for i in range(self.N - 1):
			tagList.insert(0, '^')
			tagList.append('$')

		# initialize the variables
		numerator = float(1.0)
		denominator = float(1.0)

		# calculate numerator & denominator
		length = len(tagList)
		for start in range(length - self.N + 1):
			tmp = []
			for index in range(self.N):
				tmp.append(tagList[start+index]) 
			gramTuple = tuple(tmp) # now gramTuple is the tuple for this NGRAM (self).

			numerator *= self.getProb(gramTuple)
			if start != 0:
				prefixGramTuple = self.getPrefixGram(gramTuple)
				denominator *= self.prefixNGRAM.getProb(prefixGramTuple)

		# special case
		if numerator == 0:
			return 0

		return float(numerator / denominator)

	# Returns a float number: the probability of gramTuple in this NGRAM model
	def getProb(self, gramTuple):
		gramCount = self.getGramCount(gramTuple)
		totalCount = self.gramCount
		return float(float(gramCount) / float(totalCount))


class GRAM:

	def __init__(self, gramTuple):
		self.Content = gramTuple
		self.Count = 1
	
	def __repr__(self):
		return ("This gram: "+str(self.Content)+" Count = "+str(self.Count))

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

# return list of POS tags, given rawLine (either Correct or Error)
def process_raw_line2(rawLines):
	result = [[], []]
	tmp = rawLines.split();
	for i in tmp:
		tmp2 = i.split('#')
		result[0].append(tmp2[1])
		result[1].append(len(tmp2[0]))
	return result

# find out the most-likely redundant tag. Returns the index (0 ~ len-1).
def guess(tagList):
	global biGram, biGramNeg, triGram, triGramNeg
	mostLikelyTag = 0
	mostLikely = -float("inf")
	for i in range(len(tagList)):
		tmpList = list(tagList)

		# remove one of the tags
		tmpList.pop(i)

		# utilize NGRAM.getFitness to see how well it fits the models
		# combine those data from getFitness() => determine the position
		likelihood = 0.7*(biGram.getFitness(tmpList) - biGramNeg.getFitness(tmpList))
		likelihood += 0.3*(triGram.getFitness(tmpList) - triGramNeg.getFitness(tmpList))
		if likelihood > mostLikely:
			mostLikelyTag = i
			mostLikely = likelihood
	
	return mostLikelyTag

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
uniGram = NGRAM(1, None)
biGram = NGRAM(2, uniGram)
triGram = NGRAM(3, biGram)

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
	"""
	i += 1
	if i == 10:
		break
	"""

#############################
# calculate the total count #
# for each NGRAM instance   #
#############################

uniGram.countAll()
biGram.countAll()
triGram.countAll()

uniGramNeg.countAll()
biGramNeg.countAll()
triGramNeg.countAll()

print uniGram.gramCount
print biGram.gramCount
print triGram.gramCount
print "===================="
print uniGramNeg.gramCount
print biGramNeg.gramCount
print triGramNeg.gramCount

#################
# start testing #
#################
while True:
	line = testFile.readline()
	if line == "":
		break
	# testList = process_raw_line(line)
	tmp = process_raw_line2(line)
	print tmp[0]
	print tmp[1]
	pass
	# print guess(testList)


###############
# close files #
###############
trainFile.close()
testFile.close()

pass
