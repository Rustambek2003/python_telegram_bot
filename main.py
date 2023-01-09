from telegram import Bot
import os

# get token from env
TOKEN = os.environ['TOKEN']
# Create a bot object
bot = Bot(token=TOKEN)

chat_id =996172963
# Send message
bot.sendMessage(chat_id=chat_id,text='Salom')
