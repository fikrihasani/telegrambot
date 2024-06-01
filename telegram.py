import os
import telebot

bot = telebot.TeleBot("7257981613:AAGG5XuQV3jF-H3E3PyZS1ypXHh4Zt8eCuc")

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()