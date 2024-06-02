import telebot
from telebot import types
from config import token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    item_yes = types.KeyboardButton('Да')
    item_no = types.KeyboardButton('Нет')
    markup.add(item_yes, item_no)
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}! Хочешь стать участником арт-базара?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Нет')
def handle_no(message):
    bot.send_message(message.chat.id, "С какой целью обратился ко мне?")

@bot.message_handler(func=lambda message: message.text == 'Да')
def handle_yes(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    item_agree = types.KeyboardButton('Готов')
    item_disagree = types.KeyboardButton('Не готов')
    markup.add(item_agree, item_disagree)
    bot.send_message(message.chat.id, "Отлично! Давай начнем с нескольких вопросов...", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Готов')
def handle_agree(message):
    bot.send_message(message.chat.id, "Ты дизайнер/художник или владелец магазина?")

bot.polling()

