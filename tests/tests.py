from nose.tools import *
import json
import rand_tweet
from rand_tweet import rand_tweet
from rand_tweet.rand_tweet import RandomTweet

def test_random_tweet_return_obj():
    f = open('tests/sample_json.txt', 'r+')
    sample_json = json.loads(f.read())
    t = RandomTweet(sample_json).pick_one()
    assert 'tweet' in t
    assert 'user' in t
    assert 'urls' in t
