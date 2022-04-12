import random
import json
import bs4
import requests
from telebot import types
import telebot


bot = telebot.TeleBot('5214235125:AAHOZOca1VqP2LDPLZWk5srQGi7WDRKGPnc')


@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Главное меню")
    btn2 = types.KeyboardButton("Помощь")
    markup.add(btn1, btn2)


    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! Я тестовый бот для курса программирования на языке ПаЙтон".format(
                         message.from_user), reply_markup=markup)



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text
    if ms_text == "Главное меню" or ms_text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Треки")
        btn2 = types.KeyboardButton("Управление")
        back = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id, text="Вы в главном меню ", reply_markup=markup)
    elif ms_text == "Треки":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Прислать рандомную обложку")
        btn2 = types.KeyboardButton("Прислать текст песни")
        btn3 = types.KeyboardButton("Прислать рандомный текст песни")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(chat_id, text="Вы перешли в Треки", reply_markup=markup)
    elif ms_text == "/cover" or ms_text == "Прислать рандомную обложку":
        contents = requests.get('https://randomfox.ca/floof.json').json()
        urlCOV = contents['#fox_img_link']
        bot.send_photo(chat_id, photo=urlCOV, caption="Обложка трека")
    elif ms_text == "Прислать текст песни":
        bot.send_message(chat_id, text="Она улетела, уехала или умерла\nЭтой ночью\nОна улетела, уехала или умерла\nНе знаю точно\nОна улетела, уехала или умерла\nТак будет проще\nОна лишь хотела тепла, но как спичка сгорела дотла\nВ моей личке последняя строчка")
    elif ms_text == "Управление":
        bot.send_message(chat_id, text="будет позже")
    elif ms_text == "Прислать рандомный текст песни":
        bot.send_message(chat_id, text=get_text())
    elif ms_text == "Помощь" or ms_text == "/help":
        bot.send_message(chat_id, text="Автор: стдуент группы 1-мд-20 Поспелов Никита ")
    else:
        bot.send_message(chat_id, text="Вас слышно... Ваше сообщение: " + ms_text)


def get_text():
    array_texts = ['https://www.lyrics.com/lyric/28267385/Kendrick+Lamar/Bitch%2C+Don%E2%80%99t+Kill+My+Vibe', 'https://www.lyrics.com/lyric/29260986/Kendrick+Lamar/Swimming+Pools+%28Drank%29', 'https://www.lyrics.com/lyric/28219632/Kendrick+Lamar/Compton', 'https://www.lyrics.com/lyric/38645539/MORGENSHTERN/Cristal+%26+%D0%9C%D0%9E%D0%81%D0%A2', 'https://www.lyrics.com/lyric-lf/4533121/MORGENSHTERN/Lollipop', 'https://www.lyrics.com/lyric/35696775/Joji/Slow+Dancing+in+the+Dark', 'https://www.lyrics.com/lyric/35597036/Joji/Can%27t+Get+Over+You']
    bobtek = requests.get(random.choice(array_texts))
    soup = bs4.BeautifulSoup(bobtek.text, "html.parser")
    result_find = soup.select('#lyric-body-text')
    return result_find[0].getText()


# -----------------------------------------------------------------------
bot.polling(none_stop=True, interval=0) # Запускаем бота

print()