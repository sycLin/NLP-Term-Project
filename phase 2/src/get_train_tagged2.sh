#!/bin/bash

SOURCE_FILE='train_cut.c'

# compile the train_cut.c for scws
INC_FLAG='-I/usr/local/scws/include/scws/'
LIB_FLAG='-L/usr/local/scws/lib/'
LINK_FLAG='-lscws'
OUTPUT_NAME='a.out'

gcc $INC_FLAG $LIB_FLAG $SOURCE_FILE $LINK_FLAG -o $OUTPUT_NAME

# tag the training data

./$OUTPUT_NAME < ../data/p2.train.sentences.txt > ../data/p2.train.tagged.txt

rm -f $OUTPUT_NAME