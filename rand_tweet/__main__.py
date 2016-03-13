from sys import argv
import json
import client, config, rand_tweet
from client import Client

def build_query_param():
    return '%20'.join(argv[1:]) + '%20'

client = Client(config.KEY, config.SECRET)

query = build_query_param()
url = 'https://api.twitter.com/1.1/search/tweets.json?q=' + query + 'lang%3Aen&src=typd'
tweets = client.req(url)
random_tweet = rand_tweet.RandomTweet(tweets).pick_one()

print '@' + random_tweet['user'] + ': ' + random_tweet['tweet']
print 'media:'
for url in random_tweet['urls']:
    print '\t' + url
