import sopel, time, sys, os
import markovify
from mastodon import Mastodon

@sopel.module.commands('tootmarkov')
def tootmarkov(bot, trigger):
        keys = open(os.getcwd()+"/SECRET_SAUCE/masto.txt","r")
        client_id = keys.readline().rstrip()
        client_secret = keys.readline().rstrip()
        access_token = keys.readline().rstrip()
        api_base_url = keys.readline().rstrip()
        mastodon = Mastodon(client_id,client_secret,access_token,api_base_url)
        keys.close()

	# Get raw text as string.
        f = open(os.getcwd()+"/all_of_bgtopics.txt", "r")
        text = f.read()

        # Build the model.
        text_model = markovify.Text(text)

	mytoot = text_model.make_short_sentence(140)
	output = mytoot+"\n\n[Generated by TootMarkov]"
	
	mastodon.toot(output)
	bot.say("I tooted: "+mytoot)


