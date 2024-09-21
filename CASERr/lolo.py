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
import json
import redis, re
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps
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
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError,AlreadyJoinedError)
from pyrogram.enums import ChatType
from pyrogram.types import Chat, User
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from asyncio import gather
from io import BytesIO
from pyrogram import Client, filters
from config import *
from config import user, dev, call, logger, logger_mode, botname, appp
from CASERr.daty import get_call, get_userbot, get_dev, get_logger
from CASERr.CASERr import get_channel, devchannel, source, caes, johned
from casery import ch as chh
import logging
import re

logging.basicConfig(level=logging.INFO)

@Client.on_message(filters.text)
async def extract_code(client, message):
    logging.info(f"Received message: {message.text}")
    match = re.search(r'my Code:\s*([A-Z0-9]+)', message.text)
    if match:
        code = match.group(1)
        logging.info(f"Extracted code: {code}")
        await message.reply_text(f"{code}") 
    else:
        logging.info("No code found in the message.") 
        
src = []

@Client.on_message(filters.command(["قفل التسليه", "تعطيل التسليه"], ""), group=73) 
async def fffcaesar(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
       if message.chat.id in src:
         return await message.reply_text("تم معطل من قبل🔒")
       src.append(message.chat.id)
       return await message.reply_text("تم تعطيل التسليه بنجاح ✅🔒")
    else:
       return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر لا يخصك✨♥")

@Client.on_message(filters.command(["فتح التسليه", "تفعيل التسليه"], ""), group=703) 
async def caesarrf(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
       if not message.chat.id in src:
         return await message.reply_text("االتسليه مفعل من قبل ✅")
       src.remove(message.chat.id)
       return await message.reply_text("تم فتح التسليه بنجاح ✅🔓")
    else:
       return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر لا يخصك✨♥")

@Client.on_message(filters.command(["قتل","تخ"], ""), group=1024)
async def ceev(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.username in caes:
        await message.reply_text("• عذرآ لا تستطيع استخدام الأمر على مطور السورس")
    else:
        caesar = await client.get_chat(message.from_user.id)
        CASER = caesar.username
        usr = await client.get_users(message.reply_to_message.from_user.id)
        name = usr.username
        user_id = message.reply_to_message.from_user.id
        chat_id = message.chat.id
        await message.reply_video(
          video="https://telegra.ph/file/a2c9fa6de45e0fc4fc81e.mp4",
          caption=f"• تم قتل هذا الشخص @{name}\n\n※ بواسطة @{CASER}\n\n ان لله وان اليه راجعون ⚰😭",
          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("المقتول ⚰??", url=f"https://t.me/{name}"), 
                                ],[InlineKeyboardButton("القاتل 👿🔪", url=f"https://t.me/{CASER}"), 
                                ],[InlineKeyboardButton("ضيفني في جروب والنبي🥺♥", url=f"https://t.me/{bot_username}?startgroup=tru")]]))
                                
@Client.on_message(filters.command(["بوسه","مح"], ""), group=1025554)
async def cee6v(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.username in caes:
        await message.reply_text("• عذرآ لا تستطيع استخدام الأمر على مطور السورس")
    else:
        caesar = await client.get_chat(message.from_user.id)
        CASER = caesar.username
        usr = await client.get_users(message.reply_to_message.from_user.id)
        name = usr.username
        user_id = message.reply_to_message.from_user.id
        chat_id = message.chat.id
        await message.reply_video(
          video="https://telegra.ph/file/f9fca108067895e042f1f.mp4",
          caption=f"••القميل هذا ✨♥ @{CASER}\n\n※ بعتلك بوسه يا 😘♥ @{name} \n\n عيب كده اي المحن ده 😹",
          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("المقبول 👻??", url=f"https://t.me/{name}"), 
                                ],[InlineKeyboardButton("القابل 😘🥹", url=f"https://t.me/{CASER}"), 
                                ],[InlineKeyboardButton("ضيفني في جروب والنبي🥺♥", url=f"https://t.me/{bot_username}?startgroup=tru")]]))         


@Client.on_message(filters.command(["تفو","تف"], ""), group=105524)
async def ceev55(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.username in caes:
        await message.reply_text("• عذرآ لا تستطيع استخدام الأمر على مطور السورس")
    else:
        caesar = await client.get_chat(message.from_user.id)
        CASER = caesar.username
        usr = await client.get_users(message.reply_to_message.from_user.id)
        name = usr.username
        user_id = message.reply_to_message.from_user.id
        chat_id = message.chat.id
        await message.reply_video(
          video="https://telegra.ph/file/7f4c6eebf2f23b41dea45.mp4",
          caption=f"• تم التف علي هذا الشخص @{name}\n\n※ بواسطة @{CASER} \n\n اععع اي القرف ده 🤢",
          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("المتفوف عليه😂💔", url=f"https://t.me/{name}"), 
                                ],[InlineKeyboardButton("التافف 😂👻", url=f"https://t.me/{CASER}"), 
                                ],[InlineKeyboardButton("ضيفني في جروب والنبي🥺♥", url=f"https://t.me/{bot_username}?startgroup=tru")]]))              


