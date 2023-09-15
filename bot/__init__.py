import telebot
import requests
import time

bot = telebot.TeleBot("5963775988:AAHEIZ6vo2hCnAVMNrQGBOdLo7jUs-AGS54")  # Replace with your bot token

# /start command for your bot
@bot.message_handler(commands=['start'])
def handle_start(message):
    start_message = '''
<b>Hey Folks,
Welcome to Tocsi Server Key Generator
Tab Here For Genrate 1hrs Key DDDDDD
      /getkey 
It's Work In All App
Join Our Channel @Tocsiserver </b>
    '''
    bot.reply_to(message, start_message, parse_mode='HTML')


@bot.message_handler(commands=['getkey'])
def handle_start(message):
    res = requests.get('https://tocsiiserver.xyz/Key/redirect.php')
    g = (res.text)
    t = '''
<b> We Genrate Key For 1 Hrs❤️
your Key Is 👇🏻👇🏻👇🏻</b>
    '''
    r = requests.get('https://api.github.com/events', stream = True)
    bot.reply_to(message, t+g[2600:2688], parse_mode='HTML')
    


# A text message handler
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    reply_text = message.text
    bot.reply_to(message, reply_text)

# Start the bot

bot.polling()
