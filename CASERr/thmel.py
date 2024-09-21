from pyrogram import Client, filters
from youtubesearchpython.__future__ import VideosSearch 
import os
import aiohttp
import requests
import random 
import asyncio
import yt_dlp
import time 
from datetime import datetime, timedelta
from youtube_search import YoutubeSearch
from pyrogram import Client as client
from pyrogram.errors import (ChatAdminRequired,
                             UserAlreadyParticipant,
                             UserNotParticipant)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatType, ChatMemberStatus
import asyncio
from config import *
import numpy as np
from yt_dlp import YoutubeDL
from config import user, dev, call, logger, logger_mode, botname, appp
from CASERr.daty import get_call, get_userbot, get_dev, get_logger
from pyrogram import Client
from youtubesearchpython import SearchVideos
from CASERr.CASERr import get_channel, devchannel, source, caes, devgroup, devuser, group, casery, johned
from io import BytesIO
import aiofiles
import wget

yoro = ["Xnxx", "سكس","اباحيه","جنس","اباحي","زب","كسمك","كس","شرمطه","نيك","لبوه","فشخ","مهبل","نيك خلفى","بتتناك","مساج","كس ملبن","نيك جماعى","نيك جماعي","نيك بنات","رقص","قلع","خلع ملابس","بنات من غير هدوم","بنات ملط","نيك طيز","نيك من ورا","نيك في الكس","ارهاب","موت","حرب","سياسه","سياسي","سكسي","قحبه","شواز","ممويز","نياكه","xnxx","sex","xxx","Sex","Born","borno","Sesso"]
    
@Client.on_message(filters.command(["تحميل", "نزل", "يوتيوب","حمل"], "") & filters.group, group=71328934)
async def gigshkdnnj(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    keybord = InlineKeyboardMarkup([[InlineKeyboardButton("تحميل صوت ⚡", callback_data=f"hidhkdhj"),InlineKeyboardButton("تحميل فديو ⚡", callback_data=f"voic54e1")], [InlineKeyboardButton(text="𝗔𝗱𝗗 𝗕𝗼𝗧 𝗧𝗼 𝗬𝗼𝗨𝗿 𝗚𝗿𝗢𝘂𝗣 ⤶", url=f"https://t.me/{bot_username}?startgroup=True")]])
    chat_idd = message.chat.id
    await message.reply_text(f"اختر الان بالاسفل ماذا تريد تحميله ✨♥", reply_markup=keybord)
    
@Client.on_message(filters.command(["تحميل", "نزل", "يوتيوب","حمل"], "") & filters.private, group=71328934)
async def gigshgxvkdnnj(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    keybord = InlineKeyboardMarkup([[InlineKeyboardButton("تحميل صوت ⚡", callback_data=f"hidhkdhj"),InlineKeyboardButton("تحميل فديو ⚡", callback_data=f"voic54e1")], [InlineKeyboardButton(text="𝗔𝗱𝗗 𝗕𝗼𝗧 𝗧𝗼 𝗬𝗼𝗨𝗿 𝗚𝗿𝗢𝘂𝗣 ⤶", url=f"https://t.me/{bot_username}?startgroup=True")]])
    chat_idd = message.chat.id
    await message.reply_text(f"اختر الان بالاسفل ماذا تريد تحميله ✨♥", reply_markup=keybord)
    
@Client.on_callback_query(filters.regex("voic54e1"))
async def h24dgfgbie(client: Client, CallbackQuery):
    bot_username = client.me.username
    name = await client.ask(CallbackQuery.message.chat.id, text="**ارسل الان ما تريد تحميله ✨♥**", filters=filters.user(CallbackQuery.from_user.id), timeout=200)
    text = name.text
    if text in yoro:
      return await CallbackQuery.message.reply_text("**لا يمكن تنزيل هذا**")  
    else:      
     print("احم")    
    h = await CallbackQuery.message.reply_text(f"جاري البحث عن {text}")
    search = SearchVideos(text, offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    url = mo
    sedlyf = wget.download(kekme)
    opts = {"format": "best", "keepvideo": True, "prefer_ffmpeg": False, "geo_bypass": True, "outtmpl": "%(title)s.%(ext)s", "quite": True}
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)
            video_file = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        print(f"   : {e}")
        return
    c_time = time.time()
    capy = f"[{thum}]({mo})"
    await h.delete()
    try:
        await client.send_video(CallbackQuery.message.chat.id,video=video_file,duration=int(ytdl_data["duration"]),file_name=str(ytdl_data["title"]),thumb=sedlyf, supports_streaming=True,caption=capy)
        os.remove(video_file)
        os.remove(sedlyf)
    except Exception as e:
        print(f" \n{e}")

@Client.on_callback_query(filters.regex("hidhkdhj"))
async def h24dg54hfbie(client: Client, CallbackQuery):
    bot_username = client.me.username
    name = await client.ask(CallbackQuery.message.chat.id, text="**ارسل الان ما تريد تحميله ✨♥**", filters=filters.user(CallbackQuery.from_user.id), timeout=200)
    text = name.text
    if text in yoro:
      return await CallbackQuery.message.reply_text("**لا يمكن تنزيل هذا**")  
    else:      
     print("احم")    
    h = await CallbackQuery.message.reply_text(f"جاري البحث عن {text}")
    search = SearchVideos(text, offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    mio[0]["duration"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    sedlyf = wget.download(kekme)
    opts = {'format': 'bestaudio[ext=m4a]', 'keepvideo': False, 'prefer_ffmpeg': False, 'geo_bypass': True, 'outtmpl': '%(title)s.%(ext)s', 'quite': True}
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(mo, download=True)
            audio_file = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        print(f"   : {e}")
        return
    c_time = time.time()
    capy = f"[{thum}]({mo})"
    file_stark = f"{ytdl_data['id']}.mp3"
    await h.delete()
    try:
        await client.send_audio(CallbackQuery.message.chat.id, audio=audio_file, duration=int(ytdl_data["duration"]), title=str(ytdl_data["title"]), performer=str(ytdl_data["uploader"]), file_name=str(ytdl_data["title"]), thumb=sedlyf,caption=capy)
        os.remove(audio_file)
        os.remove(sedlyf)
    except Exception as e:
        print(f" \n{e}")