from telebot import * 
from telebot.types import *
import time

bot = telebot.TeleBot("6306162064:AAEBC9t6QLhQg9crdIK9gL2-ONauDJdQiPY")

маты = [
    'лох', 'сука', 'бля', 'пиздец', 'сучары', 'хуй', 'пизда', 'блин', 'ебать', 'нахуй', 'блядь', 'ебануться', 'пидар', 'гандон', 'мудак', 'член', 'долбоеб', 'срака', 'ебаный', 'ебаться', 'ебало', 'хуесос', 'ебло', 'ебал', 'ебанный', 'хуило', 'пердун', 'падла', 'блять']
@bot.message_handler(func=lambda message: True)
def main(message):
    
    for мат in маты:
        if мат in message.text.lower():

            bot.delete_message(message.chat.id, message.message_id)
            break
        if message.text.startswith('!ban'):
            if message.reply_to_message:
                user_id = message.reply_to_message.from_user.id 
                duration = int(message.text.split()[1])  
                bot.restrict_chat_member(message.chat.id, user_id, until_date=time.time() + duration * 60)  
                bot.send_message(message.chat.id, f"Пользователь {message.reply_to_message.from_user.first_name} заблокирован на {duration} минут.")
                break
            else:
                bot.reply_to(message.chat.id, f"Это должно быть ответом")
    bot.send_message(1245413255, f"Отправитель: {message.from_user.first_name}\nСообщение: {message.text} ")
    




bot.polling(none_stop=True)