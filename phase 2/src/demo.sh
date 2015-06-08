#!/bin/bash


echo "Step 1) we grap a few sentences from p2.train.txt."

head -10 p2.train.txt | cut -d $'\t' -f 2,3 | tr $'\t' $'\n' > demo_sentences.txt

echo "Step 2) slice the sentences with Stanford segmenter."

./stanford-segmenter-2015-04-20/segment.sh -k pku demo_sentences.txt UTF-8 0 > demo_segmented.txt

echo "Step 3) Tag the sliced sentences with Stanford POS Tagger."

cp demo_segmented.txt stanford-postagger-full-2015-04-20/
cd stanford-postagger-full-2015-04-20/
./stanford-postagger.sh models/chinese-distsim.tagger demo_segmented.txt > demo_tagged.txt
cp demo_tagged.txt ../
rm -f demo_tagged.txt demo_segmented.txt
cd ..

