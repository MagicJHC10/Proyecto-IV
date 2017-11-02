import telebot 
from telebot import types 
from telebot import util
import time # Librería para hacer que el programa que controla el bot no se acabe.
import os
bot = telebot.TeleBot("474881369:AAEZ8tf53Su3TUSnPeaJ2k4IuPPavtWLXGo")
chat_id=update.message.chat_id,
#############################################
# log                                       #
#############################################
def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
	for m in messages: # Por cada dato 'm' en el dato 'messages'
        	if m.content_type == 'text': # Filtramos mensajes que sean tipo texto.
			cid = m.chat.id # Almacenaremos el ID de la conversación.
		    	print ("[" + str(cid) + "]: " + m.text) # Y haremos que imprima algo parecido a esto -> [52033876]: /start

bot.set_update_listener(listener)
@bot.message_handler(commands=['holaclash']) 
# Método que mandará el mensaje "¡Hola, lector de Bytelix!"
def hola_mundo(update):
	chat_id = update.chat.id
   	mensaje='¡Hola, jugador de Clash Royale!'
	bot.send_message( chat_id, mensaje)

# Método que mandará el logo de la página
#def logo(bot, update):
    # Enviamos de vuelta una foto. Primero indicamos el ID del chat a donde
    # enviarla y después llamamos al método open() indicando la dónde se encuentra
    # el archivo y la forma en que queremos abrirlo (rb = read binary)
    #bot.sendPhoto(chat_id=update.message.chat_id, photo=open('Icono.png', 'rb'))

bot.polling(none_stop=True)
