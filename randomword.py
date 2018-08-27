import sopel
from PyDictionary import PyDictionary
import random

@sopel.module.commands('randomword')
def wk(bot, trigger):
	arg_list = trigger.split(" ", 1)
	try:
		wordlist = []

		with open('/usr/share/dict/words') as f:
			lines = f.read().splitlines()

		for line in lines:
			if "'" not in line:
				wordlist.append(line)
		word = random.choice(wordlist)
		
		#if arg_list[1].lower() == "random":
		#	wrandom = wik.random()
		#	result = "Random article - '" + wrandom + "': " + wik.summary(wrandom, sentences=1)
		#else:
		#	result = wik.summary(str(arg_list[1]), sentences=1)
		mydict = PyDictionary()
		myresult = mydict.meaning(word.lower())
		mykeys = myresult.keys()
		result = random.choice(myresult[random.choice(mykeys)])
	except:
		result = "Dictionary lookup failed due to complex computer reasons and/or dickery-fuckery."

	bot.say(word.lower()+": "+result)
