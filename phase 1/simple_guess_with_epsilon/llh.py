# -*- coding: utf-8 -*-


#################### Import Modules ####################
import os
import sys


#################### Class Definitions ####################
class DataSet:
	def __init__(self):
		self.BiGramList = [] # list of BiGram instances
		self.TotalCount = 0 # total count of all BiGram instances
	def countAll(self): # calculate the total_count of all bigrams
		total = 0
		for bigram in self.BiGramList:
			total += bigram.Count
		self.TotalCount = total
		return total
	def hasBiGram(self, bigramTuple): # whether the bigram exists in this dataset
		for i in self.BiGramList:
			if i.Content == bigramTuple:
				return i
		return False
	def addBigram(self, BiGramInstance): # given BiGramInstance => add it to dataset
		self.BiGramList.append(BiGramInstance)
	def printBigram(self): # print all bigrams in this dataset
		for bigram in self.BiGramList:
			bigram.printBigram()
	def getCount(self, bigramTuple): # given bigram tuple => return exact count
		BiGramInstance = self.hasBiGram(bigramTuple)
		if BiGramInstance == False:
			return 0
		return BiGramInstance.Count
	def getProb(self, bigramTuple): # given bigram tuple => return SMOOTHED probability
		count = self.getCount(bigramTuple)#+1 # mind this "+1", it's smoothing.
		return float(float(count) / float(self.TotalCount))
	def getProbProd(self, tagslist): # return the product of probabilities of bigrams in tagslist
		product = float(1.0)
		for i in range(len(tagslist)-1):
			bigram = (tagslist[i], tagslist[i+1])
			product *= self.getProb(bigram)
		return product
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


#################### Helper Functions ####################

def print_usage():
	print "Usage: python llh.py [train_dataset_path] [held-out_dataset_path]"

def guess(tagslist): # goal: to take a guess this sentence is T or F.
	# tagslist: POS tags of a sentence in test data
	llh1 = PosDataset.getProbProd(tagslist) # positive likelihood
	llh2 = NegDataset.getProbProd(tagslist) # negative likelihood
	# let's do a simple guessing: simply compare the llh1 and llh2
	if tagslist[len(tagslist)-1] == "uj":
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
	if linebuf == "": # if reaching EOF, get out of the loop
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
	
	pass # that's is? this while-loop?


############################
# Now we can calculate the #
# TotalCount of DataSet    #
############################

PosDataset.countAll()
NegDataset.countAll()


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




