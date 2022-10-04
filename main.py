from email import message
from telegram.ext import *
import keys

print('starting up bot')

def start_command(update,context):
    update.message.reply_text('Hello there! I\'m a bot. This is for test, nice to meet you')

def help_command(update,context):
    update.message.reply_text('Try typing anything and i will respond!')

def custom_command(update,context):
    update.message.reply_text('This is a custom command!')




def handle_response(text: str) -> str:  # parameter type of string and return a string
    if 'hello' in text:
        return 'Hey there!'

    if 'how are you' in text:
        return 'Im doing good'


    return 'I don\'t understand'

def handle_message(update,context):
    message_type = update.message.chat.type
    text = str(update.message.chat).lower()
    response = ''

    print(f'User ({update.message.chat.id}) says: "{text}" in: {message_type}')

    if message_type == 'group':
        if '@MrTestSyarifBot' in text:
            new_text=text.replace('@MrTestSyarifBot','').strip()
            response = handle_response(new_text)

    else:
        response = handle_response(text)

    update.message.reply_text(response)


def error(update,context):
    print(f'User ({update}) caused error: {context.error}"')


if __name__ == '__main__':
    updater=Updater(keys.token,use_context=True)
    dispatch=updater.dispatcher

    #commands
    dispatch.add_handler(CommandHandler('start',start_command))
    dispatch.add_handler(CommandHandler('help',help_command))
    dispatch.add_handler(CommandHandler('custom',custom_command))

    #Messages
    dispatch.add_handler(MessageHandler(Filters.text,handle_message))

    #Errors
    dispatch.add_error_handler(error)

    #Run bot with schedule or how often this running
    updater.start_polling(1.0)
    updater.idle()