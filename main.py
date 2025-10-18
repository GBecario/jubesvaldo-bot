import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

class jubesvaldoInit(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix="!",
            intents=intents
        )

    async def setup_hook(self):
        
        diretorio = "cogs"
        for root, dirs, files in os.walk(diretorio):
            for file in files:
                if file.endswith(".py") and file != "__init__.py":
                    path = os.path.join(root, file).replace("\\", "/").replace("/",".")[:-3]
                    await self.load_extension(path)
        
        await self.tree.sync()
    
    async def on_ready(self):
        print("Bot inicializado.")

bot = jubesvaldoInit()

bot.run(DISCORD_TOKEN)