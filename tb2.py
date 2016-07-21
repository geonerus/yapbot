import time
from bd import *
import telebot
from func import GetState
print('я воркаю')
#token='244184804:AAFPQ14tkOVvs0CXny9epeUUhSRLpWd8iTY'
token='237129667:AAGQ1T7qmJ6OyrBriz_-XF3tNsKReSDqvAQ'
bot = telebot.TeleBot(token)
print(time.strftime('%H'))
while 5:
    if int(time.strftime('%H'))<17:
        t=((17-int(time.strftime('%H')))*3600)-(int(time.strftime('%M'))*60)+300
        
        print(t)
        time.sleep(t)
    a=GetState()
    if a[0]<5:
        for u in user.select(): 
            if a[3]==True:
                print('true')
                bot.send_message(u.userId, 'Сейчас пробки равны '+str(a[0])+'. Они снизятся в ближайшее время.')
            if a[3]==False:
                print('false')
                bot.send_message(u.userId, 'Сейчас пробки равны '+str(a[0])+'. Они Увеличатся в ближайшее время.')
            if a[3]==None:
                print('none')
                bot.send_message(u.userId, 'Сейчас пробки равны '+str(a[0])+'. Они не изменятся в ближайшее время.')
            time.sleep(3612*5)
    print('сплю')
    time.sleep(15*60)
    print('апдейт')
