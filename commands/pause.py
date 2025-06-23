from discord.ext import commands
from utils.audio_handler import pause_audio

@commands.command(name='pause', aliases=['pausar'])
async def pause(ctx):
    await pause_audio(ctx)

