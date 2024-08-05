"""
Main module
"""
import random

import discord
from discord.ext import commands

import src.constans.COMMANDS as COMMANDS
import src.constans.LOGS as LOGS
import src.constans.OUTPUTS as OUTPUTS
import src.constans.OTHERS as OTHERS

from src.scripts.memes import random_meme

intents = discord.Intents.default()
intents.message_content = True
Kirby = commands.Bot(
    command_prefix=COMMANDS.PREFIX,
    description=OUTPUTS.HI,
    intents=intents,
)

@Kirby.event
async def on_ready():
    """
    Bot start console flag
    """

    print(LOGS.LOG_INIT)

@Kirby.event
async def on_message(message):
    """
    Message control
    """

    if message.content.startswith(COMMANDS.RANDOM):
        OUTPUTS.RANDOM = random_meme(random.randint(0, 50)) # Movida rara
        if OUTPUTS.RANDOM:
            print(LOGS.LOG_200)
            await message.channel.send(OUTPUTS.RANDOM)
        else:
            print(LOGS.LOG_ERROR)
            await message.channel.send(OUTPUTS.ERROR)

    elif message.content.startswith(COMMANDS.HI):
        print(LOGS.LOG_200)
        await message.channel.send(OUTPUTS.HI)

    elif message.content.startswith(COMMANDS.HOLA):
        print(LOGS.LOG_200)
        await message.channel.send(OUTPUTS.HOLA)


Kirby.run(OTHERS.TOKEN)
