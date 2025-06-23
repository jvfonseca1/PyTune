from discord.ext import commands
from utils.audio_handler import skip_audio

@commands.command(name='skip', aliases=['next'])
async def skip(ctx):
    await skip_audio(ctx)
