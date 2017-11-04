import telebot 
from telebot import types 
from telebot import util
import time
import os
import scrapeo

bot = telebot.TeleBot("474881369:AAEZ8tf53Su3TUSnPeaJ2k4IuPPavtWLXGo")


def listener(messages): 
	for m in messages: 
        	if m.content_type == 'text': 
			cid = m.chat.id 
		    	print ("[" + str(cid) + "]: " + m.text) 

bot.set_update_listener(listener)
@bot.message_handler(commands=['holaclash']) 
def hola_mundo(update):
	chat_id = update.chat.id
   	mensaje= "Hola jugador de clash royale"
	bot.send_message( chat_id, mensaje)


bot.set_update_listener(listener)
@bot.message_handler(commands=['listacartas']) 
def listadocartas(update):
	chat_id = update.chat.id
	mensaje= scrapeo.mostrarcartas()
	bot.send_message( chat_id, mensaje)

bot.polling(none_stop=True)
