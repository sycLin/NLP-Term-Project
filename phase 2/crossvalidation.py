#!/usr/bin/python
# -*- coding: utf-8 -*-

#################### Import Modules ####################
import os
import sys

#################### Class Definitions ####################

class NGRAM:

	def __init__(self, n):
		self.N = n
		self.gramDict = {}
		self.gramCount = 0
	
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
			tmp = str(tagList[start])
			for index in range(1, self.N):
				tmp += ("+" + str(tagList[start + index]))
			self.addGram(tmp)
			"""
			if self.gramDict.has_key(tmp):
				self.gramDict[tmp] += 1
			else:
				self.gramDict[tmp] = 1
			# add this tuple to NGRAM
			"""
	def combineModel(self, crossedOut):
		pass

	# count total occurences of all gram instances
	def countAll(self):
		total = 0
		for i, j in self.gramDict.iteritems():
			total = total + j
		self.gramCount = total
		return total

	# check if the tuple already exists in gramList
	# 1) return the GRAM instance if found.
	# 2) return False if not found.
	def hasGram(self, gramTuple):
		if self.gramDict.has_key(gramTuple):
			return True
		else:
			return False

	# add a gram instance of the tuple
	# 1) if didn't exist, creat and insert.
	# 2) if already exists, count += 1
	def addGram(self, gramTuple):
		tmp = self.hasGram(gramTuple)
		if tmp == False: # does not exist, yet.
			# create a GRAM instance, and insert.
			self.gramDict[gramTuple] = 1
		else: # already exists
			self.gramDict[gramTuple] += 1

	# return the count corresponding to the given tuple
	def getGramCount(self, gramTuple):
		tmp = self.hasGram(gramTuple)
		if tmp == False:
			return 0
		return tmp.Count

	# return a probability indicating how much the tagList fits this NGRAM model
	def getFitness(self, tagList):
		pass

class GRAM:

	def __init__(self, gramTuple):
		self.Content = gramTuple
		self.Count = 1
	
	def __repr__(self):
		return ("This gram: "+str(self.Content)+" Count = "+str(self.Count))

pass

#################### Helper Functions ####################

def print_usage():
	sys.stderr.write("Usage: ./crossvalidation.py [train_file]\n")

# return list of POS tags, given rawLine (either Correct or Error)
def process_raw_line(rawLines):
	result = []
	tmp = rawLines.split();
	for i in tmp:
		tmp2 = i.split('#')
		result.append(tmp2[1])
	return result

# find out the most-likely redundant tag
def guess(tagList):
	# remove one of the tags

	# utilize NGRAM.getFitness to see how well it fits the models

	# combine those data from getFitness() => determine the position
	
	pass

pass

#################### Variables Declaration ####################

sectionSize = 593

pass

#################### Main Program ####################

##################
# check argument #
##################

if len(sys.argv) != 2:
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
"""
try:
	testFile = open(sys.argv[2], 'r')
except:
	sys.stderr.write("[Error] test data file: %s does not exist.\n" % sys.argv[2])
	sys.exit(1)
"""
print("files opened successfully!")

###############
# build NGRAM #
###############

# positive ones
uniGram = []
biGram = []
triGram = []
for i in range(5):
	tmp = NGRAM(1)
	uniGram.append(tmp)
	tmp = NGRAM(2)
	biGram.append(tmp)
	tmp = NGRAM(3)
	triGram.append(tmp)


"""
uniGram = NGRAM(1)
biGram = NGRAM(2)
triGram = NGRAM(3)
"""
# negative ones
uniGramNeg = []
biGramNeg = []
triGramNeg = []
for i in range(5):
	tmp = NGRAM(1)
	uniGramNeg.append(tmp)
	tmp = NGRAM(2)
	biGramNeg.append(tmp)
	tmp = NGRAM(3)
	triGramNeg.append(tmp)



"""
uniGramNeg = NGRAM(1)
biGramNeg = NGRAM(2)
triGramNeg = NGRAM(3)
"""
########################
# process the raw data #
########################



i = 0
for i in range(10000): # Won't reach it though

	# get lines from p2.*.tagged.txt two by two
	rawErrorLine = trainFile.readline()
	if rawErrorLine == "": # EOF reached
		break
	rawCorrectLine = trainFile.readline()

	# process the line, to get the POS tags sequence only
	negList = process_raw_line(rawErrorLine)
	posList = process_raw_line(rawCorrectLine)

	print i
	# build the NGRAMs
	part = i / sectionSize
	uniGram[part].build(posList)
	biGram[part].build(posList)
	triGram[part].build(posList)

	uniGramNeg[part].build(negList)
	biGramNeg[part].build(negList)
	triGramNeg[part].build(negList)
	

#############################
# calculate the total count #
# for each NGRAM instance   #
#############################

for i in range(5):
	uniGram[i].countAll()
	biGram[i].countAll()
	triGram[i].countAll()

	uniGramNeg[i].countAll()
	biGramNeg[i].countAll()
	triGramNeg[i].countAll()

	"""
	print uniGram[i].gramCount
	print biGram[i].gramCount
	print triGram[i].gramCount
	print "===================="
	print uniGramNeg[i].gramCount
	print biGramNeg[i].gramCount
	print triGramNeg[i].gramCount
	"""

###########################
# 5-fold cross validation #
###########################
for i in range(5):
	tmpUniGram = uniGram.combineModel(i)
	tmpBiGram = biGram.combineModel(i)
	tmpTriGram = triGram.combineModel(i)

	tmpUniGramNeg = uniGramNeg.combineModel(i)
	tmpBiGramNeg = biGramNeg.combineModel(i)
	tmpTriGramNeg = triGramNeg.combineModel(i)
	

###############
# close files #
###############
trainFile.close()

pass
