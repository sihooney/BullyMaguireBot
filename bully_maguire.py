import discord
from random import choice

class BullyMaguire(discord.Client):

    spidey_keywords = "spider", "peter", "parker", "maguire", "bully"
    jonah_keywords = "john", "jonah", "jameson", "bugle", "jjj"

    async def on_ready(self):
        print('We have logged in as {}'.format(client.user))
    
    async def on_message(self, message: discord.Message):
        lower = message.content.lower()
        if message.author != self.user.id:
            for word in self.spidey_keywords:
                if word in lower:
                    with open("spidey_quotes.txt", "r", encoding="utf-8") as f:
                        quotes = f.readlines()
                        await message.channel.send(choice(quotes))
                    break
            for word in self.jonah_keywords:
                if word in lower:
                    with open("john_jonah_jameson.txt", "r", encoding="utf-8") as f:
                        quotes = f.readlines()
                        await message.channel.send(choice(quotes))
                    break


client = BullyMaguire()
client.run("token")
