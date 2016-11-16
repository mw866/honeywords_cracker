#!/usr/bin/env python2.7
#howard

def decide_func(char):
	'''Given char and return the corresponding detecting function.'''
	def isspecial(char):
		return not str.isalpha(char) and not str.isdigit(char)
	if str.isalpha(char):
		return str.isalpha
	elif str.isdigit(char):
		return str.isdigit
	else:
		return isspecial

def get_block_scores(sweetwords=['aa123hello#@', 'a1a2a3', 'thisIsCool', '@#!@#haha', 'a!1c#3f%'], m=8, n=5):
	scores = []
	#print(sweetwords)
	for sweetword in sweetwords:
		block_num = 1
		func = decide_func(sweetword[0])
		for i in range(len(sweetword) - 1):
			if not func(sweetword[i]) == func(sweetword[i + 1]):
				block_num += 1
				func = decide_func(sweetword[i + 1])
		scores.append(1.0 / block_num)
	scores = [float(s) / sum(scores) for s in scores]
	#print(scores)
	return scores

if __name__ == '__main__':
	get_block_scores()
