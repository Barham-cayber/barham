import asyncio
import requests
import random
import re
import textwrap
import aiofiles
import aiohttp
import os
import sqlite3
import time
import datetime
from pyrogram import Client as client
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from pyrogram import filters, Client
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from typing import List, Union
from pyrogram import *
import pyromod.listen
from dotenv import load_dotenv
from os import getenv
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import *
from pyrogram.errors import PeerIdInvalid
import aiohttp
from datetime import datetime
from random import choice
from collections import defaultdict
from pyrogram import enums
from pyrogram.types import ChatPermissions, ChatPrivileges
from aiohttp import ClientSession
from traceback import format_exc
import string
import lyricsgenius as lg
from pyrogram.types import (InlineKeyboardButton, ChatPermissions, InlineKeyboardMarkup, Message, User)
import sys
from pyrogram.errors import FloodWait
from os import remove
from asyncio import sleep
from pyrogram.types import *
from telegraph import upload_file
from unidecode import unidecode
import sqlite3
from pyrogram import Client, idle
from random import randint
from pyrogram.enums import ChatType
from pyrogram.types import Chat, User
from asyncio import gather
from io import BytesIO
from pyrogram import Client, filters
from config import *
from config import user, dev, call, logger, logger_mode, botname, appp
from CASERr.daty import get_call, get_userbot, get_dev, get_logger
from CASERr.CASERr import get_channel, devchannel, source, caes, johned





