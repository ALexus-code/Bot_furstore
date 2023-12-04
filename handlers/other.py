from aiogram import types, Dispatcher
from create_bot import dp
import json, string

#@dp.message_handler()
async def echo_send(message : types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}.intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Сегодня не материшься')
        await message.delete()

#@dp.message_handler()
#async def echo_send(message : types.Message):
    #if message.text == 'Привет':

        #await message.answer('Ну БАЗА БАЗА')
    #await message.answer(message.text) ##Простоответ
    #await message.reply(message.text) ##ОТвет на сообщение c упоминанием автора
    #await bot.send_message(message.from_user.id, message.text)  ##Если писать именно боту отвечает в личку

def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(echo_send)