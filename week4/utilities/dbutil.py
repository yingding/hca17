# Tutorial for pymongo 3 http://api.mongodb.com/python/current/tutorial.html
from pymongo import MongoClient
import datetime as dt

class MongoDbUtil:
    @classmethod
    def getDB(cls, user, password, host, port, dbname):
        uri = "mongodb://{}:{}@{}:{}/{}?authMechanism=SCRAM-SHA-1".format(user, password, host, port, dbname)
        client = MongoClient(uri)
        db = client.get_default_database()
        return db

    @staticmethod
    def test(db):
        # get the name list of collections in the given db
        for name in db.collection_names():
            print(name)