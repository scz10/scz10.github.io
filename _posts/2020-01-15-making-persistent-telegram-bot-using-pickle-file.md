---
title: Python Telegram Bot - Making persistent bot using pickle file
mode: immersive
header:
  theme: dark
article_header:
  type: overlay
  theme: dark
  background_color: '#123'
  background_image: false
tags: [python,telegram-bot]
key: python-telegram-bot-1
aside:
  toc: true
---

# Background
In version 12.0b1 [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) a wrapper for telegram bot, release persistence mechanism to telegram.ext package.

<!--more-->
---

## What data can become persistent?
This feature is designed to make **chat_data**, **user_data** and **ConversationHandler** state become persistent. 

## Existing code, what do i need to change?
* Create a persistence objectCreate a persistence object

  e.g. using **pickle persistence** class
  ```
    persistence = PicklePersistence('./db')
  ```

* Construct Updater with the persistence
  ```
    updater = Updater(TOKEN, use_context=True, persistence=persistence)
  ```

## Getting Started
Today im gonna build a simple bot that will do [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete). that wil save the data to pickle file.

### Create new bot
First thing first we need a bot. to register a bot you should go to the [BotFather](https://telegram.me/BotFather) ( login your normal telegram account ). and then simply send command **/newbot** . and the you will be asked what bot name and username for your bot. after that you will get token for your bot.

 ![bot-created](https://chmy.xyz/post_data/1/bot-created.png){:.border.rounded}

### Install python virtual environment (optional)

#### First install virtualenv package first
```
pip install virtualenv
```
#### Now create your virtualenv
To create virtual environment, you must specify a path. ( e.g. installing on local directory called 'venv' )
```
virtualenv venv
```
#### Activate the virtual environment
To activate you can type

MacOS / Linux 
```
source mypython/bin/activate
```
Windows
```
venv\Scripts\activate
```
#### Deactive virtual environment
```
deactivate
```

### Install the library
In this tutorial we only need **python-telegram-bot** library
Install it by type following

```
pip3 install python-telegram-bot
```

### Now the code.. 
In this code, i will make 4+2 function (or we can call it command in this bot). which is **/create**, **/read**, **/update** and **/delete**.

#### Import the libraries, define TOKEN bot and logging

```python
from telegram.ext import Updater, CommandHandler, CallbackContext, PicklePersistence
from telegram import Update
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
TOKEN = 'urtokenhere'
```

#### The first 2 function

```python
def parse_db(context: CallbackContext):
    return context.user_data.setdefault('user_account', {})
```
This parse db function used to retrieve object that unique to every user. because in **CallbackContext** there is an **user_data** object. then we use **setdefault** to retrieve the data if exist or to create if it empty.

```python
def parse_cmd(update: Update):
    command , text = update.message.text.split(' ', 1 )
    return command,text
```
this parse_cmd function used to get the user input. we can read user input that delimited by ' ' (space) and also what command it come from.

#### The /create function
```python
def create(update: Update, context: CallbackContext):
    command, text = parse_cmd(update)
    parse_db(context)["account"] = text.split()
    update.message.reply_text('Account data saved 💾')
```
![create-func](https://chmy.xyz/post_data/1/create-img.png){:.border.rounded}

#### The /read function
```python
def read(update: Update, context: CallbackContext):
    if "account" in parse_db(context):
        update.message.reply_text('Username : {} \nPassword : {} \n'.format(parse_db(context)["account"][0],parse_db(context)["account"][1]))
    else:
        update.message.reply_text('Account data not exist, please add')
```
![read-func](https://chmy.xyz/post_data/1/read-img.png){:.border.rounded}

#### The /update function
```python
def update(update: Update, context: CallbackContext):
    parse_db(context).pop("account")
    command , text = parse_cmd(update)
    parse_db(context)["account"] = text.split()
    update.message.reply_text('Account data updated 💾')
```
![update-func](https://chmy.xyz/post_data/1/update-read-img.png){:.border.rounded}

#### The /delete function
```python
def delete(update: Update, context: CallbackContext):
    parse_db(context).pop("account")
    update.message.reply_text('Account data removed 💾')
```
![delete-func](https://chmy.xyz/post_data/1/delete-read-img.png){:.border.rounded}

#### The Main function
```python
def main():

    # init the Updater
    updater = Updater(TOKEN, use_context=True, persistence=persistence)
    
    # add command handler 'command in telegram' -> function name
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('create', create))
    dp.add_handler(CommandHandler('delete', delete))
    dp.add_handler(CommandHandler('update', update))
    dp.add_handler(CommandHandler('read', read))

    # make the bot idle and receive update frequently
    updater.start_polling()
    updater.idle()

# to make program run from  main()
if __name__ == '__main__':
    main()
```
#### Sums up

```python
from telegram.ext import Updater, CommandHandler, CallbackContext, PicklePersistence
from telegram import Update
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

TOKEN = 'urtokenhere'

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

```

Thats it, now you have a persisten bot!! :tada: :tada: :tada:.
Next you need to deploy it to make it "online". i will post about it later. and also you can check this code in my Github 
[Here](https://github.com/scz10/scz10.github.io/blob/master/post_data/1/src/main.py)

See you!! in my next post :grin: :grin: