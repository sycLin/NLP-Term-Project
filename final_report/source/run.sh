#!/bin/bash

# check argument

if [ $# != 1 ]; then
	echo "Usage: $0 <scws|stanford>"
	exit 1
elif [ $1 == "scws" ]; then
	TRAIN_FILE='./data/p2.train.tagged.scws.txt'
	TEST_FILE='./data/p2.test.tagged.scws.txt'
elif [ $1 == "stanford" ]; then
	TRAIN_FILE='./data/p2.train.tagged.stanford.txt'
	TEST_FILE='./data/p2.test.tagged.stanford.txt'
else
	echo "Usage: $0 <scws|stanford>"
	exit 1
fi


# set variables (files)

MAIN_FILE='./src/main.py'

# check if the directory testResult/ exists or not
if ! [ -d testResult/ ];then
	mkdir testResult
fi

# run it!!!

$MAIN_FILE $TRAIN_FILE $TEST_FILE > testResult/answer.txt

