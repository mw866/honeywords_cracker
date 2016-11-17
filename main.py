#!/bin/env python2.7
## [TODO] Comment debugging outputs before submission
import sys, block, frequency, dictionary

def main():
	print "Usage: python ", sys.argv[0], " m  (no. of sweetword sets/rows), n = 5 (no. of sweetwords/columns) filename\nExample: python main.py 100 5 real_and_sweet.txt "
	m = int(sys.argv[1])
	n = int(sys.argv[2])
	filename = sys.argv[3]

	password_freq_dict = frequency.init_frequency_scores()

	with open(filename) as f:
		line_n = 1
		for line in f:

			if line_n >= m: break
			line_n += 1

			passwords = line.rstrip('\n').split(',')
			print '\npasswords: ', passwords
			n = min(len(passwords), n)

			frequency_scores = frequency.get_frequency_scores(password_freq_dict, m, n, passwords)
			print "frequency_scores:\t", frequency_scores
			block_scores = block.get_block_scores(passwords, m, n)
			print "block_scores:\t\t", block_scores
			dictionary_scores = dictionary.get_dictionary_scores(passwords, m, n)
			print "dictionary_scores:\t", dictionary_scores
			get_real(passwords, frequency_scores, block_scores, dictionary_scores)

	return

def get_real(passwords, frequency_scores, block_scores, dictionary_scores):
	total_scores_list = []

	for i in range(len(passwords)):
		password = passwords[i]
		# [TODO] To fine tune the scoring system.
		total_score = frequency_scores[i] + block_scores[i] + dictionary_scores[i]
		total_scores_list.append(total_score)
	max_score = max(total_scores_list)
	print 'total_scores_list:\t', total_scores_list
	print 'Best Guess Indices(', max_score, '): ', total_scores_list.index(max_score)
	print 'Best Guess (', max_score, '): ', passwords[total_scores_list.index(max_score)]

if __name__ == '__main__':
  main()
