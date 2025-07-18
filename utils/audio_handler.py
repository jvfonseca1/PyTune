import discord
import yt_dlp
import asyncio
import os

from collections import defaultdict, deque
from utils.logger import logger

queues = defaultdict(deque)
disconnect_task = None

YDL_OPTIONS = {
    'format': 'bestaudio',
    'quiet': True,
    'noplaylist': True,
    'cookiefile':  os.path.join(os.path.dirname(__file__), '..', 'cookies.txt'),
    'default_search': 'ytsearch'
}

FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
}

async def play_audio(ctx, url):
    guild_id = ctx.guild.id
    with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        queues[guild_id].append([info['url'], info.get('title', url), url])

    voice = ctx.guild.voice_client
    if voice and voice.is_playing():
        await ctx.send("🎵 Video adicionado à fila.")
        return

    await _play_next(ctx)

async def _play_next(ctx):
    global disconnect_task
    
    guild_id = ctx.guild.id
    if not queues[guild_id]:
        return

    info = queues[guild_id].popleft()
    voice = ctx.guild.voice_client

    if not ctx.author.voice:
        await ctx.send("Você precisa estar em um canal de voz.")
        return

    if not voice or not voice.is_connected():
        channel = ctx.author.voice.channel
        voice = await channel.connect()

    source = discord.FFmpegPCMAudio(info[0], **FFMPEG_OPTIONS)
    voice.play(source, after=lambda e: asyncio.run_coroutine_threadsafe(_play_next(ctx), ctx.bot.loop))

    logger.info(f"Tocando video: {info[1]}")

    if not disconnect_task:
        disconnect_task = asyncio.create_task(disconnect_if_idle(ctx))

    await ctx.send(f"🎵 Tocando agora: {info[1]}")

async def stop_audio(ctx):
    guild_id = ctx.guild.id
    queues[guild_id].clear()

    voice = ctx.guild.voice_client
    if voice and voice.is_connected():
        await voice.disconnect()
        logger.info("Desconectado do canal de voz.")
        await ctx.send("⏹️ Parado e desconectado.")
    else:
        await ctx.send("Não estou em um canal de voz.")

async def skip_audio(ctx):
    voice = ctx.guild.voice_client
    if not voice or not voice.is_playing():
        await ctx.send("Nenhuma música está tocando.")
        return

    logger.info("⏭️ Música pulada")
    await ctx.send("Pulando música...")
    voice.stop()

queues = defaultdict(deque)

async def show_queue(ctx):
    guild_id = ctx.guild.id
    queue = queues[guild_id]
    if not queue:
        await ctx.send("A fila está vazia.")
        return

    msg = "**Fila atual:**\n"
    for i, info in enumerate(queue, 1):
        msg += f"{i}. {info[1]}\n"
    await ctx.send(msg)

async def clear_queue(ctx):
    guild_id = ctx.guild.id
    queues[guild_id].clear()
    await ctx.send("Fila limpa.")

async def pause_audio(ctx):
    voice = ctx.guild.voice_client
    if not voice or not voice.is_playing():
        await ctx.send("Nenhuma música está tocando para pausar.")
        return
    voice.pause()
    logger.info("Música pausada.")
    await ctx.send("⏸️ Música pausada.")

async def resume_audio(ctx):
    voice = ctx.guild.voice_client
    if not voice or not voice.is_paused():
        await ctx.send("Nenhuma música está pausada para retomar.")
        return
    voice.resume()
    logger.info("Música retomada.")
    await ctx.send("▶️ Música retomada.")

async def disconnect_if_idle(ctx):
    try:
        global disconnect_task
        logger.info("Iniciando verificação de inatividade")
        voice = ctx.voice_client
        while voice and voice.is_connected():
            await asyncio.sleep(180)
            guild_id = ctx.guild.id
            if voice and voice.is_connected() and not queues[guild_id] and not voice.is_playing() and not voice.is_paused():
                await voice.disconnect()
                await ctx.send("⏹️ Nenhuma música tocada há pelo menos 3 minutos. Saindo do canal de voz.")
                logger.info("Tempo de inatividade atingido. Saindo do canal de voz.")
                disconnect_task = None
                break

            members = voice.channel.members
            non_bots = [m for m in members if not m.bot]
            if voice and voice.is_connected() and not non_bots:
                await voice.disconnect()
                await ctx.send("⏹️ Todos os membros saíram do canal de voz. Saindo do canal de voz.")
                logger.info("Todos os membros saíram do canal de voz. Saindo do canal de voz.")
                disconnect_task = None
                break
    except Exception as e:
        logger.error(f"Erro na conferência de inatividade: {e}")
        disconnect_task = None
        pass
