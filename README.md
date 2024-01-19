import telebot
from telebot import types

markup = types.InlineKeyboardMarkup()

bot = telebot.TeleBot('6415511856:AAFDpvJ-2YsryCM_fv09CnYPBqOMiMlqpbg')


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Здравствуйте! Какое направление вы хотите выбрать?', reply_markup=get_markup())


def get_markup():
    markup = types.InlineKeyboardMarkup()
    btnIt = types.InlineKeyboardButton('Айти', callback_data='it')
    btnrobo = types.InlineKeyboardButton('Робо', callback_data='robo')
    btnavto = types.InlineKeyboardButton('Авто', callback_data='auto')
    btnaer = types.InlineKeyboardButton('Аэро', callback_data='aero')
    btnIdk = types.InlineKeyboardButton('Я не знаю', callback_data='idk')
    markup.add(btnIt, btnrobo, btnavto, btnaer, btnIdk)
    return markup


@bot.callback_query_handler(func=lambda call: True)
def callback_markup(call):
    if call.data == 'it':
        ##bot.answer_callback_query(call.id, 'Вы выбрали Айти', reply_markup=itkvant())
        bot.send_message(call.message.chat.id, "Что вы хотите узнать?", reply_markup=itkvant())

    elif call.data == 'robo':
        bot.answer_callback_query(call.id, 'Вы выбрали Робо')

    elif call.data == 'auto':
        bot.answer_callback_query(call.id, 'Вы выбрали Авто')

    elif call.data == 'aero':
        bot.answer_callback_query(call.id, 'Вы выбрали Аэро')

    elif call.data == 'idk':
        bot.answer_callback_query(call.id, 'Если вы не знаете какое напрвление вам выбрать предлогаем пройти тест!')



def itkvant():
    btnItinfo = types.InlineKeyboardButton('Иноформация об квантуме', callback_data='itinf')
    btnItproj = types.InlineKeyboardButton('Примеры проектов созданые в It квантуме', callback_data='itproj')
    btnItteach = types.InlineKeyboardButton('Предподаватели квантума', callback_data='itteach')
    markup.add(btnItinfo)
    markup.add(btnItproj)
    markup.add(btnItteach)
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_infIt(call):
    if call.data == 'itinf':
        ##bot.answer_callback_query(call.id, 'Вы выбрали Айти', reply_markup=itkvant())
        bot.send_message(call.message.chat.id, "")

    elif call.data == 'itproj':
        bot.answer_callback_query(call.id, 'Вы выбрали Робо')

    elif call.data == 'itteach':
        bot.answer_callback_query(call.id, 'Вы выбрали Авто')



bot.polling(none_stop=True)
