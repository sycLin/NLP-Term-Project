#!/bin/bash

# 1) get the sentences
cat ../data/p2.test.txt | cut -d $'\t' -f 2 > ../data/p2.test.sentences.txt

# 2) segment them

../stanford-segmenter-2015-04-20/segment.sh -k pku ../data/p2.test.sentences.txt UTF-8 0 > ../data/p2.test.segmented.txt

# 3) tag them

cp ../data/p2.test.segmented.txt ../stanford-postagger-full-2015-04-20/
cd ../stanford-postagger-full-2015-04-20/
./stanford-postagger.sh models/chinese-distsim.tagger p2.test.segmented.txt > p2.test.tagged.txt
cp p2.test.tagged.txt ../data/
rm p2.test.tagged.txt p2.test.segmented.txt
cd ../src/

