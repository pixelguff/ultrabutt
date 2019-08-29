import sopel
import time
import sys
import os
from mastodon import Mastodon


@sopel.module.commands('toot')
def toot(bot, trigger):
    # bot.say(os.getcwd())
    mytoot = trigger.split(' ', 1)[1]

    try:
        keys = open(os.getcwd() + "/SECRET_SAUCE/masto.txt", "r")

        client_id = keys.readline().rstrip()
        client_secret = keys.readline().rstrip()
        access_token = keys.readline().rstrip()
        api_base_url = keys.readline().rstrip()

        mastodon = Mastodon(client_id, client_secret,
                            access_token, api_base_url)

        mastodon.toot(mytoot)

        keys.close()

        bot.say("OK, I tooted that to " + api_base_url)
    except:
        bot.say("It all went to shit, son.")
