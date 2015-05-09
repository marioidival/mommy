# -*- coding: utf-8 -*-

from time import sleep
from random import choice
import tweepy


# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
CONSUMER_KEY = ""
CONSUMER_SCT = ""

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SCT)
auth.secure = True
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# 24 words to describe your Mommy <3
words_mommy = []

# Your Mommy
MOMMY = ""

# Your status, you can use format() to concat strings
# STATUS = "My example status, {}, to {}"
# example = "example"
# STATUS.format(example, MOMMY)
STATUS = ""

while True:
    description = words_mommy.pop(
        words_mommy.index(
            choice(words_mommy)
        )
    )

    api.update_status(status=STATUS.format(description, MOMMY))

    if not words_mommy:
        break

    sleep(3600)
