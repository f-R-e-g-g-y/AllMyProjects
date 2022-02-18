import discord
import json
import requests
from discord.ext import commands
import random
import io
import aiohttp
import sqlite3
import os
from io import BytesIO
from PIL import Image, ImageFilter, ImageDraw, ImageFont
from Cybernator import Paginator as Pag

from Random_Words import cums,kissgif,hoin,huggif

class command(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.Cog.listener()
  async def on_member_join(self, member):
    channel = bot.get_channel(799619076150001717) #Скидывает эмбед-приветствие в данный канал(Основной)
    if role := member.guild.get_role(872205390874562651): #ID role
        await member.add_roles(role)
    await channel.send( embed = discord.Embed( description = f'``{member.name}`` присоединился', color = 0x0c0c0c))

    role_1 = member.guild.get_role(872823382767452202)
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    chania=member.id
    cursor.execute(f"SELECT user_id FROM users WHERE user_id={chania}")
    data=cursor.fetchone()
    if data is None:
      pass
    else:
      user_id=[member.id]
      cursor.execute("INSERT INTO users VALUES(?);", user_id)
      connect.commit()
      await member.add_roles(role_1)
  
  @commands.command()
  @commands.has_guild_permissions(administrator=True)
  async def jail(self, ctx, member: discord.Member):
    role_1 = member.guild.get_role(872823382767452202)
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER
    )""")
    connect.commit()
    chania = member.id
    cursor.execute(f"SELECT user_id FROM users WHERE user_id={chania}")
    data=cursor.fetchone()
    print(data, 'добавление')
    if data is None:
          user_id=[member.id]
          cursor.execute("INSERT INTO users VALUES(?);", user_id)
          connect.commit()
          await member.add_roles(role_1)

  @commands.command()
  @commands.has_guild_permissions(administrator=True)
  async def unjail(self, ctx, member: discord.Member):
        role_1 = member.guild.get_role(872823382767452202)
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        chania=member.id
        cursor.execute(f'DELETE FROM users WHERE user_id = {chania}')
        connect.commit()
        await member.remove_roles(role_1)
  
  #Гифки и картинки----------------------------------------------------------------------------------
  @commands.command()
  async def РосИм(self, ctx):
      await ctx.send('https://media.discordapp.net/attachments/799619076150001717/877468058518716466/flag-i-gerb-rossijskoj-imperii.png')

  @commands.command()
  async def usa(self, ctx):
      await ctx.send('https://media.discordapp.net/attachments/799619076150001717/876213148338774076/ad7tx-0asa6.png?width=755&height=566')

  @commands.command()
  async def hoi(self, ctx):
      await ctx.send(random.choice(hoin))

  @commands.command(help='Флаг Советского союза, команда пишется на русском!')
  async def СССР(self, ctx):
      await ctx.send("https://avatars.mds.yandex.net/get-zen_doc/2851998/pub_5f2965a1fb7bda4f071c1d9e_5f296638b0d961407f58a17b/scale_1200")

  #Оверлеи--------------------------------------------------------------------------------------------------------------
  @commands.command()
  async def rosimp(self, ctx, user: discord.Member = None):
      if user == None:
          user = ctx.author
          
      watermark = Image.open('fotki/dunia.png')
      watermark = watermark.crop((135, 0, 565, 430))
      avatar = user.avatar_url_as(size = 128)
      avt = BytesIO(await avatar.read())
      img = Image.open(avt)
      img = img.resize((430, 430))

      img.paste(watermark, (0, 0),  watermark)
      img.save("image.png")
      await ctx.send(file = discord.File("image.png"))

  @commands.command()
  async def ch(self, ctx,forma, user : discord.Member=None):
      if user == None:
          user = ctx.author
      f1='gay'
      f2='glass'
      f3='wasted'
      f4='passed'
      f5='jail'
      f6='comrade'
      f7='wanted'
      f8='shit'
      f9='mnenie'
      f10='rosimp'
      if forma == f1:
          asil = 'https://some-random-api.ml/canvas/gay?avatar='
      if forma == f2:
          asil = 'https://some-random-api.ml/canvas/glass?avatar='
      if forma == f3:
          asil = 'https://some-random-api.ml/canvas/wasted?avatar='
      if forma == f4:
          asil = 'https://some-random-api.ml/canvas/passed?avatar='
      if forma == f5:
          asil = 'https://some-random-api.ml/canvas/jail?avatar='
      if forma == f6:
          asil = 'https://some-random-api.ml/canvas/comrade?avatar='
      if forma == f7:
          wanted = Image.open('fotki/wan.jpg')
          avatar = user.avatar_url_as(size = 128)
          avt = BytesIO(await avatar.read())
          img = Image.open(avt)
          img = img.resize((315, 315))
          wanted.paste(img, (125, 252))
          wanted.save("image.png")
          await ctx.send(file = discord.File("image.png"))
      if forma == f8:
          wanted = Image.open('fotki/doge.jpg')
          avatar = user.avatar_url_as(size = 128)
          avt = BytesIO(await avatar.read())
          img = Image.open(avt)
          img = img.resize((120, 120))
          wanted.paste(img, (560, 520))
          wanted.save("image.png")
          await ctx.send(file = discord.File("image.png"))
      if forma == f9:
          wanted = Image.open('fotki/egomnenie.jpg')
          avatar = user.avatar_url_as(size = 128)
          avt = BytesIO(await avatar.read())
          img = Image.open(avt)
          img = img.resize((310, 310))
          wanted.paste(img, (180, 80))
          wanted.save("image.png")
          await ctx.send(file = discord.File("image.png"))
      if forma == f10:
          watermark = Image.open('fotki/dunia.png')
          watermark = watermark.crop((135, 0, 565, 430))
          avatar = user.avatar_url_as(size = 128)
          avt = BytesIO(await avatar.read())
          img = Image.open(avt)
          img = img.resize((430, 430))
          img.paste(watermark, (0, 0),  watermark)
          img.save("image.png")
          await ctx.send(file = discord.File("image.png"))
      z=[f1,f2,f3,f4,f5,f6]
      if forma in z:
          bsil = user.avatar_url
          c= asil + str(bsil)
          silka=c[:-14]
          forma='jpg'
          silka=silka+forma
          await ctx.send(silka)

  @commands.command()
  async def triggered(self, ctx, member: discord.Member=None):
      if not member:
          member = ctx.author
          
      async with aiohttp.ClientSession() as trigSession:
          async with trigSession.get(f'https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg:
              imageData = io.BytesIO(await trigImg.read())
              
              await trigSession.close()
              
              await ctx.reply(file=discord.File(imageData, 'triggered.gif'))
              
  #Упоминание + определенная гифка--------------------------------------------------------------------------------------
  @commands.command(help='Поцелуйте кого-нибудь из этого сервера)))')
  async def kiss(self, ctx, member: discord.Member = None):

      if member == None:
          return
      b=random.choice(kissgif)
      await ctx.send(f"{ctx.author.mention} поцеловал(а) {member.mention}")
      await ctx.send(b)

  @commands.command(help='Обнимите кого-нибудь из этого сервера)))')
  async def hug(self, ctx, member: discord.Member = None):

      if member == None:
          return
      b=random.choice(huggif)
      await ctx.send(f"{ctx.author.mention} обнял(а) {member.mention}")
      await ctx.send(b)

  #Рандомные гифки панд, лисов и тд-------------------------------------------------------------------------------------
  @commands.command(help='Рандомная фотка панды')
  async def panda(self, ctx):
      pandavib=['Успокойся и полюбуйся на панду', 'Панда', 'Во какой красавец))']
      response = requests.get('https://some-random-api.ml/img/panda') # Get-запрос
      json_data = json.loads(response.text) # Извлекаем JSON
      embed = discord.Embed(color = 0xff9900, title = random.choice(pandavib)) # Создание Embed'a
      embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
      await ctx.send(embed = embed) # Отправляем Embed

  @commands.command(help='Рандомная фотка лисы')
  async def fox(self, ctx):
      foxvib=['Смотри какая лисичка!', 'Fox', 'Лисичка']
      response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
      json_data = json.loads(response.text) # Извлекаем JSON

      embed = discord.Embed(color = 0xff9900, title = random.choice(foxvib)) # Создание Embed'a
      embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
      await ctx.send(embed = embed) # Отправляем Embed


  @commands.command(help='Рандомная гифка с аниме')
  async def anime(self, ctx):
      num =random.randint(1,3)
      if num == 1:
          response = requests.get('https://some-random-api.ml/animu/wink')
      elif num == 2:
          response = requests.get('https://some-random-api.ml/animu/pat')
      else:
          response = requests.get('https://some-random-api.ml/animu/hug')
      json_data = json.loads(response.text)

      embed_k = discord.Embed(color = 0xff9900, title = 'Рандомная анимешечка')
      embed_k.set_image(url = json_data['link'])
      await ctx.send(embed = embed_k)

  @commands.command(help='Рандомная фотка кота')
  async def cat(self, ctx):
      catvib=['Кот', 'Кошак', 'Cat']
      response = requests.get('https://some-random-api.ml/img/cat') # Get-запрос
      json_data = json.loads(response.text) # Извлекаем JSON

      embed = discord.Embed(color = 0xff9900, title = random.choice(catvib)) # Создание Embed'a
      embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
      await ctx.send(embed = embed)

  @commands.command(help='Рандомная гифка-cum')
  async def cum(self, ctx):
      await ctx.send(random.choice(cums))

  #Узнай когда кто-либо присоединился-----------------------------------------------------------------------------------
  @commands.command(help='Узнай когда кто-либо присоединился к этому серверу')
  async def joined(self, ctx, *, member: discord.Member):
      await ctx.send('{0} joined on {0.joined_at}'.format(member))

  @commands.command()
  async def help(self, ctx):
    emb=discord.Embed(title='Доступные команды', description='Страница 1/2', colour=discord.Color.red())
    emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
    emb.add_field( name = 'Музыка', value ='!play - Введи чтобы запустить музыкального бота\n!stop - Останавливает воспроизведение и очищает queue\n!queue - Список песен\n!skip - Пропуск текущей песни\n!join - Бот заходит в голосовой канал\n!leave - Бот выходит из голосового канала\n!volume - Ставит громкость на СЛЕДУЮЩУЮ песню\n!now - Текущий трек\n!pause - Пауза\n!resume - Продолжить воспроизведение\n!shuffle - Перемешивает queue\n!remove - Удаляет песню из queue\n!loop - Бесконечное воспроизведение', inline=False)
    emb.set_thumbnail(url = self.bot.user.avatar_url)
    emb.set_footer( icon_url = ctx.guild.owner.avatar_url, text = f'{ctx.guild.owner.name} © Copyright 2021 | Все права защищены' )
    

    emb2=discord.Embed(title='Доступные команды', description='Страница 2/2', colour=discord.Color.red())
    emb2.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
    emb2.add_field( name = 'Оверлеи', value ='!triggered\n!ch + `gay`,`glass`,`wasted`,`wanted`,`jail`,`comrade`,`passed`,`shit`,`mnenie`,\n`rosimp`', inline=False)
    emb2.add_field( name = 'Другие команды', value = '!kiss - Поцелуйте кого-нибудь\n!hug - Обнимите кого-нибудь\n!panda - Рандомная картинка панды\n!fox - Рандомная картинка лисы\n!cat - Рандомная картинка кота\n!anime - Рандомная анимешечка\n!cum - Cum-gif\n!joined - Узнайте когда кто-либо зашел на сервер\n!jail(unjail) - Посадить кого-нибудь в карцер(Доступно только админам)', inline=False)
    emb2.set_thumbnail(url = self.bot.user.avatar_url)
    emb2.set_footer( icon_url = ctx.guild.owner.avatar_url, text = f'{ctx.guild.owner.name} © Copyright 2021 | Все права защищены' )

    embeds=[emb,emb2]
    message = await ctx.send(embed=emb)
    page = Pag(self.bot, message, only=ctx.author, use_more=False, embeds=embeds, footer=False) 
    await page.start()

def setup(bot):
  bot.add_cog(command(bot))