import telebot

token = "temp"
bot = telebot.TeleBot(token, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

data = {}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text.startwith("یادت"):
        data[message.from_user.username] = message.text
        answer = "باشه ارباب یادم موند"
    else:
        user = message.from_user.username
        if user in data: 
            answer = data[user]
        else:
            answer = "جدیدی که"
    bot.reply_to(message, answer)

bot.infinity_polling()