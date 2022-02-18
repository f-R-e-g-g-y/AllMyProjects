import discord
from discord.ext import commands
from pymongo import MongoClient
import os
from Cybernator import Paginator as Pag

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())
cluster = MongoClient("mongodb+srv://login:passwords@cluster0.jnfni.mongodb.net/ecodb?retryWrites=true&w=majority")
collection = cluster.ecodb.colldb

bot.remove_command('help')

@bot.event
async def on_ready():
	print("Bot connected to the server")

	for guild in bot.guilds:
		for member in guild.members:
			post = {
				"_id": member.id,
				"balance": 300,
				"xp": 0,
				"lvl": 1
			}

			if collection.count_documents({"_id": member.id}) == 0:
				collection.insert_one(post)


@bot.event
async def on_member_join(member):
	post = {
		"_id": member.id,
		"balance": 300,
		"xp": 0,
		"lvl": 1
	}

	if collection.count_documents({"_id": member.id}) == 0:
		collection.insert_one(post)


@bot.event
async def on_command_error(ctx, error):
	print(error)

	if isinstance(error, commands.UserInputError):
		await ctx.send(embed = discord.Embed(
			description = f"Правильное использование команды: `{ctx.prefix}{ctx.command.name}` ({ctx.command.brief}): `{ctx.prefix}{ctx.command.usage}`"
		))


@bot.command()
@commands.is_owner()
async def load(ctx, extension):
	bot.load_extension(f"cogs.{extension}")


@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
	bot.unload_extension(f"cogs.{extension}")


@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
	bot.unload_extension(f"cogs.{extension}")
	bot.load_extension(f"cogs.{extension}")



for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		bot.load_extension(f"cogs.{filename[:-3]}")

bot.run('PasteToken')
