import discord
from discord import app_commands
import re

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

que = "بـــــابـــــای تـــــو کــــــیـــــه ؟"

@tree.command(name = "papa", description = "generate ComixZone funny and stereotypy Farsi question") #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def papa_command(interaction ,user : discord.User):
    await interaction.response.send_message(f'{re.sub(r'\s+\#d+',r'\@\s+',user)} {que}')
@client.event
async def on_ready():
    await tree.sync()
    print("Ready!")
client.run('MTA5NTA0NDY4Mjg0Njg0MzA2MQ.GGQ2bW.UqS9kUQxh55X4bem3iXosg0E8n_QHaPbGqVwLs')