@Client.on_message(filters.command(["غنيلي", "غني", "❤️‍🔥غنيلي", "غنيي"], ""), group=73)
async def ih25d(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in src:
        return
    rl = random.randint(2, 90)
    url = f"https://t.me/gukygn/{rl}"
    await client.send_voice(message.chat.id, url, caption=f"╭───── : ◖⋮◗ : ─────╮\n𝗖𝗵: @{chh}\n╰───── : ◖⋮◗ : ─────╯", parse_mode=enums.ParseMode.HTML, reply_to_message_id=message.id)

@Client.on_message(filters.command(["صوره", "❤️‍🔥صوره", "صورهه", "صور"], ""), group=713)
async def ihd21(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in src:
        return
    rl = random.randint(2, 100)
    url = f"https://t.me/Caser_Rady_3/{rl}"
    await client.send_photo(message.chat.id, url, caption=f"╭───── : ◖⋮◗ : ─────╮\n𝗖𝗵: @{chh}\n╰───── : ◖⋮◗ : ─────╯", parse_mode=enums.ParseMode.HTML, reply_to_message_id=message.id)

@Client.on_message(filters.command(["❤️‍🔥انمي", "انمي"], ""), group=723)
async def i15hd(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in src:
        return
    rl = random.randint(2, 90)
    url = f"https://t.me/LoreBots7/{rl}"
    await client.send_photo(message.chat.id, url, caption=f"╭───── : ◖⋮◗ : ─────╮\n𝗖𝗵: @{chh}\n╰───── : ◖⋮◗ : ─────╯", parse_mode=enums.ParseMode.HTML, reply_to_message_id=message.id)

@Client.on_message(filters.command(["❤️‍🔥متحركه", "متحركه"], ""), group=733)
async def ih48d(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in src:
        return
    rl = random.randint(2, 90)
    url = f"https://t.me/GifWaTaN/{rl}"
    await client.send_animation(message.chat.id, url, caption=f"╭───── : ◖⋮◗ : ─────╮\n𝗖𝗵: @{chh}\n╰───── : ◖⋮◗ : ─────╯", parse_mode=enums.ParseMode.HTML, reply_to_message_id=message.id)

@Client.on_message(filters.command(["❤️‍🔥اقتباسات", "اقتباس"], ""), group=753)
async def ih289d(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in src:
        return
    rl = random.randint(2, 90)
    url = f"https://t.me/LoreBots9/{rl}"
    await client.send_photo(message.chat.id, url, caption=f"╭───── : ◖⋮◗ : ─────╮\n𝗖𝗵: @{chh}\n╰───── : ◖⋮◗ : ─────╯", parse_mode=enums.ParseMode.HTML, reply_to_message_id=message.id)

@Client.on_message(filters.command(["هيدرا", "❤️‍🔥هيدرات"], ""), group=743)
async def ih67d(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in src:
        return
    rl = random.randint(2, 90)
    url = f"https://t.me/flflfldld/{rl}"
    await client.send_photo(message.chat.id, url, caption=f"╭───── : ◖⋮◗ : ─────╮\n𝗖𝗵: @{chh}\n╰───── : ◖⋮◗ : ─────╯", parse_mode=enums.ParseMode.HTML, reply_to_message_id=message.id)

@Client.on_message(filters.command(["❤️‍🔥صور بنات", "صور بنات"], ""), group=763)
async def ih467d(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in src:
        return
    rl = random.randint(2, 70)
    url = f"https://t.me/Caser_Rady_1/{rl}"
    await client.send_photo(message.chat.id, url, caption=f"╭───── : ◖⋮◗ : ─────╮\n𝗖𝗵: @{chh}\n╰───── : ◖⋮◗ : ─────╯", parse_mode=enums.ParseMode.HTML, reply_to_message_id=message.id)

@Client.on_message(filters.command(["صور شباب", "❤️‍🔥صور شباب"], ""), group=773)
async def i378hd(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in src:
        return
    rl = random.randint(2, 70)
    url = f"https://t.me/Caser_Rady_2/{rl}"
    await client.send_photo(message.chat.id, url, caption=f"╭───── : ◖⋮◗ : ─────╮\n𝗖𝗵: @{chh}\n╰───── : ◖⋮◗ : ─────╯", parse_mode=enums.ParseMode.HTML, reply_to_message_id=message.id)

@Client.on_message(filters.command(["❤️‍🔥قران", "قران"], ""), group=783)
async def ihd97(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in src:
        return
    rl = random.randint(1, 90)
    url = f"https://t.me/opuml/{rl}"
    await client.send_voice(message.chat.id, url, caption=f"╭───── : ◖⋮◗ : ─────╮\n𝗖𝗵: @{chh}\n╰───── : ◖⋮◗ : ─────╯", parse_mode=enums.ParseMode.HTML, reply_to_message_id=message.id)

@Client.on_message(filters.command(["❤️‍🔥الشيخ نقشبندي", "النقشبندي", "نقشبندي"], ""), group=793) 
async def ih907d(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in src:
        return
    rl = random.randint(1, 90)
    url = f"https://t.me/ggcnjj/{rl}"
    await client.send_voice(message.chat.id, url, caption=f"╭───── : ◖⋮◗ : ─────╮\n𝗖𝗵: @{chh}\n╰───── : ◖⋮◗ : ─────╯", parse_mode=enums.ParseMode.HTML, reply_to_message_id=message.id)

@Client.on_message(filters.command(["فيلم", "❤️‍🔥فيلم"], ""), group=7823) 
async def ih579d(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in src:
        return
    rl = random.randint(2, 34)
    url = f"https://t.me/gyigkk/{rl}"
    await client.send_audio(message.chat.id, url, caption=f"╭───── : ◖⋮◗ : ─────╮\n𝗖𝗵: @{chh}\n╰───── : ◖⋮◗ : ─────╯", parse_mode=enums.ParseMode.HTML, reply_to_message_id=message.id)

@Client.on_message(filters.command(["استوري", "❤️‍🔥استوريهات"], ""), group=7553) 
async def i803hd(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in src:
        return
    rl = random.randint(1, 50)
    url = f"https://t.me/yoipopl/{rl}"
    await client.send_audio(message.chat.id, url, caption=f"╭───── : ◖⋮◗ : ─────╮\n𝗖𝗵: @{chh}\n╰───── : ◖⋮◗ : ─────╯", parse_mode=enums.ParseMode.HTML, reply_to_message_id=message.id)

@Client.on_message(filters.command(["كت","تويت","❤️‍🔥كت","تويت"], ""), group=764653) 
async def cu24tt(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return    
    rl = random.randint(2, 400)
    url = f"https://t.me/Caser_Rady/{rl}"
    name = url.replace("https://t.me/", "")
    path_parts = name.split("/")
    group_id = path_parts[0]
    message_id = int(path_parts[1])    
    await client.copy_message(message.chat.id, group_id, message_id, reply_to_message_id=message.id)

@Client.on_message(filters.command(["مثل" ,"امثله"], ""), group=70973)
async def cae57sar(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    rl = random.randint(2, 168)
    url = f"https://t.me/Caser_Rady_5/{rl}"
    name = url.replace("https://t.me/", "")
    path_parts = name.split("/")
    group_id = path_parts[0]
    message_id = int(path_parts[1])    
    await client.copy_message(message.chat.id, group_id, message_id, reply_to_message_id=message.id)

@Client.on_message(filters.command(["خيروك","خيرني","❤️‍🔥خيرني", "لو خيروك"], ""), group=764643)
async def khyro(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    rl = random.randint(2, 230)
    url = f"https://t.me/Caser_Rady_4/{rl}"
    name = url.replace("https://t.me/", "")
    path_parts = name.split("/")
    group_id = path_parts[0]
    message_id = int(path_parts[1])    
    await client.copy_message(message.chat.id, group_id, message_id, reply_to_message_id=message.id)
    
txt = [

"عامل الناس بأخلاقك ولا بأخلاقهم", 
"الجمال يلفت الأنظار لكن الطيبه تلفت القلوب ", 
"الاعتذار عن الأخطاء لا يجرح كرامتك بل يجعلك كبير في نظر الناس ",
"لا ترجي السماحه من بخيل.. فما في البار لظمان ماء",
"لا تحقرون صغيره إن الجبال من الحصي",
"لا تستحي من إعطاء فإن الحرمان أقل منه ", 
"لا تظلم حتى لا تتظلم ",
"لا تقف قصاد الريح ولا تمشي معها ",
"لا تكسب موده التحكم الا بالتعقل",
"لا تمد عينك في يد غيرك ",
"لا تملح الا لمن يستحقاها ويحافظ عليها",
"لا حياه للإنسان بلا نبات",
"لا حياه في الرزق.. ولا شفاعه في الموت",
"كما تدين تدان",
"لا دين لمن لا عهد له ",
"لا سلطان على الدوق فيما يحب أو بكره",
"لا مروه لمن لادين له ",
"لا يدخل الجنه من لايأمن من جازه بوائقه",
"يسروا ولا تعسروا... ويشورا ولا تنفروا",
"يدهم الصدر ما يبني العقل الواسع ",
"أثقل ما يوضع في الميزان يوم القيامة حسن الخلق ",
"أجهل الناس من ترك يقين ما عنده لظن ما عند الناس ",
"أحياناً.. ويصبح الوهم حقيقه ",
"مينفعش تعاتب حد مبيعملش حساب لزعلك عشان متزعلش مرتين . ",
"السفر ومشاهده اماكن مختلفه وجديده ",
"عدم تضيع الفرص واسثمارها لحظه مجبئها ",
" اعطاء الاخرين اكثر من ما يتوقعون",
"معامله الناس بلطف ولكن عدم السماح لاحد بستغالال ذالك ",
"تكوين صدقات جديده مع الحفظ بلاصدقاء القودامي ",
"تعلم اصول المهنه بدلا من تضيع الوقت ف تعلم حيل المهنه ",
"مدح ع الاقل ثلاث اشخاص يوميا ",
"النظر ف عيون الشخاص عند مخاطبتهم ",
"التحلي بلسماح مع الاخرين او النفس ",
"الاكثار من قول كلمه شكرا ",
" مصافحه الاخرين بثبات وقوة ",
"الابتعاد عن المناطق السيئه السمعه لتجنب الاحداث السئه ",
" ادخار 10٪ع الاقل من الدخل",
" تجنب المخاوف من خلال التعلم من تجارب مختلفه",
" الحفاظ ع السمعه لانها اغلي ما يملك الانسان",
" تحويل الاعداء الي اصدقاء من خلال القيام بعمل جيد",
"لا تصدق كل ما تسمعع. ولا تنفق كل ما تمتلك . ولا تنم قدر ما ترغب ",
" اعتني بسمعتك جيدا فستثبت للك الايام انها اغلي ما تملك",
"حين تقول والدتك ستندم ع فعل ذالك ستندم عليه غالبا.. ",
" لا تخش العقبات الكبيره فخلفها تقع الفرص العظيمه",
"قد لا يتطلب الامر اكثر من شخص واحد لقلب حياتك رأس ع عقب ",
"اختر رفيقه حياتك بحرص فهو قرار سيشكل 90٪من سعادتك او بؤسك ",
" اقلب اداءك الاصدقاء بفعل شي جميل ومفجائ لهم",
"حين تدق الفرصه ع باباك ادعوها للبيت ",
"تعلم القواعد جيدا ثن اكسر بعدها ",
"احكم ع نجاحك من خلال قدرتك ع العطاء وليس الاخذ ",
" لا تتجاهل الشيطان مهما بدل ثيابه",
"ركز ع جعل الاشياء افضل وليس اكبر او اعظم ",
"كن سعيد  بما تمتلك واعمل لامتلاك ما تريد ",
"اعط الناس اكثر من ما يتوقعون ",
" لا تكن منشغل لدرجه عدم التعرف ع اصدقاء جدد",
"استحمه يوم العيد يمعفن🐰",
"مش تحب اي حد يقرب منك ",
" خليك مع البت راجل خليك تقيل",
" انصح نفسك بنفسك بمت😂",
" كنت نصحت نفسي ياخويا🗿", 

        ]
      
@Client.on_message(filters.command(["انصحني","❤️‍🔥انصحني"], ""), group=6761)
async def anshny(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    a = random.choice(txt)
    await message.reply(f"{a}")
        
tt = [
" مدينة بحرف ⇦ ع  ",
" حيوان ونبات بحرف ⇦ خ  ", 
" اسم بحرف ⇦ ح  ", 
" اسم ونبات بحرف ⇦ م  ", 
" دولة عربية بحرف ⇦ ق  ", 
" جماد بحرف ⇦ ي  ", 
" نبات بحرف ⇦ ج  ", 
" اسم بنت بحرف ⇦ ع  ", 
" اسم ولد بحرف ⇦ ع  ", 
" اسم بنت وولد بحرف ⇦ ث  ", 
" جماد بحرف ⇦ ج  ",
" حيوان بحرف ⇦ ص  ",
" دولة بحرف ⇦ س  ",
" نبات بحرف ⇦ ج  ",
" مدينة بحرف ⇦ ب  ",
" نبات بحرف ⇦ ر  ",
" اسم بحرف ⇦ ك  ",
" حيوان بحرف ⇦ ظ  ",
" جماد بحرف ⇦ ذ  ",
" مدينة بحرف ⇦ و  ",
" اسم بحرف ⇦ م  ",
" اسم بنت بحرف ⇦ خ  ",
" اسم و نبات بحرف ⇦ ر  ",
" نبات بحرف ⇦ و  ",
" حيوان بحرف ⇦ س  ",
" مدينة بحرف ⇦ ك  ",
" اسم بنت بحرف ⇦ ص  ",
" اسم ولد بحرف ⇦ ق  ",
" نبات بحرف ⇦ ز  ",
"  جماد بحرف ⇦ ز  ",
"  مدينة بحرف ⇦ ط  ",
"  جماد بحرف ⇦ ن  ",
"  مدينة بحرف ⇦ ف  ",
"  حيوان بحرف ⇦ ض  ",
"  اسم بحرف ⇦ ك  ",
"  نبات و حيوان و مدينة بحرف ⇦ س  ", 
"  اسم بنت بحرف ⇦ ج  ", 
"  مدينة بحرف ⇦ ت  ", 
"  جماد بحرف ⇦ ه  ", 
"  اسم بنت بحرف ⇦ ر  ", 
" اسم ولد بحرف ⇦ خ  ", 
" جماد بحرف ⇦ ع  ",
" حيوان بحرف ⇦ ح  ",
" نبات بحرف ⇦ ف  ",
" اسم بنت بحرف ⇦ غ  ",
" اسم ولد بحرف ⇦ و  ",
" نبات بحرف ⇦ ل  ",
"مدينة بحرف ⇦ ع  ",
"دولة واسم بحرف ⇦ ب  ",
        ]
@Client.on_message(filters.command(["حروف","❤️‍🔥حروف"], ""), group=157) 
async def ahrof(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    a = random.choice(tt)
    await message.reply(f"{a}")

xt = ["لا إِلَهَ إِلا أَنتَ سُبْحَانَكَ إِنِّي كُنتُ مِنَ الظَّالِمِينَ🌸",
                     "اللَّهُمَّ أَعِنِّي عَلَى ذِكْرِكَ , وَشُكْرِكَ , وَحُسْنِ عِبَادَتِكَ🎈💞",
                     "استغفر الله العظيم وأتوبُ إليه 🌹",
                     "حَسْبِيَ اللَّهُ لا إِلَـهَ إِلاَّ هُوَ عَلَيْهِ تَوَكَّلْتُ وَهُوَ رَبُّ الْعَرْشِ الْعَظِيم"
                     "ِ سبع مرات، كفاه الله تعالى ما أهمه من أمور الدنيا والآخرة🌹🌸",
                     "ربنا اغفر لنا ذنوبنا وإسرافنا فِي أمرنا وثبت أقدامنا وانصرنا على القوم الكافرين🌸",
                     "أشهد أنْ لا إله إلا الله وحده لا شريك له، وأشهد أن محمدًا عبده ورسوله🌺",
                     "سبحان الله وبحمده سبحان الله العظيم🌸",
                     "أشهد أنْ لا إله إلا الله وحده لا شريك له، وأشهد أن محمدًا عبده ورسوله🌺",
                     "اللهم إنك عفو تُحب العفو فاعفُ عنّا 🌿🌹",
                     "استغفر الله العظيم وأتوبُ إليه 🌹",
                     "لا تقطع صلاتك، إن كنت قادراً على الصلاة في الوقت فصلِي و أكثر من الدعاء لتحقيق ما تتمنى💙",
                     "قال ﷺ : ”حَيْثُمَا كُنْتُمْ فَصَلُّوا عَلَيَّ، فَإِنَّ صَلَاتَكُمْ تَبْلُغُنِي“.",
                     "يا رب أفرحني بشيئاً انتظر حدوثه،اللهم إني متفائلاً بعطائك فاكتب لي ما أتمنى🌸",
                     "﴿ رَبِّ اشْرَحْ لِي صَدْرِي وَيَسِّرْ لِي أَمْرِي ﴾",
                     "‏{ تَوَفَّنِي مُسْلِمًا وَأَلْحِقْنِي بِالصَّالِحِينَ }",
                     "‏اللهّم لطفك بقلوبنا وأحوالنا وأيامنا ،‏اللهّم تولنا بسعتك وعظيم فضلك ",
                     "ومن أحسن قولاً ممن دعا إلى الله وعمل صالحاً وقال أنني من المسلمين .💕",
                     "‏إن الله لا يبتليك بشيء إلا وبه خيرٌ لك فقل الحمدلله.",
                     "رَبِّ أَوْزِعْنِي أَنْ أَشْكُرَ نِعْمَتَكَ",
                     "اللهم اشفي كل مريض يتألم ولا يعلم بحاله إلا أنت",
                     "استغفر الله العظيم وأتوبُ إليه.",
                     "‏لَم تعرف الدنيا عظيماً مِثله صلّوا عليه وسلموا تسليم",
                     " أنتَ اللّطيف وأنا عبدُك الضّعيف اغفرلي وارحمني وتجاوز عنّي.",
                     "ماتستغفر ربنا كده🥺❤️",
                     "فاضي شويه نصلي ع النبي ونحز خته فى الجنه❤️❤️",
                     "ماتوحدو ربنا يجماعه قولو لا اله الا الله❤️❤️",
                     "يلا كل واحد يقول سبحان الله وبحمده سبحان الله العظيم 3 مرات🙄❤️",
                     "قول لاحول ولا قوه الا بالله يمكن تفك كربتك🥺❤️",
                     "اللهم صلي عللى سيدنا محمد ماتصلي على النبي كده",
                     "- أسهل الطرق لإرضاء ربك، أرضي والديك 🥺💕",
                     "- اللهُم صبراً ، اللهم جبراً ، اللهم قوّة",
                     "أصبحنا وأصبح الملك لله ولا اله الا الله.",
                     "‏إنَّ اللهَ يُحِبُ المُلحِينَ فِي الدُّعَاء.",
                     "‏إن الله لا يخذل يداً رُفعت إليه أبداً.",
                     "يارب دُعاء القلب انت تسمعه فأستجب لهُ.",
                     "- اللهم القبول الذي لا يزول ❤️🍀.",
                     "- اللهُم خذ بقلبّي حيث نورك الذي لا ينطفِئ.",
                     "سبحان الله وبحمده ،سبحان الله العظيم.",
                     "لا تعودوا أنفسكم على الصمت، اذكرو الله، استغفروه، سبّحوه، احمدوه،"
                     " عودوا السنتكم على الذكر فإنها إن اعتادت لن تصمت أبدًا.",
                     "- اللهم بلغنا رمضان وأجعلنا نختم القرآن واهدنا لبر الامان يالله يا رحمان 🌙",
                     "بسم الله الذي لا يضر مع اسمه شيء في الأرض ولا في السماء وهو السميع العلي- ثلاث مرات -",
                     "- اللهم احرمني لذة معصيتك وارزقني لذة طاعتك 🌿💜.",
                     "- اللهُم إن في صوتي دُعاء وفي قلبِي أمنية اللهُم يسر لي الخير حيث كان.",
                     "‏اللهم أرني عجائب قدرتك في تيسير أموري 💜.",
                     "يغفر لمن يشاء إجعلني ممن تشاء يا الله.*",
                     "‏يارب إن قصّرنا في عبادتك فاغفرلنا، وإن سهينا عنك بمفاتن الدنيا فردنا إليك رداً جميلاً 💜🍀",
                     "صلوا على من قال في خطبة الوداع  ‏و إني مُباهٍ بكم الأمم يوم القيامة♥️⛅️",
                     "اللهـم إجعلنا ممن تشهد أصابعهم بذكـر الشهادة قبل الموت ??💜.",
                     "- وبك أصبحنا يا عظيم الشأن ??❤️.",
                     "اللهُم الجنة ونعيَّم الجنة مع من نحب💫❤️🌹",
                     "‏اللهم قلبًا سليمًا عفيفًا تقيًا نقيًا يخشاك سرًا وعلانية🤍🌱",
                     "- أسجِد لربِك وأحضِن الارض فِي ذِ  لاضَاق صَدرِك مِن هَموم المعَاصِي 🌿.",
                     "صلي على النبي بنيه الفرج❤️",
                     "استغفر ربنا كده 3 مرات هتاخد ثواب كبير اوى❤️",
                     "اشهد ان لا اله الا الله وان محمدا عبده ورسوله",
                     "لا اله الا الله سيدنا محمد رسول الله🌿💜",
                     "قول معايا - استغفر الله استفر الله استغفر الله -",
                     "مُجرد ثانية تنفعِك : أستغفُرالله العظيِم وأتوب إليّه.",
                     "أدعُ دُعاء الواثِق فالله لايُجرّبُ معه‌‏",
                     "صلي على محمد❤️",
                     "ماتيجو نقرء الفاتحه سوا🥺"]

@Client.on_message(filters.command(["ازكار","الازكار","❤️‍🔥ازكار"], ""), group=6971) 
async def azkar(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    a = random.choice(xt)
    await message.reply(f"{a}")
        
txkt = [

"‏من علامات جمال المرأة .. بختها المايل ! ",
"‏ انك الجميع و كل من احتل قلبي🫀🤍",
"‏ ‏ لقد تْعَمقتُ بكَ كَثيراً والمِيمُ لام .♥️",
"‏ ‏ممكن اكون اختارت غلط بس والله حبيت بجد🖇️",
"‏ علينا إحياء زَمن الرّسائل الورقيّة وسط هذه الفوضى الالكترونية العَارمة. ℘︙ 💜",
"‏ يجي اي الصاروخ الصيني ده جمب الصاروخ المصري لما بيلبس العبايه السوده.🤩♥️",
"‏ كُنت أرقّ من أن أتحمّل كُل تلك القَسوة من عَينيك .🍍",
"‏أَكَان عَلَيَّ أَنْ أغْرَس انيابي فِي قَلْبِك لتشعر بِي ؟.",
"‏ : كُلما أتبع قلبي يدلني إليك .",
"‏ : أيا ليت من تَهواه العينُ تلقاهُ .",
"‏ ‏: رغبتي في مُعانقتك عميقة جداً .??",
"ويُرهقني أنّي مليء بما لا أستطيع قوله.✨",
"‏ من مراتب التعاسه إطالة الندم ع شيء إنتهى. ℘︙ ",
"‏ ‏كل العالم يهون بس الدنيا بينا تصفي 💙",
"‏ بعض الاِعتذارات يجب أن تُرفَضّ.",
"‏ ‏تبدأ حياتك محاولاً فهم كل شيء، وتنهيها محاولاً النجاة من كل ما فهمت.",
"‏ إن الأمر ينتهي بِنا إلى أعتياد أي شيء.",
"‏ هل كانت كل الطرق تؤدي إليكِ، أم أنني كنتُ أجعلها كذلك.",
"‏ ‏هَتفضل تواسيهُم واحد ورا التاني لكن أنتَ هتتنسي ومحدِش هَيواسيك.",
"‏ جَبَرَ الله قلوبِكُم ، وقَلبِي .🍫",
"‏ بس لما أنا ببقى فايق، ببقى أبكم له ودان.💖",
"‏ ‏مقدرش عالنسيان ولو طال الزمن 🖤",
"‏ أنا لستُ لأحد ولا احد لي ، أنا إنسان غريب أساعد من يحتاجني واختفي.",
"‏ ‏أحببتك وأنا منطفئ، فما بالك وأنا في كامل توهجي ؟",
"‏ لا تعودني على دفء شمسك، إذا كان في نيتك الغروب .َ",
"‏ وانتهت صداقة الخمس سنوات بموقف.",
"‏ ‏لا تحب أحداً لِدرجة أن تتقبّل أذاه.",
"‏ إنعدام الرّغبة أمام الشّيء الّذي أدمنته ، انتصار.",
"‏مش جايز , ده اكيد التأخير وارهاق القلب ده وراه عوضاً عظيماً !?? ",
" مش جايز , ده اكيد التأخير وارهاق القلب ده وراه عوضاً عظيماً !💙",
"فـ بالله صبر  وبالله يسر وبالله عون وبالله كل شيئ ♥️. ",
"أنا بعتز بنفسي جداً كصاحب وشايف اللي بيخسرني ، بيخسر أنضف وأجدع شخص ممكن يشوفه . ",
"فجأه جاتلى قافله ‏خلتنى مستعد أخسر أي حد من غير ما أندم عليه . ",
"‏اللهُم قوني بك حين يقِل صبري... ",
"‏يارب سهِل لنا كُل حاجة شايلين هَمها 💙‏ ",
"انا محتاج ايام حلوه بقي عشان مش نافع كدا ! ",
"المشكله مش اني باخد قررات غلط المشكله اني بفكر كويس فيها قبل ما اخدها .. ",
"تخيل وانت قاعد مخنوق كدا بتفكر فالمزاكره اللي مزكرتهاش تلاقي قرار الغاء الدراسه .. ",
" مكانوش يستحقوا المعافرة بأمانه.",
"‏جمل فترة في حياتي، كانت مع اكثر الناس الذين أذتني نفسيًا. ",
" ‏إحنا ليه مبنتحبش يعني فينا اي وحش!",
"أيام مُمله ومستقبل مجهول ونومٌ غير منتظموالأيامُ تمرُ ولا شيَ يتغير ", 
"عندما تهب ريح المصلحه سوف ياتي الجميع رتكدون تحت قدمك ❤️. ",
"عادي مهما تعادي اختك قد الدنيا ف عادي ❤. ",
"بقيت لوحدي بمعنا اي انا اصلا من زمان لوحدي.❤️ ",
"- ‏تجري حياتنا بما لاتشتهي أحلامنا ! ",
"تحملين كل هذا الجمال، ‏ألا تتعبين؟",
"البدايات للكل ، والثبات للصادقين ",
"مُؤخرًا اقتنعت بالجملة دي جدا : Private life always wins. ",
" الافراط في التسامح بيخللي الناس تستهين بيك🍍",
"مهما كنت كويس فـَ إنت معرض لـِ الاستبدال.. ",
"فخوره بنفسي جدًا رغم اني معملتش حاجه فـ حياتي تستحق الذكر والله . ",
"‏إسمها ليلة القدر لأنها تُغير الأقدار ,اللهُمَّ غير قدري لحالٍ تُحبه وعوضني خير .. ",
"فى احتمال كبير انها ليلة القدر ادعوا لنفسكم كتير وأدعو ربنا يشفى كل مريض. 💙 ",
"أنِر ظُلمتي، وامحُ خطيئتي، واقبل توبتي وأعتِق رقبتي يا اللّٰه. إنكَ عفوٌّ تُحِبُّ العفوَ؛ فاعفُ عني 💛 "
        ]
        
@Client.on_message(filters.command(["كتبات","حكمه","❤️‍🔥حكمه"], ""), group=73973) 
async def ktbat(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    a = random.choice(txkt)
    await message.reply(f"{a}")
        
thdhbxt = [
            "هل تخربني اسم والدتك ما هو.",
            "ليك اسم شهره بتحبو ؟",
            "ممكن تعمل اي في حياتك",                        
            "انت راضي عن حياتك",            
            "اسم حببتك الاوله ايه",           
            "ما هو هدفك في الحياه",
            "كم مجموعك الدراسي",                      
            "ما هو الاكل المفضل لك",            
            "هل تحب سماع القران الكريم",           
            "هل تامن بالحب",
            "ماهو اخطر سر اليك",                    
            "هل تامن بالارتباط السوشيال",                       
            "متي ستتزوج",                        
            "هل تحب الفتيات ام الصبيان",                        
            "ماهو قولك عندما تره ما تحب",          
            "مانوع هاتفك الجوال",            
            "ماذا تفعل في الشتاء",                        
            "هل تحب والديك ام خوتك",                       
            "هل لك اسم شهره",                        
            "سبق و فعلت شي ندمان علي فعله",           
            "ما هو هدفك في الوقت الحالي",                        
            "ما اسم فلمك المفضل",                        
            "هل تحب الصراحه ام الكذب",                        
            "• أوصف نفسك بكلمة؟",                        
            "ممكن تقدم نصيحه لاحدهم بعنوان متغلطش غلطتي",           
            "تاريخ ميلادك ايه?",                        
            "مرتبط ولا سنجل ؟",          
            "انت بخير حاليا ؟",           
            "اسمك ايه",                        
            "منين داهيه",                        
            "عندك صحاب بنات",                        
            "عندك صحاب ولاد",                       
            "لونك المفضل",                       
            "جربت حاجه نجحت واي هي ؟",                        
            "رايك في البار",                        
            "مين اكتر حد بتحبه هنا",                      
            "هات رقمك",                        
            "بتحب المغامره",              
            "احسن حاجه حصلتلك الفتره دي",            
            "بتصلي",                        
            "كم فرد في الاسلام",                       
            "ممكن تقدم نصيحه لاحدهم بعنوان متغلطش غلطتي",                        
            "كم ركعه في صلاه العصر",                      
            "ما هيا اليلله التي خير من الف شهر",                        
            "سرقت قبل كدا",            
            "هل تحب الموسيقى",           
            "هل تحب مصر",            
            "لو الحمه غلت تاكل ايه",           
            "ايه رايك فيا كابوت موز",            
            "بتحب مين من الفنانين",                        
            "امك حلوه",                        
            "عندك كم اخ",                        
            "تقدر تنصح غيرك",                       
            "عاوز تعمل نصيبه امتي",                        
            "اي اللي مخليك فجروب الزباله دا",                      
            "لابس ايه دلوقتي",                        
            "لابسه ايه دلوقتي",                        
            "حد باسك قبل كدا",                        
            "بوست حد قبل كدا",                        
            "بتحب الفلوس",                        
            "بتحب الكشري",                        
            "نفسك تسافر فيه",                        
            "عالطلاق انت كحيااان",                        
            "بتعرف ترقص",                       
            "بتعرف تغني",                        
            "بتحب المدرسه",                        
            "ارتبط من المدرسه قبل كدا",                        
            "اكتر اتنين بتحب تخرج معاهم",                        
            "بتحب الفصح",                     
            "بتحب المناسبات",                        
            "بتحب الفول",                        
            "عاوز تخرج فين",                        
            "جربت تموت من الجوع قبل كدا",                        
            "بتحب تربي القطط",                        
            "مامتك عايشه",                        
            "ايه رايك في تليجرام",                        
            "ايه رايك في بت اللي فكول دي",                        
            "ايه رايك في اسعار في البلد",                       
            "ناوي تغير فونك امتي",                       
            "تعرف تشتم حد بتحبو",                        
            "بتحب الصعيد",                        
            "بتحب اسكندريه",                       
            "متابع ايه في مسلسلات التركي",                        
            "عندك واتساب",                        
            "ايه رايك في الشتاء",                       
            "ايه رايك في الصيف",                       
            "ايه رايك في الخريف",                       
            "كم فصل في سنه",                        
            "قاعد فين دلوقتي",                        
            "شربت حشيش قبل كدا",                       
            "بتشرب سجاير",                        
            "بتشربي سجاير",                        
            "عيط علي حاجه قبل كدا",           
            "بتنام امتي",                        
            "شغال ايه",                        
            "شغاله ايه",                        
            "بتحب شغالك",                        
            "نفسك تبقي غني",                        
            "بتعرف تخبي مشعارك",            
            "لون عيونك ايه",            
            "لون شعرك ايه",
             "حبيت كام مره 💏",             
                "اتعاكست كام مره☹️☹️",                
                "خونت كام مره 😈",                
                "موقف محرج حصلك😳",                
                "اكتر شخص حبيته وكسرك💔",                
                "شايف نفسك فين  بعد 5 سنين🤑",                
                "لو بقيت بنت ليوم اول حاجه هتعملها ايه والعكس لو بقيتي ولد ليوم اول حاجه هتعمليها ايه🤐🤐",                
                "اغرب موقف حصلك🤨",                
                "اقرب انسان لقلبك 💑",                
                "قولي اغلي 5 اشخاص في حياتك 👨‍👩‍👦‍👦",                
                "اوصف نفسك في كلمتين👼",                
                "لو ليك 3 امنيات هيبقوا ايه 🧚‍♂️🧚‍♀️",                
                "اكتر شخص بتحبه هنا مين😍",                
                "اوصف صاحب ليك في 3 كلمات😌",                
                "عاكست قبل كده وكان مين😘",                
                "اتخانت قبل كده ؟🤣",                
                "لو اتجبرت علي جواز صالونات هتوافق 👰🤵",                
                "لو هترتبط بحد في الروم هيبقي مين ??",                
                "اهلك بيدلعوك بيقولولك ايه 😁😁",               
                "صوتك حلو؟",                
                "لقيت الناس اللي بوشين؟",                
                "شيء وكنت تحقق اللسان؟",                
                "أنا شخص ضعيف عندما؟",                
                "هل ترغب في إظهار حبك ومرفق لشخص أو رؤية هذا الضعف؟",
                "هل الكذب يكون ضروري وقتا ما؟",                
                "أتشعر بالوحدة على الرغم انه يحاط بك الكثير من البشر؟",                
                "كيفية الكشف عن من يكمن عليك؟",               
                "إذا حاول شخص ما أن يكرهه أن يقترب منك ويهتم بك تعطيه فرصة؟",                
                "أشجع حاجه حلوه ف حياتك؟",                
                "طريقة جيدة يقنع حتى لو كانت الفكرة خاطئة"                 
                "كيف تتصرف مع من يسيئون فهمك ويأخذ على ذهنه ثم ينتظر أن يرفض؟",                
                "التغيير العادي عندما يكون الشخص الذي يحبه؟",               
                "المواقف الصعبة تضعف لك ولا ترفع؟",                
                "نظرة و يفسد الصداقة؟",                
                "‏‏لو حد قالك كلام سئ في الغالب اي رد فعلك؟",                
                "شخص معاك بالحلوه والمُره؟",                
                "‏هل تحب إظهار حبك وتعلقك بالشخص أم ترى ذلك ضعف؟",                
                "تاخد بكلام اللي ينصحك وماتعملش اللي انت عاوزة؟",               
                "اي تتمني الناس تعرفه عليك؟",                
                "ابيع المجرة عشان؟",                
                "أحيانا بحس ان الناس ، كمل؟",                
                "صدفة العمر الحلوة هي اني؟",             
                "الكُره العظيم دايم يجي بعد حُب قوي "
                "صفة تحبها في نفسك؟",               
                "‏الفقر فقر العقول ليس الجيوب "                
                "تصلي صلواتك الخمس كلها؟",                
                "‏تجامل أحد على راحتك؟",                
                "اشجع شيء عملته ف حياتك؟",                
                "ناوي تعمل اي النهارده؟",                
                "اي بيكون شعورك لما بتشوف المطر؟",
                "غيرتك هاديه ومابتعملش مشاكل؟",
                "اي اكتر حاجه ندمت عليها؟",
                "اي الدول اللي تتمنى تزورها؟",
                "اخره مره بكيت امتي؟",
                "تقييم حظك ؟ من عشره؟",
                "هل تعتقد ان حظك سيئ؟",
                "شـخــص تتمنــي الإنتقــام منـــه؟",
                "كلمة تود سماعها كل يوم؟",
                "**هل تُتقن عملك أم تشعر بالممل؟",
                "هل قمت بانتحال أحد الشخصيات لتكذب على من حولك؟",
                "متى آخر مرة قمت بعمل مُشكلة كبيرة وتسببت في خسائر؟",
                "ما هو اسوأ خبر سمعته بحياتك؟",                
                "‏ هل جرحت شخص تحبه من قبل ؟",               
                "ما هي العادة التي تُحب أن تبتعد عنها؟",
                "‏هل تحب عائلتك ام تكرههم؟",
                "‏من هو الشخص الذي يأتي في قلبك بعد الله – سبحانه وتعالى- ورسوله الكريم – صلى الله عليه وسلم؟",
                "‏هل خجلت من نفسك من قبل؟",                
                "‏ما هو ا الحلم الذي لم تستطيع ان تحققه؟",                
                "‏ما هو الشخص الذي تحلم به كل ليلة؟",              
                "‏هل تعرضت إلى موقف مُحرج جعلك تكره صاحبهُ؟",
                "‏هل قمت بالبكاء أمام من تُحب؟",              
                "‏ماذا تختار حبيبك أم صديقك؟",               
                "‏ هل حياتك سعيدة أم حزينة؟",                
                "ما هي أجمل سنة عشتها بحياتك؟",                
                "‏ما هو عمرك الحقيقي؟",                
                "ما هي أمنياتك المُستقبلية؟"
        ]
       
@Client.on_message(filters.command(["صراحه","اسال","سوال","اس","❤️‍🔥اسال"], ""), group=75583)
async def c5455utt(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    a = random.choice(thdhbxt)
    await message.reply(f"{a}")
        

tjgkgjhjxt = [
"واحد مشغول أتجوز واحدة مشغولة خلفوا عيل مش فاضيلهم 👻😹",
"مرة القمر كان عايز يتجوز الشمس قالتله أتجوز واحد صايع طول الليل 👻😹",
"ولد بيسأل أبوه هو الحب أعمى رد عليه أبوه بص في وش أمك وأنت تعرف 👻😹",
"مرة مفتاح مات أهله ما زعلوش عليه عشان معاهم نسخة تانية ??😹",
"ممرضة خلفت توأم سمت واحد عضل والتاني وليد 👻😹",
"مسطول أتجوز صينية قالتله مالك ساكت ليه؟ قالها مش عارف افتكرتك نايمة 👻😹",
"واحدة صعيدية جوزها رماها من الدور الثالث طلعتله وقالتله بلاش الهزار البايخ ده 👻😹",
"اتنين مساطيل حبوا يسرقوا عمارة فقالوا لبعض إحنا ناخد العمارة بعيد ونسرقها برحتنا 👻😹",
"منهم بص ورا ملقاش الهدوم فقال له كفاية كدة احنا بعدنا أوى 👻😹",
"حر جدًا، قالتله مفيش مشكلة نطلعها بالليل ??😹",
"واحد رجع في كلامه خبط اللي وراه 👻😹",
"واحد خلقه ضاق أعطاه لأخوه الصغير 👻😹",
"مرة مدرس رياضيات خلف ولدين واستنتج التالت 👻😹",
"واحد كهربائي أتجوز أربعة جابلهم مشترك 👻😹",
"كفايه عليك كده ياد يبن الحلوهه 👻😹",
"واحدة اسمها ساندي دخلت هندسة بقت ساندي متر مربع 👻😹",
"مرة شرطي مرور خلّف ولد بيتكلم بالإشارة 👻😹",
"مره واحد اسمو جابوا  كان بيرجم ابليس ف الحج قالولو ليه؟ قال عشان يمكن احتاجو 👻😹",
"ﻣﺮه واﺣﺪ ﻣﺴﻄﻮل ﻣﺎﺷﻰ ﻓﻰ اﻟﺸﺎرع ﻟﻘﻰ مذﻳﻌﻪ ﺑﺘﻘﻮﻟﻪ ﻟﻮ ﺳﻤﺤﺖ ﻓﻴﻦ اﻟﻘﻤﺮ ﻗﺎﻟﻬﺎ اﻫﻮه ﻗﺎﻟﺘﻠﻮ ﻣﺒﺮوك ﻛﺴﺒﺖ ﻋﺸﺮﻳﻦ ﺟﻨﻴﻪ ﻗﺎﻟﻬﺎ ﻓﻰ واﺣﺪ ﺗﺎﻧﻰ ﻫﻨﺎك اﻫﻮه  👻😹",
"واحد بيشتكي لصاحبه بيقوله أنا مافيش حد بيحبني ولا يفتكرني أبدًا، ومش عارف أعمل إيه قاله سهلة استلف من الناس فلوس هيسألوا عليك كل يوم 👻😹",
" مرة واحد مصري دخل سوبر ماركت في الكويت عشان يشتري ولاعة راح عشان يحاسب بيقوله الولاعة ديه بكام قاله دينار قاله منا عارف ان هي نار بس بكام 👻😹",
"بنت حبت تشتغل مع رئيس عصابة شغلها في غسيل الأموال 👻😹",
"واحد بيشتكي لصاحبه بيقوله أنا مافيش حد بيحبني ولا يفتكرني أبدًا، ومش عارف أعمل إيه قاله سهلة استلف من الناس فلوس هيسألوا عليك كل يوم 👻😹",
"ﻣﺮه واﺣﺪ ﻣﺴﻄﻮل ﻣﺎﺷﻰ ﻓﻰ اﻟﺸﺎرع ﻟﻘﻰ مذﻳﻌﻪ ﺑﺘﻘﻮﻟﻪ ﻟﻮ ﺳﻤﺤﺖ ﻓﻴﻦ اﻟﻘﻤﺮ؟ ﻗﺎﻟﻬﺎ اﻫﻮه ﻗﺎﻟﺘﻠﻮ ﻣﺒﺮوك ﻛﺴﺒﺖ ﻋﺸﺮﻳﻦ ﺟﻨﻴﻪ ﻗﺎﻟﻬﺎ ﻓﻰ واﺣﺪ ﺗﺎﻧﻰ ﻫﻨﺎك اﻫﻮه 👻😹",
"واحده ست سايقه على الجي بي اي قالها انحرفي قليلًا قلعت الطرحة 👻😹",
"مرة واحد غبي معاه عربية قديمة جدًا وبيحاول يبيعها وماحدش راضي يشتريها.. راح لصاحبه حكاله المشكلة صاحبه قاله عندي لك فكرة جهنمية هاتخليها تتباع الصبح أنت تجيب علامة مرسيدس وتحطها عليها. بعد أسبوعين صاحبه شافه صدفة قاله بعت العربية ولا لاء؟ قاله انت  مجنون حد يبيع مرسيدس 👻😹",
"مره واحد بلديتنا كان بيدق مسمار فى الحائط فالمسمار وقع منه فقال له :تعالى ف مجاش, فقال له: تعالي ف مجاش. فراح بلديتنا رامي على المسمار شوية مسمامير وقال: هاتوه 👻😹",
"واحدة عملت حساب وهمي ودخلت تكلم جوزها منه ومبسوطة أوي وبتضحك سألوها بتضحكي على إيه قالت لهم أول مرة يقول لي كلام حلو من ساعة ما اتجوزنا 👻😹",
"بنت حبت تشتغل مع رئيس عصابة شغلها في غسيل الأموال 👻😹",
"مره واحد اشترى فراخ علشان يربيها فى قفص صدره 👻😹",
"مرة واحد من الفيوم مات اهله صوصوا عليه 👻😹",
"ﻣﺮه واﺣﺪ ﻣﺴﻄﻮل ﻣﺎﺷﻰ ﻓﻰ اﻟﺸﺎرع ﻟﻘﻰ مذﻳﻌﻪ ﺑﺘﻘﻮﻟﻪ ﻟﻮ ﺳﻤﺤﺖ ﻓﻴﻦ اﻟﻘﻤﺮ ﻗﺎﻟﻬﺎ اﻫﻮه ﻗﺎﻟﺘﻠﻮ ﻣﺒﺮوك ﻛﺴﺒﺖ ﻋﺸﺮﻳﻦ ﺟﻨﻴﻪ ﻗﺎﻟﻬﺎ ﻓﻰ واﺣﺪ ﺗﺎﻧﻰ ﻫﻨﺎك اﻫﻮه 👻😹",
"مره واحد شاط كرة فى المقص اتخرمت. 👻😹",
"مرة واحد رايح لواحد صاحبهفا البواب وقفه بيقول له انت طالع لمين قاله طالع أسمر شوية لبابايا قاله يا أستاذ طالع لمين في العماره 👻😹",
" وهه عاوز تانيي 👻😹 "
        ]

@Client.on_message(filters.command(["نكته","❤️‍🔥نكته"], ""), group=7380)
async def nokt(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    a = random.choice(tjgkgjhjxt)
    await message.reply(
        f"{a}")

txjfjvkbkvt = [
" اتحداك تقول سر محدش يعرفو", 
" تحداك تطلع تغني ف الكول،🤡", 
" اتحداك تقفل الكول🤡🌟", 
" اتحداك تقول حاجه محدش يعرفها عن صاحب البار،🤡", 
" اتحداك تقلد صوت حيوان😂♥", 
" اتحداك تتصل بمطعم وتقوله عايز بيبرونة😂♥🤡", 
" اتحداك تخرج من كل الجروبات ال عندك 😂♥️", 
" اتحداك تقول اخر مره اتضربت امتا🤡🤡", 
" اتحداك تحكي شويه عن شخصيتك 🤡🌟", 
" اتحداك تجيب اسكرين من سيرش جوجل بتاعك😂♥", 
" اتحداك تغير صورة البروفايل زي بتاعتي", 
" اتحداك تقولي امك اسمها اي 😹♥️", 
" اتحداك تقطع 10 جنيه دلوقتي😂♥", 
" اتحداك تقفل الكول🤡🌟", 
" اتحداك تقلد صوت حيوان😂♥", 
" اتحداك تبعت اخر سكرين شوت عندك 😹♥", 
" اتحداك تقولي امك اسمها اي 😹♥️", 
" اتحداك تقول لحد دا امك اسمها اي", 
" اتحداك تقول اكتر اكله بتحبها🤡😹", 
" اتحداك تقول اسم البيست فريند❤️😹", 
" اعمل منشن لوحده وقولها هاتي رقمك 😂♥️", 
" اتحداك تمنشن لواحد كلاون 🤡", 
" اتحداك تدخل الكول وتقولهم بصوت عالي انا حامل 😂♥️", 
" اتحداك تجيب سكرين شوت ل شات اكتر حد بتضحك معاه 😂♥️", 
" اتحداك تقول لحد دا امك اسمها اي", 
" اتحداك تغني في ريكورد وتبعتو", 
" اتحداك تقول اخر مره اتضربت امتا🤡🤡", 
" لو راجل قولي انت مرتبط بكام وحده دلوقتي 😂♥️", 
" اتحداك تبعتلي صوره حبيبتك 😂♥️", 
" غنيلي اغنيه ل حمو بيكا 😂♥️", 
" اتحداك تمنشن لحد وتقوله انت حكاك❤️😹", 
" اتحداك تمنشن اطيب واحد هنا🤡??", 
" اتحداك تقول مين الي انت بتكراش عليها هنا ♥️😹", 
" اتحداك تقول اسم حبيبتك", 
" اتحداك تقول اخر رساله جاتلك من مين", 
" اتحداك تبعت رقمك 😂♥️", 
" اتحداك تقول اسم حبيبتك", 
" اتحداك تقفل الكول 😂♥️", 
" اتحداك تقوم تصلي دلوقتي ♥️", 
" اتحداك تمنشن لحد وتقوله انت حكاك❤️😹", 
" اتحداك تقول لحد امك رقاصه", 
" اتحداك تجيب سكرين شوت ل شات اكتر حد بتضحك معاه 😂♥️", 
" اتحداك تمنشن لواحده وتقولها تيجي نتجوز ❤️😹", 
" اتحداك تقول اخر مره اتضربت امتا🤡🤡", 
" اتحداك تجيب اسكرين من سيرش جوجل بتاعك😂♥", 
" اتحداك تقول اسم اغلي صاحب بتحبه❤️😹", 
" اتحداك تمنشن اكتر واحد شايفه م محترم😹🤡", 
" اتحداك تحذف تلي دلوقتي 😂♥️", 
" اتحداك تقول بحبك لخمس منشن😂😉", 
" اتحداك تقفل الكول 😂♥️", 
" اتحداك تغني لحسن شاكوش❤️😹", 
" اتحداك تقول رايك عن السوشيال ميديا 🤡", 
"ا تحداك تتكلم بلهجة مختلفة لمدة دقيق😂♥", 
" اتحداك تعمل منشن لحد وتقول نكته سخيفة😂♥", 
" اتحداك تصور نفسك دلوقتي وتبعتها", 
" اتحداك تقول لاي حد بحبك", 
" اتحداك تنزل واقع وتقابلني 😂❤️", 
" اتحداك تقطع الهاند بتاعتك دلوقتي😂♥", 
" اتحداك تقول اخر رساله جاتلك من مين", 
" اتحداك تفتح كام وتقول كبسو كبسو🤡😹", 
" اتحداك تقوم تصلي دلوقتي ♥️", 
" اتحداك تقول انا م راجل 😹🤡", 
" اتحداك تقول مواصفات فتاة احلامك😹🩶", 
" اتحداك تطلع الكول ترقص عقباوي 😂♥️", 
" اتحداك تمنشن لواحده وتقولها امك حماتي❤️😹", 
" اتحداك تقول للقيصر بحبك 😹♥", 
" اتحداك ترمي نفسك من البلكونة 😂♥", 
" اتحداك تقولي عندك كام اكس ف حياتك 😹♥️", 
" اتحداك تقول ع عاده بتحب تعملها❤️😹", 
" اتحداك تقطع الهاند بتاعتك دلوقتي😂♥", 
" اتحداك تمنشن لواحده وتقولها امك حماتي❤️😹", 
" اتحداك تبعت اسكرين لشات اكتر واحد بتكلمه❤️😹", 
" اتحداك تقول اسم بنت معرفتش تشقطها ♥️😹", 
" اتحداك تقول مين اخر حد بعتلك رساله", 
" اتحداك تمنشن اكتر واحد شايفه م محترم😹🤡", 
" صلي على النبي وتبسم ♥️✨", 
" اتحداك تقول اسم كراش الطفوله ♥️😹", 
" اتحداك تمنشن لحد وتقوله ارقلصي😂♥", 
" اتحداك تمنشن لحد وتقوله ارقلصي😂♥", 
" اتحداك تغني لحسن شاكوش❤️😹", 
" اتحداك تقول اسم كراش الطفوله ♥️😹", 
" اتحداك تقول اسم كراش الطفوله ♥️😹", 
" اتحداك تعمل منشن لحد وتقول نكته سخيفة😂♥", 
" اتحداك تبعت رقم امك😂♥", 
" اتحداك تقلد صوت حيوان😂♥", 
" اتحداك تعمل منشن لواحد وتقولو تعال نرتبط 😂♥️", 
" اتحداك تقول بتعمل اي ف اوقات فراغك🤡😹", 
" اتحداك تقول موقف حصلك ومش قادر تنساه ♥️😹", 
" اتحداك تحط البايو بحبك الى مغلبنى 10 دقايق ??↫ᶜᵃᵉˢᵃʳ", 
" اتحداك تسال صحبك رأيه ف شخصيتك وتصرفاتك🤡🌟",

        ]

@Client.on_message(filters.command(["تحدي"], ""), group=75543)
async def caes253ar(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    a = random.choice(txjfjvkbkvt)
    await message.reply(f"{a}")    
    
rdod = []

@Client.on_message(filters.command(["قفل الردود", "تعطيل الردود"], ""), group=7243) 
async def iddloc25k(client, message):
    bot_username = client.me.username    
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
       if message.chat.id in rdod:
         return await message.reply_text("تم معطل من قبل🔒")
       rdod.append(message.chat.id)
       return await message.reply_text("تم تعطيل الردود بنجاح ✅🔒")
    else:
       return await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")

@Client.on_message(filters.command(["فتح الردود", "تفعيل الردود"], ""), group=703) 
async def iddopen(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
       if not message.chat.id in rdod:
         return await message.reply_text("الردود مفعل من قبل ✅")
       rdod.remove(message.chat.id)
       return await message.reply_text("تم فتح الردود بنجاح ✅🔓")
    else:
       return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر لا يخصك✨♥")

@Client.on_message(filters.text, group=57355566)
async def d5548on(client, message):
   bot_username = client.me.username
   if message.chat.id in rdod:
    return  
   if message.text == "😒":
       await message.reply_text(f"عدل وشك ونت بتكلمني")
   elif message.text == "💋":
       await message.reply_text(f" نا عايز مح انا كمان ")
   elif message.text ==  "😭":
       await message.reply_text(f"بتعيط تيب لي طيب")
   elif message.text == "🥺":
       await message.reply_text(f"متزعلش بحبك ")
   elif message.text == "😂":
       await message.reply_text(f"ضحكتك عثل زيكك ينوحيي ")
   elif message.text == "🤔":
       await message.reply_text(f"بتفكر في اي")
   elif message.text == "🌚":
       await message.reply_text(f"القمر ده شبهك ")
   elif message.text == "نعم":
       await message.reply_text(f" نعم الله عليك ")
   elif "." in message.text:
       await message.reply_text(f"صلي علي النبي وتبسم ")
   elif message.text == "سلام":
       await message.reply_text(f" مع الف سلامه يقلبي متجيش تاني")
   elif message.text == "🙄":
       await message.reply_text(f" نزل عينك تحت كدا علشان هتخاد علي قفاك ")
   elif message.text == "برايفت":
       await message.reply_text(f"خدوني معاكم برايفت والنبي ")
   elif message.text == "السلام عليكم":
       await message.reply_text(f"وعليكم السلام ")
   elif message.text == "هاي":
       await message.reply_text(f"هآي تع اشب شااي • ")        
   elif message.text == "محح":
       await message.reply_text(f" محات حياتي يروحي ")
   elif message.text == "بحبك":
       await message.reply_text(f"وانا كمان بعشقك يا روحي")
   elif message.text == "الحمدلله":
       await message.reply_text(f"دايما ياحبيبي ")
   elif message.text == "هشش":
       await message.reply_text(f" بنهش كتاكيت احنا هنا ولا اي")        
   elif message.text == "هلا":
       await message.reply_text(f" هلا بيك ياروحي")
   elif message.text == "بف":
       await message.reply_text(f"وحيات امك ياكبتن خدوني معاكو بيف ")
   elif message.text == "خاص":
       await message.reply_text(f"ونجيب اشخاص ")
   elif message.text == "بخير":
       await message.reply_text(f"انت الخير يعمري ")        
   elif message.text == "اه":
       await message.reply_text(f" اه اي يا قدع عيب")
   elif message.text == "حصل":
       await message.reply_text(f"خخخ امال")        
   elif message.text == "تع":
       await message.reply_text(f"لا عيب بتكسف")
   elif message.text == "منور":
       await message.reply_text(f" ده نورك ي قلبي")        
   elif message.text == "ويت":
       await message.reply_text(f" اي الثقافه دي")
   elif message.text == "خخخ":
       await message.reply_text(f" اهدا يوحش ميصحش كدا ")        
   elif message.text == "باي":
       await message.reply_text(f"ع فين لوين رايح وسايبنى ")
   elif message.text == "شكرا":
       await message.reply_text(f"العفو ياروحي ")        
   elif message.text == "حلوه":
       await message.reply_text(f" انت الي حلو ياقمر")
   elif message.text == "بموت":
       await message.reply_text(f"موت بعيد م ناقصين مصايب ")        
   elif message.text == "تيب":
       await message.reply_text(f"فرح خالتك قريب")
   elif message.text == "اي":
       await message.reply_text(f"جتك اوهه م سامع ولا ايي")        
   elif message.text == "حاضر":
       await message.reply_text(f"حضرلك الخير يارب")
   elif message.text == "سي في":
       await message.reply_text(f"كفيه شقط سيب حاجه لغيرك")        
   elif message.text == "جيت":
       await message.reply_text(f"لف ورجع تانى مشحوار")
   elif message.text == "بخ":
       await message.reply_text(f"يوه خضتني ياسمك اي")        
   elif message.text == "خلاص":
       await message.reply_text(f"خلصتت روحكك يبعيد")
   elif message.text == "حبيبي":
       await message.reply_text(f"اوه ياه")
   elif message.text == "تمام":
       await message.reply_text(f"امك اسمها احلام")    