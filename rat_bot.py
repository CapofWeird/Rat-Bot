from random import choice
from dotenv import load_dotenv
import os

# Load from .env
load_dotenv()

import discord

client = discord.Client()

activity_type = discord.ActivityType.listening
activity_name = "squeaks"
prefix = "!"

ball_choices = (
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
    "Very doubtful."
)

coin_choices = ( "Heads", "Tails")

# Define events
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(f'Setting presence to {activity_name}')
    print('Prefix is ' + '"' + prefix + '"')
    
    activity = discord.Activity(type=activity_type, name=activity_name)
    await client.change_presence(activity=activity)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # Rat emoji function
    lower_case_message = message.content.lower()
    lower_case_message = ''.join(lower_case_message.split())
    
    if (("rat" in lower_case_message) or (client.user in message.mentions)):
        rat_message = lower_case_message
        rat_num = rat_message.count("rat")
        rat_num += rat_message.count("671793984435126277")      
        await message.channel.send(':rat: ' * rat_num)
            
    # Magic 8 Ball function
    if message.content.startswith(prefix + "oracle"):
        # Thanks @PlusReed this is much better
        try:
            ball_result = choice(ball_choices)
            await message.channel.send(
                "Squeek squeek! ({0})".format(ball_result),
                mention_author=True, # Mention the user
                reference=message # Set message_reference to the message.
            )
        except:
            await message.channel.send(
                "Squeek squeek... (Something went wrong, make <@457637280539082763> fix it...",
                mention_author=True,
                reference=message
            )
            
    # Coin function
    if message.content.startswith(prefix + "coin"):
        try:
            coin_result = choice(coin_choices)
            await message.channel.send(
                "Squeek squeek! :coin: ({0})".format(coin_result),
                mention_author=True, # Mention the user
                reference=message # Set message_reference to the message.
            )
        except:
            await message.channel.send(
                "Squeek squeek... (Something went wrong, make <@457637280539082763> fix it...",
                mention_author=True,
                reference=message
            )

client.run(os.getenv('TOKEN'))
