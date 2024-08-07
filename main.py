"""
Main module
"""
import random as rm

import discord
from discord.ext import commands

import src.constans.COMMANDS as COMMANDS
import src.constans.LOGS as LOGS
import src.constans.OUTPUTS as OUTPUTS
import src.constans.OTHERS as OTHERS

from src.scripts.memes import get_meme

intents = discord.Intents.default()
intents.message_content = True
Kirby = commands.Bot(
    command_prefix=f"{COMMANDS.PREFIX} ",
    intents=intents,
)



@Kirby.event
async def on_ready():
    """
    Bot start console flag
    """

    print(LOGS.LOG_INIT)



@Kirby.command()
async def hola(ctx):
    await ctx.send(OUTPUTS.HOLA)

@Kirby.command()
async def hi(ctx):
    await ctx.send(OUTPUTS.HI)

@Kirby.command()
async def random(ctx):
    OUTPUTS.RANDOM = rm.choice(get_meme())
    if OUTPUTS.RANDOM:
        await ctx.send(OUTPUTS.RANDOM)
        return
    ctx.send(OUTPUTS.ERROR)

@Kirby.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not muted_role:
        muted_role = await ctx.guild.create_role(name="Muted")
        for channel in ctx.guild.channels:
            await channel.set_permissions(muted_role, speak=False, send_messages=False, read_message_history=True, read_messages=True)

    await member.add_roles(muted_role, reason=reason)
    await ctx.send(f'{member.mention} ha sido silenciado. Motivo: {reason}')

@Kirby.command()
async def check_role(ctx, member: discord.Member, role_name: str):
    role = discord.utils.get(ctx.guild.roles, name=role_name)
    
    if role is None:
        await ctx.send(f'Rol "{role_name}" no encontrado.')
        return

    if role in member.roles:
        await ctx.send(f'{member.mention} tiene el rol {role_name}.')
    else:
        await ctx.send(f'{member.mention} no tiene el rol {role_name}.')

@Kirby.command()
async def check_admin(ctx, role_name: str):
    role = discord.utils.get(ctx.guild.roles, name=role_name)
    
    if role is None:
        await ctx.send(f'Rol "{role_name}" no encontrado.')
        return
    
    if role.permissions.administrator:
        await ctx.send(f'El rol {role_name} tiene permisos de administrador.')
    else:
        await ctx.send(f'El rol {role_name} no tiene permisos de administrador.')

Kirby.run(OTHERS.TOKEN)
