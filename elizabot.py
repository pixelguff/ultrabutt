import sopel
import eliza


@sopel.module.commands('eliza')
# @sopel.module.nickname_commands("\ *")
def elizabot(bot, trigger):
    usercommand = trigger.split(' ', 1)[1]

    el = eliza.eliza()

    response = el.respond(usercommand)

    bot.reply(response)
