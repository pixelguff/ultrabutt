import sopel
import wikipedia as wik


@sopel.module.commands('wk')
def wk(bot, trigger):
    arg_list = trigger.split(" ", 1)
    try:
        if arg_list[1].lower() == "random":
            wrandom = wik.random()
            result = "Random article - '" + wrandom + \
                "': " + wik.summary(wrandom, sentences=1)
        else:
            result = wik.summary(str(arg_list[1]), sentences=1)

    except wik.exceptions.DisambiguationError as e:
        result = "DISAMBIGULATOR: Did you mean one of these?"
        for option in e.options:
            result = result + " '" + str(option) + "'"
    except:
        result = "Wiki done a poo poo in its pantsies. Or you've searched for something that's not a thing."
    bot.say(result)
