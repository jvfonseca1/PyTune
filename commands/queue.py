from discord.ext import commands
from utils.audio_handler import show_queue

@commands.command(name='queue', aliases=['fila', 'q'])
async def queue(ctx):
    await show_queue(ctx)
