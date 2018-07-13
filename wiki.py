import sopel
import wikipedia as wik

@sopel.module.commands('wk')
def wk(bot, trigger):
	arg_list = trigger.split(" ", 1)
	try:
		result = wik.summary(str(arg_list[1]), sentences=1)
	except wik.exceptions.DisambiguationError as e:
		result = "DISAMBIGULATOR: Did you mean one of these?"
	        for option in e.options:
        	        result = result+" '"+str(option)+"'"
	bot.say(result)
