#!/bin/env python2.7
#sonia
'''
Gives higher scores to passwords that have dictionary words or names in them (rather than randomness)
We will also look for when the dictionary word or name is capitalized on the first letter only.
We will also be creating and searching for a common numbers dictionary
  * Capitalization
  * Names
  * Common numbers
'''
import numpy as np

def get_dictionary_scores(inputs, m, n):
  # print "Calculating dictionary scores..."
  scores = np.zeros(len(inputs))

  wordsFound = {}

  #Retrieving the dictionary words
  f = open('words.txt', 'r')
  words = f.read().splitlines()

  #Going through the given sweetword input
  for i, sweetword in enumerate(inputs):


    #If there is a WORD found, increase the score
    for w in words:

      if w.lower() in sweetword.lower():
        scores[i] += 1

        #if the word is capitalized, give it extra score
        if sweetword[sweetword.lower().index(w.lower())].isupper():
          scores[i] += 1

        #if a word is found multiple times
        if w in wordsFound:
          wordsFound[w].append(i)
        else:
          wordsFound[w] = [i]

  #increasing score from repeat words/names/numbers located in wordsFound dictionary
  for key, value in wordsFound.items():
    for v in value:
      scores[v] += 1

  #normalizing the score by the sum of all scores
  if sum(scores):
    scores = [float(s) / sum(scores) for s in scores]

  # print scores
  return scores
