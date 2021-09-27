# encoding: utf-8
# Author: Zehao Hui

import tweepy
from tweepy import OAuthHandler
import json
import os

f = open("key.txt")

consumer_key = f.readline().strip()
consumer_secret = f.readline().strip()
access_key = f.readline().strip()
access_secret = f.readline().strip()

f.close()


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
