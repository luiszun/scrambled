#!/usr/env/python
from .dictionary import Dictionary


def sanitize_input(wordList):
    if isinstance(wordList, tuple):
        wordList = list(wordList)
    elif isinstance(wordList, str):
        wordList = [wordList]
    return wordList


def purge_invalid_words(dictionary, wordList):
    MIN_WORDLEN = 4
    validWords = []
    for word in wordList:
        if dictionary.searchWord(word) is True and len(word) >= MIN_WORDLEN:
            validWords.append(word)
    return validWords


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
