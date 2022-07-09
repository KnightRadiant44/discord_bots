import discord
import random

TOKEN = '(TOKEN here)'

'''Connect to the client and make the bot come online'''
client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

''''''

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user: #making sure the bot doesn't respond to itself
        return
    
    if message.channel.name == 'hometown-of-silence': #making sure that the bot responds ONLY in a certain channel. This is to prevent the bot from responding everywhere. this is also for the bot to start chatting
        if user_message.lower() == "hello": #notice the .lower() -> this is necessary in order for the bot to recognize the message. Bots only recognize LOWERCASE messages.
            await message.channel.send(f'Hello {username}!')
            return
        if user_message.lower() == "bye": #cue for the bot to stop chatting
            await message.channel.send(f'See you later {username}!')
            return
        if user_message.lower() == "!random": #any random response for the bot
            response = f'This is your random number: {random.randrange(10000000)}'
            await message.channel.send(response)
            return
    if user_message.lower() == "!anywhere":
        await message.channel.send('This can be used anywhere!')
        return

client.run(TOKEN)