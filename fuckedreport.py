import sopel 
from subprocess import *
import string
import time 
from datetime import date

@sopel.module.commands('fuckedreport')
def fuckedreport(bot, trigger):
	bot.say("Fucked Report: Oh God. Everything's on fire. Abandon ship!")	
# get pound value
#        raw_output = check_output(['curl','-s','https://www.xe.com/currencyconverter/convert/?From=GBP&amp;To=USD'])
#	index = raw_output.find("1 GBP")
#	hack = raw_output.split("1 GBP")

#	try:
#		hack2 = hack[2].split("USD")
#	except:
#               pass

#	hack3 = hack2[0].split(" = ")
#	pound_value = hack3[1]
#	bot.say("The Pound is worth: " + pound_value[:4] + " USD.")

# Thatcher
#	if str(time.strftime("%d%m")) == "0104":
#		bot.say("Is Thatcher still dead: No. Run.")
#	else: 
#		bot.say("Is Thatcher still dead: Yes.")
#		bot.say("Farage: Cunt.")
#		bot.say("Tories: Fucked it.")

# Brexmas
#	d0 = date(2016, 06, 23)
#	d1 = date.today()

#	brexit_days = str((d1 - d0)).split(",")[0]
#	brexit_days += ". "

#	if str(time.strftime("%d%m")) == "2306":
#		brexit_days += "Merry Brexmas!"

#	bot.say("Number of days since The Brexiting: " + brexit_days)

#       bot.say("Fucked report: Not Fucked")
