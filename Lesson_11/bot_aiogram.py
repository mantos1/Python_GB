from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

import os
import time

bot = Bot(token=open('TOKEN.txt', "r").readline()) #os.getenv('TOKEN'))
dp = Dispatcher(bot)

dict_url = {
            "Водолей":"https://horo.mail.ru/prediction/aquarius/today/"
            ,"Рыбы":"https://horo.mail.ru/prediction/pisces/today/"
            ,"Овен":"https://horo.mail.ru/prediction/aries/today/"
            ,"Телец":"https://horo.mail.ru/prediction/taurus/today/"
            ,"Близнецы":"https://horo.mail.ru/prediction/gemini/today/"
            ,"Рак":"https://horo.mail.ru/prediction/cancer/today/"
            ,"Лев":"https://horo.mail.ru/prediction/leo/today/"
            ,"Дева":"https://horo.mail.ru/prediction/virgo/today/"
            ,"Весы":"https://horo.mail.ru/prediction/libra/today/"
            ,"Скорпион":"https://horo.mail.ru/prediction/scorpio/today/"
            ,"Стрелец":"https://horo.mail.ru/prediction/sagittarius/today/"
            ,"Козерог":"https://horo.mail.ru/prediction/capricorn/today/"
            }

async def start(_):
    print("Bot starting")

@dp.message_handler(commands = ['start', 'help'])
async def command_start(message: types.Message):
    try:
        bb1 = KeyboardButton("/Получить_рандомное_число")
        bb2 = KeyboardButton("/Глянуть_гороскоп")
        keyboard_client = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        keyboard_client.row(bb1,bb2)
        await bot.send_sticker(chat_id=message.from_user.id, sticker = r"CAACAgIAAxkBAAEGt2tjj9hOfIP35jdACg7xuKEIMSJZyQACgxQAAmFXSEjQI8I-g2gtjysE")
        await bot.send_message(message.from_user.id, 'Не прошло и года...!', reply_markup=keyboard_client)
        await message.delete()
    except:
        await message.reply_sticker(sticker = r"CAACAgIAAxkBAAEGt4djj-X4Khyv61zbG-ijwY95AfwH0wAC4REAAkOxgEhbmzVHOzKMBSsE")
        await message.reply('Напиши мне в личку, живо!\nhttps://t.me/MinionMinion_Bot')

@dp.message_handler(commands = 'Получить_рандомное_число')
async def command_answer_random_number(message: types.Message):
        # t = await message.answer('Укажите диапазон чисел через запятую в промежутке от 1 до 100:')
        msg = await message.reply_dice(emoji="🎲")
        # print(msg.dice.value)
        time.sleep(5)
        await message.reply(f'Щенок, твое число {msg.dice.value}!')

@dp.message_handler(commands='Глянуть_гороскоп')
async def command_answer_goroscope(message: types.Message):
    await message.delete()
    b1 = InlineKeyboardButton('Водолей', callback_data="Водолей")       #, url='https://horo.mail.ru/prediction/aquarius/today/')
    b2 = InlineKeyboardButton('Рыбы', callback_data="Рыбы")             #url='https://horo.mail.ru/prediction/pisces/today/')
    b3 = InlineKeyboardButton('Овен', callback_data="Овен")             #url='https://horo.mail.ru/prediction/aries/today/')
    b4 = InlineKeyboardButton('Телец', callback_data="Телец")           # url='https://horo.mail.ru/prediction/taurus/today/')
    b5 = InlineKeyboardButton('Близнецы', callback_data="Близнецы")     # url='https://horo.mail.ru/prediction/gemini/today/')
    b6 = InlineKeyboardButton('Рак', callback_data="Рак")               # url='https://horo.mail.ru/prediction/cancer/today/')
    b7 = InlineKeyboardButton('Лев', callback_data="Лев")               # url='https://horo.mail.ru/prediction/leo/today/')
    b8 = InlineKeyboardButton('Дева', callback_data="Дева")             # url='https://horo.mail.ru/prediction/virgo/today/')
    b9 = InlineKeyboardButton('Весы', callback_data="Весы")             # url='https://horo.mail.ru/prediction/libra/today/')
    b10 = InlineKeyboardButton('Скорпион', callback_data="Скорпион")    # url='https://horo.mail.ru/prediction/scorpio/today/')
    b11 = InlineKeyboardButton('Стрелец', callback_data="Стрелец")      # url='https://horo.mail.ru/prediction/sagittarius/today/')
    b12 = InlineKeyboardButton('Козерог', callback_data="Козерог")      # url='https://horo.mail.ru/prediction/capricorn/today/')

    key_client = InlineKeyboardMarkup()
    key_client.row(b1,b2,b3).row(b4,b5,b6).row(b7,b8,b9).row(b10,b11,b12)
    await  message.answer(message.text)
    # await message.answer_sticker(r'https://tlgrm.ru/_/stickers/061/2ac/0612acc2-f6fd-3470-83df-429ee8ba3d3b/192/25.webp',reply_markup=key_client)
    # await bot.send_sticker(chat_id=message.from_user.id, sticker=r"CAACAgIAAxkBAAED7aNiCmNgcLCdHjYZIU2Yf9sLNxTiEAACVhQAAhzIoEuxFOaAT2TuaSME")
    await bot.send_sticker(chat_id=message.chat.id, sticker = r"CAACAgIAAxkBAAEGt2ljj9gsDlQZi_3czbxgnBNNKnUupQAClxoAAmpUOUigbPi998pdDisE",reply_markup=key_client)

@dp.callback_query_handler(text= [key for key  in dict_url.keys()])
async def command_callback_goroscope(call: types.CallbackQuery):
    msg = call.message
    chat_id = msg.chat.id
    msg_id = msg.message_id
    await bot.answer_callback_query(call.id, "Подавись...")
    await bot.delete_message(chat_id=chat_id, message_id=msg_id)
    await bot.send_message(chat_id, dict_url[str(call.data)])


executor.start_polling(dp, skip_updates=True, on_startup=start)









