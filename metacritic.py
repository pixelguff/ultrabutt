import sopel
import bs4
from bs4 import BeautifulSoup
import urllib2
import sys
from string import *

@sopel.module.commands('MC')
def metafetch(bot, trigger):

	arg_list = split(trigger)
	if len(arg_list) < 3:
		bot.say('Usage: .MC platform Full Game Title')
	        bot.say('Platforms are: ps1,ps2,ps3,ps4,psp,psvita,xbox,360,xbone,dreamcast,n64,gamecube,wii,wiiu,switch,gba,ds,3ds,pc')
	else:
		platforms = [
		"ps1",
		"ps2",
		"ps3",
		"ps4",
		"psp",
		"psvita",
		"xbox",
		"360",
		"xbone",
		"dreamcast",
		"n64",
		"gamecube",
		"wii",
		"wiiu",
		"switch",
		"gba",
		"ds",
		"3ds",
		"pc"
		]

		platform = arg_list[1].lower()
		if platform not in platforms:
			bot.say("Because you didn't pick a valid platform, I'm defaulting to 'xbone' to mock you.")
			platform = "xbone"
		
		
		if platform == "ps3":
		        platform = "playstation-3"
		elif platform == "ps4":
		        platform = "playstation-4"
		elif platform == "ps1":
		        platform = "playstation"
		elif platform == "ps2":
		        platform = "playstation-2"
		elif platform == "xbone":
		        platform = "xbox-one"
		elif platform == "wiiu":
		        platform = "wii-u"
		elif platform == "switch":
                        platform = "switch"
		elif platform == "psvita":
		        platform = "playstation-vita"
		elif platform == "gba":
		        platform = "game-boy-advance"
		elif platform == "n64":
		        platform = "nintendo-64"
		elif platform == "360":
		        platform = "xbox-360"


		del(arg_list[0])
		del(arg_list[0])

		game = []

		for word in arg_list:
			game.append(word.lower())
			game.append("-")
		del(game[-1])

		gamestring = "".join(game)

		gamestring = gamestring.replace(":","")
		gamestring = gamestring.replace("'","")
		gamestring = gamestring.replace("\"","")
		gamestring = gamestring.replace("&'","and")
		gamestring = gamestring.replace("%","")
		gamestring = gamestring.replace("/","")
		gamestring = gamestring.replace("*","")
		gamestring = gamestring.replace("!","")
		
		##### START THE ACTUAL SHIT! ######

		opener = urllib2.build_opener()
		opener.addheaders = [('User-agent', 'Mozilla/5.0')]
		try:
			webpage = opener.open("http://www.metacritic.com/game/"+platform+"/"+gamestring)
		except urllib2.HTTPError, e:
			bot.say("Oopsie. I done an http boo boo.")
			
		else:
			html = webpage.read()
			opener.close()

			soup = BeautifulSoup(html)

			result = soup.find_all(attrs={"itemprop": "ratingValue"})

			if len(result) != 0:
			        score = result[0].text
				bot.reply("I found it, and it scored: "+score)
			else:
			        bot.reply("I couldn't find it. Either it's not on Metacritic, or you typed the name wrong with your stupid chimp fingers.")


