import discord
from discord.ext import commands
from pymongo import MongoClient

"""
1. balance -> вывод баланса пользователя
2. pay -> перевод денег
3. LVL-System
"""

class Economic(commands.Cog):

	def __init__(self, bot):
		self.bot = bot
		self.cluster = MongoClient("mongodb+srv://login:passwords@cluster0.jnfni.mongodb.net/ecodb?retryWrites=true&w=majority")
		self.collection = self.cluster.ecodb.colldb

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author == self.bot.user:
			return

		user = message.author
		data = self.collection.find_one({"_id": user.id})

		if data["xp"] == 500 + 100 * data["lvl"]:
			self.collection.update_one({"_id": user.id},
				{"$set": {"lvl": data["lvl"] + 1}})
			self.collection.update_one({"_id": user.id},
				{"$set": {"xp": 0}})

			await message.channel.send(f"{user.mention} + 1 lvl")
		else:
			self.collection.update_one({"_id": user.id},
				{"$set": {"xp": data["xp"] + 50}})


	@commands.command(
		name = "баланс",
		aliases = ["balance", "cash"],
		brief = "Вывод баланса пользователя",
		usage = "balance <@user>"
	)
	async def user_balance(self, ctx, member: discord.Member = None):
		if member is None:
			await ctx.send(embed = discord.Embed(
				description = f"Баланс пользователя __{ctx.author}__: **{self.collection.find_one({'_id': ctx.author.id})['balance']}**"
			))
		else:
			await ctx.send(embed = discord.Embed(
				description = f"Баланс пользователя __{member}__: **{self.collection.find_one({'_id': member.id})['balance']}**"
			))

	@commands.command(
		name = "перевод",
		aliases = ["pay", "givecash"],
		brief = "Перевод денег другому пользователю",
		usage = "pay <@user> <amount>"	
	)
	async def pay_cash(self, ctx, member: discord.Member, amount: int):
		ubalance = self.collection.find_one({"_id": ctx.author.id})["balance"]
		mbalance = self.collection.find_one({"_id": member.id})["balance"]

		if amount <= 0:
			await ctx.send(embed = discord.Embed(
				description = f"__{ctx.author}__, конечно извините меня, но проход хацкерам сегодня закрыт."
			))
		else:
			self.collection.update_one({"_id": ctx.author.id},
				{"$set": {"balance": ubalance - amount}})

			self.collection.update_one({"_id": member.id},
				{"$set": {"balance": mbalance + amount}})

			await ctx.message.add_reaction("✅")


def setup(bot):
  bot.add_cog(Economic(bot))