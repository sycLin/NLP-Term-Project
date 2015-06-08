#!/bin/bash

# files required
MAIN_FILE="./src/main.py"

# check those files required
if ! [ -f $MAIN_FILE ]; then
	echo "Error: $MAIN_FILE does not exist!"
	exit 1
fi

# if ./cvResult/ firectory not exist, create it
if ! [ -d ./cvResult/ ]; then
	mkdir cvResult
fi

# run 5 times
for i in `seq 5`
do
	$MAIN_FILE ./data/tmp_train_$i.txt ./data/tmp_test_$i.txt > ./cvResult/tmp_answer_$i.txt
done
