
import bs4
import requests
import telebot
from telebot import types

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
        btn2 = types.KeyboardButton("WEB-камера")
        btn3 = types.KeyboardButton("Управление")
        back = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(chat_id, text="Вы в главном меню ", reply_markup=markup)
    elif ms_text == "Треки":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Прислать обложку")
        btn2 = types.KeyboardButton("Прислать текст песни")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id, text="Вы перешли в Треки", reply_markup=markup)
    elif ms_text == "/cover" or ms_text == "Прислать обложку":
        bot.send_photo(chat_id, photo="https://upload.wikimedia.org/wikipedia/ru/9/97/One_More_City.jpg")
    elif ms_text == "Прислать текст песни":
        bot.send_message(chat_id, text="Она улетела, уехала или умерла\nЭтой ночью\nОна улетела, уехала или умерла\nНе знаю точно\nОна улетела, уехала или умерла\nТак будет проще\nОна лишь хотела тепла, но как спичка сгорела дотла\nВ моей личке последняя строчка")
    elif ms_text == "WEB-камера":
        bot.send_message(chat_id, text="будет позже")
    elif ms_text == "Управление":
        bot.send_message(chat_id, text="будет позже")
    elif ms_text == "Помощь" or ms_text == "/help":
        bot.send_message(chat_id, text="Автор: стдуент группы 1-мд-20 Поспелов Никита ")
    else:
        bot.send_message(chat_id, text="Вас слышно... Ваше сообщение: " + ms_text)
def get_text():
    array_texts = []
    req_anek = requests.get('https://www.azlyrics.com/lyrics/rexorangecounty/sunflower.html')
    soup = bs4.BeautifulSoup(req_anek.text, "html.parser")
    result_find = soup.select('body > div.container.main-page > div > div.col-xs-12.col-lg-8.text-center > div:nth-child(8)')
    return result_find.getText().strip()


# -----------------------------------------------------------------------
bot.polling(none_stop=True, interval=0) # Запускаем бота

print()