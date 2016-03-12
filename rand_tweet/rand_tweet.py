from random import randint


class RandomTweet(Object):

    def __init__(self, json):
        self.json = json


    def pick_one(self):
