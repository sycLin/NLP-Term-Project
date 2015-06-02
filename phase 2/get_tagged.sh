#!/bin/bash

# 1) get the sentences
cat p2.train.txt | cut -d $'\t' -f 2,3 | tr $'\t' $'\n' > p2.sentences.txt

# 2) segment them

./stanford-segmenter-2015-04-20/segment.sh -k pku demo_sentences.txt UTF-8 0 > p2.segmented.txt

# 3) tag them

cp p2.segmented.txt stanford-postagger-full-2015-04-20/
cd stanford-postagger-full-2015-04-20/
./stanford-postagger.sh models/chinese-distsim.tagger p2.segmented.txt > p2.tagged.txt
cp p2.tagged.txt ../
rm p2.tagged.txt p2.segmented.txt
cd ../

