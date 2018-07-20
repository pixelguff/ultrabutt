import sopel
from googlesearch import search

@sopel.module.commands('goog')
def goog(bot, trigger):
	arg_list = trigger.split(" ", 1)
	try:
		for url in search(str(arg_list[1]), stop=1):
			result = str(url)
	except:
		result = "Dunno, mate."
	bot.say(result)
