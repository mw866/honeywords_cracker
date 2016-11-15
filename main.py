#!/bin/env python2.7
import sys, block, frequency, dictionary

def main():
	print "Usage: python your_program.py m(no. of sweetword sets/rows), n (no. of sweetwords/columns) filename"

	m = int(sys.argv[1])
	n = int(sys.argv[2])
	filename = sys.argv[3] 

	with open(filename) as f:
		for line in f:
			passwords = line.split(',')
			frequency_scores = frequency.get_frequency_scores(passwords)
			block_scores = block.get_block_scores(passwords)
			dictionary_scores = dictionary.get_dictionary_scores(passwords)
			get_real(passwords, frequency_scores, block_scores, dictionary_scores)
	return

def get_real(passwords, frequency_scores, block_scores, dictionary_scores):
	score_list = []
	for i in range(len(passwords)):
		password = passwords[i]
		score = frequency_scores[i] + block_scores[i] + dictionary_scores[i]
		score_list.append(score)
	max_score = max(score_list)
	print passwords[score_list.index(max_score)] , max_score

if __name__ == '__main__':
  main()