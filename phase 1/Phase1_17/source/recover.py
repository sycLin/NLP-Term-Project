# -*- coding: utf-8 -*-


#################### Import Modules ####################
import os
import sys


R_FILE = open("tmp_result.txt", "r")
T_FILE = open("p1.test.txt", "r")

while True:
	linebuf1 = T_FILE.readline()
	if linebuf1 == "":
		break
	linebuf2 = R_FILE.readline()
	List1 = linebuf1.split()
	List2 = linebuf2.split()
	print "%s\t%s" % (List1[0], List2[0])
