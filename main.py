import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {@.user}`'.format(client))

# onmessage -> 모든 메세지를 받았을 때 실행된다.
@client.event
async def onmessage(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello')

client.run('your token here')


