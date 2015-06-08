import difflib


readPathName = 'p2.train.txt'
writePathName = 'answer_for_training_data.txt'
r = open(readPathName, "r")
w = open(writePathName, "w")

while True:
	small = 1000
	large = 0
	lineBuf = r.readline()
	if lineBuf == "":
		break
	sentences = lineBuf.split()
	sentences.pop(0)
	print sentences[0], sentences[1]
	for i, s in enumerate(difflib.ndiff(unicode(sentences[0], 'utf-8'), unicode(sentences[1], 'utf-8'))):
		if s[0] == '-':
			print i+1
			if small > (i + 1):
				small = i + 1
			if large < (i + 1):
				large = i + 1
	print small, large
	w.write('%d\t%d\n' % (small, large))
	

	