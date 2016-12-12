# CS 5435 Homework 4
## Description:
A Python program that attacks against the "honeywords" as proposed in 

__Juels, Ari, and Ronald L. Rivest. "Honeywords: Making password-cracking detectable." Proceedings of the 2013 ACM SIGSAC conference on Computer & communications security. ACM, 2013.__
Link: https://people.csail.mit.edu/rivest/honeywords/ 
 
## Convention
Inputs: array of honeywords + password.

Output: array of scores between 0 and 1

## Strategy
1. Frequency analysis 
  * Only if all the honeywords are found in the dataset
  * Put weights based on the height in the list
  
2. Find dictionary words 
  * Capitalization
  * Names
  * Common numbers

3. Blocks of alphabet, numbers, special characters 
  * If they exist
  * The same length
  * In what order
  * Add Comment Collapse
