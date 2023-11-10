import telebot
from api_key import API_KEY
import stealer

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['test'])
def test(message):
    bot.send_message(message.chat.id, "zhopa")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Paste a link to a songsterr tab and I will return a direct link to a Guitar "
                                      "Pro file")


@bot.message_handler(content_types=['text'])
def text_handler(message):
    if "songsterr" in message.text.lower():
        try:
            bot.reply_to(message, stealer.get_gp_file(message.text.lower()))
        except:
            bot.reply_to(message, "Something went wrong")
    else:
        bot.reply_to(message, "Ты ебанулся, хуила? Тебе же долбаёбине английским языком написали, запости линк на сонгстерр")


bot.polling()
