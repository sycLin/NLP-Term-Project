#Phase 1 Presentation

##Our Source Code

+ autorun.sh
+ 240365\_p1.train.txt
+ nlp.py
+ train\_cut.c
+ p1.test.txt
+ llh.py
+ recover.py

##What do they do

|Files|Functionality|
|:----|:-----------|
|autorun.sh|as a autograder?|
|240365\_p1.train.txt|the training data|
|nlp.py|finding pairs?|
|train\_cut.c|from sentences to POS tags?|
|p1.test.txt|the test data|
|llh.py|learning from training data|
|recover.py|add id to answer|

##Usage

####Step1
```sh
python nlp.py | tr -s $'\n' > tmp1.txt
```


