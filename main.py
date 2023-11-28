import telebot

bot = telebot.TeleBot('6745555966:AAE6f0lPa_9P-Q-qRhPsQkdDgjB4oLoxljw')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет!', parse_mode='Markdown')


@bot.message_handler(commands=['help'])
def main2(message):
    bot.send_message(message.chat.id, 'Чем тебе помочь?')


@bot.message_handler(commands=['Ymskyl'])
def main3(message):
    bot.send_message(message.chat.id,
                     'Умскул - онлайн-школа для учеников 9-11 классов, где ты сможешь подготовиться к ЕГЭ и ОГЭ, подтянуть оценки в 10 классе или подготовиться к олимпиаде.')


@bot.message_handler(commands=['minus'])
def main4(message):
    bot.send_message(message.chat.id, 'Есть ли минусы у этой школы? Правильно, нет минусов.')


bot.infinity_polling()