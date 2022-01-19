import os
import discord
from function_callback import *

client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$price'):
        await message.channel.send(price(message.content[7:]))

    if message.content.startswith('$supply'):
        await message.channel.send(supply(message.content[8:]))


client.run('OTMwMDM4NzYxNTUzNzk3MTIw.YdwEGA.iFzOUhwTo0FRbXhekgmTHycqaGY')
