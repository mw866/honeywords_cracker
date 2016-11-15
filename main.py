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
			n = min(len(passwords), n)
			frequency_scores = frequency.get_frequency_scores(passwords, m, n)
			block_scores = block.get_block_scores(passwords, m, n)
			dictionary_scores = dictionary.get_dictionary_scores(passwords, m, n)
			get_real(passwords, frequency_scores, block_scores, dictionary_scores)
	return

def get_real(passwords, frequency_scores, block_scores, dictionary_scores):
	scores_list = []
	for i in range(len(passwords)):
		password = passwords[i]
		score = frequency_scores[i] + block_scores[i] + dictionary_scores[i]
		scores_list.append(score)
	
	max_score = max(scores_list)
	print passwords[scores_list.index(max_score)] , "->" , max_score

if __name__ == '__main__':
  main()