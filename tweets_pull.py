#
import json
from twitter import TwitterStream, OAuth
#
# authenticate to Twitter
#
CONSUMER_KEY = raw_input('Enter the Twitter  consumer key: ')
CONSUMER_SECRET = raw_input('Enter the Twitter  consumer key secret: ')
ACCESS_TOKEN = raw_input('Enter the Twitter  access token: ')
ACCESS_SECRET = raw_input('Enter the Twitter  access token secret: ')
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
#
# pull some tweets
#
twitter_stream = TwitterStream(auth=oauth)
iterator = twitter_stream.statuses.filter(follow="14677919")
#
# put the tweets into a file 
#
i = 50
tweets = open("./static/tweets_14677919.json", "w")
for tweet in iterator:
    tweet_raw = json.dumps(tweet)
    print >> tweets, tweet_raw
    tweet_text = json.loads(tweet_raw.strip())
    if 'text' in tweet_text:
        print tweet['text'].encode('utf-8')
    i -= 1
    if i == 0:
        break
tweets.close()
#
# extract only the text of the tweets and put into a file
#
tweetfile = open("./static/tweets_14677919.json", "r")
textfile = open("./static/tweets_14677919.txt", "w")
for line in tweetfile:
    parsed_json = json.loads(line)
    tweet_text = parsed_json['text']
    print "tweet text:", tweet_text
    textfile.write(tweet_text)
    continue
tweetfile.close()
textfile.close()
#
