# encoding: utf-8
# Author: Zehao Hui

import tweepy
from tweepy import OAuthHandler
import json

consumer_key = 'MBcExfr5FfXZdI47kDmUH8XrJ'
consumer_secret = 'fawfPjqtC4GqAIVCPz9iUUoHH8XP2kpWmfQmMFrQbtqE3ihmIH'
access_key = '1439356284529221637-w7oLiJuRtpfZ2bR4ZsKxco25wN6W7R'
access_secret = 'IbUfiw7g5drxAhYG14ueD5tr5FQ42RuTWewiE0a5wMqNT'


def get_all_tweets(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    alltweets = []
    new_tweets = api.user_timeline(screen_name=screen_name, count=10)
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1
    while len(new_tweets) > 0:
        new_tweets = api.user_timeline(screen_name=screen_name, count=10, max_id=oldest)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
        if len(alltweets) > 15:
            break
        print("...%s tweets downloaded so far" % (len(alltweets)))

    file = open('tweet.json', 'w')
    print("Writing tweet objects to JSON please wait...")
    for status in alltweets:
        json.dump(status._json, file, sort_keys=True, indent=4)

    print("Done")
    file.close()


if __name__ == '__main__':
    get_all_tweets("@BlackMyth_GS")
