#!/bin/env python2.7
#chris
from bz2 import BZ2File

def get_frequency_scores(sweetwords=['a','a','a','a','a'], m=10, n=5):
	print "Calculating frequency scores..."
	filename = 'rockyou-withcount.txt.bz2'
	print "Extracting and Loading file: ", filename

	with BZ2File(filename, 'r') as rockyou_bz2:
		rockyou_list = rockyou_bz2.readlines()

	password_freq_dict  ={}
	max_counts =  290729 # '123456'

	for pwd_count_pair in rockyou_list:
		pwd_count_pair =  pwd_count_pair.strip().split(' ')
		if len(pwd_count_pair) !=2: continue
		count, password  = pwd_count_pair
		password_freq_dict[password] = float(count)/max_counts

	scores = [None] * n
	for i in range(n):
		if sweetwords[i] not in password_freq_dict.keys(): 
			scores[i]=0
		else:
			scores[i]=password_freq_dict[sweetwords[i]]
	print scores
	return scores

if __name__ == '__main__':
	get_frequency_scores()