#!/usr/env/python
import os

class Node:
    def __init__(self):
        self.isWord = False
        self.children = {}


class Dictionary:
    def __init__(self):
        self.wordCount = 0
        self.Tree = Node()
        self.charCount = {}

    def loadDictionary(self, filename):
        __location__ = os.path.realpath(os.path.join(
            os.getcwd(), os.path.dirname(__file__)))
        file = open(os.path.join(__location__, filename), "r")
        for i in file:
            words = i.rstrip().split(",")
            for word in words:
                self.insertWord(word)

    def insertWord(self, word):
        inode = self.Tree
        for i, char in enumerate(word):
            char = char.lower()

            if not char.isalpha():
                return False

            if char not in inode.children:
                inode.children[char] = Node()
            inode = inode.children[char]
            if i == len(word)-1:
                inode.isWord = True

            if char in self.charCount:
                self.charCount[char] += 1
            else:
                self.charCount[char] = 1

    def searchWord(self, word):
        inode = self.Tree
        for i, char in enumerate(word):
            char = char.lower()
            if char not in inode.children:
                return False
            inode = inode.children[char]

            if i == len(word)-1:
                return inode.isWord
        # Empty string
        return False
