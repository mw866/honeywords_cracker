#!/bin/env python2.7
#chris
from bz2 import BZ2File

def init_frequency_scores():
	filename = 'rockyou-withcount.txt.bz2'
	print "Extracting and loading file: ", filename
	with BZ2File(filename, 'r') as rockyou_bz2:
		rockyou_list = rockyou_bz2.readlines()

	password_count_dict  ={}
	# max_counts =  290729 # '123456'

	for pwd_count_pair in rockyou_list:
		pwd_count_pair =  pwd_count_pair.strip().split(' ')
		if len(pwd_count_pair) !=2: continue
		count, password  = pwd_count_pair
		password_count_dict[password] = int(count)
	return password_count_dict

# input m is not used.
def get_frequency_scores(password_count_dict, m=10, n=5, sweetwords=['abc','123','123456','&)(#!*', 'trumpispresident']):
	counts = [None] * n
	for i in range(n):
		if sweetwords[i] not in password_count_dict.keys(): 
			counts[i]=0
		else:
			counts[i]=password_count_dict[sweetwords[i]]
	total_count = sum(counts)
	if total_count != 0:
		scores = [(float(count)/total_count) for count in counts]
	else:
		scores= [0 for count in counts]
	return scores

if __name__ == '__main__':
	print get_frequency_scores(init_frequency_scores())