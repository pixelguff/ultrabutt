import sopel
import subprocess as sp


@sopel.module.commands('ukdeathwatch')
def ukdeathwatch(bot, trigger):

    getpm = "curl https://www.gov.uk/government/ministers/prime-minister 2> /dev/null | grep Current | grep span | cut -d'>' -f3 | cut -d'<' -f1"

    process = sp.Popen(getpm, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
    pm, error = process.communicate()

    pm = pm.rstrip()

    pm = " ".join(pm.split())

    bot.say("Prime Minister: " + pm)

    getqueen = "curl https://en.wikipedia.org/wiki/Elizabeth_II 2> /dev/null | grep '6 February 1952' | grep Reign | cut -d'>' -f9 | cut -d'<' -f1"

    process = sp.Popen(getqueen, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
    queen, error = process.communicate()

    if "present" in queen:
        bot.say("Queen: Alive")
    else:
        bot.say("Queen: Taking a dirt nap")

    bot.say("Thatcher: Still dead")
