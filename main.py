#!/bin/env python2.7

import block
import frequency
import dictionary

def main():
	print "Usage: python your_program.py m(no. of sweetword sets/rows), n (no. of sweetwords/columns) filename"

	m = int(sys.argv[1])
	n = int(sys.argv[2])
	input_filename = sys.argv[3] 

	input_passwords = []
	with open(input_filename) as f:
		for line in f:
			print(line.strip())




if __name__ == '__main__':
  main()