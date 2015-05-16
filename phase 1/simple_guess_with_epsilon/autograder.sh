#!/bin/bash

SFILE='benchou.sh'
PFILE='llh.py'
CFILE='check.py'

# get epsilon from argument
EPSILON='1.5'
EPSILON_s='2.0'
if [ $(($#)) -gt 0 ]; then
	EPSILON=$1
fi
if [ $(($#)) -gt 1 ];then
	EPSILON_s=$2
fi


if ! [ -f $SFILE ]; then
	echo "Error: file $SFILE does not exist!"
	exit 1
fi

if ! [ -f $PFILE ]; then
	echo "Error: file $PFILE does not exist!"
	exit 1
fi

if ! [ -f $CFILE ]; then
	echo "Error: file $CFILE does not exist!"
	exit 1
fi

# execute the SFLIE
chmod a+x $SFILE
./$SFILE

# check if the data is sliced correctly
for i in `seq 5`
do
	if ! [ -f tmp_test_${i}.txt ];then
		echo "Error: $SFILE didn't slice the data into 5 pieces!"
		exit 1
	fi
	if ! [ -f tmp_train_${i}.txt ];then
		echo "Error: $SFILE didn't slice the data into 5 pieces!"
		exit 1
	fi
done

# run the PFILE with tmp_train_{1~5}.txt and tmp_test_{1~5}.txt
for i in `seq 5`
do
	python $PFILE tmp_train_${i}.txt tmp_test_${i}.txt $EPSILON $EPSILON_s > tmp_my_answer_${i}.txt
done

# check the answers: compare tmp_my_answer_{1~5} with tmp_answer_{1~5}.txt
echo "==================== EPSILON: ${EPSILON} EPSILON_s: ${EPSILON_s} ====================" >> autograder_log
for i in `seq 5`
do
	python check.py tmp_my_answer_${i}.txt tmp_answer_${i}.txt >> autograder_log
done

tail -21 autograder_log

# clean-up
rm -f tmp_*.txt
