import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "TOKEN_AQUI"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    markup = InlineKeyboardMarkup(row_width=2)
    button1 = InlineKeyboardButton("GRUPO", url="https://t.me/GRUPOCN")
    button2 = InlineKeyboardButton("CANAL CODERS", url="https://t.me/CODIGOCN")
    button3 = InlineKeyboardButton("CANAL DO VILHALVA", url="https://t.me/VILHALVA100_CANAL")
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, "Use os botões inline para acessar os links!", reply_markup=markup)

bot.polling()
