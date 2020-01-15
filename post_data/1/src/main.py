from telegram.ext import Updater, CommandHandler, CallbackContext, PicklePersistence
from telegram import Update
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

TOKEN = '1015576274:AAFLAeIEjhiGkSXoNFM4tvfiE5UK-D98T2s'

persistence = PicklePersistence('./db')

def parse_cmd(update: Update):
    command , text = update.message.text.split(' ', 1 )
    return command,text

def parse_db(context: CallbackContext):
    return context.user_data.setdefault('user_account', {})

def create(update: Update, context: CallbackContext):
    command, text = parse_cmd(update)
    parse_db(context)["account"] = text.split()
    update.message.reply_text('Account data saved 💾')

def delete(update: Update, context: CallbackContext):
    parse_db(context).pop("account")
    update.message.reply_text('Account data removed 💾')

def update(update: Update, context: CallbackContext):
    parse_db(context).pop("account")
    command , text = parse_cmd(update)
    parse_db(context)["account"] = text.split()
    update.message.reply_text('Account data updated 💾')

def read(update: Update, context: CallbackContext):
    if "account" in parse_db(context):
        update.message.reply_text('Username : {} \nPassword : {} \n'.format(parse_db(context)["account"][0],parse_db(context)["account"][1]))
    else:
        update.message.reply_text('Account data not exist, please add')

def main():
    updater = Updater(TOKEN, use_context=True, persistence=persistence)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('create', create))
    dp.add_handler(CommandHandler('delete', delete))
    dp.add_handler(CommandHandler('update', update))
    dp.add_handler(CommandHandler('read', read))
    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()

