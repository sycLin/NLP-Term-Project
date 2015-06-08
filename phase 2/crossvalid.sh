#!/bin/bash

# check argument

if [ $# != 1 ]; then
	echo "Usage: $0 <scws|stanford>"
	exit 1
elif [ $1 == "scws" ]; then
	TRAIN_FILE='./data/p2.train.tagged.scws.txt'
elif [ $1 == "stanford" ]; then
	TRAIN_FILE='./data/p2.train.tagged.stanford.txt'
else
	echo "Usage: $0 <scws|stanford>"
	exit 1
fi

# slice the training data

cd src
./slice_train.sh $1
cd ..

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
	$MAIN_FILE ./data/tmp_train_$i.txt ./data/tmp_test_$i.txt > ./cvResult/tmp_answer_$i.txt 2>./cvResult/tmp_likelyhood_$i.txt
done

# evaluate my answer

./src/evaluation.py ./data/answer_for_training_data_1.txt ./cvResult/tmp_answer_1.txt > ./cvResult/result_1.txt
./src/evaluation.py ./data/answer_for_training_data_2.txt ./cvResult/tmp_answer_2.txt > ./cvResult/result_2.txt
./src/evaluation.py ./data/answer_for_training_data_3.txt ./cvResult/tmp_answer_3.txt > ./cvResult/result_3.txt
./src/evaluation.py ./data/answer_for_training_data_4.txt ./cvResult/tmp_answer_4.txt > ./cvResult/result_4.txt
./src/evaluation.py ./data/answer_for_training_data_5.txt ./cvResult/tmp_answer_5.txt > ./cvResult/result_5.txt

