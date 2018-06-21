# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 01:06:36 2018

@author: shweta
"""
from pickle import load
from pickle import dump
from numpy.random import rand
from numpy.random import shuffle
from sklearn.model_selection import train_test_split
 
# load a clean dataset
def load_clean_sentences(filename):
	return load(open(filename, 'rb'))
 
# save a list of clean sentences to file
def save_clean_data(sentences, filename):
	dump(sentences, open(filename, 'wb'))
	print('Saved: %s' % filename)
 
# load dataset
raw_dataset = load_clean_sentences('english-german.pkl')
 
# reduce dataset size
n_sentences = 10000
dataset = raw_dataset[:n_sentences, :]
# random shuffle
shuffle(dataset)
# split into train/test
train, test = train_test_split( dataset , test_size=0.10, random_state=42)

# save
save_clean_data(dataset, 'english-german-both.pkl')
save_clean_data(train, 'english-german-train.pkl')
save_clean_data(test, 'english-german-test.pkl')