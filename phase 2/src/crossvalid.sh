#!/bin/bash

# files required
MAIN_FILE="main.py"
TRAIN_FILE="p2.train.txt"

# check those files required
if ! [ -f $MAIN_FILE ]; then
	echo "Error: $MAIN_FILE does not exist!"
	exit 1
fi

if ! [ -f $TRAIN_FILE ]; then
	echo "Error: $TRAIN_FILE does not exist!"
	exit 1
fi

# if the training data not tagged, tag it!
if ! [ -f p2.train.tagged.txt ]; then
	./get_train_tagged.sh
fi

#slice the training data into 5 portions
./slice.sh

# run 5 times
for i in `seq 5`
do
	./$MAIN_FILE tmp_train_$i.txt tmp_test_$i.txt > tmp_answer_$i.txt
done

