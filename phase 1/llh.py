# -*- coding: utf-8 -*-


#################### Import Modules ####################
import os
import sys


#################### Class Definitions ####################
class DataSet:

	def __init__(self):
		self.BiGramList = [] # list of BiGram instances
		self.TriGramList = [] # list of TriGram instances
		self.STriGramList = [] # list of special TriGram instances
		self.TotalBiGramCount = 0 # total count of all BiGram instances
		self.TotalTriGramCount = 0
		self.TotalSTriGramCount = 0

	def countAllBiGram(self): # calculate the total_count of all bigrams
		total = 0
		for bigram in self.BiGramList:
			total += bigram.Count
		self.TotalBiGramCount = total
		return total
	
	def countAllTriGram(self): # calculate the total_count of all trigrams
		total = 0
		for trigram in self.TriGramList:
			total += trigram.Count
		self.TotalTriGramCount = total
		return total

	def countAllSTriGram(self):
		total = 0
		for trigram in self.STriGramList:
			total += trigram.Count
		self.TotalSTriGramCount = total
		return total
	
	def hasBiGram(self, bigramTuple): # whether the bigram exists in this dataset
		for i in self.BiGramList:
			if i.Content == bigramTuple:
				return i
		return False
	
	def hasTriGram(self, trigramTuple): # whether the trigram exists in this dataset
		for i in self.TriGramList:
			if i.Content == trigramTuple:
				return i
		return False

	def hasSTriGram(self, trigramTuple):
		for i in self.STriGramList:
			if i.Content == trigramTuple:
				return i
		return False
	
	def addBigram(self, BiGramInstance): # given BiGramInstance => add it to dataset
		self.BiGramList.append(BiGramInstance)
	
	def addTrigram(self, TriGramInstance): # given TriGramInstance => add it to dataset
		self.TriGramList.append(TriGramInstance)

	def addSTrigram(self, TriGramInstance):
		self.STriGramList.append(TriGramInstance)
	
	def printBigram(self): # print all bigrams in this dataset
		for bigram in self.BiGramList:
			bigram.printBigram()
	
	def printTrigram(self): # print all trigrams in this dataset
		for trigram in self.TriGramList:
			trigram.printTrigram()

	def printSTrigram(self):
		for trigram in self.TriGramList:
			trigram.printTrigram()
	
	def getBigramCount(self, bigramTuple): # given bigram tuple => return exact count
		BiGramInstance = self.hasBiGram(bigramTuple)
		if BiGramInstance == False:
			return 0
		return BiGramInstance.Count
	
	def getBigramCountPrefix(self, bigramTuple):
		count = 0
		for i in self.BiGramList:
			if i.Content[0] == bigramTuple[0]:
				count += i.Count
		return count
	
	def getTrigramCount(self, trigramTuple): # given trigram tuple => return exact count
		TriGramInstance = self.hasTriGram(trigramTuple)
		if TriGramInstance == False:
			return 0
		return TriGramInstance.Count
	
	def getTrigramCountPrefix(self, trigramTuple):
		count = 0
		for i in self.TriGramList:
			if i.Content[0] == trigramTuple[0] and i.Content[1] == trigramTuple[1]:
				count += i.Count
		return count

	def getSTrigramCount(self, trigramTuple):
		TriGramInstance = self.hasSTriGram(trigramTuple)
		if TriGramInstance == False:
			return 0
		return TriGramInstance.Count

	def getSTrigramCountPrefix(self, trigramTuple):
		count = 0
		for i in self.STriGramList:
			if i.Content[0] == trigramTuple[0] and i.Content[2] == trigramTuple[2]:
				count += i.Count
		return count
	
	def getBiProb(self, bigramTuple): # given bigram tuple => return SMOOTHED probability
		count = self.getBigramCount(bigramTuple)
		# smoothing:
		numerator = float(count + LAMBDA)
		denominator = float(self.TotalBiGramCount + 45*45*LAMBDA)
		return float(numerator / denominator)
		#
		#return float(float(count) / float(self.TotalBiGramCount)) # this is not smooth-ed
	
	def getBiProbPrefix(self, bigramTuple):
		count = self.getBigramCountPrefix(bigramTuple)
		# smoothing:
		numerator = float(count + 45*LAMBDA)
		denominator = float(self.TotalBiGramCount + 45*45*LAMBDA)
		return float(numerator / denominator)
		#
		#return float(float(count) / float(self.TotalBiGramCount)) # this is not smooth-ed
	
	def getBiProbProd(self, tagslist): # return the product of probabilities of bigrams in tagslist
		numerator = float(1.0)
		for i in range(len(tagslist)-1):
			bigram = (tagslist[i], tagslist[i+1])
			numerator *= self.getBiProb(bigram)
		# return numerator
		# if the "return" above is activated,
		# the following piece of code is discarded.
		denominator = float(1.0)
		for i in range(1, len(tagslist)-1):
			bigram = (tagslist[i], tagslist[i+1])
			denominator *= self.getBiProbPrefix(bigram)
		if numerator == 0:
			# print "FUCK!!"
			return 0
		return float(numerator / denominator)
	
	def getTriProb(self, trigramTuple):
		count = self.getTrigramCount(trigramTuple)
		# smoothing:
		numerator = float(count + LAMBDA)
		denominator = float(self.TotalTriGramCount + 45*45*45*LAMBDA)
		return float(numerator / denominator)
		#
		#return float(float(count) / float(self.TotalTriGramCount)) # this is not smooth-ed
	
	def getTriProbPrefix(self, trigramTuple):
		count = self.getTrigramCountPrefix(trigramTuple)
		# smoothing:
		numerator = float(count + 45*LAMBDA)
		denominator = float(self.TotalTriGramCount + 45*45*45*LAMBDA)
		return float(numerator / denominator)
		#
		#return float(float(count) / float(self.TotalTriGramCount)) # this is not smooth-ed
	
	def getTriProbProd(self, tagslist):
		numerator = float(1.0)
		for i in range(len(tagslist)-2):
			trigram = (tagslist[i], tagslist[i+1], tagslist[i+2])
			numerator *= self.getTriProb(trigram)
		denominator = float(1.0)
		for i in range(1, len(tagslist)-2):
			trigram = (tagslist[i], tagslist[i+1], tagslist[i+2])
			denominator *= self.getTriProbPrefix(trigram)
		if numerator == 0:
			# print "FUCK!!!"
			return 0
		return float(numerator / denominator)

	def getSTriProb(self, trigramTuple):
		count = self.getSTrigramCount(trigramTuple)
		# smoothing:
		# numerator = float(count + LAMBDA)
		# denominator = float(self.TotalSTriGramCount + 45*45*45*LAMBDA)
		# return float(numerator / denominator)
		#
		return float(float(count) / float(self.TotalSTriGramCount)) # this is not smooth-ed

	def getSTriProbPrefix(self, trigramTuple):
		count = self.getSTrigramCountPrefix(trigramTuple)
		# smoothing:
		numerator = float(count + 45*LAMBDA)
		denominator = float(self.TotalSTriGramCount + 45*45*45*LAMBDA)
		return float(numerator / denominator)
		#
		#return float(float(count) / float(self.TotalSTriGramCount)) # this is not smooth-ed

	def getSTriProbProd(self, tagslist):
		numerator = float(1.0)
		for i in range(len(tagslist)-2):
			trigram = (tagslist[i], tagslist[i+1], tagslist[i+2])
			numerator *= self.getSTriProb(trigram)
		denominator = float(1.0)
		for i in range(1, len(tagslist)-2):
			trigram = (tagslist[i], tagslist[i+1], tagslist[i+2])
			denominator *= self.getSTriProbPrefix(trigram)
		if numerator == 0:
			# print "FUCK!!!!"
			return 0
		return float(numerator / denominator)
	
	pass

