import sopel, time, sys, os
from mastodon import Mastodon

@sopel.module.commands('tootndb')
def toot(bot, trigger):

        keys = open(os.getcwd()+"/SECRET_SAUCE/masto.txt","r")

        client_id = keys.readline().rstrip()
        client_secret = keys.readline().rstrip()
        access_token = keys.readline().rstrip()
        api_base_url = keys.readline().rstrip()
        mastodon = Mastodon(client_id,client_secret,access_token,api_base_url)
        keys.close()

	mytoot = '+------------------+' + \
        	'|                  |' + \
        	'|        NO        |' + \
        	'|    DOUCHEBAGS    |' + \
        	'|                  |' + \
        	'+------------------+' + \
        	'         ||         ' + \
        	'         ||    @    ' + \
        	'___\/____||___\|/___'
	
	mastodon.toot(mytoot)
