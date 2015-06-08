#!/bin/bash

MAIN_FILE='./src/main.py'
TRAIN_FILE='./data/p2.train.tagged.txt'
TEST_FILE='./data/p2.test.tagged.txt'

# check if the directory testResult/ exists or not
if ! [ -d testResult/ ];then
	mkdir testResult
fi

# run it!!!

$MAIN_FILE $TRAIN_FILE $TEST_FILE > testResult/answer.txt

