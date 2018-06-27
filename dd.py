import sopel
from ddate.base import DDate

@sopel.module.commands('dd')
def dd(bot, trigger):
	bot.say(str(DDate()))
