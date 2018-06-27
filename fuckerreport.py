import sopel
import time
from random import randint

@sopel.module.commands('fuckerreport')
def fuckerreport(bot, trigger):
	bot.reply("YOU. IT IS YOU WHO ARE THE FUCKER.")
	time.sleep(randint(10,20))
	bot.reply("YOU.")

