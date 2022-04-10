import discord
import random

class BullyMaguire(discord.Client):

    CMD = "!spider"

    async def on_ready(self):
        print("Bot ready")
    
    async def on_message(self, message: discord.Message):
        if self.CMD in message.content and message.author != self.user.id:
            with open("spidey_quotes.txt", "r", encoding="utf-8") as f:
                quotes = f.readlines()
                await message.channel.send(random.choice(quotes))

client = BullyMaguire()
client.run("token")
