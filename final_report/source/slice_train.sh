#!/bin/bash

if [ $1 == 'scws' ]; then
	FILENAME='../data/p2.train.tagged.scws.txt'
else
	FILENAME='../data/p2.train.tagged.stanford.txt'
fi

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
cat tmp_portion_1.txt > XDDTMP.txt
awk 'NR % 2 == 1' XDDTMP.txt > tmp_test_1.txt
cat tmp_portion_2.txt > tmp_train_1.txt
cat tmp_portion_3.txt >> tmp_train_1.txt
cat tmp_portion_4.txt >> tmp_train_1.txt
cat tmp_portion_5.txt >> tmp_train_1.txt

# create the SECOND TEST: using second 1/5 as held-out dataset
cat tmp_portion_1.txt > tmp_train_2.txt
cat tmp_portion_2.txt > XDDTMP.txt
awk 'NR % 2 == 1' XDDTMP.txt > tmp_test_2.txt
cat tmp_portion_3.txt >> tmp_train_2.txt
cat tmp_portion_4.txt >> tmp_train_2.txt
cat tmp_portion_5.txt >> tmp_train_2.txt

# create the THIRD TEST: using third 1/5 as held-out dataset
cat tmp_portion_1.txt > tmp_train_3.txt
cat tmp_portion_2.txt >> tmp_train_3.txt
cat tmp_portion_3.txt > XDDTMP.txt
awk 'NR % 2 == 1' XDDTMP.txt > tmp_test_3.txt
cat tmp_portion_4.txt >> tmp_train_3.txt
cat tmp_portion_5.txt >> tmp_train_3.txt

# create the FOURTH TEST: using fourth 1/5 as held-out dataset
cat tmp_portion_1.txt > tmp_train_4.txt
cat tmp_portion_2.txt >> tmp_train_4.txt
cat tmp_portion_3.txt >> tmp_train_4.txt
cat tmp_portion_4.txt > XDDTMP.txt
awk 'NR % 2 == 1' XDDTMP.txt > tmp_test_4.txt
cat tmp_portion_5.txt >> tmp_train_4.txt

# create the FIRST TEST: using first 1/5 as held-out dataset
cat tmp_portion_1.txt > tmp_train_5.txt
cat tmp_portion_2.txt >> tmp_train_5.txt
cat tmp_portion_3.txt >> tmp_train_5.txt
cat tmp_portion_4.txt >> tmp_train_5.txt
cat tmp_portion_5.txt > XDDTMP.txt
awk 'NR % 2 == 1' XDDTMP.txt > tmp_test_5.txt

# delete the temporary files
rm -f tmp_portion_1.txt
rm -f tmp_portion_2.txt
rm -f tmp_portion_3.txt
rm -f tmp_portion_4.txt
rm -f tmp_portion_5.txt
rm -f XDDTMP.txt

# move the files to ../data
mv tmp_test_*.txt ../data/
mv tmp_train_*.txt ../data/
