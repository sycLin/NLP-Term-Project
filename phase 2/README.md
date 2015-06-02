#Phase 2

given a sentence with redundant words, find out where the redundancy is.
(sentences are all in simplified Chinese)

---

## Tools

+ Stanford Segmenter
+ Stanford POS Tagger

## Stanford Segmenter

> How to use it:

```sh
$./segment.sh [-k] [ctb|pku] <filename> <encoding> <size>
```

> -k: keep all white spaces in the input

> ctb: chinese penn treebank

> pku: beijing univ.

> filename: file that you want to segment. each line is a sentence.

> encoding: must be a character encoding name known by JAVA. (ex. UTF-8, GB18030)

> size: size of the n-best list. (0: print the best without probabilities)

## Stanford POSTagger

> How to use it:

```sh
$./stanford-postagger.sh <model> <input-file>
```

> models: can be found in models/

> input-file: sentences to be POS tagged


