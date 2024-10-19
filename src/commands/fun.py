import discord, psutil, time, os, aiohttp
from discord.commands import SlashCommandGroup
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = time.time()
        self.bot.version = os.getenv("version")
        
    @discord.slash_command(description="Is IDU deleted?")
    async def idu(self, ctx):
        if (self.bot.get_guild(746844357205950606)):
            await ctx.send("IDU is not deleted.")
        else:
            await ctx.send("IDU is deleted.")
    
    @discord.slash_command(description="Generate freaky text")
    async def freaky(self, ctx: discord.ApplicationContext, *, text: str):

        mapping = {
            "𝓪": "a", "𝓫": "b", "𝓬": "c", "𝓭": "d", "𝓮": "e", "𝓯": "f", "𝓰": "g", "𝓱": "h", "𝓲": "i", "𝓳": "j",
            "𝓴": "k", "𝓵": "l", "𝓶": "m", "𝓷": "n", "𝓸": "o", "𝓹": "p", "𝓺": "q", "𝓻": "r", "𝓼": "s", "𝓽": "t",
            "𝓾": "u", "𝓿": "v", "𝔀": "w", "𝔁": "x", "𝔂": "y", "𝔃": "z", "𝓐": "A", "𝓑": "B", "𝓒": "C", "𝓓": "D",
            "𝓔": "E", "𝓕": "F", "𝓖": "G", "𝓗": "H", "𝓘": "I", "𝓙": "J", "𝓚": "K", "𝓛": "L", "𝓜": "M", "𝓝": "N",
            "𝓞": "O", "𝓟": "P", "𝓠": "Q", "𝓡": "R", "𝓢": "S", "𝓣": "T", "𝓤": "U", "𝓥": "V", "𝓦": "W", "𝓧": "X",
            "𝓨": "Y", "𝓩": "Z"
        }
        result = ""
        for char in text:
            if char in mapping:
                result += mapping[char]
            else:
                result += char
        await ctx.send(result)
        
    @discord.slash_command(description="Prompt Kendale")
    async def kendale(self, ctx:discord.ApplicationContext, query: str):
        
        await ctx.defer()
        
        ollama_url = "http://localhost:11434/api/generate"
        
        payload = {
            "model": "llama3.1",
            "prompt": query,
            "stream": False
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(ollama_url, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    response_text = data.get('response', 'No response from Ollama.')
                    await ctx.respond(response_text)
                
                else:
                    await ctx.respond(f"An error occurred. {response.status}")
        
def setup(bot):
    bot.add_cog(Fun(bot))

