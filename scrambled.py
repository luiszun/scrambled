#!/usr/env/python
from dictionary import Dictionary

def sanitize_input(wordList):
    if isinstance(wordList, tuple):
        wordList = list(wordList)
    elif isinstance(wordList, str):
        wordList = [wordList]
    return wordList

def purge_invalid_words(dictionary, wordList):
    # Note the list is being copied per https://docs.python.org/3/tutorial/controlflow.html
    for  word in wordList[:]:
        if dictionary.searchWord(word) is False:
            wordList.remove(word)
    return wordList

def remove_duplicates(wordList):
    # Case-insensitive removal
    return list(set(i.lower() for i in wordList))

def calculate_score(dictionary, wordList):
    MIN_WORDLEN = 4
    totalPoints = 0

    wordList = sanitize_input(wordList)
    wordList = purge_invalid_words(dictionary, wordList)
    wordList = remove_duplicates(wordList)

    for word in wordList:
        totalPoints += len(word) - MIN_WORDLEN + 1

    return totalPoints