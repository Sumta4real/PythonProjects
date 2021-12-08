#####Python Challenge 
#A pangram is a sentence that contains every single letter of the alphabet 
#at least once. For example, the sentence "The quick brown fox jumps over
# the lazy dog" is a pangram, because it uses the letters A-Z at least
# once (case is irrelevant).Given a string, detect whether or not it is
# a pangram. Return True if it is, False if not. Ignore numbers and 
####### punctuation.

from typing import Counter

import time
import string 
start = time.time()
def pangram(sentence):
    """
    This program checks if a string contains all english alphabet at least once.
    It returns True if yes and otherwise, it returns false

    Input (str) : A Sentence
    Output (bool) : True or False
    """
    words = sentence.lower().split()
    letters = []
    for i in words:
        for x in i:
            letters += x
    if all(var in letters for var in string.ascii_lowercase): #checks if all elements in alphabets appear in list named LETTERS 
        return True
    else:
        return False

###Optimised Solution
def is_pangram(s):
    s = s.lower()
    return all(letter in s for letter in string.ascii_lowercase)
    
print(is_pangram('Amoke is a lovely damsel becfghi jkl mmmn pp qq rer ss tt uu vv ww xx yy zzz'))
print(is_pangram( "The quick brown fox jumps over the lazy dog"))
print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
print(is_pangram("Aacdefghijklmnopqrstuvwxyz"))
#print(is_pangram(""))
