import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os
import re

load_dotenv()
ADM_ID = int(os.getenv("ADM_ID"))
GUILD_ID = int(os.getenv("GUILD_ID"))

class moderation(commands.Cog):
    def __init__(self, client:commands.Bot):
        self.client: commands.Bot = client

    def search_bad_words(content: str):
        # Lista de palavrões
        bad_words = ["Cacete", "Puta merda", "Porra", "Caralho", "Carai", "Puta que Pariu", "Filho da Puta", "Foda-se", "Foder", "Cu", "Puta", "Bicha", "Viado", "Buceta", "Bosta", "Merda"]

        # Cria os padrões que serão usados na busca
        patterns = re.compile(r'\b(' + '|'.join(bad_words) + r')\b', re.IGNORECASE)

        # Se uma das palavras for encontrada na string ele retorna True
        if patterns.search(content):
                return True

    @commands.Cog.listener()
    async def on_message(self, msg: discord.Message):
        # Busca o servidor especificado
        guild = await self.client.fetch_guild(GUILD_ID)

        # Se o servidor da menssagem for o especificado ele contiua senão retorna nada
        if msg.guild == guild:
            # Se a função retornar True envia uma menssagem ao adm avisando sobre tal menssagem referenciando o autor da menssagem e a menssagem em si senão retorna nada
            if moderation.search_bad_words(msg.content) == True:
                print(msg.content)
                adm_member = await self.client.fetch_user(ADM_ID)

                try:
                    dm_channel = await self.client.create_dm(adm_member)
                    await dm_channel.send(f"O membro {msg.author} enviou a seguinte messagem: '{msg.content}'")
                except discord.Forbidden as f:
                    print(f)
                except Exception as e:
                    print(e)

                return
            else:
                return
        else:
            return

    @commands.Cog.listener()    
    async def on_message_edit(self, msg_before:discord.Message, msg_after:discord.Message):
        # Busca o servidor especificado
        guild = await self.client.fetch_guild(GUILD_ID)

        # Se o servidor da menssagem for o especificado ele contiua senão retorna nada
        if msg_after.guild == guild:
            # Se a função retornar True envia uma menssagem ao adm avisando sobre tal menssagem referenciando o autor da menssagem e a menssagem em si senão retorna nada
            if moderation.search_bad_words(msg_after.content) == True:
                print(msg_before.content)
                print(msg_after.content)
                adm_member = await self.client.fetch_user(ADM_ID)

                try:
                    dm_channel = await self.client.create_dm(adm_member)
                    await dm_channel.send(f"O membro {msg_after.author} alterou a seguinte messagem: '{msg_before.content}', para está '{msg_after.content}'")
                except discord.Forbidden as f:
                    print(f)
                except Exception as e:
                    print(e)
            else:
                return
        else:
            return

async def setup(client: commands.Bot) -> None:
    await client.add_cog(moderation(client))