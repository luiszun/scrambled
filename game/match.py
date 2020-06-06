from .dictionary import Dictionary
from .charpicker import getScramble
from .scrambled import *
from .gamedb import *
import time


class Match:
    MATCH_LEN_SECONDS = 60 * 2

    def __init__(self, userIds, srambleLen):
        self.userIds = set(userIds)

        # TODO: Avoid reinitialization of dictionary. Consider daemonizing it
        # TODO: Support multiple languages and multilanguage matches
        # -- Spanish, English, Spanglish
        self.dictionary = Dictionary()
        self.dictionary.loadDictionary("dictionary.txt")
        self.scramble = getScramble(self.dictionary, srambleLen)
        self.startTime = time.time()
        self.userAnswers = {}
        self.userScore = {}

        # This match is still being active (not just a log)
        self.active = True

    def addUser(self, userId):
        if self.active is True:
            self.userIds.add(userId)

    def userLeft(self, userId):
        if self.active is True:
            if userId in self.userIds:
                self.userIds.remove(userId)

    def addUserWords(self, userId, wordSet):
        if not self.active:
            return False

        if userId not in self.userIds:
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
            answers = {}
            if user in self.userAnswers:
                answers = self.userAnswers[user]

            answers = self.purgeInvalidAnswers(answers)

            self.userScore[user] = calculate_score(
                self.dictionary, answers)

        self.updateScores()
        return True

    def purgeInvalidAnswers(self, answers):
        finalAnswers = []
        for answer in answers:
            if set(answer).issubset(self.scramble):
                finalAnswers.append(answer)
        return finalAnswers

    def updateScores(self):
        db = getDB()
        cur = db.cursor()

        for user in self.userIds:
            score = self.userScore[user]
            cur.execute(
                "INSERT INTO user (id, username, score) VALUES(?, ?, ?) ON CONFLICT(id) DO UPDATE SET score = score+?", [user, user, score, score])
        db.commit()

        return True
