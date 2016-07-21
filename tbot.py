import peewee
#пакет в пипе называется pytelgrambotapi
import telebot
from bd import *
#token='244184804:AAFPQ14tkOVvs0CXny9epeUUhSRLpWd8iTY'
token='237129667:AAGQ1T7qmJ6OyrBriz_-XF3tNsKReSDqvAQ'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def main(message):
    
    #bot.send_message(message.chat.id, message.text)
    if message.text.lower()=='add':
        try:
            user.create(userId=message.chat.id)
            bot.send_message(message.chat.id, 'Добавленно, наверно')
            return True
        except peewee.IntegrityError:
            bot.send_message(message.chat.id, 'Вы уже есть в нашей базе данных!')
            return True
    if message.text.lower()=='del':
        try:
            user.get(user.userId==message.chat.id).delete_instance()
            bot.send_message(message.chat.id, 'Удалено, наверно')
            return True
        except BaseException: #я не смог сделать это исключение нормально, извините за быдлокод
            bot.send_message(message.chat.id, 'Вас нет в нашей базе данных!')
            return True
    bot.send_message(message.chat.id, 'я умею только добавлять пользователя (add) и удолять (del)')
    return True

if __name__ == '__main__':
    print('я работаю')
    bot.polling(none_stop=True)
