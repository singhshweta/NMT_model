# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 12:10:18 2018

@author: shweta
"""
import string
import re
from pickle import dump
from unicodedata import normalize
from numpy import array
 
# load doc into memory
def data_load():
	# open the file as read only
	file = open("deu.txt", mode='rt').read()
	return file
 
# split a loaded document into sentences
def map_data(doc):
    doc = doc.strip().split('\n')
    pairs = [line.split("\t") for line in  doc]
    return pairs
    
# clean a list of doc
def clean_mapping(doc):
    cleaned = list()
	# prepare regex for char filtering
    re_print = re.compile('[^%s]' % re.escape(string.printable))
	# prepare translation table for removing punctuation
    table = str.maketrans('', '', string.punctuation)
    for pair in doc:
        clean_pair = list()
        for line in pair:
			# normalize unicode characters
            line = normalize('NFD', line).encode('ascii', 'ignore')
            line = line.decode('UTF-8')
            
			# tokenize on white space
            line = line.split()
            
			# convert to lowercase
            line = [word.lower() for word in line]
            
			# remove punctuation from each token
            line = [w.translate(table) for w in line]
			# remove non-printable chars form each token
            line = [re_print.sub('', w) for w in line]
            
			# remove tokens with numbers in them
            line = [word for word in line if word.isalpha()]
			# store as string
            clean_pair.append(' '.join(line))
        cleaned.append(clean_pair)
    return array(cleaned)
 
# save a list of clean sentences to file
def save_clean_data(sentences, filename):
	dump(sentences, open(filename, 'wb'))
	print('Saved: %s' % filename)

#doc ="hello Mr. Khanna,how are you? I am doing good here. The weather is very hot here."

# load dataset

# split into english-german pairs
pairs = map_data(data_load())

# clean sentences
clean_mapping = clean_mapping(pairs)
# save clean pairs to file
save_clean_data(clean_mapping, 'eng-ger.pkl')
# spot check
print(clean_mapping)

for i in range(100):
    print('[%s] => [%s]' % (clean_mapping[i,0], clean_mapping[i,1]))



