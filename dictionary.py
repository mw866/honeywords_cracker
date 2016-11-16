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
  print "Calculating dictionary scores..."

  scores = np.zeros(len(inputs))

  wordsFound = {}

  #Retrieving the names corpus
  names = ["Teddy", "chris", "howard", "andrew"]

  #Retrieving the dictionary words
  words = ["tweety", "monkey", "sylvester"]

  #Retrieving the most common numbers
  numbers = ["123", "3456", "69"]

  #Going through the given sweetword input
  for i, sweetword in enumerate(inputs):

    #If there is a NAME found, increase the score
    for n in names:
      if n.lower() in sweetword.lower():
        scores[i] += 1

        #if the name is capitalized, give it extra score
        if sweetword[sweetword.lower().index(n.lower())].isupper():
          scores[i] += 1

        #if name is found multiple times
        if n in wordsFound:
          wordsFound[n].append(i)
        else:
          wordsFound[n] = [i]


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


    #If there is a NUMBER found, increase the score
    for num in numbers:
      if num in sweetword:
        scores[i] += 1

        #if a number is found multiple times
        if num in wordsFound:
          wordsFound[num].append(i)
        else:
          wordsFound[num] = [i]

  #increasing score from repeat words/names/numbers located in wordsFound dictionary
  for key, value in wordsFound.items():
    for v in value:
      scores[v] += 1

  #normalizing the score by the sum of all scores
  scores = [float(s) / sum(scores) for s in scores]

  print scores
  return scores
