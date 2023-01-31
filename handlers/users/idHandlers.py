from aiogram import types 
from aiogram.dispatcher import filters 

from loader import dp
from data.config import ADMINS

SUPERUSERS = ADMINS
QORAROYXAT = [22342421,5235443]

@dp.message_handler(chat_id=SUPERUSERS, text = 'secret')
async def id_filter_example(msg: types.Message):
    await msg.answer("Xush kelibsiz, SuperUser")