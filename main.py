import discord
import function_callback

cmc_api_key = '2fb74590-7a69-4d74-823d-a1f4e495b147'
discord_api_key = 'OTMwMDM4NzYxNTUzNzk3MTIw.YdwEGA.iFzOUhwTo0FRbXhekgmTHycqaGY'

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(message.content())
    if message.content.startswith('&price'):

        await message.channel.send('Hello!')

client.run(discord_api_key)