class BiGram:
	def __init__(self, bigramTuple):
		self.Content = bigramTuple
		self.Count = 1
	def printBigram(self):
		print "BiGram",
		print self.Content,
		print "Count = %d" % self.Count
	pass

class TriGram:
	def __init__(self, trigramTuple):
		self.Content = trigramTuple
		self.Count = 1
	def printTrigram(self):
		print "TriGram",
		print self.Content,
		print "Count = %d" % self.Count
	pass


#################### Helper Functions ####################

def print_usage():
	print "Usage: python llh.py [train_dataset_path] [held-out_dataset_path]"

def guess(tagslist): # goal: to take a guess this sentence is T or F.
	# tagslist: POS tags of a sentence in test data
	##### start B #####
	llhb = []
	llhb.append(PosDataset.getBiProbProd(tagslist)) # positive likelihood
	llhb.append(NegDataset.getBiProbProd(tagslist)) # negative likelihood
	##### start ST #####
	llhst = []
	llhst.append(PosDataset.getSTriProbProd(tagslist)) # positive likelihood
	llhst.append(NegDataset.getSTriProbProd(tagslist)) # negative likelihood
	##### start T #####
	tagslist.append("$") # for TriGram, we need 2 start-symbols and 2 end-symbols
	tagslist.insert(0, "^")
	llht = []
	llht.append(PosDataset.getTriProbProd(tagslist))
	llht.append(NegDataset.getTriProbProd(tagslist))

	llh1 = 0.7*llhb[0] + 0.1*llht[0] + 0.2*llhst[0]
	llh2 = 0.7*llhb[1] + 0.1*llht[1] + 0.2*llhst[1]

	if tagslist[len(tagslist)-2] == "uj":
		epsilon = EPSILON_S
	else:
		epsilon = EPSILON

	if llh1 > (llh2*epsilon):
		return True
	else:
		return False
	pass


#################### Variables Declaration ####################

