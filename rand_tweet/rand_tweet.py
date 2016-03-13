from random import randint

"""
RandomTweet encapsulates the logic for returning a dict with a random tweet,
the username that tweeted it, and the link to media (if any) from
the tweet for a given JSON object.
"""

class RandomTweet(object):

    def __init__(self, json):
        self.json = json


    def pick_one(self):
        index = randint(0,len(self.json['statuses'])-1)
        tweet_obj = self.json['statuses'][index]
        data = {}
        data['tweet'] = tweet_obj['text'].encode('ascii', errors='xmlcharrefreplace')
        data['user'] = tweet_obj['user']['screen_name']
        data['urls'] = []
        for url in tweet_obj['entities']['urls']:
            data['urls'].append(url['url'])
        return data
