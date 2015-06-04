#!/bin/bash

# 1) get the sentences
cat p2.test.txt | cut -d $'\t' -f 2 > p2.test.sentences.txt

# 2) segment them

./stanford-segmenter-2015-04-20/segment.sh -k pku p2.test.sentences.txt UTF-8 0 > p2.test.segmented.txt

# 3) tag them

cp p2.test.segmented.txt stanford-postagger-full-2015-04-20/
cd stanford-postagger-full-2015-04-20/
./stanford-postagger.sh models/chinese-distsim.tagger p2.test.segmented.txt > p2.test.tagged.txt
cp p2.test.tagged.txt ../
rm p2.tagged.txt p2.test.segmented.txt
cd ../

