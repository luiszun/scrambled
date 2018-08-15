#!/usr/env/python
# http://www.lexically.net/downloads/BNC_wordlists/e_lemma.txt

from dictionary import Dictionary
from charpicker import getScramble
from scrambled import *

dictionary = Dictionary()
dictionary.loadDictionary("dictionary.txt")

(str(dictionary.searchWord("table") == True))
print (str(dictionary.searchWord("ball") == True))
print (str(dictionary.searchWord("dog") == True))
print (str(dictionary.searchWord("cock") == True))
print (str(dictionary.searchWord("pigs") == True))
print (str(dictionary.searchWord("running") == True))
print (str(dictionary.searchWord("sky") == True))
print (str(dictionary.searchWord("cleaning") == True))
print (str(dictionary.searchWord("been") == True))
print (str(dictionary.searchWord("cleaned") == True))
print (str(dictionary.searchWord("") == False))
print (str(dictionary.searchWord("b") == False))
print (str(dictionary.searchWord("z") == False))
print (str(dictionary.searchWord("e") == False))
print (str(dictionary.searchWord("i") == False))
print (str(dictionary.searchWord("sdaf") == False))
print (str(dictionary.searchWord("fdgsd") == False))
print (str(dictionary.searchWord("sdafsadf") == False))
print (str(dictionary.searchWord("skysky") == False))

s1 = getScramble(dictionary, 50)
s2 = getScramble(dictionary, 50)
s3 = getScramble(dictionary, 5)
print (str(s1 != s2))
print (str(len(s1) == 50))
print (str(len(s2) == 50))
print (str(len(s3) == 5))

print (str(calculate_score(dictionary, "teas") == 1))
print (str(calculate_score(dictionary, "tEAs") == 1))
print (str(calculate_score(dictionary, ("teas","teas","teas","teas")) == 1))
print (str(calculate_score(dictionary, ("table","teas","tables","tables","casdaSDte")) == 6))
print (str(calculate_score(dictionary, ("taBle","tEas","Tables","tables","casdaSDte")) == 6))