# encoding: utf-8
# Author: Zehao Hui

import tweepy
from tweepy import OAuthHandler
import json
import os

consumer_key = 'MBcExfr5FfXZdI47kDmUH8XrJ'
consumer_secret = 'fawfPjqtC4GqAIVCPz9iUUoHH8XP2kpWmfQmMFrQbtqE3ihmIH'
access_key = '1439356284529221637-w7oLiJuRtpfZ2bR4ZsKxco25wN6W7R'
access_secret = 'IbUfiw7g5drxAhYG14ueD5tr5FQ42RuTWewiE0a5wMqNT'


def find_tag_tweets(searchhash):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    search_results = api.search_tweets(q=searchhash, count=10)
    file = open('tagfind.json', 'w')
    print("Writing tweet objects to JSON please wait...")
    for status in search_results:
        json.dump(status._json, file, sort_keys=True, indent=4)

    print("Done")
    file.close()


if __name__ == '__main__':
    find_tag_tweets("blackmythwukng")
