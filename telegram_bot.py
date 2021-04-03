#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

API_TOKEN = ''

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hello! I'm a price trackerrrrrr!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.text == 'hello':
        bot.reply_to(message, 'english')
    elif message.text == 'ciao':
        bot.reply_to(message, 'italiano')
    else:
        bot.reply_to(message, 'different language')


bot.polling()
