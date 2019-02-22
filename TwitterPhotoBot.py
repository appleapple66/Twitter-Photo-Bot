# twitter photo bot

import tweepy as tp
import time
import os

# credentials to login to twitter api (get these value through twitter developer website first)
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

os.chdir('twitterImage')

# iterates over pictures in twitterImage folder
for tweet_image in os.listdir('.'):
    api.update_with_media(tweet_image)
    time.sleep(3)

