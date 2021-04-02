import discord
import main

@app.command()
async def hello(ctx):
    await ctx.send('Hello')