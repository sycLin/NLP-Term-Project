#!/bin/bash

FILENAME='../data/answer_for_training_data.txt'

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

# rename the files

mv tmp_portion_1.txt ../data/answer_for_training_data_1.txt
mv tmp_portion_2.txt ../data/answer_for_training_data_2.txt
mv tmp_portion_3.txt ../data/answer_for_training_data_3.txt
mv tmp_portion_4.txt ../data/answer_for_training_data_4.txt
mv tmp_portion_5.txt ../data/answer_for_training_data_5.txt
