import sopel
from PyDictionary import PyDictionary
import random


@sopel.module.commands('lookup')
def wk(bot, trigger):
    arg_list = trigger.split(" ", 1)
    try:
        # if arg_list[1].lower() == "random":
        #	wrandom = wik.random()
        #	result = "Random article - '" + wrandom + "': " + wik.summary(wrandom, sentences=1)
        # else:
        #	result = wik.summary(str(arg_list[1]), sentences=1)
        mydict = PyDictionary()
        myresult = mydict.meaning(arg_list[1].lower())
        mykeys = myresult.keys()
        result = random.choice(myresult[random.choice(mykeys)])
    except:
        result = "Dictionary lookup failed due to complex computer reasons and/or dickery-fuckery."

    bot.say(arg_list[1].lower() + ": " + result)
