from random import choice

import discord

client = discord.Client()

ballChoices = (
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",
)

# Define events
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Rat emoji function
    lowerCaseMessage = message.content.lower()
    lowerCaseMessage = ''.join(lowerCaseMessage.split())
    
    if (("rat" in lowerCaseMessage) or (client.user in message.mentions)):
        ratMessage = lowerCaseMessage
        ratNum = ratMessage.count("rat")
        ratNum += ratMessage.count("671793984435126277")      
        await message.channel.send(':rat: ' * ratNum)

    # Magic 8 Ball function
    if message.content.startswith("!oracle"):
        # Thanks @PlusReed this is much better
        try:
            ballResult = choice(ballChoices)
            await message.channel.send("{0.author.mention} Squeek squeek! ({1})".format(message, ballResult))
        except:
            await message.channel.send("Squeek squeek... (Something went wrong, make <@457637280539082763> fix it...")

client.run('TOKEN')
