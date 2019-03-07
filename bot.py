### Required imports ###
import os
import logging
from datetime import datetime

from telegram.ext import Updater, MessageHandler, CommandHandler, Filters


### Command handlers ###
def hello(bot, update):
    """ Handles command /hello """
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id, 'Hello world!')


def handle_message(bot, update):
    """ Handles messages that match "all" filter """
    chat_id = update.message.chat.id

    # Check that we are dealing with message involving text
    if update.message.text:
        words = update.message.text.split()

        # Loop through keywords and stickers in pairs
        for hotword, sticker in sticker_map.items():

            # Send a sticker for each matching keyword
            if hotword in words:
                bot.sendSticker(chat_id, sticker)


### Config ###
# Set logging on and level to info
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s'
)

# Load bot token from environment variables
token = os.environ['TG_TOKEN']

# Create mapping for keywords and stickers
sticker_map = {
    'sos': 'CAADBAADKgADvbDdC_O7HYCpzvT_Ag',
    'valde': 'CAADBAADQAADLswmBje1Jh_E-RtbAg',
    ':D': 'CAADBAADagADUV7SAngezZiEm4kmAg',
    'saukko': 'CAADBAADBQADDzYrCUepNdq7cgVyAg',
    'joo': 'CAADBAADDQEAAkX3XwcDoHchIyp7dQI',
    'resilar': 'CAADBAADRQIAAtSNlgGZiGPuJp6IeQI',
    'setii': 'CAADBAADQgADLswmBl7QG4W_aDBZAg',
    'nmwsbrai': 'CAADBAADngADvbDdC8F_2pka0oOTAg',
    'ferrantai': 'CAADBAADhAADvbDdC3Tu3538DOsDAg',
    '9': 'CAADBAADTQADvbDdC4mFHb8kC26AAg',
    'tää': 'CAADBAADHgADYqcCFeXF-TQNMnZKAg'
}


### Start the Bot ###
updater = Updater(token)

# Add event handlers
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(MessageHandler(Filters.all, handle_message))

# Start the bot and then idle to prevent code from finishing
updater.start_polling()
updater.idle()
