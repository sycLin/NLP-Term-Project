#!/bin/bash

# check argument

if [ $# != 1 ]; then
	echo "Usage: $0 <scws|stanford>"
	exit 1
elif [ $1 == "scws" ]; then
	TRAIN_TAG_SCRIPT='get_train_tagged2.sh'
	TEST_TAG_SCRIPT='get_test_tagged2.sh'
elif [ $1 == "stanford" ]; then
	TRAIN_TAG_SCRIPT='get_train_tagged.sh'
	TEST_TAG_SCRIPT='get_test_tagged.sh'
else
	echo "Usage: $0 <scws|stanford>"
	exit 1
fi

# tag the training data
cd src
./$TRAIN_TAG_SCRIPT
./$TEST_TAG_SCRIPT
cd ..

# set variables (files)

MAIN_FILE='./src/main.py'
TRAIN_FILE='./data/p2.train.tagged.txt'
TEST_FILE='./data/p2.test.tagged.txt'

# check if the directory testResult/ exists or not
if ! [ -d testResult/ ];then
	mkdir testResult
fi

# run it!!!

$MAIN_FILE $TRAIN_FILE $TEST_FILE > testResult/answer.txt

