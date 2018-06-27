import sopel, tweepy, time, sys, os

@sopel.module.commands('tweet')
def tweet(bot, trigger):

        keys = open(os.getcwd()+"/SECRET_SAUCE/twitter.txt","r")

	CONSUMER_KEY = keys.readline().rstrip()
	CONSUMER_SECRET = keys.readline().rstrip()
	ACCESS_KEY = keys.readline().rstrip()
	ACCESS_SECRET = keys.readline().rstrip()
        
        keys.close()

	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)
 
	#api.update_status("HELLO, THIS WAS POSTED FROM A SCRIPT")
	mytweet = trigger.split(' ', 1)[1] 
	api.update_status(mytweet)
