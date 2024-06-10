import discord
import os
from discord.ext import commands
from myserver import server_on

 # ganti dengan token bot anda

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot ready")
    synced = await bot.tree.sync()
    print(f"(len{synced}) command(s)")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1239224281284481134)
    text = f"Hello World, {member.mention}!"

    emmbed = discord.Embed(title = 'Welcome to My World', description = text, color = 0x66ffff)

    await channel.send(text)
    await channel.send(embed = emmbed)
    await member.send(text)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1249552387476295780)
    text = f"{member.name} has left the server!"
    await channel.send(text)

@bot.event
async def on_message(message):
    mes = message.content
    if 'หวัดดี' in mes:
        await message.channel.send("หวัดไม่ดีนะ")

    elif 'บอท' in mes :
        await message.channel.send("ผมบอทเองครับ" + str(message.author.name))

    await bot.process_commands(message)


@bot.command()
async def hello(ctx):
    await ctx.send('Hello, {}! Jangan lupa subscribenya ya :)'.format(ctx.author.name.title()))

server_on()
bot.run(os.getenv("TOKEN"))
