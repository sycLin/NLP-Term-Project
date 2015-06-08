#!/usr/bin/python
# -*- coding: utf-8 -*-

#################### Import Modules ####################
import sys
import os

#################### Helper Functions ####################

# if the arguments are incorrect, print to let user know the usage
def print_usage():
	sys.stderr.write("Usage: ./evaluation.py [stdAnswer] [yourAnswer]\n")

# calculate the f1 score, given correct sequence and the sequence answered
def get_f1_score(corStart, corEnd, yourStart, yourEnd):

	# get the length of the two sequences
	corLen = corEnd - corStart + 1 # the length of correct sequence
	yourLen = yourEnd - yourStart + 1 # the length of your sequence
	
	# find overlap
	overlapCount = 0
	i = yourStart
	while i <= yourEnd:
		if i >= corStart and i <= corEnd:
			overlapCount += 1
		i += 1
	
	# calculate RECALL and PRECISION according to equations provided by TAs
	recall = float(float(overlapCount) / float(corLen))
	prec = float(float(overlapCount) / float(yourLen))
	try:
		result = float(2*recall*prec/(recall+prec))
	except ZeroDivisionError:
		result = float(0.0)
	if result == 0.0:
		print "fuck..."
	else:
		print "f1_score = %f" % result
	return result

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
	stdAnswer = open(sys.argv[1], 'r')
except:
	sys.stderr.write("[Error] the file %s does not exist!" % sys.argv[1])
	sys.exit(1)
try:
	yourAnswer = open(sys.argv[2], 'r')
except:
	sys.stderr.write("[Error] the file %s does not exist!" % sys.argv[2])
	sys.exit(1)

########################
# calculate f1_score's #
# and average them     #
########################

finalScore = 0.0
caseCount = 0
print "aloha"
while True:
	
	# read the files
	lineBuf1 = stdAnswer.readline()
	lineBuf2 = yourAnswer.readline()
	
	# check if EOF encountered
	if lineBuf1 == "" or lineBuf2 == "": # encounter EOF
		break
	tmpList1 = lineBuf1.split()
	tmpList2 = lineBuf2.split()
	if len(tmpList1) != 2 or len(tmpList2) != 2:
		sys.stderr.write("[Error] file format error. Not <number><tab><number>\n")
		sys.exit(1)
	finalScore += get_f1_score(int(tmpList1[0]), int(tmpList1[1]), int(tmpList2[0]), int(tmpList2[1]))
	caseCount += 1
	# print "--- Now (finalScore, caseCount) = (%f, %d)" % (finalScore, caseCount)
	pass

print "Of all %d cases, the average F1 score: %f" % (caseCount, float(finalScore / float(caseCount)))

