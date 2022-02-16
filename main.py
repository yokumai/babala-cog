import discord
from discord.ext import commands, tasks
import random
import asyncio
import json
import keep_alive
import time
import os
from datetime import datetime
from random import randrange
#from cmds import music
from core.classes import Cog_Extension
#from cmds import Music



i = 0
stop = 0
wr1 = ""
wr2 = ""
wr3 = ""
wr4 = ""
wr5 = ""
month1 = 0
date1 = 0

#game = "垃圾Programming"
#status_w = discord.Status.online
#status_n = "online"
#activity_w = discord.Activity(type=discord.ActivityType.watching, name=game)



with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)


bot = commands.Bot(command_prefix='[', intents = discord.Intents.all())


for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'載入**{extension}**完成')
    await ctx.message.delete()


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'卸載**{extension}**完成')
    await ctx.message.delete()


@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'重新-載入**{extension}**完成')
    await ctx.message.delete()

@bot.command()
async def reload_all(ctx):
  for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
      bot.reload_extension(f'cmds.{filename[:-3]}')
    await ctx.send(f'重新-載入完成')
    await ctx.message.delete()

@bot.event
async def on_ready():
    global status_w, activity_w, game
    print(">>Bot is online")
    #discord.Status.<狀態>，可以是online（上線）,offline（下線）,idle（閒置）,dnd（請勿打擾）,invisible（隱身）
    Game_status = jdata['Game_status']
    status_w = jdata['Bot_status']
    if status_w == "online":
      Bot_status = discord.Status.online
    elif status_w == "idle":
      Bot_status = discord.Status.idle
    elif status_w == "dnd":
      Bot_status = discord.Status.dnd
    elif status_w == "invisible":
      Bot_status = discord.Status.invisible
    
    #type可以是playing（遊玩中）、streaming（直播中）、listening（聆聽中）、watching（觀看中）、custom（自定義）
    #game = "世界計畫 繽紛舞台！feat.初音未來"
    
    Game_activity = discord.Activity(type=discord.ActivityType.watching,name=Game_status)
    await bot.change_presence(status=Bot_status, activity=Game_activity)


@bot.command()
async def clean(ctx,num:int):
    await ctx.message.delete()
    await ctx.channel.purge(limit=num)


keep_alive.keep_alive()

if __name__ == "__main__":
  bot.run(jdata['TOKEN'])