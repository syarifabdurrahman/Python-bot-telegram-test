import traceback
from telegram import *
from telegram.ext import *
from requests import *
from Gempa_terkini import GempaTerkini
import response as r
import keys

def start_command(update:Update,context:CallbackContext):
    update.message.reply_text('Welcome to the bot!\n ')

def help_command(update:Update,context:CallbackContext):
    helpStr=[
     "1. /start to start",
     "2. /help to view helpers",
     "3. type 'bmkg' atau 'gempa terkini' untuk menampilkan gempa terkini ",
     ]
    text="\n"


    update.message.reply_text(text.join(helpStr))

def handle_message(update:Update,context:CallbackContext):
    text = str(update.message.text).lower()
    response= r.sample_responses(text)

    update.message.reply_text(response)
    if text == "bmkg" or text == "gempa terkini":
        buttons=[
            [InlineKeyboardButton("🗺️",callback_data="show_image")],
        ]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="Tampilkan gambar?")


def queryHandler(update:Update,context:CallbackContext):
    try:
        query = update.callback_query.data
        update.callback_query.answer()
        
        gempa_di_indonesia = GempaTerkini()
        gempa_di_indonesia.run()
        a = gempa_di_indonesia.get_image()

        if "show_image" in query:
            context.bot.send_photo(chat_id=update.effective_chat.id,photo=f"{a}")

    except:
        traceback.print_exc()


def error(update:Update,context:CallbackContext):
    print(context.error)

def main():
    updater= Updater(keys.token, use_context=True)
    dp= updater.dispatcher

    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("help",help_command))
    dp.add_handler(CallbackQueryHandler(queryHandler))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling(3.0)
    updater.idle()



if __name__ == "__main__":
    print('starting up bot')
    main()