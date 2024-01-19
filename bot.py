import telebot
from telebot import types

bot = telebot.TeleBot('6415511856:AAFDpvJ-2YsryCM_fv09CnYPBqOMiMlqpbg')


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'здравсствуйте! какое направление вы хотите выбрать?')
    markup = types.InlineKeyboardMarkup()
    btnIt = types.InlineKeyboardButton('айти')
    btnrobo = types.InlineKeyboardButton('робо')
    btnavto = types.InlineKeyboardButton('авто')
    btnaer = types.InlineKeyboardButton('аэро')
    btnIdk = types.InlineKeyboardButton('я не знаю')
    markup.row(btnIt, btnrobo, btnavto, btnaer, btnIdk)


def direction(message):
    None


bot.polling(none_stop=True)
