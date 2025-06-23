from discord.ext import commands
from utils.audio_handler import clear_queue

@commands.command(name='clear', aliases=['limpar'])
async def clear(ctx):
    await clear_queue(ctx)
