#!/usr/env/python
# http://www.lexically.net/downloads/BNC_wordlists/e_lemma.txt
import unittest
from game.match import *
import sys
sys.path.append('..')


class TestMatch(unittest.TestCase):

    match = Match({"one", "two", "three"}, 10)

    def test_addUser(self):
        nUsers = len(self.match.userIds)
        self.match.addUser("luiszunAdd")
        self.assertEqual(len(self.match.userIds), nUsers+1)

        self.match.addUser("luiszunAdd")
        self.assertEqual(len(self.match.userIds), nUsers+1)

        self.match.addUser("luiszunAdd2")
        self.assertEqual(len(self.match.userIds), nUsers+2)

    def test_userLeft(self):
        nUsers = len(self.match.userIds)
        self.match.userLeft("nonexistent")
        self.assertEqual(len(self.match.userIds), nUsers)

        self.match.userLeft("one")
        self.assertEqual(len(self.match.userIds), nUsers-1)

    def test_addWords(self):
        self.assertFalse(self.match.addUserWords(
            "nonexistent", {"a", "b", "c"}))
        self.assertTrue(self.match.addUserWords("two", {"a", "b", "c"}))
        self.assertTrue(self.match.addUserWords("two", {"a", "b", "c"}))
        self.assertTrue(self.match.addUserWords("three", {"a", "b", "c"}))

    def test_endMatch(self):
        self.match.scramble = "altiudecrobn"
        self.match.addUserWords("two", {"altitude", "b", "carrot"})
        self.match.addUserWords(
            "three", {"a", "banner", "c", "acknowledgement"})
        self.match.endMatch()
        self.assertEqual(self.match.userScore["two"], 8)


if __name__ == '__main__':
    unittest.main()
