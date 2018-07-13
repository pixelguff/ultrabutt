import sopel
import wikipedia as wk

@sopel.module.commands('wiki')
def wiki(bot, trigger):
        result = wk.summary(trigger, sentences=1)
	bot.say(result)
