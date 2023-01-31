from aiogram import types
from aiogram.dispatcher import filters 

from loader import dp

#@dp.message_handler(content_types=types.ContentTypes.PHOTO)
@dp.message_handler(content_types='photo')

async def photo_handler(msg: types.Message):
    await msg.answer("Kim nima rasm?")