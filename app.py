import os
from flask import Flask
import random
from pyrogram import Client, filters
import requests
from config import *
import asyncio

# TinyURL API 

API_KEY=API_KEY

# Session Authorization

app = Client("tinyurl_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Start Command

@app.on_message(filters.command('start'))
async def start_command_handler(client, message):
    await message.reply_photo(
            photo=random.choice(PICS),
            caption=(f"<b>𝙷𝚎𝚕𝚕𝚘 !! {message.from_user.mention} \n𝚂𝚎𝚗𝚍 𝚖𝚎 𝙻𝚘𝚗𝚐 𝚄𝚁𝙻, 𝙸'𝚕𝚕 𝚂𝚑𝚘𝚛𝚝𝚎𝚗 𝚒𝚝.</b>")
    )

# url shorten via the TinyURL API

@app.on_message(filters.regex('https?://\S+'))
async def url_message_handler(client, message):
    try:
        response = requests.get(f'https://tinyurl.com/api-create.php?url={message.text}&apikey={API_KEY}')
        shortened_url = response.text
        await message.reply_text(f'𝙷𝚎𝚛𝚎 𝚒𝚜, \n𝚈𝚘𝚞𝚛 𝚂𝚑𝚘𝚛𝚝𝚎𝚗 𝙻𝚒𝚗𝚔 : {shortened_url}')
    except:
       await message.reply_text('Sorry. Please Try Again.')

# Check whether Bot Started or Idle !!

print('Bot Started !!')

# Run

app = Flask(__name__)

# ...

if __name__ == '__main__':

# Bind to PORT if defined, otherwise default to 5000.

port = int(os.environ.get('PORT', 8080))

app.run(host='0.0.0.0', port=port)
