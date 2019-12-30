import sqlite3
import os


def getDB():
    filename = "gamedb.db"
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))

    return sqlite3.connect(os.path.join(__location__, filename))
