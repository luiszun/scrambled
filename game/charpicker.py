#!/usr/env/python
import operator
import random


def getScramble(dictionary, num):
    listRange = 0
    scramble = ""
    charcount = dictionary.charCount

    for i in charcount:
        listRange += charcount[i]

    for i in range(num):
        currentSum = 0
        charIndex = random.randrange(listRange)
        for key, value in sorted(charcount.items(), key=lambda x: x[1]):
            currentSum += value
            if currentSum >= charIndex:
                scramble += key
                break

    return scramble
