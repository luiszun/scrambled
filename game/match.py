from dictionary import Dictionary
from charpicker import getScramble
from scrambled import *
from gamedb import *
import time


class Match:
    MATCH_LEN_SECONDS = 60 * 2

    def __init__(self, userIds, num):
        self.userIds = set(userIds)

        # TODO: Avoid reinitialization of dictionary. Consider daemonizing it
        # TODO: Support multiple languages and multilanguage matches
        # -- Spanish, English, Spanglish
        self.dictionary = Dictionary()
        self.dictionary.loadDictionary("dictionary.txt")
        self.scramble = getScramble(dictionary, num)
        self.startTime = time.time()
        self.userAnswers = {}
        self.active = True

    def addUser(self, userId):
        if self.active is True:
            self.userIds.add(userId)

    def userLeft(self, userId):
        if self.active is True:
            self.userIds.remove(userId)

    def addUserWords(self, userId, wordSet):
        if not self.active:
            return False

        elapsedTime = time.time() - self.startTime

        assert elapsedTime > 0

        if elapsedTime > self.MATCH_LEN_SECONDS:
            return False

        if userId in self.userAnswers:
            self.userAnswers[userId] = self.userAnswers[userId].union(wordSet)
        else:
            self.userAnswers[userId] = set(wordSet)

        return True

    def endMatch(self):
        if not self.active:
            return False

        matchAbort = False
        elapsedTime = time.time() - self.startTime

        if elapsedTime < self.MATCH_LEN_SECONDS:
            matchAbort = True

        for user in self.userIds:
            self.userScore[user] = calculate_score(
                self.dictionary, self.userAnswers[user])

        return True

    def updateScores(self):
        # TODO: Actually keep score :)
        return True