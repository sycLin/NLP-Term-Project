# -*- coding: utf-8 -*-


#################### Import Modules ####################
import os
import sys
import Levenshtein


#################### Variable Setups ####################
trainFilePath = "240365_p1.train.txt"


#################### Class Definition ####################
class DataEntry:
	def __init__(self, s_id, s_id_num, s_correct, s_content):
		self.ID = s_id # the id of that sentence
		self.NID = s_id_num # the numerical id
		if s_correct == "0": # True => correct, False => incorrect.
			self.Correctness = True
		else:
			self.Correctness = False
		self.Content = s_content # the sentence itself
		self.MyPair = -1;
	def __str__(self):
		return "ID: %s, Correct: %r, %s" % (self.ID, self.Correctness, self.Content)
	
	def isCorrect(self):
		return self.Correctness

	def find_pair(self):
		global DataList, Distance
		min_dist = float("INF") # infinity constant in python.
		my_pair = -1
		for i in range(len(DataList)):
			cur_dist = get_distance(self.NID, i)
			if cur_dist != 0: # not self
				if cur_dist < min_dist:
					min_dist = cur_dist
					my_pair = i
		self.MyPair = my_pair


#################### Helper Functions ####################
def get_distance(phrase_num1, phrase_num2):
	global Distance
	# self distance? Of course zero!
	if phrase_num1 == phrase_num2:
		return 0
	# make sure phrase_num1 is smaller than phrase_num2
	if phrase_num1 > phrase_num2:
		phrase_num1, phrase_num2 = phrase_num2, phrase_num1
	return Distance[phrase_num1][phrase_num2-phrase_num1-1]




#################### START OF THE PROGRAM ####################

################
# opening file #
################

# f is the file object
try:
	f = open(trainFilePath, "r")
except:
	print "Couldn't open file: %s" % trainFilePath
	sys.exit(1)

###################
# initializing DS #
###################

# DataList stores the DataEntry(-ies)
DataList = []

#####################
# reading data file #
#####################

lineCount = 0
lineBuf = f.readline()
while lineBuf != "" :
	# print "Got the %d-th line!" % (lineCounter+1)
	# parse the line and save with DataEntry class
	# print "\tparsing..."
	elements = lineBuf.split() # default: split by white-space => there shall be 3 elements
	# processing for encoding problem
	elements[0] = unicode(elements[0], "utf-8") # ID
	elements[1] = unicode(elements[1], "utf-8") # T/F
	elements[2] = unicode(elements[2], "utf-8") # Content
	# create DataEntry object and append to DataList
	tmp = DataEntry(elements[0], lineCount, elements[1], elements[2])
	lineCount += 1
	DataList.append(tmp)
	# finish parsing
	lineBuf = f.readline()

#######################
# check DataList size #
#######################

"""
print "#"*47
print "finish reading whole training data file"
print "the size of the DataList = %d" % len(DataList)
print "#"*47
"""


#############################
# Calculating Edit Distance #
#############################

Distance = []

for i in range(len(DataList)):
	tmp_list = []
	for j in range(i+1, len(DataList)):
		tmp = Levenshtein.distance(DataList[i].Content, DataList[j].Content)
		tmp_list.append(tmp)
	Distance.append(tmp_list)


################################
# Applying Hungarian Algorithm #	NO, we change out method.
# Find the best assignment     #	Just find the min-value.
################################

# find the pairs
for data_entry in DataList:
	data_entry.find_pair()

# output the pairs

for i in DataList:
	j = i.MyPair # j is i's pair
	if int(i.NID) < int(DataList[j].NID): # in order not to print each pair twice
		# print "%d %d" % (i.NID, DataList[j].NID)
		if i.Correctness == True:
			print 0
		else:
			print 1
		print i.Content.encode("utf-8")	
		if DataList[j].Correctness == True:
			print 0
		else:
			print 1
		print DataList[j].Content.encode("utf-8")
		print ""
		







