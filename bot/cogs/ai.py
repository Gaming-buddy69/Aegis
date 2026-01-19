import aiohttp, os
from discord.ext import commands

class AI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.key = os.getenv("DEEPSEEK_API_KEY")

    @commands.hybrid_command()
    async def ai(self, ctx, *, prompt):
        async with aiohttp.ClientSession() as s:
            async with s.post(
                "https://api.deepseek.com/chat/completions",
                headers={"Authorization": f"Bearer {self.key}"},
                json={
                    "model": "deepseek-chat",
                    "messages": [{"role": "user", "content": prompt}]
                }
            ) as r:
                data = await r.json()
        await ctx.send(data["choices"][0]["message"]["content"])

async def setup(bot):
    await bot.add_cog(AI(bot))
