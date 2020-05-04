#--[Discord spammer I created with little to none coding knowledge, so expect bugs or instability :)]--#
#--[This bot is a self bot, designed to reply to a user with a custom message then mention them]--#
#--[Lots of things aren't necessary so if you want to clean this up, be my guest]--#

import discord
import asyncio
import random
from discord.ext import commands
from discord.ext.commands import Bot



client = discord.Client()
approved = [USER ID HERE] #--[IMPORTANT: replace this with the channel ID in a server, enable developer mode then right click a channel and hit 'copy ID']--#
messages = ["EXAMPLE MESSAGE {0.mention}", "EXAMPLE MESSAGE 2"]

client = commands.Bot(command_prefix=prefix, self_bot=True)
client.remove_command("help")

@client.event
async def on_message(message):
	if not message.author.id == USER ID HERE: #--[IMPORTANT: Replace this with the User ID of the bot account or it will spam itself (unless that's what u want)]--#
		author = message.author
		if message.channel.id in approved:
			await message.channel.send(random.choice(messages).format(author)) #--[Replace the text, don't remove 0.mention unless u don't want it to mention them, or change it to 0.name so it just repeats the name]


client.run("TOKEN HERE", bot=False) #--[IMPORTANT: Find your account token and pop it into here]--#




#note for future self: this is discord.py 1.2.2, i think it's rewrite but maybe not
#await message.channel.send is for rewrite
#await client.send_message is official (it could be vice versa)

#instead of mentioning u can do {0.name}
