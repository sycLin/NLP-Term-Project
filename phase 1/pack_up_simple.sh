#!/bin/bash

DIR_NAME='simple_guess_with_epsilon'

mkdir $DIR_NAME
cp autograder.sh benchou.sh check.py llh.py train_only_correctness_and_pos.txt $DIR_NAME
zip -r ${DIR_NAME}.zip $DIR_NAME
rm -rf $DIR_NAME