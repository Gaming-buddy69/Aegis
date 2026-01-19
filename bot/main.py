import discord, os
from discord.ext import commands
from bot.config import TOKEN, PREFIX

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"Aegis online as {bot.user}")
    await bot.tree.sync()

async def load_cogs():
    for f in os.listdir("bot/cogs"):
        if f.endswith(".py"):
            await bot.load_extension(f"bot.cogs.{f[:-3]}")

@bot.event
async def setup_hook():
    await load_cogs()

bot.run(TOKEN)
