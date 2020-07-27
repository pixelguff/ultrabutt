import sopel
import pytumblr
import time
import datetime
import os
import sys
import tweepy
from mastodon import Mastodon

reload(sys)
sys.setdefaultencoding("utf8")


@sopel.module.rule('.*')
@sopel.module.event('TOPIC')
def topicthing(bot, event):

    ts = time.time()

    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    keys = open(os.getcwd() + "/SECRET_SAUCE/tumblr.txt")
    CONSUMER_KEY = keys.readline().rstrip()
    CONSUMER_SECRET = keys.readline().rstrip()
    OAUTH_TOKEN = keys.readline().rstrip()
    OAUTH_TOKEN_SECRET = keys.readline().rstrip()
    keys.close()
    client = pytumblr.TumblrRestClient(
        CONSUMER_KEY,
        CONSUMER_SECRET,
        OAUTH_TOKEN,
        OAUTH_TOKEN_SECRET
    )

    tkeys = open(os.getcwd() + "/SECRET_SAUCE/twitter.txt", "r")

    TCONSUMER_KEY = tkeys.readline().rstrip()
    TCONSUMER_SECRET = tkeys.readline().rstrip()
    TACCESS_KEY = tkeys.readline().rstrip()
    TACCESS_SECRET = tkeys.readline().rstrip()

    tkeys.close()

    tauth = tweepy.OAuthHandler(TCONSUMER_KEY, TCONSUMER_SECRET)
    tauth.set_access_token(TACCESS_KEY, TACCESS_SECRET)
    tapi = tweepy.API(tauth)

    # Get Masto Keys
    keys = open(os.getcwd() + "/SECRET_SAUCE/masto.txt", "r")
    client_id = keys.readline().rstrip()
    client_secret = keys.readline().rstrip()
    access_token = keys.readline().rstrip()
    api_base_url = keys.readline().rstrip()
    mastodon = Mastodon(client_id, client_secret, access_token, api_base_url)
    keys.close()

    TOPIC = event

    POST_BODY = "This topic was set at " + st

    params = {'state': 'published', 'format': 'markdown',
              'title': TOPIC, 'body': POST_BODY}

    result = client.create_text('bgtopics.tumblr.com', **params)

    mastodon.toot("[New Topic]\n\n" + event
                  + "\n\n[#bibeogaem at bibeogaem.zone]\n"
                  "[See more at http://bgtopics.tumblr.com/]")

    tapi.update_status("[New Topic in #bibeogaem]\n\n" + event)

    try:
        err = result['id']
        bot.say("Topic tumbld at http://bgtopics.tumblr.com/, tooted at"
                " https://bibeogaem.zone/, and fuckin tweeted.")
    except Exception:
        bot.say("For some reason, I couldn't post that. "
                "It's probably a duff key.")
