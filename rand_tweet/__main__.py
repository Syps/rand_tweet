import json
import client, config

client = client.Client(config.KEY, config.SECRET)

tweet = client.req('https://api.twitter.com/1.1/search/tweets.json?q=%40twitterapi')
print json.dumps(tweet, sort_keys=True, indent=4, separators=(',', ':'))
