import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import time

load_dotenv()

TOKEN = os.environ["TOKEN"]
delete = bool(os.environ["DELETE"])
imageonly = bool(os.environ["IMAGEONLY"])

client = commands.Bot(command_prefix=">", self_bot=True)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.command()
async def images(ctx):
    directory = os.getcwd()
    amount = 0
    total =len(os.listdir())
    for filename in os.listdir(directory+"/Images"):
        if imageonly and not filename.endswith((".png", ".jpg", ".webp", ".jpeg", ".bmp")): continue
        file_path = os.path.join(directory+"/Images", filename)
        if os.path.isfile(file_path):
            file = discord.File(file_path, filename)
            print(f"Sending: {filename} - {total - amount} images remaining")
            try:
                await ctx.send(file=file)
            except Exception:
                print("Bad image, couldnt send")
            if delete: os.remove(file_path)
            amount = amount + 1
            time.sleep(5)
    print(f"Done! send {amount} Images")
            

client.run(TOKEN)
