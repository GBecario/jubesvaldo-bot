import discord
from discord.ext import commands, tasks
from discord import app_commands
from datetime import date, datetime
from db.conection import start_conn, finish_conn
import os
from dotenv import load_dotenv

load_dotenv()
CONVERSATION_ID = os.getenv("CONVERSATION_ID")

class user_tasks(commands.Cog):
    def __init__(self, client:commands.Bot):
        self.client: commands.Bot = client
        self.on_member_birthday.start()
    
    # Transforma a função em tarefa e determina que ela será executada a cada 24 horas
    @tasks.loop(hours=24)
    async def on_member_birthday(self):
        channel_id = CONVERSATION_ID
        bot_date = "09-13"
        
        # Busca o canal do servidor pelo id
        message_channel = await self.client.fetch_channel(channel_id)
        
        # Inicia a conexão com o banco de dados e executa uma busca no banco de dados
        connection = start_conn()
        cursor = connection.cursor()
        cursor.execute("SELECT m.member_birthdate_id, m.member_birthdate, m.member_name, m.member_mention_name from public.members_birthday m ORDER BY m.member_birthdate_id, member_birthdate_id ASC")
        rows = cursor.fetchall()
        print(rows)

        # Inicia uma lista vazia e formata a data atual
        birthdays = []
        now = datetime.now()
        today = now.strftime('%m-%d')

        # Insere os dados da busca na lista
        for row in rows:
            i = 0
            birthdays.insert(i, row)
            i += 1

        for birthday in birthdays:
            # Transforma a data em string e extrai o mês e o dia
            birthdate = str(birthday[1])
            birthdate_corresp = birthdate[5:10]
            
            # Verifica se a data atual é igual a data de um aniversário
            if today == birthdate_corresp:
                # Se houver um aniversário no dia envia uma menssagem de feliz aniversário com uma menção ao membro aniversariante
                await message_channel.send(f"Hoje é o aniversário de {birthday[3]}.")
                await message_channel.send(f"Feliz aniversário {birthday[3]}.")
            elif today == bot_date and birthdate_corresp == bot_date: 
                # Se for o aniversário do bot envia uma menssagem de feliz aniversário para o para o próprio bot
                await message_channel.send(f"Hoje é meu aniversário!")
                await message_channel.send(f"Parabéns pra mim!")
            else:
                # Se não houver nenhum aniversário no dia, retorna nada
                print(today == birthdate_corresp)
        
        # Encerra o cursor e a conexão com o banco de dados
        cursor.close()
        finish_conn(connection)

# Adiciona o cog ao bot
async def setup(client: commands.Bot) -> None:
    await client.add_cog(user_tasks(client))