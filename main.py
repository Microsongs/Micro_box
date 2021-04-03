import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# .env file 로드
load_dotenv(verbose=True)
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
YOUTUBE_TOKEN = os.getenv('YOUTUBE_TOKEN')

#app의 커맨드 접두사 -> -로 하였으므로 명령어는 -로 시작한다
app = commands.Bot(command_prefix='-')

@app.event
async def on_ready():
    print('We have logged in as {@.user}`'.format(app))
    print('Connection was successful')
    await app.change_presence(status=discord.Status.online, activity="Listening the Music")

# onmessage -> 모든 메세지를 받았을 때 실행된다.
@app.event
async def onmessage(message):
    if message.author == app.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello')

@app.command(aliases=['안녕','hello','こんにちは'])
async def welcome(ctx):
    await ctx.send('hello')

app.run(DISCORD_TOKEN)


