import discord
from discord.ext import commands
from discord import app_commands

class conversation(commands.Cog):
    def __init__(self, client:commands.Bot):
        self.client: commands.Bot = client
    
    @commands.Cog.listener()
    async def on_message(self, message:discord.Message):
        if message.content.startswith("Olá jubesvaldo") and message.content.endswith("tudo bem?") and message.channel.category_id == 1364692042147561482:
            print(f"Autor: {message.author}")
            print(f"message: {message.content}")
            await message.reply(f"Olá {message.author.mention}, por aqui está tudo bem!")
        elif message.content.startswith("Olá jubesvaldo") and message.channel.category_id == 1364692042147561482:
            print(f"Autor: {message.author}")
            print(f"message: {message.content}")
            await message.reply(f"Olá {message.author.mention}, tudo bem?")
        else:
            return
    
async def setup(client: commands.Bot) -> None:
    await client.add_cog(conversation(client))