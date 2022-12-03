import discord
from discord.ext import commands

from services.bot.register import register_user
from services.bot.swap import swap_currency
from services.bot.transfer import erc721, erc20, eth

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = False
intents.message_content = False

bot = commands.Bot(command_prefix='/', description=description, intents=intents)

token = 'token goes here'


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def register(ctx):
    register_user(ctx.author.id)
    await ctx.send("this will register users")

@bot.command(description="transfers eth")
async def transfer_eth(ctx, to_address, amount):
    eth(to_address, amount)
    await ctx.send("this will transfer " + amount + " eth to " + to_address)


@bot.command()
async def transfer_nft(ctx, token_address, to_address, token_id):
    erc721(to_address, token_address, token_id)
    await ctx.send("(nft) this will transfer " + token_id + " " + token_address + " to " + to_address)


@bot.command()
async def transfer_erc20(ctx, token_address, to_address, amount):
    erc20(to_address, token_address, amount)
    await ctx.send("(erc20) this will transfer " + amount + " " + token_address + " to " + to_address)


@bot.command()
async def swap(ctx, from_currency, to_currency, from_amount):
    swap_currency(from_currency, to_currency, from_amount)
    await ctx.send("this will swap " + from_amount + " " + from_currency + " to " + to_currency)

bot.run(token)