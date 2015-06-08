#!/bin/bash

# 1) get the sentences
cat ../data/p2.train.txt | cut -d $'\t' -f 2,3 | tr $'\t' $'\n' > ../data/p2.train.sentences.txt

# 2) segment them

../stanford-segmenter-2015-04-20/segment.sh -k pku ../data/p2.train.sentences.txt UTF-8 0 > ../data/p2.train.segmented.txt

# 3) tag them

cp ../data/p2.train.segmented.txt ../stanford-postagger-full-2015-04-20/
cd ../stanford-postagger-full-2015-04-20/
./stanford-postagger.sh models/chinese-distsim.tagger p2.train.segmented.txt > p2.train.tagged.txt
cp p2.train.tagged.txt ../data/
rm p2.train.tagged.txt p2.train.segmented.txt
cd ../src/

