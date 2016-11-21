# CS 5435 Homework 4
## Description:
A Python program that identify the "honeywords" as proposed in 
 Juels, Ari, and Ronald L. Rivest. "Honeywords: Making password-cracking detectable." Proceedings of the 2013 ACM SIGSAC conference on Computer & communications security. ACM, 2013.
 http://www.arijuels.com/wp-content/uploads/2013/09/JR13.pdf
 
## Convention
Inputs: array of honeywords + password.

Output: array of scores between 0 and 1

## Strategy
1. Frequency analysis [Chris]
  * Only if all the honeywords are found in the dataset
  * Put weights based on the height in the list
  
2. Find dictionary words [Sonia]
  * Capitalization
  * Names
  * Common numbers

3. Blocks of alphabet, numbers, special characters [Howard]
  * If they exist
  * The same length
  * In what order
  * Add Comment Collapse

===
Find similar/outliers and kick those ones out
  * Majority vote
  * Finding tough nuts
  * If there is only one digit, 50% make it 1

