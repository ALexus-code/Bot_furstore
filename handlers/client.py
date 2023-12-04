from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove

#@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет, это бренд жесть какой раскакой одежды пурландд, а этот текст поменяет Юлечка', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('чтобы бот работал напишите ему что угодно: \nhttps://t.me/FurrLand_bot')

#@dp.message_handler(commands=['Режим_работы'])
async def pur_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'часы работыа')

#@dp.message_handler(commands=['Расположение'])
async def pur_Place_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'адрес)')#, reply_markup=ReplyKeyboardRemove()) Если надо удалить клаву

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pur_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pur_Place_command, commands=['Расположение'])
