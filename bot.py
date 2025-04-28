# This example requires the 'message_content' intent.
import discord
from dotenv import load_dotenv
from discord.ext import commands
import os
load_dotenv()


bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is ready")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return 

    if message.content.lower() == "ping":
        channel = message.channel
        author = message.author
        await author.send("pong")


@bot.tree.command(name="warning",description="Send a warning message")
async def warning(interaction: discord.Interaction, member: discord.Member):
   await interaction.response.send_message(f"Warning sent")
   await member.send("You have been warned")

@bot.tree.command(name="ping",description="Ping the bot")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("pong")





@bot.tree.command(name="test",description="Test command")
async def test(interaction: discord.Interaction):
    embed = discord.Embed(title="Test", description="This is a test command", color=0x00ff00)
    embed.add_field(name="Field 1", value="This is a test field", inline=False)
    await interaction.response.send_message(embed=embed)







bot.run(os.getenv("DISCORD_TOKEN"))
