from sys import argv
import json
import client, config, rand_tweet
from client import Client
from rand_tweet import RandomTweet

def build_query_param():
    return '%20'.join(argv[1:]) + '%20lang%3Aen&src=typd'

client = Client(config.KEY, config.SECRET)
url = 'https://api.twitter.com/1.1/search/tweets.json?q=' + build_query_param()
tweets = client.req(url)
random_tweet = RandomTweet(tweets).pick_one()

print '@' + random_tweet['user'] + ': ' + random_tweet['tweet']
print 'media:'
for url in random_tweet['urls']:
    print '\t' + url
