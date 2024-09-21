import asyncio
from pytgcalls import idle
import os
import sys
import random
import asyncio
import redis, re
from pyrogram import Client
from pytgcalls import PyTgCalls
from config import user, dev, call, logger, logger_mode, botname, appp
from bot import bot_id

API_ID = int("27442758")
API_HASH = "8288c5c54f568ee346b3227271700b52"

# Get ur redis url from https://app.redislabs.com/
r = redis.from_url(
    'redis://default:7Y5TfjyNwOkPaRc8Bxn5oux1gXJUWM32@redis-18539.c267.us-east-1-4.ec2.redns.redis-cloud.com:18539')

def add_Bots(bots):
    if is_Bots(bots):
        return
    r.sadd(f"maker{bot_id}", str(bots))

def is_Bots(bots):
    try:
        a = get_Bots()
        if bots in a:
            return True
        return False
    except:
        return False

def del_Bots(bots):
    if not is_Bots(bots):
        return False
    r.srem(f"maker{bot_id}", str(bots))

def get_Bots():
    try:
        lst = []
        for a in r.smembers(f"maker{bot_id}"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except:
        return []
        
async def get_dev(bot_username):
  dev_id = dev.get(bot_username)
  if not dev_id:
   for x in get_Bots():
    if x[0] == bot_username:
     dev_id = x[1]
     dev[bot_username] = dev_id
     return dev_id
  return dev_id

async def get_logger(bot_username):
  logg = logger.get(bot_username)
  if not logg:
   for x in get_Bots():
    if x[0] == bot_username:
     logg = x[4]
     logger[bot_username] = logg
     return logg
  return logg
  
async def get_owner_id(client):
    bot_username = client.me.username
    for x in get_Bots():
        if x[0] == bot_username:
            owner_id = x[1]
            dev[bot_username] = owner_id
            return int(owner_id)
            
async def get_userbot(bot_username):
  userbot = user.get(bot_username)
  if not userbot:
   for x in get_Bots():
    if x[0] == bot_username:
     SESSION = x[3]
     userbot = Client("CASER", api_id=API_ID, api_hash=API_HASH, session_string=SESSION)
     user[bot_username] = userbot
     return userbot
  return userbot

async def get_call(bot_username):
  calll = call.get(bot_username)
  if not calll:
   for x in get_Bots():
    if x[0] == bot_username:
     userbot = await get_userbot(bot_username)
     calo = PyTgCalls(userbot, cache_duration=100)
     await calo.start()
     call[bot_username] = calo
     return calo
  return calll  
  
