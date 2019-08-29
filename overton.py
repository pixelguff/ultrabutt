import sopel


@sopel.module.commands('overton')
def overton(bot, trigger):
    mystring = trigger.split(' ', 1)[1]

    outputstring = ''

    for idx, letter in enumerate(mystring):
        if letter == "o":
            outletter = "overto"
        elif letter == "O":
            try:
                if mystring[idx + 1].isupper() == True:
                    outletter = "OVERTO"
                else:
                    outletter = "Overto"
            except:
                outletter = "OVERTO"

        else:
            outletter = letter
        outputstring = outputstring + outletter

    bot.reply(outputstring)
