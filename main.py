import os
import telebot

API_TOKEN = '9178523960:AAHWU7_Qd1G6xLXqYshqQNy8YCDykPvo-58'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True, content_types=['text', 'photo', 'sticker', 'video', 'voice', 'document'])
def answer_all(message):
    bot.send_message(message.chat.id, "fuck you")

if __name__ == '__main__':
    bot.polling(none_stop=True)
