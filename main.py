import telebot
 
TOKEN = 'paste your token from BotFather here'

#Init the  bot with token
bot = telebot.TeleBot(TOKEN)

#To catch the message you need to use this decorator. 
@bot.message_handler(commands=['start'])
def send_hello(message):
    bot.reply_to(message, """Hello world!""")
  
#Launches the bot in infinite loop mode with additional
#...exception handling, which allows the bot
#...to work even in case of errors. 
bot.infinity_polling()