@Client.on_message(filters.command(["قفل الدردشه","قفل الدردشة"], "")) 
async def enabled(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
        if message.chat.id in mangof:
            return await message.reply_text(f"عذرا عزيزي [ {message.from_user.mention} ] الامر معطل من قبل مالك الجروب ✨✅")
        await client.set_chat_permissions(message.chat.id, ChatPermissions(can_send_messages=False))
        await message.reply_text(f"• تم قفل الدردشه بواسطه ↤︎「 {message.from_user.mention}")
    else:
        return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر يخص المالك والمشرفين فقط ✨♥")
   
@Client.on_message(filters.command(["فتح الدردشه","فتح الدردشة"], "")) 
async def undard(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
        if message.chat.id in mangof:
            return await message.reply_text(f"عذرا عزيزي [ {message.from_user.mention} ] الامر معطل من قبل مالك الجروب ✨✅")
        await client.set_chat_permissions(message.chat.id, ChatPermissions(can_send_messages=True))
        await message.reply_text(f"• تم فتح الدردشه بواسطه ↤︎「 {message.from_user.mention}")
    else:
        return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر يخص المالك والمشرفين فقط ✨♥")
    
@Client.on_message(filters.command("قفل التثبيت", "")) 
async def taspit(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
       if message.chat.id in mangof:
           return await message.reply_text(f"عذرا عزيزي [ {message.from_user.mention} ] الامر معطل من قبل مالك الجروب ✨✅")
       await client.set_chat_permissions(message.chat.id, ChatPermissions(
       can_pin_messages=False,
       can_send_messages=True))
       await message.reply_text(f"• تم قفل التثبيت بواسطه ↤︎「 {message.from_user.mention}")
    else:
       return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر يخص المالك والمشرفين فقط ✨♥")
       
@Client.on_message(filters.command("فتح التثبيت", "")) 
async def tasspit(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
       if message.chat.id in mangof:
           return await message.reply_text(f"عذرا عزيزي [ {message.from_user.mention} ] الامر معطل من قبل مالك الجروب ✨✅")
       await client.set_chat_permissions(message.chat.id, ChatPermissions(
       can_pin_messages=True,
       can_send_messages=True))
       await message.reply_text(f"• تم فتح التثبيت بواسطه ↤︎「 {message.from_user.mention}")
    else:
       return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر يخص المالك والمشرفين فقط ✨♥")
       
@Client.on_message(filters.command("قفل الدعوة", "")) 
async def dasoo(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
       if message.chat.id in mangof:
           return await message.reply_text(f"عذرا عزيزي [ {message.from_user.mention} ] الامر معطل من قبل مالك الجروب ✨✅")
       await client.set_chat_permissions(message.chat.id, ChatPermissions(
       can_invite_users=False,
       can_send_messages=True))
       await message.reply_text(f"• تم قفل الدعوة بواسطه ↤︎「 {message.from_user.mention}")
    else:
       return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر يخص المالك والمشرفين فقط ✨♥")
  
@Client.on_message(filters.command("فتح الدعوة", "")) 
async def zombeee(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
       if message.chat.id in mangof:
           return await message.reply_text(f"عذرا عزيزي [ {message.from_user.mention} ] الامر معطل من قبل مالك الجروب ✨✅")
       await client.set_chat_permissions(message.chat.id, ChatPermissions(
       can_invite_users=True,
       can_send_messages=True))
       await message.reply_text(f"• تم فتح الدعوة بواسطه ↤︎「 {message.from_user.mention}")
    else:
       return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر يخص المالك والمشرفين فقط ✨♥")
   
@Client.on_message(filters.command("قفل الميديا", "")) 
async def mediazomb(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return    
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
       if message.chat.id in mangof:
           return await message.reply_text(f"عذرا عزيزي [ {message.from_user.mention} ] الامر معطل من قبل مالك الجروب ✨✅")
       await client.set_chat_permissions(message.chat.id, ChatPermissions(
       can_invite_users=True,
       can_send_media_messages=False,
       can_send_messages=True))
       await message.reply_text("تم قفل الميديا")
    else:
       return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر يخص المالك والمشرفين فقط ✨♥")
  
@Client.on_message(filters.command("فتح الميديا", "")) 
async def zombmeddia(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
       if message.chat.id in mangof:
           return await message.reply_text(f"عذرا عزيزي [ {message.from_user.mention} ] الامر معطل من قبل مالك الجروب ✨✅")
       await client.set_chat_permissions(message.chat.id, ChatPermissions(
       can_send_media_messages=True,
       can_pin_messages=True,
       can_send_messages=True))
       await message.reply_text("تم فتح الميديا")
    else:
       return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر يخص المالك والمشرفين فقط ✨♥")
    
@Client.on_message(filters.command("قفل المتحركات", "")) 
async def motahark(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
       if message.chat.id in mangof:
           return await message.reply_text(f"عذرا عزيزي [ {message.from_user.mention} ] الامر معطل من قبل مالك الجروب ✨✅")
       await client.set_chat_permissions(message.chat.id, ChatPermissions(
       can_send_other_messages=False,
       can_pin_messages=True,
       can_add_web_page_previews=True,
       can_invite_users=True,
       can_send_media_messages=True,
       can_send_messages=True))
       await message.reply_text("تم قفل المتحركات")
    else:
       return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر يخص المالك والمشرفين فقط ✨♥")
   
@Client.on_message(filters.command("فتح المتحركات", ""))
async def motazombie(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
       if message.chat.id in mangof:
           return await message.reply_text(f"عذرا عزيزي [ {message.from_user.mention} ] الامر معطل من قبل مالك الجروب ✨✅")
       await client.set_chat_permissions(message.chat.id, ChatPermissions(
       can_send_other_messages=True,
       can_pin_messages=True,
       can_add_web_page_previews=True,
       can_invite_users=True,
       can_send_media_messages=True,
       can_send_messages=True))
       await message.reply_text("تم فتح المتحركات")
    else:
       return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر يخص المالك والمشرفين فقط ✨♥")
       

@Client.on_message(filters.command(["حذف", "مسح"], "") & filters.group)
async def delete_message(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
        if message.reply_to_message is not None:
            replied_user = message.reply_to_message.from_user
            await message.delete()
            await client.delete_messages(message.chat.id, [message.reply_to_message.id, message.id])
            await message.reply_text(f"تم حذف رسالة هذا الشخص {replied_user.mention} بنجاح ✨✅")
    else:
        await message.reply_text(f"عذرًا عزيزي {message.from_user.mention}\n هذا الأمر يخص المالك والمشرفين فقط ✨♥")
       
@Client.on_message(filters.new_chat_members)
async def welco857me(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    try:
        user = await client.get_chat(OWNER_ID)
        CASER = user.username 
        if message.new_chat_members[0].username == f"{CASER}":
            try:
                chat_id = message.chat.id
                user_id = message.new_chat_members[0].id
                await client.promote_chat_member(
                    chat_id=chat_id,
                    user_id=user_id,
                    privileges=ChatPrivileges(
                        can_promote_members=True,
                        can_manage_video_chats=True,
                        can_pin_messages=True,
                        can_invite_users=True,
                        can_restrict_members=True,
                        can_delete_messages=True,
                        can_change_info=True
                    )
                )
                await client.set_administrator_title(chat_id, user_id, "مطور البوت")
                await client.send_message(message.chat.id, 
                    f"**انضم مطور البوت الى هنا الآن [مطور البوت](https://t.me/{CASER})⚡** يرجى من الأعضاء احترام وجوده 🥷🥷"
                )
            except Exception as e:
                await client.send_message(message.chat.id, f"**انضم مطور البوت الى هنا الآن [مطور البوت](https://t.me/{CASER})⚡** يرجى من الأعضاء احترام وجوده 🥷🥷")
    except Exception as e:
        print(e)
	
@Client.on_message(filters.command(["معلوماته","كشف"], ""))
async def kashf(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.reply_to_message:
       user_id = message.reply_to_message.from_user.id
       user = await client.get_chat_member(message.chat.id, user_id)  
       name = user.user.first_name
       CASER = await client.get_chat(user_id)
       bioo = CASER.bio
    elif message.text:
       username = message.text.split(" ", 1)[1]
       user = await client.get_chat_member(message.chat.id, username)
       name = user.user.first_name
       CASER = await client.get_chat(username)
       bioo = CASER.bio
    else:
       await message.reply_text("قم بإرسال الأمر مع اسم المستخدم الذي ترغب في رفعه")
       return
    await message.reply_text(f"❤ ¦ ɴᴀᴍᴇ : {user.user.mention}\n🥰 ¦ ᴜѕᴇ : @{user.user.username}\n🔥 ¦ ɪᴅ : {user.user.id}\n♥¦ ɪᴅ ᥇𝓲ꪮꪮ : {bioo}\n?? ¦ ɪᴅ ᴄʜᴀᴛ : {message.chat.id}\n☠️ ¦ ᴄʜᴀᴛ : {message.chat.title}\n💕 ¦ ɢʀᴏᴜᴘ : @{message.chat.username}\n", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(name, url=f"https://t.me/{user.user.username}")]]))

@Client.on_message(filters.command(["المالك", "صاحب الخرابه", "المنشي"], "")) 
async def ownner(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    x = []
    async for m in client.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
         if m.status == ChatMemberStatus.OWNER:
            x.append(m.user.id)
    if len(x) != 0:        
       m = await client.get_users(int(x[0]))
       if m.photo:
         async for photo in client.get_chat_photos(x[0],limit=1):
          await message.reply_photo(photo.file_id,caption=f"🧞‍♂️ ¦𝙺𝙸𝙽𝙶 :{m.first_name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{m.username}\n🎃 ¦𝙸𝙳 :{m.id}\n✨ ¦𝙲𝙷𝙰𝚃: {message.chat.title}\n♻️ ¦𝙸𝙳.𝙲𝙷𝙰𝚃 :{message.chat.id}",reply_markup=InlineKeyboardMarkup(
             [              
               [          
                 InlineKeyboardButton(m.first_name, url=f"https://t.me/{m.username}")
               ],             
             ]                 
            )                     
          )
       else:
        await message.reply_text(f"🧞‍♂️ ¦𝙺𝙸𝙽𝙶 :{m.first_name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{m.username}\n🎃 ¦𝙸𝙳 :{m.id}\n💌 ¦𝙱𝙸𝙾 :{m.bio}\n✨ ¦𝙲𝙷𝙰𝚃: {message.chat.title}\n♻️ ¦𝙸𝙳.𝙲𝙷𝙰𝚃 :{message.chat.id}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(m.first_name, url=f"https://t.me/{m.username}")],]))
    else:
        await message.reply_text("الاك محذوف يقلب")

array = []
@Client.on_message(filters.command(["@all", "تاك","all","تكك"], "") & ~filters.private)
async def nummmm(client: client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and not message.from_user.id == OWNER_ID and not message.from_user.username in caes:
     await message.reply("**♪ عذرا عزيزي هذا الامر للادمن الجروب فقط  💎 .**")
     return
    await message.reply_text("**♪ جاري بدأ المنشن ، لايقاف الامر اضغط /cancel  💎 .**")
    i = 0
    txt = ""
    zz = message.text
    if message.photo:
          photo_id = message.photo.file_id
          photo = await client.download_media(photo_id)
          zz = message.caption
    try:
     zz = zz.replace("@all","").replace("تاك","").replace("all","").replace("تكك","")
    except:
      pass
    array.append(message.chat.id)
    async for x in client.get_chat_members(message.chat.id):
       if message.chat.id not in array:
         return
       if not x.user.is_deleted:
        i += 1
        txt += f" {x.user.mention} ›"
        if i == 20:
         try:
              if not message.photo:
                    await client.send_message(message.chat.id, f"{zz}\n{txt}")
              else:
                    await client.send_photo(message.chat.id, photo=photo, caption=f"{zz}\n{txt}")
              i = 0
              txt = ""
              await asyncio.sleep(2)
         except FloodWait as e:
                    flood_time = int(e.x)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
         except Exception:
              array.remove(message.chat.id)
    array.remove(message.chat.id)


@Client.on_message(filters.command(["/cancel", "بس منشن"], "")) 
async def stop(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and not message.from_user.id == OWNER_ID and not message.from_user.username in caes:
     await message.reply("**♪ عذرا عزيزي هذا الامر للادمن الجروب فقط  💎 .**")
     return
    if message.chat.id not in array:
      await message.reply("**♪ المنشن متوقف بي الفعل  💎 .**")
      return 
    if message.chat.id in array:
     array.remove(message.chat.id)
     await message.reply("**♪ تم ايقاف المنشن عزيزي  💎 .**")
     return                    

iddof = []
@Client.on_message(filters.command(["قفل الايدي", "تعطيل الايدي"], ""), group=73) 
async def iddlock(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.username in wenru or message.from_user.username in caes:
       if message.chat.id in iddof:
         return await message.reply_text("تم معطل من قبل🔒")
       iddof.append(message.chat.id)
       return await message.reply_text("تم تعطيل الايدي بنجاح ✅🔒")
    else:
       return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر لا يخصك✨♥")

@Client.on_message(filters.command(["فتح الايدي", "تفعيل الايدي"], ""), group=703) 
async def iddopen(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.username in wenru or message.from_user.username in caes:
       if not message.chat.id in iddof:
         return await message.reply_text("الايدي مفعل من قبل ✅")
       iddof.remove(message.chat.id)
       return await message.reply_text("تم فتح الايدي بنجاح ✅🔓")
    else:
       return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر لا يخصك✨♥")
      
@Client.on_message(filters.command(["ايدي","الايدي","ا"], ""), group=713) 
async def iddd(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in iddof:
        return await message.reply_text(f"عزرا عزيزي [{message.from_user.mention}] \n الايدي معطل اطلب من الادمنيه تفعيله ✨♥")  
    if message.from_user.photo:
        usr = await client.get_chat(message.from_user.id)
        user_id = usr.id
        CASER = usr.username
        name = usr.first_name
        await message.reply_text(text=f"""╭⎋¦ᚐ𝙽𝙰𝙼𝙴 :{message.from_user.mention}\n╰⊚ᚐᴜsᴇʀᚐ :@{message.from_user.username}\n╭⎋ɪᴅᚐ:{message.from_user.id}\n╰⊚ᚐʙɪᴏᚐ:{usr.bio}\n♥ ¦𝙲𝙷𝙰𝚃: {message.chat.title}\n♻️ ¦𝙸𝙳.𝙶𝚁𝙾𝚄𝙿 :{message.chat.id}""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(name, url=f"https://t.me/{message.from_user.username}")]]))
    else:
        usr = await client.get_chat(message.from_user.id)
        user_id = usr.id
        name = usr.first_name
        await message.reply_text(text=f"""╭⎋¦ᚐ𝙽𝙰𝙼𝙴 :{message.from_user.mention}\n╰⊚ᚐᴜsᴇʀᚐ :@{message.from_user.username}\n╭⎋ɪᴅᚐ:{message.from_user.id}\n╰⊚ᚐʙɪᴏᚐ:{usr.bio}\n♥ ¦𝙲𝙷𝙰𝚃: {message.chat.title}\n♻️ ¦𝙸𝙳.𝙶𝚁𝙾𝚄𝙿 :{message.chat.id}""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(name, url=f"https://t.me/{message.from_user.username}")]]))
