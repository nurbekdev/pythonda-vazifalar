# -*- coding: utf-8 -*-
"""
Created on Fri May  6 15:03:56 2022

@author: User
"""
import asyncio
from PIL import Image, ImageDraw ,  ImageFont
import logging
from aiogram import Bot, Dispatcher, executor,filters, types

API_TOKEN = '5370003808:AAH5pf1GKw6ppWTsyWz85YrjofW-M4CWayQ'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
   Start yoki Help tugamasi bosilganda
    """
    await message.reply("Assalomu Alaykum @yoshmaslahatchilar dan ism botiga Xush Kelibsiz\nIsm va Familiyangizni kiriting\n👇👇👇")

@dp.message_handler()
async def sendWiki(message: types.Message):
    print(message.chat.id)
    img = Image.open('uz.png')
    d =ImageDraw.Draw(img)
    fnt  = ImageFont.truetype("comicbd.ttf", 30)
    d.text((60,60), message.text , font= fnt, fill=(153,229,255))
    img.save('nurbek.png')
    await types.ChatActions.upload_photo()
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('nurbek.png'), '@yoshmaslahatchilar')
    await message.reply_media_group(media=media)
  

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
