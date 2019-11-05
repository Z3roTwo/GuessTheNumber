import discord
import random

loop = True
guess = 0
number = 0
rounds = 0
name = 0

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('$start'):
        number = random.randint(1, 10)
        await message.channel.send('Ok the bot has chosen a number!')
    if message.content.startswith('$1'):
        await message.channel.send(number)
    if message.content.startswith('1' or '2' or '3' or '5' or '6' or '7' or '8' or '9'):
        guess = message.content
        if guess > number:
            await message.channel.send("Aw too bad that's the wrong number, it's too high! :(")
        elif guess < number:
            await message.channel.send("Aw too bad that's the wrong number, it's to low! :(")
        elif guess == number:
            await message.channel.send("Congrats you did it! The number was and it only took you rounds :D")
        else:
            pass

client.run('token :(')