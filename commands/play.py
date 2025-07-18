from discord.ext import commands
from utils.audio_handler import play_audio

@commands.command(name='play', aliases=['p'], help='Toca uma música do YouTube')
async def play(ctx, url: str):
    await play_audio(ctx, url)
