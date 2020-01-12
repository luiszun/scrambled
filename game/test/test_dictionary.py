#!/usr/env/python
# http://www.lexically.net/downloads/BNC_wordlists/e_lemma.txt
import sys
sys.path.append('..')

from dictionary import Dictionary
from charpicker import getScramble
from scrambled import *
import unittest

class TestDictionary(unittest.TestCase):

    dictionary = Dictionary()
    dictionary.loadDictionary("dictionary.txt")

    def test_search(self):
        self.assertTrue(self.dictionary.searchWord("table"))
        self.assertTrue(self.dictionary.searchWord("ball"))
        self.assertTrue(self.dictionary.searchWord("dog"))
        self.assertTrue(self.dictionary.searchWord("cock"))
        self.assertTrue(self.dictionary.searchWord("pigs"))
        self.assertTrue(self.dictionary.searchWord("running"))
        self.assertTrue(self.dictionary.searchWord("sky"))
        self.assertTrue(self.dictionary.searchWord("cleaning"))
        self.assertTrue(self.dictionary.searchWord("been"))
        self.assertTrue(self.dictionary.searchWord("cleaned"))
        self.assertFalse(self.dictionary.searchWord(""))
        self.assertFalse(self.dictionary.searchWord("b"))
        self.assertFalse(self.dictionary.searchWord("z"))
        self.assertFalse(self.dictionary.searchWord("e"))
        self.assertFalse(self.dictionary.searchWord("i"))
        self.assertFalse(self.dictionary.searchWord("sdaf"))
        self.assertFalse(self.dictionary.searchWord("fdgsd"))
        self.assertFalse(self.dictionary.searchWord("sdafsadf"))
        self.assertFalse(self.dictionary.searchWord("skysky"))

    def test_scramble(self):
        s1 = getScramble(self.dictionary, 50)
        s2 = getScramble(self.dictionary, 50)
        s3 = getScramble(self.dictionary, 5)
        self.assertEqual(len(s1), len(s2))
        self.assertEqual(len(s1), 50)
        self.assertEqual(len(s2), 50)
        self.assertEqual(len(s3), 5)

    def test_score(self):
        self.assertEqual(calculate_score(self.dictionary, "teas"), 1)
        self.assertEqual(calculate_score(self.dictionary, "tEAs"), 1)
        self.assertEqual(calculate_score(
            self.dictionary, ("teas", "teas", "teas", "teas")), 1)
        self.assertEqual(calculate_score(
            self.dictionary, ("table", "teas", "tables", "tables", "casdaSDte")), 6)
        self.assertEqual(calculate_score(
            self.dictionary, ("taBle", "tEas", "Tables", "tables", "casdaSDte")), 6)


if __name__ == '__main__':
    unittest.main()