EPSILON = float(1.5)
EPSILON_S = float(2.0)
LAMBDA = 0.01
# some lambda stuff?

#################### Main Program ####################

#############
# Arguments #
#############

# argument 1: path to training data file
# argument 2: path to held-out data file
# (arg0 is this .py file)

if len(sys.argv) < 3:
	print "Error: bad number of arguments"
	print_usage()
	sys.exit(1)

try:
	T_file = open(sys.argv[1], "r")
except:
	print "Error: cannot open training data file"
	sys.exit(1)

try:
	H_file = open(sys.argv[2], "r")
except:
	print "Error: cannot open held-out data file"
	sys.exit(1)

if len(sys.argv) >= 4:
	EPSILON = float(sys.argv[3])

if len(sys.argv) >= 5:
	EPSILON_S = float(sys.argv[4])

# lambda

####################
# build the bigram #
#   => from T_file #
####################

# initialize the variables
PosDataset = DataSet()
NegDataset = DataSet()

# loop for reading training data file
while True:
	linebuf = T_file.readline() # first line of each case: correctness
	# terminal condition
	if linebuf == "" or linebuf[0] == '\n': # if reaching EOF, get out of the loop
		break
	correctness = linebuf[0] # correctness = "0" or "1"
	linebuf = T_file.readline() # second line of each case: POS tags
	tagslist = linebuf.split()
	tagslist.pop(0) # the first and second items are "POS" and "tags:" ...
	tagslist.pop(0) # so we have to pop them
	tagslist.append("$") # add end-of-line symbol to POS tag list
	tagslist.insert(0, "^") # add start-of-line symbol to POS tag list

	# add bigrams
	for i in range(len(tagslist)-1):
		bigram = (tagslist[i], tagslist[i+1])
		if correctness == "0": # positive
			ret = PosDataset.hasBiGram(bigram)
			if ret != False: # the BiGram already exists in the Dataset
				ret.Count += 1
			else: # the BiGram doesn't exist, we'll have to create it
				newbigram = BiGram(bigram)
				PosDataset.addBigram(newbigram)
		elif correctness == "1": # negative
			ret = NegDataset.hasBiGram(bigram)
			if ret != False:
				ret.Count += 1
			else:
				newbigram = BiGram(bigram)
				NegDataset.addBigram(newbigram)

	# add special trigrams
	for i in range(len(tagslist)-2):
		trigram = (tagslist[i], tagslist[i+1], tagslist[i+2])
		if correctness == "0":
			ret = PosDataset.hasSTriGram(trigram)
			if ret != False: # the STrigram instance already in dataset
				ret.Count += 1
			else: # create one special trigram
				newtrigram = TriGram(trigram)
				PosDataset.addSTrigram(newtrigram)
		elif correctness == "1":
			ret = NegDataset.hasSTriGram(trigram)
			if ret != False: # already exists
				ret.Count += 1
			else:
				newtrigram = TriGram(trigram)
				NegDataset.addSTrigram(newtrigram)

	# add trigrams
	tagslist.append("$") # there are supposed to be 2 end-symbols and 2 start-symbols.
	tagslist.insert(0, "^")
	for i in range(len(tagslist)-2):
		trigram = (tagslist[i], tagslist[i+1], tagslist[i+2])
		if correctness == "0": # positive
			ret = PosDataset.hasTriGram(trigram)
			if ret != False:
				ret.Count += 1
			else: # the TriGram doesn't exist in the dataset, add it!
				newtrigram = TriGram(trigram)
				PosDataset.addTrigram(newtrigram)
		elif correctness == "1": # negative
			ret = NegDataset.hasTriGram(trigram)
			if ret != False:
				ret.Count += 1
			else:
				newtrigram = TriGram(trigram)
				NegDataset.addTrigram(newtrigram)

	pass # that's is? this while-loop?


############################
# Now we can calculate the #
# TotalCount of DataSet    #
############################

PosDataset.countAllBiGram()
NegDataset.countAllBiGram()
PosDataset.countAllTriGram()
NegDataset.countAllTriGram()
PosDataset.countAllSTriGram()
NegDataset.countAllSTriGram()


#############################
# Print to check if bigrams #
# are added succesfully.    #
# (usually commented)       #
#############################
"""
PosDataset.printBigram()
print ""
NegDataset.printBigram()
"""

#################
# Held-out Data #
#     => H_file #
#################

while True:
	linebuf = H_file.readline()
	if linebuf == "": # reaching EOF
		break
	tagslist = linebuf.split() # get POS tags
	tagslist.pop(0) # discard "POS"
	tagslist.pop(0) # discard "tags:"
	tagslist.append("$") # add end-of-line symbol to POS tag list
	tagslist.insert(0, "^") # add start-of-line symbol to POS tag list
	# guess() function!
	if guess(tagslist) == True:
		print 0
	else:
		print 1
	pass



###################
# close the files #
###################

T_file.close()
H_file.close()




