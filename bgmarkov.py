import sopel
import markovify
import os

@sopel.module.commands('markov')
def markov(bot, trigger):
	# Get raw text as string.
	f = open("os.getcwd()+"/all_of_bgtopics.txt", "r")
	text = f.read()

	# Build the model.
	text_model = markovify.Text(text)

	bot.say(text_model.make_short_sentence(140))

