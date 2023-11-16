import telebot
from api_key import API_KEY
import stealer
import stealer_type as steal

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
    try:
        if "songsterr" in message.text.lower():
            bot.reply_to(message, stealer.get_gp_file(message.text.lower(), steal.BY_URL))
        else:
            bot.reply_to(message, stealer.get_gp_file(message.text.lower(), steal.BY_SEARCH_STRING))

    except:
        bot.reply_to(message, "Something went wrong")


bot.infinity_polling()
