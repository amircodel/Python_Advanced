import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True

que = "بـــــابـــــای تـــــو کــــــیـــــه ؟"

bot = commands.Bot(command_prefix='/', case_insensitive=True, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Customize a command
@bot.command(name='papa', help='Can generate a funny and stereotypy Farsi question')
# @commands.cooldown(1, 5, commands.BucketType.user)
async def papa_command(ctx, name : str):
    await ctx.send(f'{name} {que}')

# Add papa command if it not exists
if not bot.get_command('papa'):
    bot.add_command(papa_command)

# Enable command auto-complete suggestion feature in Discord
bot.remove_command('help')
bot.load_extension("jishaku")

bot.run('MTA5NTA0NDY4Mjg0Njg0MzA2MQ.GGQ2bW.UqS9kUQxh55X4bem3iXosg0E8n_QHaPbGqVwLs')