#!/usr/bin/python
# -*- coding: utf-8 -*-

#################### Import Modules ####################
import os
import sys

#################### Class Definitions ####################

class NGRAM:
	def __init__(self):
		pass
	
	# build up the n-gram model from lines of data
	def build(self, linesOfData):
		# add start symbols and end symbols
		# process the linesOfData
		pass

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
# close files #
###############
trainFile.close()
testFile.close()

pass
