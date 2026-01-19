import discord
from discord.ext import commands
from datetime import timedelta

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="No reason"):
        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member}")

    @commands.hybrid_command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="No reason"):
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member}")

    @commands.hybrid_command()
    @commands.has_permissions(moderate_members=True)
    async def timeout(self, ctx, member: discord.Member, minutes: int):
        await member.timeout(discord.utils.utcnow() + timedelta(minutes=minutes))

async def setup(bot):
    await bot.add_cog(Moderation(bot))
