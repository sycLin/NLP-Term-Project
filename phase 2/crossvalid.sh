#!/bin/bash

# files required
MAIN_FILE="./src/main.py"
TRAIN_FILE="./data/p2.train.txt"

# check those files required
if ! [ -f $MAIN_FILE ]; then
	echo "Error: $MAIN_FILE does not exist!"
	exit 1
fi

if ! [ -f $TRAIN_FILE ]; then
	echo "Error: $TRAIN_FILE does not exist!"
	exit 1
fi

# run 5 times
for i in `seq 5`
do
	$MAIN_FILE ./data/tmp_train_$i.txt ./data/tmp_test_$i.txt > ./data/tmp_answer_$i.txt
done

