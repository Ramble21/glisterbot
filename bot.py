import discord
from discord import app_commands
import json

token = None
with open('config.json') as file:
    token = json.loads(file.read())['token']

client = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(client)
default_color = 0x1f8b4c
neutral_color = 0x2b2d31

def commafy(number):
    return '{:,}'.format(number)

#import poker
#import profanity

# importCommand('frequency')
# importCommand('top_messagers')
# importCommand('wordbomb')
# importCommand('profanity')
# importCommand('quote')
# importCommand('guess')
# tree.add_co


# import guess
# guess.client = client
# tree.add_command(guess.export.callback)

# importCommand('trivia')
# importCommand('rankings')

@client.event
async def on_ready():
    await tree.sync()
    print('tree synced')
