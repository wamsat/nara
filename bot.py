from telegram.ext import Updater

from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import  Filters
from settings import  TG_TOKEN, TG_API_URL

def sms(bot,update):
    print('Кто -то отправил команду /start. Что мне делать?')
    bot.message.reply_text('Здравсвуйте, {}! \n'
    'Поговорите со мной!'.format(bot.message.chat.first_name))
def parrot(bot, update):
    print(bot.message.text)
    bot.message.reply_text(bot.message.text)


def main():
    my_bot = Updater('1475163613:AAEDMOAcb-9X4Q9LFDfsUUi0wofj_bAONAo', 'https://telegg.ru/orig/bot', use_context=True)
    my_bot.dispatcher.add_handler(CommandHandler('start',sms))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text,parrot))
    my_bot.start_polling()
    my_bot.idle()

main()