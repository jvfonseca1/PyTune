from discord.ext import commands
from utils.audio_handler import stop_audio

@commands.command(name='stop', aliases=['s'])
async def stop(ctx):
    await stop_audio(ctx)
