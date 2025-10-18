import discord
from discord.ext import commands
from discord import app_commands
from datetime import date
from db.conection import start_conn, finish_conn

class user(commands.Cog):
    def __init__(self, client:commands.Bot):
        self.client: commands.Bot = client

    @app_commands.command(
        name="aniversario",
        description="Guarda o aniversario de um membro." 
    )
    @app_commands.describe(
        birthday_date="Data de aniversário do membro",
        member_name="Nome do membro",
        member_mention_name="Menção do membro"
    )
    async def member_birthdate(self, interaction:discord.Interaction, birthday_date: str, member_name: str, member_mention_name: str):
        # Inicia a conexão com o banco de dados
        connection = start_conn()
        
        # Formata a data fornecida no formato americano
        day = int(birthday_date[0:2])
        month = int(birthday_date[3:5])
        year = int(birthday_date[6:10])
        birthday_date1 = date(year, month, day)

        # Inicia o cursor    
        cursor = connection.cursor()

        # Executa uma inserção no banco de dados
        cursor.execute(f"INSERT INTO members_birthday(member_birthdate, member_name, member_mention_name) VALUES(%s, %s, %s)", (birthday_date1, member_name, member_mention_name))
        connection.commit()

        # Executa uma busca no banco de dados
        cursor.execute("SELECT m.member_birthdate_id, m.member_birthdate, m.member_name, m.member_mention_name from public.members_birthday m ORDER BY m.member_birthdate_id, member_birthdate_id ASC")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        # Encerra o cursor e a conexão com o banco de dados
        cursor.close()
        finish_conn(connection)

        # Envia uma menssagem confirmando a inserção
        await interaction.response.send_message("Inserção feita com sucesso.")

# Adiciona o cog ao bot
async def setup(client: commands.Bot) -> None:
    await client.add_cog(user(client))