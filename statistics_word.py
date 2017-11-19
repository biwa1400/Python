import sys
import re
import collections

WORD_RE = re.compile('\w+')
'''
index = {}
'''

'''
index = collections.defaultdict(list)
'''

with open(sys.argv[1], encoding='utf-8')  as fp:
	for sentence_num,sentence in enumerate(fp):
		for match in WORD_RE.finditer(sentence):
			word = match.group()
			location = (sentence_num,match.start())
			
			'''
			unit = index.get(word,[])
			unit.append(location)
			index[word] = unit
			'''
			
			'''
			index.setdefault(word,[]).append(location)
			'''
			
			'''
			index[word].append(location)
			'''

for a in sorted(index, key=str.upper):
	print(a,index[a])		