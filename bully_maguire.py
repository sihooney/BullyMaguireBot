import discord
from random import choice

class BullyMaguire(discord.Client):

    spidey_keywords = "spider", "peter", "parker", "maguire", "bully"
    jameson_keywords = "john", "jonah", "jameson", "bugle", "jjj"

    with open("spidey_quotes.txt", "r", encoding="utf-8") as f:
        peter_quotes = f.readlines()
    
    with open("john_jonah_jameson.txt", "r", encoding="utf-8") as f:
        jameson_quotes = f.readlines()

    async def on_ready(self):
        print('We have logged in as {}'.format(self.user))
    
    async def on_message(self, message: discord.Message):
        if self.user.mentioned_in(message):
            await message.reply("I'm gonna put some dirt in your eye")
            return
        lower = message.content.lower()
        if message.author != self.user.id:
            for word in self.spidey_keywords:
                if word in lower:
                    await message.channel.send(choice(self.peter_quotes))
                    break
            for word in self.jameson_keywords:
                if word in lower:
                    await message.channel.send(choice(self.jameson_quotes))
                    break


client = BullyMaguire()
client.run(token")
