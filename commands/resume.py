from discord.ext import commands
from utils.audio_handler import resume_audio

@commands.command(name='resume', aliases=['retomar', 'continuar'])
async def resume(ctx):
    await resume_audio(ctx)
