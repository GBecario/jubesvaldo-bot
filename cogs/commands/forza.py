import discord
from discord.ext import commands
from discord import app_commands

class forza(commands.Cog):
    def __init__(self, client:commands.Bot):
        self.client: commands.Bot = client
    
    @app_commands.command(
        name="calculo_das_molas",
        description="faz o calcúlo da rigidez das molas da suspenção em libras"
    )
    @app_commands.describe(
        peso="Peso do veiculo",
        peso_dianteira="Porcentagem do peso do veiculo"
    )
    async def spring_calculation(self, interaction:discord.Interaction, peso: int, peso_dianteira: int):
        peso_traseira = (100 - peso_dianteira) / 100

        rigidez_dianteira = round((peso * (peso_dianteira / 100)) / 2, 2)
        rigidez_traseira = round((peso * peso_traseira) / 2, 2)

        await interaction.response.send_message(f"A rigidez dianteira é {rigidez_dianteira} lbs e a rigidez traseira é {rigidez_traseira} lbs.", ephemeral=False)

    @app_commands.command(
        name="calculo_dos_amortecedores",
        description="Calcúla a rigidez do retorno e da compressão dos amortecedores"
    )
    @app_commands.describe(
        rigidez_mola_dianteira="Rigidez da mola dianteira",
        rigidez_mola_traseira="Rigidez da mola traseira"
    )
    async def shock_absorber_calculation(self, interaction:discord.Interaction, rigidez_mola_dianteira: str, rigidez_mola_traseira: str):
        valor1 = rigidez_mola_dianteira[0] + "." + rigidez_mola_dianteira[1]
        valor2 = rigidez_mola_traseira[0] + "." + rigidez_mola_traseira[1]
        print(f"{valor1}")
        print(f"{valor2}")
        try:
            valor_convertido1 = float(valor1)
            valor_convertido2 = float(valor2)
        except ValueError:
            print("Não foi possível fazer o cálculo com os valores fornecidos.")
            await interaction.response.send_message("Não foi possível fazer o cálculo com os valores fornecidos.")
        
        retorno_dianteiro = round(valor_convertido1 + 1.0, 1)
        retorno_traseiro = round(valor_convertido2 + 1.0, 1)

        compressao_dianteira = round(retorno_dianteiro + (retorno_dianteiro * 0.50), 1)
        compressao_traseira = round(retorno_traseiro + (retorno_traseiro * 0.50), 1)

        await interaction.response.send_message(f"O retorno dianteiro é {retorno_dianteiro}, e o traseiro {retorno_traseiro}, a compressão dianteira é {compressao_dianteira}, e a traseira é {compressao_traseira}.", ephemeral=False)

    @app_commands.command(
        name="calculo_barra_estabilizadora",
        description="Calcúla a rigidez das barras estabilizadoras"
    )
    @app_commands.describe(
        peso_dianteira="Porcentagem do peso do veiculo"
    )
    async def stabilizer_bar_calculation(self, interaction:discord.Interaction, peso_dianteira: int):
        peso_traseira = (100 - peso_dianteira) / 100

        rigidez_dianteira = round(65 * (peso_dianteira / 100), 2)
        rigidez_traseira = round(65 * peso_traseira, 2)

        await interaction.response.send_message(f"A rigidez da barra estabilizadora dianteira é {rigidez_dianteira}, e a rigidez traseira é {rigidez_traseira}.", ephemeral=False)


async def setup(client: commands.Bot) -> None:
    await client.add_cog(forza(client))