# -*- coding: utf-8 -*-


#################### Import Modules ####################
import os
import sys

#################### Helper Functions ####################
def print_usage():
	print "Usage: python check.py [path_to_my_answer] [path_to_standard_answer]"


#################### Files to Open ####################

# argument 1: path to my_answer file
# argument 2: path to standard_answer file
# (arg0 is this .py file)

if len(sys.argv) != 3:
	print "Error: bad number of arguments"
	print_usage()
	sys.exit(1)

try:
	M_file = open(sys.argv[1], "r")
except:
	print "Error: cannot open my answer file: %s" % sys.argv[1]
	sys.exit(1)

try:
	S_file = open(sys.argv[2], "r")
except:
	print "Error: cannot open standard answer file: %s" % sys.argv[2]
	sys.exit(1)

# statistics = [correct_pos, correct_neg, total_pos, total_neg]
statistics = [0, 0, 0, 0]

while True:
	linebuf1 = M_file.readline()
	if linebuf1 == "" or linebuf1 == "\n":
		break
	linebuf2 = S_file.readline()
	if linebuf2 == "" or linebuf2 == "\n":
		break
	if linebuf2[0] == "0": # standard answer is positive
		statistics[2] += 1 # increase total_pos
		if linebuf1 == linebuf2: # answer correctly
			statistics[0] += 1
	else: # standard answer is negative
		statistics[3] += 1
		if linebuf1 == linebuf2:
			statistics[1] += 1
	pass

# output the result
print statistics
recall = float(statistics[1]) / float(statistics[3])
# precision = float(statistics[0] + statistics[1]) / float(statistics[2] + statistics[3]) => Ben Chou got it wrong
precision = float(statistics[1]) / float(statistics[2]-statistics[0]+statistics[1])
print "Correctness:\t",
print float(statistics[0] + statistics[1]) / float(statistics[2] + statistics[3])
print "F1_Score:\t",
print float(float(2*recall*precision) / float(recall+precision))
print ""
