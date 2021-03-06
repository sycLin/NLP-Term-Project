#!/bin/bash

FILENAME='train_only_correctness_and_pos.txt'

# test if the file exist
if ! [ -f $FILENAME ]; then
	echo "Error: file $FILENAME does not exist!"
fi

linecount=`wc -l $FILENAME | tr -s ' ' | cut -d ' ' -f 2`


portion=$((linecount / 5))

# make $portion a even number
rem=$(($portion % 2))
if ! [ $rem == 0 ]; then
	portion=$(($portion + 1))
fi


# create 5 portions of original file
head -$portion $FILENAME > tmp_portion_1.txt
tail -$(($linecount - $portion)) $FILENAME > tmp_tmp.txt
head -$portion tmp_tmp.txt > tmp_portion_2.txt
linecount=`wc -l tmp_tmp.txt | tr -s ' ' | cut -d ' ' -f 2`
tail -$(($linecount - $portion)) tmp_tmp.txt > tmp_tmp2.txt
head -$portion tmp_tmp2.txt > tmp_portion_3.txt
linecount=`wc -l tmp_tmp2.txt | tr -s ' ' | cut -d ' ' -f 2`
tail -$(($linecount - $portion)) tmp_tmp2.txt > tmp_tmp.txt
head -$portion tmp_tmp.txt > tmp_portion_4.txt
linecount=`wc -l tmp_tmp.txt | tr -s ' ' | cut -d ' ' -f 2`
tail -$(($linecount - $portion)) tmp_tmp.txt > tmp_portion_5.txt
# delete the temporary files
rm -f tmp_tmp.txt tmp_tmp2.txt

# create the FIRST TEST: using first 1/5 as held-out dataset
cat tmp_portion_1.txt > tmp_test_1.txt
cat tmp_portion_2.txt > tmp_train_1.txt
cat tmp_portion_3.txt >> tmp_train_1.txt
cat tmp_portion_4.txt >> tmp_train_1.txt
cat tmp_portion_5.txt >> tmp_train_1.txt

# create the SECOND TEST: using second 1/5 as held-out dataset
cat tmp_portion_1.txt > tmp_train_2.txt
cat tmp_portion_2.txt > tmp_test_2.txt
cat tmp_portion_3.txt >> tmp_train_2.txt
cat tmp_portion_4.txt >> tmp_train_2.txt
cat tmp_portion_5.txt >> tmp_train_2.txt

# create the THIRD TEST: using third 1/5 as held-out dataset
cat tmp_portion_1.txt > tmp_train_3.txt
cat tmp_portion_2.txt >> tmp_train_3.txt
cat tmp_portion_3.txt > tmp_test_3.txt
cat tmp_portion_4.txt >> tmp_train_3.txt
cat tmp_portion_5.txt >> tmp_train_3.txt

# create the FOURTH TEST: using fourth 1/5 as held-out dataset
cat tmp_portion_1.txt > tmp_train_4.txt
cat tmp_portion_2.txt >> tmp_train_4.txt
cat tmp_portion_3.txt >> tmp_train_4.txt
cat tmp_portion_4.txt > tmp_test_4.txt
cat tmp_portion_5.txt >> tmp_train_4.txt

# create the FIRST TEST: using first 1/5 as held-out dataset
cat tmp_portion_1.txt > tmp_train_5.txt
cat tmp_portion_2.txt >> tmp_train_5.txt
cat tmp_portion_3.txt >> tmp_train_5.txt
cat tmp_portion_4.txt >> tmp_train_5.txt
cat tmp_portion_5.txt > tmp_test_5.txt

# test data should not contain T/F values (0 or 1)
for i in `seq 5`
do
	cat tmp_test_${i}.txt | grep "POS" > tmp_tmp_tmp.txt
	cat tmp_test_${i}.txt | grep -E "0|1" > tmp_answer_${i}.txt
	mv tmp_tmp_tmp.txt tmp_test_${i}.txt
done
rm -f tmp_tmp_tmp.txt

# delete the temporary files
rm -f tmp_portion_1.txt
rm -f tmp_portion_2.txt
rm -f tmp_portion_3.txt
rm -f tmp_portion_4.txt
rm -f tmp_portion_5.txt





