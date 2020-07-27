import sopel
import pytumblr
import time
import sys
import os
from string import split
import random

reload(sys)
sys.setdefaultencoding("utf8")


@sopel.module.commands('UltraButt')
def topiccommands(bot, trigger):

    ops = []

    fops = open(os.getcwd() + "/SECRET_SAUCE/ops.txt", "r")
    for op in fops.readline().rstrip():
        ops.append(op)
    fops.close()

    keys = open(os.getcwd() + "/SECRET_SAUCE/tumblr.txt", "r")
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

    try:
        arg_list = split(trigger)

        if arg_list[1].lower() == "no":
            # delete most recent post

            # get ID of most recent post.
            blog_info = client.posts("bgtopics", limit=1)
            latest_post = blog_info['posts'][0]
            latest_post = blog_info['posts'][0]
            latest_id = str(latest_post['id'])

            # delete if it's within 60 secs

            ts = int(time.time())

            if ts - latest_post['timestamp'] < 60:
                client.delete_post("bgtopics", latest_id)
                bot.reply("OK, I deleted it. *mumblegrumble*")
            else:
                bot.reply("Too late, fucko.")

        if arg_list[1].lower() == "del":
            if trigger.nick.lower() in ops:

                delres = client.delete_post("bgtopics", arg_list[2])

                if 'id' in delres:
                    bot.reply(
                        "OK, I think I deleted that one. Was it some cunt's "
                        "password or something?")
                else:
                    bot.reply(
                        "I couldn't find {}. Either it's already gone, or you "
                        "fucked the ID up.".format(str(arg_list[2])))
            else:
                bot.reply(
                    "You're not on the ops list for deleting stuff,"
                    " poopy pants.")

        if arg_list[1].lower() == "sexwee":
            bot.action("chucks his muck")

        if arg_list[1].lower() == "sucks":
            insults = ["Eat all of my arse-piece!",
                       "Suck a nut.",
                       "I hate you.",
                       "You smell of bumhole.",
                       "Finger a goat, knobstretcher.",
                       "Lick my chutney locker.",
                       "Ur a twat.",
                       "Smooch my hoop.",
                       "And bollocks to you, dickcheese."]

            bot.reply(random.choice(insults))

        if arg_list[1].lower() == "help":
            bot.say(
                '".UltraButt NO" will delete the most recent topic from Tumblr'
                ' within 1 minute of posting.')
            bot.say(
                '".UltraButt del <postid from tumblr>" will delete the '
                'post from Tumblr with the given ID as long as you are '
                'in the ops group.')
            bot.say('".UltraButt help". You just typed it. It is this.')
    except Exception:
        bot.reply("What?")
