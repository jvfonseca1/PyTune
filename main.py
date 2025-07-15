import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# # Registro de comandos
from commands.play import play
from commands.stop import stop
from commands.skip import skip
from commands.queue import queue
from commands.clear import clear
from commands.pause import pause
from commands.resume import resume

from utils.logger import logger

# Carrega variáveis de ambiente
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = "!"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# Carrega comandos do diretório
@bot.event
async def on_ready():
    logger.info(f'Bot conectado como {bot.user}')

bot.add_command(play)
bot.add_command(stop)
bot.add_command(skip)
bot.add_command(queue)
bot.add_command(clear)
bot.add_command(pause)
bot.add_command(resume)

bot.run(TOKEN)
