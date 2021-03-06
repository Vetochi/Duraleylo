import random
import json
import bs4
import requests
from telebot import types
import telebot
from covers.Covers import get_cover
from quiz import Quiz


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

quiz_correctanswer = ""

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global quiz_correctanswer
    chat_id = message.chat.id
    ms_text = message.text
    if ms_text == "Главное меню" or ms_text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Треки")
        btn2 = types.KeyboardButton("Картинки")
        btn3 = types.KeyboardButton("Игра")
        back = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(chat_id, text="Вы в главном меню ", reply_markup=markup)

    elif ms_text == "Треки":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Прислать текст песни")
        btn2 = types.KeyboardButton("Прислать рандомный текст песни")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id, text="Вы перешли в Треки", reply_markup=markup)
    elif ms_text == "Прислать текст песни":
        bot.send_message(chat_id, text="Она улетела, уехала или умерла\nЭтой ночью\nОна улетела, уехала или умерла\nНе знаю точно\nОна улетела, уехала или умерла\nТак будет проще\nОна лишь хотела тепла, но как спичка сгорела дотла\nВ моей личке последняя строчка")
    elif ms_text == "Прислать рандомный текст песни":
        bot.send_message(chat_id, text=get_text())

    elif ms_text == "Картинки":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Прислать собаку")
        btn2 = types.KeyboardButton("Прислать лису")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id, text="Вы перешли в Картинки", reply_markup=markup)
    elif ms_text == "Прислать собаку":
        contents = requests.get('https://random.dog/woof.json').json()
        urlDOG = contents['url']
        bot.send_photo(chat_id, photo=urlDOG, caption="Бабака")
    elif ms_text == "Прислать лису":
        contents = requests.get('https://randomfox.ca/floof/').json()
        urlCAT = contents['image']
        bot.send_photo(chat_id, photo=urlCAT, caption="Рыжая")


    elif ms_text == "Игра":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Музыкальная викторина")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, back)
        bot.send_message(chat_id, text="Вы перешли в Игра", reply_markup=markup)
    elif ms_text == "Музыкальная викторина":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        quiz = Quiz()
        quiz_correctanswer = quiz.coransw
        print(quiz.answers)
        btn1 = types.KeyboardButton(quiz.answers[0])
        btn2 = types.KeyboardButton(quiz.answers[1])
        btn3 = types.KeyboardButton(quiz.answers[2])
        btn4 = types.KeyboardButton(quiz.answers[3])
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, back)
        bot.send_photo(chat_id, photo=quiz.kart, reply_markup=markup)

    elif ms_text == "Помощь" or ms_text == "/help":
        bot.send_message(chat_id, text="Автор: стдуент группы 1-мд-20 Поспелов Никита ")
    else:
        if ms_text == quiz_correctanswer:
            bot.send_message(chat_id, 'Верно')
        else:
            bot.send_message(chat_id, 'Не верно')






def get_text():
    array_texts = ['https://www.lyrics.com/lyric/28267385/Kendrick+Lamar/Bitch%2C+Don%E2%80%99t+Kill+My+Vibe', 'https://www.lyrics.com/lyric/29260986/Kendrick+Lamar/Swimming+Pools+%28Drank%29', 'https://www.lyrics.com/lyric/28219632/Kendrick+Lamar/Compton', 'https://www.lyrics.com/lyric/38645539/MORGENSHTERN/Cristal+%26+%D0%9C%D0%9E%D0%81%D0%A2', 'https://www.lyrics.com/lyric-lf/4533121/MORGENSHTERN/Lollipop', 'https://www.lyrics.com/lyric/35696775/Joji/Slow+Dancing+in+the+Dark', 'https://www.lyrics.com/lyric/35597036/Joji/Can%27t+Get+Over+You', 'https://www.lyrics.com/lyric-lf/2478358/SLAVA+MARLOW/%D0%9D%D0%B5%D1%82+%D0%9F%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC', 'https://www.lyrics.com/lyric/38646391/SLAVA+MARLOW/%D0%91%D1%8B%D1%81%D1%82%D1%80%D0%BE', 'https://www.lyrics.com/lyric/35730891/Big+Baby+Tape/Gimme+the+Loot', 'https://www.lyrics.com/lyric/36200175/Big+Baby+Tape/Surname', 'https://www.lyrics.com/lyric/36244422/The+Notorious+B.I.G./Big+Poppa', 'https://www.lyrics.com/lyric/36244423/The+Notorious+B.I.G./Juicy', 'https://www.lyrics.com/lyric/36619616/Travis+Scott/Highest+In+the+Room', 'https://www.lyrics.com/lyric/35355400/Travis+Scott/BUTTERFLY+EFFECT', 'https://www.lyrics.com/lyric/35297817/Travis+Scott/STOP+TRYING+TO+BE+GOD']
    bobtek = requests.get(random.choice(array_texts))
    soup = bs4.BeautifulSoup(bobtek.text, "html.parser")
    result_find = soup.select('#lyric-body-text')
    return result_find[0].getText()


# -----------------------------------------------------------------------
bot.polling(none_stop=True, interval=0)

print()