import os
import random
from pyrogram import Client, filters
import requests
from requests import get
from flask import Flask
from config import *
import aiohttp
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
            caption=(f"<b>š·šššš !! {message.from_user.mention} \nšššš šš š»ššš ššš», šø'šš ššššššš šš.</b>")
    )

# url shorten via the TinyURL API

@app.on_message(filters.regex('https?://\S+'))
async def url_message_handler(client, message):
    try:
        response = requests.get(f'https://tinyurl.com/api-create.php?url={message.text}&apikey={API_KEY}')
        shortened_url = response.text
        await message.reply_text(f'š·ššš šš, \nšššš ššššššš š»ššš : {shortened_url}')
    except:
        await message.reply_text('Sorry. Please Try Again.')

# Check whether Bot Started or Idle !!



print('Bot Started !!')

# Run

port = int(os.environ.get('PORT', 8080))

app.run()
