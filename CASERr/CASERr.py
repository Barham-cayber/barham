import asyncio
import requests
import random
import re
import os
import time
import datetime
import redis, re
from pyrogram import Client as client
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from unidecode import unidecode
from pyrogram import *
from dotenv import load_dotenv
from os import getenv
from pyrogram.types import *
from pyrogram.errors import PeerIdInvalid
from collections import defaultdict
from pyrogram import enums
from pyrogram.types import (InlineKeyboardButton, ChatPermissions, InlineKeyboardMarkup, Message, User)
import sys
from pyrogram.errors import FloodWait
from os import remove
from asyncio import sleep
from pyrogram.types import *
from pyrogram import Client, idle
from random import randint
from pyrogram.enums import ChatType
from pyrogram.types import Chat, User
from config import user, dev, call, logger, logger_mode, botname, appp
from CASERr.daty import get_call, get_userbot, get_dev, get_logger
from casery import caes, casery, group, source, photosource, caserid
    
API_ID = int("27442758")
API_HASH = "8288c5c54f568ee346b3227271700b52"

# Get ur redis url from https://app.redislabs.com/
r = redis.from_url(
    'redis://default:VL9ITtuHp4uy7dJclHunfu7mBcix1jbT@redis-12071.c93.us-east-1-3.ec2.redns.redis-cloud.com:12071')




Keyard = ReplyKeyboardMarkup(
  [
    [("مطور البوت"),("مطور السورس")], 
    [("السورس")],    
    [("كت"),("تويت")],
    [("حروف")],
    [("اسال"),("زخرفه")],
    [("لو خيروك")],
    [("صور بنات"),("صور شباب")],
    [("قران")],
    [("اقتباس"),("فيلم")],
    [("غنيلي")],
    [("استوري"),("متحركه")],
  ],
  resize_keyboard=True
)

Keyboard = ReplyKeyboardMarkup(
  [
    [("مطور السورس"), ("سورس")],
    [("تعيين اسم البوت")],
    [("قسم الاذاعه"), ("قسم المساعد")],
    [("تعيين جروب السورس"), ("تعيين قناه السورس")],   
    [("تعيين مطور السورس"), ("تعيين صوره السورس")],   
    [("《الاحصائيات》")],
    [("《تفعيل التواصل》"), ("《تعطيل التواصل》")],
    [("اضف قناه اشتراك"), ("حذف قناه اشتراك")],  
    [("قنوات الاشتراك")],     
    [("الجروبات"), ("المستخدمين")],
    [("رفع نسخه الجروبات"), ("رفع نسخه الاشخاص")],
    [("قسم الترويج")],
  ],
  resize_keyboard=True
)

Keybcasoard = ReplyKeyboardMarkup(
  [
    [("مطور السورس"), ("سورس")],
    [("تعيين اسم البوت")],
    [("قسم الاذاعه"), ("قسم المساعد")],
    [("تعيين جروب السورس"), ("تعيين قناه السورس")],   
    [("تعيين مطور السورس"), ("تعيين صوره السورس")],   
    [("《الاحصائيات》")],
    [("《تفعيل التواصل》"), ("《تعطيل التواصل》")],
    [("اضف قناه اشتراك"), ("حذف قناه اشتراك")],  
    [("قنوات الاشتراك")],     
    [("الجروبات"), ("المستخدمين")],
    [("رفع نسخه الجروبات"), ("رفع نسخه الاشخاص")],
    [("تفعيل الصلاحيات المدفوعه"),("تعطيل الصلاحيات المدفوعه")],
    [("قسم الترويج")],
  ],
  resize_keyboard=True
)


Keyboazard = ReplyKeyboardMarkup(
  [
    [("《اذاعة》")],
    [("《اذاعة بالمجموعات》"), ("《اذاعة بالتوجيه》")], 
    [("《اذاعة بالتثبيت》")],  
    [("《الغاء》")],
    [("رجوع")],
  ],
  resize_keyboard=True
)

Keyttd = ReplyKeyboardMarkup(
  [
    [("ترويج للحمايه"), ("ترويج للميوزك")],
    [("《الغاء》")],
    [("رجوع")],
  ],
  resize_keyboard=True
)

caes = caes
casery = casery
source = source
group = group
caserid = caserid
photosource = photosource
name = "قيصر"
names = {} 
devuser = {} 
devchannel = {} 
devgroup = {} 
devphots = {} 
devess = {} 

@Client.on_message(filters.command(["تفعيل الصلاحيات المدفوعه"], "") & filters.private, group=667563)
async def for_5s(client, message):
  bot_username = client.me.username
  OWNER_ID = await get_dev(bot_username)
  usr1 = await client.get_chat(OWNER_ID)
  wenru = usr1.username
  if message.from_user.username in caes:
    try: 
     devess[bot_username] = wenru
     await message.reply_text(f"تم تفعيل الصلاحيات المدفوعة للبوت بنجاح، شكرا لك ✨♥")
    except:
     return await message.reply_text("تم التفعيل من قبل")
  else:
   await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر في الوضع المدفوع، تواصل مع مطور السورس")
     
@Client.on_message(filters.command(["تعطيل الصلاحيات المدفوعه"], "") & filters.private, group=667563)
async def disabl(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    usr1 = await client.get_chat(OWNER_ID)
    wenru = usr1.username
    if message.from_user.username in caes:
        if devess[bot_username] == wenru:
            del devess[bot_username]
            await message.reply_text("تم تعطيل الصلاحيات المدفوعة للبوت وحذفها من التخزين بنجاح ✨♥")
        else:
            await message.reply_text("الصلاحيات غير مفعلة من قبل")
    else:
        await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر في الوضع المدفوع، تواصل مع مطور السورس")
    
@Client.on_message(filters.regex("تعيين اسم البوت") & filters.private, group=757113)
async def bot_name(client, message):
  bot_username = client.me.username
  OWNER_ID = await get_dev(bot_username)
  if message.from_user.id == OWNER_ID or message.from_user.username in caes:
   try:
    bot = await client.ask(message.chat.id, "هات اسم البوت", timeout=200)
   except:
    return
   bot_name = bot.text
   names[bot_username] = bot_name
   await client.send_message(message.chat.id, "**تم تعيين اسم البوت بنجاح ✨♥**")

@Client.on_message(filters.regex("تعيين مطور السورس") & filters.private, group=712813)
async def dev_user(client, message):
  bot_username = client.me.username
  dev = devess.get(bot_username) if devess.get(bot_username) else f"{caes}"
  OWNER_ID = await get_dev(bot_username)
  if message.from_user.username in caes or message.from_user.username == dev:
   try:
    bot = await client.ask(message.chat.id, "هات يوزر المطور", timeout=200)
   except:
    return
   bot_name = bot.text.replace("@", "")
   devuser[bot_username] = bot_name
   await client.send_message(message.chat.id, "**تم تعيين مطور السورس بنجاح ✨♥**")
  else:
   await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر في الوضع المدفوع، تواصل مع مطور السورس")
   
@Client.on_message(filters.regex("تعيين قناه السورس") & filters.private, group=716713)
async def dev_channel(client, message):
  bot_username = client.me.username
  bot_id = client.me.id
  dev = devess.get(bot_username) if devess.get(bot_username) else f"{caes}"
  OWNER_ID = await get_dev(bot_username)
  if message.from_user.username in caes or message.from_user.username == dev:
   try:
    bot = await client.ask(message.chat.id, "هات رابط القناه", timeout=200)
   except:
    return
   bot_name = bot.text
   devchannel[bot_username] = bot_name
   await client.send_message(message.chat.id, "**تم تعيين قناه السورس بنجاح ✨♥**")
  else:
   await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر في الوضع المدفوع، تواصل مع مطور السورس")
   
@Client.on_message(filters.command(["تعيين صوره السورس"], ""), group=571135)
async def dev_phot4(client, message):
  bot_username = client.me.username
  dev = devess.get(bot_username) if devess.get(bot_username) else f"{caes}"
  OWNER_ID = await get_dev(bot_username)
  if message.from_user.username in caes or message.from_user.username == dev:
    try:
     bot = await client.ask(message.chat.id, f"ارسل لان رابط الصوره بصيغه تليجراف ميديا مثال \n{photosource} ", timeout=200)
    except:
     return
    bot_name = bot.text
    devphots[bot_username] = bot_name
    await client.send_message(message.chat.id, "**تم تعيين صوره السورس بنجاح ✨♥**")
  else:
   await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر في الوضع المدفوع، تواصل مع مطور السورس")
   
@Client.on_message(filters.regex("تعيين جروب السورس") & filters.private, group=711513)
async def dev_group(client, message):
  bot_username = client.me.username
  dev = devess.get(bot_username) if devess.get(bot_username) else f"{caes}"
  OWNER_ID = await get_dev(bot_username)
  if message.from_user.username in caes or message.from_user.username == dev:
   try:
    bot = await client.ask(message.chat.id, "هات رابط الجروب", timeout=200)
   except:
    return
   bot_name = bot.text
   devgroup[bot_username] = bot_name
   await client.send_message(message.chat.id, "**تم تعيين جروب السورس بنجاح ✨♥**")
  else:
   await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر في الوضع المدفوع، تواصل مع مطور السورس")
   
@Client.on_message(filters.regex("اضف قناه اشتراك") & filters.private, group=7113)
async def maadd_channel(client, message):
  bot_username = client.me.username
  makr = f"@{bot_username}"
  dev = devess.get(bot_username) if devess.get(bot_username) else f"{caes}"
  OWNER_ID = await get_dev(bot_username)
  if message.from_user.username in caes or message.from_user.username == dev:
    ask = await client.ask(message.chat.id, f"لتفعيل الاشتراك الاجباري \n قم باضافه هذا البوت {makr} الي قناتك\nلو ضفته ارسل `تم`", timeout=300)
    me = ask.text
    if me == "تم":
     try:
      bot = await client.ask(message.chat.id, "هات رابط القناه", timeout=200)
     except:
      return
     channel = bot.text.replace("https://t.me/", "")  
     oo = [channel]
     add_channel(oo, bot_username)
     await client.send_message(message.chat.id, "تم حفظ القناه بنجاح")
  else:
    await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر في الوضع المدفوع، تواصل مع مطور السورس")
            
@Client.on_message(filters.command("قنوات الاشتراك", "") & filters.private)
async def botzbjbbojfchhmbie(client, message):
  bot_username = client.me.username
  dev = devess.get(bot_username) if devess.get(bot_username) else f"{caes}"
  OWNER_ID = await get_dev(bot_username)
  if message.from_user.username in caes or message.from_user.username == dev:
    o = 0
    text = "قائمة القنوات\n"
    for x in get_channel(bot_username):
        o += 1
        channel = x[0]
        text += f"{o}- @{channel}\n"
    if o == 0:
        return await message.reply_text("لا يوجد قنوات")
    await message.reply_text(text)
  else:
   await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر في الوضع المدفوع، تواصل مع مطور السورس")
  
@Client.on_message(filters.command("حذف قناه اشتراك", "") & filters.private)
async def delete_bot_zchombie(client, message):
  bot_username = client.me.username
  dev = devess.get(bot_username) if devess.get(bot_username) else f"{caes}"
  OWNER_ID = await get_dev(bot_username)
  if message.from_user.username in caes or message.from_user.username == dev:
    try:
        bot = await client.ask(message.chat.id, "هات رابط القناه", timeout=200)
    except:
        return
    channel = bot.text.replace("https://t.me/", "")
    for x in get_channel(bot_username):
        if x[0] == channel:
            del_channel(x, bot_username)
    await message.reply_text("تم حذف القناه بنجاح")
  else:
   await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر في الوضع المدفوع، تواصل مع مطور السورس")
 
def add_channel(bots, bot_username):
    if is_channel(bots, bot_username):
        return
    r.sadd(f"channel{bot_username}", str(bots))

def is_channel(bots, bot_username):
    try:
        a = get_channel(bot_username)
        if bots in a:
            return True
        return False
    except:
        return False

def del_channel(bots, bot_username):
    if not is_channel(bots, bot_username):
        return False
    r.srem(f"channel{bot_username}", str(bots))

def get_channel(bot_username):
    try:
        lst = []
        for a in r.smembers(f"channel{bot_username}"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except:
        return []

async def johned(client, message):
   bot_username = client.me.username
   for x in get_channel(bot_username):
    ch = x[0]
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(" اضغط هنا للاشتراك بالقناة 🚦", url=f"https://t.me/{ch}")]])
    try:
      get = await client.get_chat_member(ch, message.from_user.id)
    except Exception as e:    	
      return await message.reply_text(f"🚦عذرا عزيزي {message.from_user.mention} يجب عليك الاشترك في القناة اولا..\n\n    قنـاة الـبـوت :\n ⤹ https://t.me/{ch} ⤸", disable_web_page_preview=True, reply_markup=keyboard)
 
caesar_responses = [
    "معاك يشق",
    "يسطا شغال شغال متقلقش",
    "بحبك يعم قول عايز اي",
    "يبني هتقول عايز اي ولا اسيبك وامشي ",
    "قلب {name} من جوه",
    "نعم يقلب {name} ",
    "قرفتني والله بس بحبك بقا اعمل اي",
    "خلاص هزرنا وضحكنا انطق بقا عايز اي ؟",
    "قوول يقلبو ",
    "طب بذمتك لو انت بوت ترضا حد يقرفقك كدا؟",
]
  
bot = [
    "اسمي {name} يصحبي",
    "يسطا قولتلك اسمي {name} الاه",
    "نعم يحب ",
    "قول يقلبو",
    "يسطا هوا عشان بحبك تصعدني؟",
    "يعم والله بحبك بس ناديلي ب {name}",
    "تعرف بالله هحبك اكتر لو ناديتلي {name}",
    "اي ي معلم مين مزعلك",
    "متصلي علي النبي كدا ",
    "مش فاضيلك نصايه وكلمني",
    "يسطا قولي مين مزعلك وعايزك تقعد وتتفرج ع اخوك",
    "انجز عايزني اشقطلك مين؟",
    "شكلها منكدا عليك وجاي تطلعهم علينا ",
    "ورحمه ابويا اسمي {name}",
]

cff = []
sc = []

@Client.on_message(filters.command(["بوت", "البوت"], ""), group=571135)
async def caesar5_bot(client, message):
    bot_username = client.me.username
    if await johned(client, message):
     return
    me = names.get(bot_username) if names.get(bot_username) else f"{name}"
    bar = random.choice(bot).format(name=me)
    await message.reply_text(text=f"**[{bar}](https://t.me/{bot_username}?startgroup=True)**", disable_web_page_preview=True)
 
@Client.on_message(filters.text & ~filters.me, group=7151535)
async def respond_to_caesar(client, message):
    bot_username = client.me.username
    me = names.get(bot_username) if names.get(bot_username) else f"{name}"
    if me in message.text:     
     bar = random.choice(caesar_responses).format(name=me)
     await message.reply_text(text=f"**[{bar}](https://t.me/{bot_username}?startgroup=True)**", disable_web_page_preview=True)


@Client.on_message(filters.command(["/start"], "") & filters.private, group=1267686)
async def for_us65ers(client, message):
   if await johned(client, message):
     return
   bot_username = client.me.username
   bot_id = client.me.id
   name = client.me.first_name
   botmention = client.me.mention
   devus = devuser.get(bot_username) if devuser.get(bot_username) else f"{casery}"
   soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
   gr = devgroup.get(bot_username) if devgroup.get(bot_username) else f"{group}"
   ff = devphots.get(bot_username) if devphots.get(bot_username) else f"{photosource}"   
   OWNER_ID = await get_dev(bot_username)
   usr1 = await client.get_chat(OWNER_ID)
   wenru = usr1.username
   namew = usr1.first_name
   button = [[InlineKeyboardButton(text="عـــربـــي 🇪🇬", callback_data=f"arbk"), InlineKeyboardButton(text="English 🏴󠁧󠁢󠁥󠁮󠁧󠁿", callback_data=f"english")],[InlineKeyboardButton(text=f"{namew}", url=f"https://t.me/{wenru}")], [InlineKeyboardButton(text="𝗔𝗱𝗗 𝗕𝗼𝗧 𝗧𝗼 𝗬𝗼𝗨𝗿 𝗚𝗿𝗢𝘂𝗣 ⤶", url=f"https://t.me/{bot_username}?startgroup=True")]]
   photo = await gen_bot(client, bot_username, bot_id)
   if await check(message.from_user.id, bot_username, bot_id):
     kep = ReplyKeyboardMarkup([["《صنع بوت》", "《حذف بوت》"], ["البوتات المصنوعه"], ["تعطيل المجاني", "تفعيل المجاني"], ["تعطيل التواصل", "تفعيل التواصل"], ["السورس"], ["الغاء"]], resize_keyboard=True)
     return await message.reply_photo(photo=photo, caption=f"**.       ╭─── : [ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh}) : ───╮\n\n⌁ | مرحبا بك {message.from_user.mention}\n⌁ | انا {botmention}\n⌁ | اتمتع بافضل اداء في سرعه التشغيل\n⌁ | واجمل حمايه جروبات وقنوات\n⌁ | واقوي منع تصفيه\n⌁ | مع جميع الرتب من الادمن للاساسي\n⌁ | ضفني في جروبك وتاكد بانفسك\n\n        ╰─── : [ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh}) : ───╯**", reply_markup=InlineKeyboardMarkup(button))
   kep = ReplyKeyboardMarkup([["مطور البوت"], ["🥺 ¦ حذف الكيبورد"]], resize_keyboard=True)
   await message.reply_photo(photo=photo, caption=f"**.       ╭─── : [ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh}) : ───╮\n\n⌁ | مرحبا بك {message.from_user.mention}\n⌁ | انا {botmention}\n⌁ | اتمتع بافضل اداء في سرعه التشغيل\n⌁ | واجمل حمايه جروبات وقنوات\n⌁ | واقوي منع تصفيه\n⌁ | مع جميع الرتب من الادمن للاساسي\n⌁ | ضفني في جروبك وتاكد بانفسك\n\n        ╰─── : [ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh}) : ───╯**", reply_markup=InlineKeyboardMarkup(button))
   if not await check(message.from_user.id, bot_username, bot_id):
     print("t")
   if not is_user(message.from_user.id, bot_id):
     add_user(message.from_user.id, bot_id)
     text = '🙍 شخص جديد دخل الى البوت !\n\n'
     text += f'🎯 الأسم: {message.from_user.first_name}\n'
     text += f'♻️ الايدي: {message.from_user.id}\n\n'
     text += f'🌐 اصبح عدد المستخدمين: {len(get_user(bot_id))}'
     reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton (message.from_user.first_name, user_id=message.from_user.id)]])
     if len(get_admins(bot_id)) > 0:
        list = get_admins(bot_id)
        for admin in list:
          await client.send_message(int(admin), text, reply_markup=reply_markup)
        await client.send_message(int(OWNER_ID), text, reply_markup=reply_markup)
     else:
        await client.send_message(int(OWNER_ID), text, reply_markup=reply_markup)

@Client.on_callback_query(filters.regex(pattern=r"^(arbk|english)$"))
async def admin_r98hts(client: Client, CallbackQuery):
    bot_username = client.me.username
    bot_id = client.me.id
    name = client.me.first_name
    botmention = client.me.mention
    devus = devuser.get(bot_username) if devuser.get(bot_username) else f"{casery}"
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    gr = devgroup.get(bot_username) if devgroup.get(bot_username) else f"{group}"
    OWNER_ID = await get_dev(bot_username)
    usr1 = await client.get_chat(OWNER_ID)
    wenru = usr1.username
    namew = usr1.first_name    
    command = CallbackQuery.matches[0].group(1)
    chat_id = CallbackQuery.message.chat.id 
    if command == "arbk":
     button = [[InlineKeyboardButton(text="اوامر التشغيل ⚡", callback_data=f"arbkm"), InlineKeyboardButton(text="اوامر الحمايه ⚡", callback_data=f"arbkh")], [InlineKeyboardButton(text=f"القـنـاة ⚡", url=f"{soesh}"), InlineKeyboardButton(text=f"الـجـروب ⚡", url=f"{gr}")], [InlineKeyboardButton(text=f"{namew}", url=f"https://t.me/{wenru}")], [InlineKeyboardButton(text="𝗔𝗱𝗗 𝗕𝗼𝗧 𝗧𝗼 𝗬𝗼𝗨𝗿 𝗚𝗿𝗢𝘂𝗣 ⤶", url=f"https://t.me/{bot_username}?startgroup=True")]]
     await CallbackQuery.answer("مرحبا بك في قسم اللغه العربيه ✨♥", show_alert=True)	
     await CallbackQuery.edit_message_text(f"**.       ╭─── : [ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh}) : ───╮\n\n⌁ | مرحبا بك {CallbackQuery.from_user.mention}\n⌁ | انا {botmention}\n⌁ | اتمتع بافضل اداء في سرعه التشغيل\n⌁ | واجمل حمايه جروبات وقنوات\n⌁ | واقوي منع تصفيه\n⌁ | ضفني في جروبك وتاكد بانفسك\n\n        ╰─── : [ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh}) : ───╯**", reply_markup=InlineKeyboardMarkup(button))
    if command == "english":
     button = [[InlineKeyboardButton(text="Play orders ⚡", callback_data=f"englishm")], [InlineKeyboardButton(text=f"Channel ⚡", url=f"{soesh}"), InlineKeyboardButton(text=f"Group ⚡", url=f"{gr}")], [InlineKeyboardButton(text=f"{namew}", url=f"https://t.me/{wenru}")], [InlineKeyboardButton(text="𝗔𝗱𝗗 𝗕𝗼𝗧 𝗧𝗼 𝗬𝗼𝗨𝗿 𝗚𝗿𝗢𝘂𝗣 ⤶", url=f"https://t.me/{bot_username}?startgroup=True")]]
     await CallbackQuery.answer("مرحبا بك في قسم اللغه الانجليزيه ✨♥", show_alert=True)	
     await CallbackQuery.edit_message_text(f"**╭─── : [ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh}) : ───╮\n\n𝗔 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗠𝘂𝘀𝗶𝗰 𝗕𝗼𝘁\n𝗣𝗹𝗮𝘆𝗲𝗱 𝗠𝘂𝘀𝗶𝗰 𝗮𝗻𝗱 𝗩𝗶𝗱𝗲𝗼 𝗶𝗻 𝗩𝗖\n𝗕𝗼𝘁 𝗢𝗻𝗹𝗶𝗻𝗲 𝗡𝗼𝘄 ......🖱️❤️\n𝗔𝗱𝗱 𝗠𝗲 𝗧𝗼 𝗬𝗼𝘂𝗿 𝗖𝗵𝗮𝘁\n\n╰─── : [ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh}) : ───╯**", reply_markup=InlineKeyboardMarkup(button))

@Client.on_callback_query(filters.regex("arbkh"))
async def hem84a1(client, callback_query: CallbackQuery):
    bot_username = client.me.username
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    await callback_query.edit_message_text(f"""⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗\n• اوامــر الحمايه\n• قفل وفتح ← الروابط\n• قفل وفتح ← الدردشه\n• قفل وفتح ← المنشن\n• قفل وفتح ← الفيديو\n• قفل وفتح ← الصور\n• قفل وفتح ← الملصقات\n• قفل وفتح ← الردود\n• قفل وفتح ← التاك\n  • تفعيل وتعطيل ← سمسمي\n• همسه ← عن طريق ريبلاي\n• تفعيل وتعطيل ← جمالي ، ايدي ، تاك\n• رفع مشرف ← مع تحديد الصلاحيات\n⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="arbk")]]))
       
@Client.on_callback_query(filters.regex("arbkm"))
async def mem84ma1(client, callback_query: CallbackQuery):
    bot_username = client.me.username
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    await callback_query.edit_message_text(f"""اوامر التشغيل ⚡:\n» شغل او تشغيل - لتشغيل الموسيقى  \n» فيد او فيديو  - لتشغيل مقطع فيديو \n» تحميل + اسم الاغنيه - لتحميل ملف صوتي\n» سورس - لعرض معلومات البوت \n»  وقف - ايقاف موقت\n» استكمال - لاستكمال التشغيل\n» تخطي - لتخطي تشغيل الحالي\n» ايقاف او اسكت - لايقاف تشغيل الحالي""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="arbk")]]))

@Client.on_callback_query(filters.regex("englishm"))
async def me25ma1(client, callback_query: CallbackQuery):
    bot_username = client.me.username
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    await callback_query.edit_message_text(f"""» /𝗽𝗹𝗮𝘆 (𝘀𝗼𝗻𝗴 𝗻𝗮𝗺𝗲/𝗹𝗶𝗻𝗸) - 𝗽𝗹𝗮𝘆 𝗺𝘂𝘀𝗶𝗰 𝗼𝗻 𝘃𝗶𝗱𝗲𝗼 𝗰𝗵𝗮𝘁\n» /𝘃𝗽𝗹𝗮𝘆 (𝘃𝗶𝗱𝗲𝗼 𝗻𝗮𝗺𝗲/𝗹𝗶𝗻𝗸) - 𝗽𝗹𝗮𝘆 𝘃𝗶𝗱𝗲𝗼 𝗼𝗻 𝘃𝗶𝗱𝗲𝗼 𝗰𝗵𝗮𝘁\n» /𝗽𝗮𝘂𝘀𝗲 - 𝗽𝗮𝘂𝘀𝗲 𝘁𝗵𝗲 𝘀𝘁𝗿𝗲𝗮𝗺\n» /𝗿𝗲𝘀𝘂𝗺𝗲 - 𝗿𝗲𝘀𝘂𝗺𝗲 𝘁𝗵𝗲 𝘀𝘁𝗿𝗲𝗮𝗺\n» /𝘀𝗸𝗶𝗽 - 𝘀𝘄𝗶𝘁𝗰𝗵 𝘁𝗼 𝗻𝗲𝘅𝘁 𝘀𝘁𝗿𝗲𝗮𝗺\n» /𝘀𝘁𝗼𝗽 - 𝘀𝘁𝗼𝗽 𝘁𝗵𝗲 𝘀𝘁𝗿𝗲𝗮𝗺𝗶𝗻𝗴""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="english")]]))
                            
@Client.on_message(filters.command(["/start","رجوع","رجوع للتحكم الكامل"], "") & filters.private, group=67875563)
async def for_users(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
      return
    if message.from_user.id == OWNER_ID:
        return await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} اليك كيب التحكم بالبوت", reply_markup=Keyboard)
    elif message.from_user.username in caes:
        return await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} اليك كيب التحكم بالبوت", reply_markup=Keybcasoard)        
    else:
        await message.reply_text(f"صلي على النبي وتبسم 🌺♥", reply_markup=Keyard)
        
@Client.on_message(filters.command(["قسم الاذاعه"], "") & filters.private, group=67563)
async def for_5useers(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.from_user.id == OWNER_ID or message.from_user.username in caes:
        return await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} اليك كيب التحكم بالبوت", reply_markup=Keyboazard)
        
@Client.on_message(filters.command(["قسم الترويج"], "") & filters.private, group=67563)
async def for_5usersKeyttd(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.from_user.id == OWNER_ID or message.from_user.username in caes:
        return await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} اليك كيب التحكم بالبوت", reply_markup=Keyttd)

@Client.on_message(filters.command(["قسم المساعد", "عوده لقسم المساعد"], "") & filters.private, group=67563)
async def foassrsKeyttd(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   userbot = await get_userbot(bot_username)
   if await johned(client, message):
     return
   me = userbot.me
   i = f"@{me.username} : {me.id}" if me.username else me.id
   b = await client.get_chat(me.id)
   b = b.bio if b.bio else "لا يوجد بايو"
   if message.from_user.id == OWNER_ID or message.from_user.username in caes:
    kep = ReplyKeyboardMarkup([["فحص المساعد"], ["تغير الاسم الاول", "تغير اسم المستخدم"], ["تغير البايو", "اضافه صوره"], ["ازاله صوره"], ["توجيه عام بالمساعد", "اذاعه عام بالمساعد"], ["دعوه المساعد الي الانضمام"], ["رجوع"]], resize_keyboard=True)
    await message.reply_text(f"**أهلا بك عزيزي المطور **\n**هنا قسم الحساب المساعد**\n**{me.mention}**\n**{i}**\n**{b}**", reply_markup=kep)

    
admins_commands = [
   '《الاحصائيات》', '《تفعيل التواصل》',
   '《تعطيل التواصل》', '《اذاعة بالتثبيت》', '《اذاعة》',
   '《اذاعة بالتوجيه》', '《تفعيل الاشتراك》', '《تعطيل الاشتراك》',
   '《ضع قناة الاشتراك》', '《حذف قناة الاشتراك》', '《قناة الاشتراك》','قائمه الأدمنيه',
   'المستخدمين', 'الأدمنية', 'الجروبات',
   '《اذاعة بالمجموعات》','《اذاعة بالتثبيت بالمجموعات》', 'اخفاء الكيبورد'
   ]
   
owner_commands = [
   'نقل ملكية البوت', 'رفع ادمن', 'تنزيل ادمن'
]

@Client.on_message(filters.text & filters.private, group=2)
async def keyboardforadmins(client, m):
  bot_username = client.me.username
  OWNER_ID = await get_dev(bot_username)
  bot_id = client.me.id
  if m.text in admins_commands:
    if not await check(m.from_user.id, bot_username, bot_id):
      return await m.reply('🌀 هذا الأمر لا يخصك', quote=True)
    else:    
      if m.text == '《الاحصائيات》':
        text = f'**👤 عدد المستخدمين: {len(get_user(bot_id))}\n'
        text += f'📊 عدد المجموعات: {len(get_groups(bot_id))}\n'
        text += f'🌀 عدد المشرفين: {len(get_admins(bot_id))}**'
        await m.reply(text, quote=True)        
      if m.text == '《تفعيل التواصل》':
        if r.get(f'enable_twasol{bot_id}'):
          return await m.reply("• تم تفعيل التواصل مسبقاً", quote=True)          
        await m.reply(f'**• بواسطة ⟨ {m.from_user.mention} ⟩\n• تم تفعيل التواصل بنجاح**', quote=True)
        r.set(f'enable_twasol{bot_id}', 1)      
      if m.text == '《تعطيل التواصل》':
        if not r.get(f'enable_twasol{bot_id}'):
          return await m.reply("• تم تعطيل التواصل مسبقاً", quote=True)
        await m.reply(f'**• بواسطة ⟨ {m.from_user.mention} ⟩\n• تم تعطيل التواصل بنجاح**', quote=True)
        r.delete(f'enable_twasol{bot_id}')      
      if m.text == 'المستخدمين':
        await m.reply_document(get_users_backup(bot_id), quote=True)      
      if m.text == 'الأدمنية':
        await m.reply_document(get_admins_backup(bot_id), quote=True)      
      if m.text == 'الجروبات':
        await m.reply_document(get_groups_backup(bot_id), quote=True)      
      if m.text == '《تفعيل الاشتراك》':
        if r.get(f"enable_force_subscribe{bot_id}"):
          return await m.reply('• تم تفعيل الاشتراك الاجباري مسبقاً',quote=True)
        await m.reply(f'**• بواسطة ⟨ {m.from_user.mention} ⟩\n• تم تفعيل الاشتراك بنجاح**', quote=True) 
        r.set(f"enable_force_subscribe{bot_id}", 1)      
      if m.text == '《تعطيل الاشتراك》':
        if not r.get(f"enable_force_subscribe{bot_id}"):
          return await m.reply('• تم تعطيل الاشتراك الاجباري مسبقاً',quote=True)
        await m.reply(f'**• بواسطة ⟨ {m.from_user.mention} ⟩\n• تم تعطيل الاشتراك بنجاح**', quote=True) 
        r.delete(f"enable_force_subscribe{bot_id}")      
      if m.text == '《ضع قناة الاشتراك》':
        await m.reply("• ارسل معرف القناة العام مثال @COURSE_CAESAR", quote=True)
        r.set(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")      
      if m.text == '《حذف قناة الاشتراك》':
        if not r.get(f'force_channel{bot_id}'):
          return await m.reply("• لا توجد قناة اشتراك معينة", quote=True)
        await m.reply("• تم حذف قناة الاشتراك بنجاح", quote=True)
        r.delete(f'force_channel{bot_id}')      
      if m.text == '《قناة الاشتراك》':
        if not r.get(f'force_channel{bot_id}'):
          await m.reply('• لاتوجد قناة مضافة', quote=True)
        else:
          channel = r.get(f'force_channel{bot_id}').decode('utf-8')
          await m.reply(f"https://t.me/{channel}", quote=True)      
      if m.text == 'قائمه الأدمنيه':
        if len(get_admins(bot_id)) == 0:
          await m.reply("• لايوجد آدمنية", quote=True)
        else:
          text = '• قائمة الأدمنية\n'
          for admin in get_admins(bot_id):
            try:
              get = await client.get_chat(int(admin))
              text += f'• [{get.first_name}](tg://user?id={admin})\n'
            except:
              text += f'• [@COURSE_CAESAR](tg://user?id={admin})\n'
          await m.reply(text, quote=True)         
      if m.text == '《اذاعة》':
        await m.reply("• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )",quote=True)
        r.set(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")      
      if m.text == '《اذاعة بالتثبيت》':
        await m.reply("• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )",quote=True)
        r.set(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")        
      if m.text == '《اذاعة بالتوجيه》':
        await m.reply("• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )",quote=True)
        r.set(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")      
      if m.text == '《اذاعة بالمجموعات》':
        await m.reply("• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )",quote=True)
        r.set(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")      
      if m.text == '《اذاعة بالتثبيت بالمجموعات》':
        await m.reply("• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )",quote=True)
        r.set(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")      
      if m.text == 'اخفاء الكيبورد':
        await m.reply("• تم اخفاء لوحة التحكم لاظهارها مجدداً ارسل /start",
        quote=True, reply_markup=ReplyKeyboardRemove (selective=True))


@Client.on_message(filters.text & filters.private, group=3)
async def for_owner(client,m):
  bot_username = client.me.username
  OWNER_ID = await get_dev(bot_username)
  bot_id = client.me.id
  text = m.text
  if text in owner_commands:
   if not m.from_user.id == int(OWNER_ID):
      return await m.reply("• هذا الأمر يخص المطور الأساسي فقط", quote=True)   
   if text == 'نقل ملكية البوت':
     await m.reply("• ارسل ايدي المالك الجديد الآن", quote=True)
     r.set(f"{m.from_user.id}transfer{m.chat.id}{bot_id}",1)
     r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
   if text == 'رفع ادمن':
     await m.reply("• ارسل ايدي الآدمن الآن", quote=True)
     r.set(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}",1)
     r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")   
   if text == 'تنزيل ادمن':
     await m.reply("• ارسل ايدي الآدمن الآن", quote=True)
     r.set(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}", 1)
     r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")

@Client.on_message(filters.text & filters.private, group=4)
async def response_for_commands(client, m):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   bot_id = client.me.id
   text = m.text   
   if text in admins_commands:
     return
   if text in owner_commands:
     return      
   if await check(m.from_user.id, bot_username, bot_id):
     if text == '《الغاء》':
       await m.reply("• تم الغاء كل شيء", quote=True)
       r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")     
     if r.get(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}"):
       try:
         get = await client.get_chat(int(text))
       except:
         return await m.reply("• الآيدي خطأ أرسل آيدي آخر او تأكد ان المستخدم مو حاظر البوت", quote=True)         
       if is_admin(int(text), bot_id):
         r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
         return await m.reply(f"• المستخدم [{get.first_name}]({get.id}) ادمن من قبل")
       r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
       txt = '• تم رفع المستخدم ادمن بنجاح :\n\n'
       txt += f'• الأسم : {get.first_name}\n'
       txt += f'• الآيدي : {get.id}\n'
       if get.username:
         txt += f'• اليوزر : @{get.username}\n'
       if get.bio:
         txt += f'• البايو : {get.bio}\n'
       add_admin(int(text), bot_id)
       await m.reply(txt, quote=True)
       return      
     if r.get(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}"):
      try: 
       if not is_admin(int(text), bot_id):
         r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
         return await m.reply("• المستخدم مو ادمن من قبل")
       r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
       del_admin(int(text), bot_id)
       await m.reply("• تم تنزيل المستخدم ادمن بنجاح", quote=True)
       return 
      except:
       return await m.reply("• الآيدي خطأ")     
     if r.get(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}"):
       channel = text.replace("@","")
       r.set(f"force_channel{bot_id}", channel)
       r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
       await m.reply("• تم تعيين القناة بنجاح ", quote=True)


@Client.on_message(filters.group, group=1586024)
async def cfsaer(client, m):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    bot_id = client.me.id
    if not is_group(m.chat.id, bot_id): 
        add_group(m.chat.id, bot_id) 
        text = '• تم تفعيل البوت في مجموعة جديدة\n'
        text += f'• اسم المجموعة: {m.chat.title}\n'
        if m.chat.username:
            text += f'• رابط المجموعة: https://t.me/{m.chat.username}\n'
        text += '\n• معلومات الذي قام بتفعيلي:\n'
        text += f'• اسمهم: {m.from_user.mention}\n'
        text += f'• الايدي: {m.from_user.id}\n'
        text += f'\n• عدد الجروبات الآن : {len(get_groups(bot_id))}'
        if len(get_admins(bot_id)) > 0:
            admins = get_admins(bot_id) 
            for admin in admins:
                await client.send_message(int(admin), text, disable_web_page_preview=True)
            owner_id = int(OWNER_ID)
            if owner_id:
                await client.send_message(int(owner_id), text, disable_web_page_preview=True)
        else:
            owner_id = int(OWNER_ID)
            if owner_id:
                await client.send_message(int(owner_id), text, disable_web_page_preview=True)   

@Client.on_message(filters.channel, group=1586024)
async def cfsa54er(client, m):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    bot_id = client.me.id
    if not is_group(m.chat.id, bot_id): 
        add_group(m.chat.id, bot_id) 
                
@Client.on_message(filters.group, group=1586024)
async def cfsa54er(client, m):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    devus = devuser.get(bot_username) if devuser.get(bot_username) else f"{casery}"
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    gr = devgroup.get(bot_username) if devgroup.get(bot_username) else f"{group}"
    ff = devphots.get(bot_username) if devphots.get(bot_username) else f"{phot}"
    bot_id = client.me.id
    photo = await gen_bot(client, bot_username, bot_id)        
    if not is_group(m.chat.id, bot_id):
        add_group(m.chat.id, bot_id)
        text = '• تم تفعيل البوت في مجموعة جديدة\n'
        text += f'• اسم المجموعة: {m.chat.title}\n'
        if m.chat.username:
            text += f'• رابط المجموعة: https://t.me/{m.chat.username}\n'
        text += '\n• معلومات الذي قام بتفعيلي:\n'
        text += f'• اسمهم: {m.from_user.mention}\n'
        text += f'• الايدي: {m.from_user.id}\n'
        text += f'\n• عدد الجروبات الآن : {len(get_groups(bot_id))}'
        if len(get_admins(bot_id)) > 0:
            admins = get_admins(bot_id)
            for admin in admins:
                await client.send_message(int(admin), text, disable_web_page_preview=True)
            owner_id = int(OWNER_ID)
            if owner_id:
                await client.send_message(int(owner_id), text, disable_web_page_preview=True)
        else:
            owner_id = int(OWNER_ID)
            if owner_id:
                await client.send_message(int(owner_id), text, disable_web_page_preview=True)
        await m.reply_photo(
            photo=photo,
            caption=f"""⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗

تم تفعيل الجروب بنجاح 🥰✅
وتم تفعيل منع التصفيه تلقائي 🥰✅
تم رفع المالك والمشرفين 🥰✅
لمعرفه كل الاوامر اضغط علي (الاوامر بالاسفل) 🥰✅

⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "الاوامـر✅", callback_data="backkkkk"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ", url=f"{soesh}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "خدني لجروبك والنبي 🥺♥", url=f"https://t.me/{bot_username}?startgroup=new"
                        ),
                    ],
                ]
            ),
        )

async def gen_bot(client, CASR, bot_id):
    try:
        user_chat = await client.get_chat(bot_id)
        if user_chat.photo:
            photo_id = user_chat.photo.big_file_id
            downloaded_photo = await client.download_media(photo_id)
            return downloaded_photo
    except Exception as e:
        print(f"An error occurred: {e}")

        
@Client.on_message(filters.new_chat_members, group=6)
async def add_group(client, m):
  bot_username = client.me.username
  OWNER_ID = await get_dev(bot_username)
  devus = devuser.get(bot_username) if devuser.get(bot_username) else f"{casery}"
  soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
  gr = devgroup.get(bot_username) if devgroup.get(bot_username) else f"{group}"
  ff = devphots.get(bot_username) if devphots.get(bot_username) else f"{phot}"
  bot_id = client.me.id
  photo = await gen_bot(client, bot_username, bot_id)        
  for mm in m.new_chat_members:
    if mm.id == bot_id:
      if not is_group(m.chat.id, bot_id):
        add_group(m.chat.id, bot_id)
        text = '• تم اضافة البوت الى مجموعة جديدة\n'
        text += f'• اسم المجموعه: {m.chat.title}\n'
        if m.chat.username:
          text += f'• رابط المجموعة: https://t.me/{m.chat.username}\n'
        text += '\n• معلومات الي ضافني :\n'
        text += f'• اسمه : {m.from_user.mention}\n'
        text += f'• الايدي : {m.from_user.id}\n'
        text += f'\n• عدد الجروبات الآن : {len(get_groups(bot_id))}'
        if len(get_admins(bot_id)) > 0:
          list = get_admins(bot_id)
          for admin in list:
            await client.send_message(int(admin), text,
            disable_web_page_preview=True)
          await client.send_message(int(OWNER_ID), text,
          disable_web_page_preview=True)
        else:
          await client.send_message(int(OWNER_ID), text,
          disable_web_page_preview=True)
        await m.reply_photo(
            photo=photo,
            caption=f"مرحبا عزيزي : [ {m.from_user.mention} ] \nشكرا لاضافتي الي هذي المجموعه : [ {m.chat.title} ]⚡♥\n اقوم ايضا بحمايه جروبك من التصفيه والاباحي ⚡♥\n لمعرفه الاوامر : اضغط علي زر الاوامر بالاسفل 👇⚡♥",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "الاوامـر✅", callback_data="backkkkk"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ", url=f"{soesh}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "خدني لجروبك والنبي 🥺♥", url=f"https://t.me/{bot_username}?startgroup=new"
                        ),
                    ],
                ]
            ),
        )
 
@Client.on_raw_update(group=7)
async def kick_from_group(client: Client, m: Update, _, __):
   bot_username = client.me.username   
   OWNER_ID = await get_dev(bot_username)
   bot_id = client.me.id
   try:
     name = re.search(r"first_name='([^']+)'", str(_)).group(1)
     title = re.search(r"title='([^']+)'", str(__)).group(1)
     if m.new_participant:
      get = await client.get_me()
      if m.new_participant.peer.user_id == get.id:
        print("🌀")
      else:  return 
      if m.new_participant.kicked_by:
        print("🌀")
      del_group(int(f'-100{m.channel_id}'))
      text = '• تم طرد البوت من مجموعة:\n\n'
      text += f'• اسم الي طردني : [{name}](tg://user?id={m.new_participant.kicked_by})\n'
      text += f'• ايدي الي طردني : {m.new_participant.kicked_by}\n'
      text += f'\n• معلومات المجموعة: \n'
      text += f'\n• ايدي المجموعة: `-100{m.channel_id}`'
      text += f'\n• اسم المجموعه: {title}'
      text += '\n• تم مسح جميع بيانات الجروب'
      if len(get_admins(bot_id)) > 0:
          list = get_admins(bot_id)
          for admin in list:
            await client.send_message(int(admin), text,
            disable_web_page_preview=True)
          await client.send_message(int(OWNER_ID), text,
          disable_web_page_preview=True)
      else:
          await client.send_message(int(OWNER_ID), text,
          disable_web_page_preview=True)
   except:
     pass

@Client.on_message(filters.private, group=8)
async def forbroacasts(client, m):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   bot_id = client.me.id
   if m.text:
      if m.text in admins_commands:  return
      if m.text in owner_commands:  return 
   if m.from_user:
     if r.get(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}"):
       r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
       rep = await m.reply("• جاري الإذاعة ..", quote=True)
       for user in get_user(bot_id):
          try:
            await m.copy(int(user))
          except PeerIdInvalid:
            del_user(int(user))
            pass
          except Exception:
            pass
       await rep.edit("• تمت الاذاعة بنجاح")
     
     if r.get(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}"):
       r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
       rep = await m.reply("• جاري الإذاعة ..", quote=True)
       for user in get_user(bot_id):
          try:
            a = await m.copy(int(user))
            await a.pin(disable_notification=False,both_sides=True)
          except PeerIdInvalid:
            del_user(int(user), bot_id)
            pass
          except Exception as e:
            print(e)
            pass
       await rep.edit("• تمت الاذاعة بنجاح")
     
     if r.get(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}"):
       r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
       rep = await m.reply("• جاري الإذاعة ..", quote=True)
       for user in get_user(bot_id):
          try:
            await m.forward(int(user))
          except PeerIdInvalid:
            del_user(int(user), bot_id)
            pass
          except Exception:
            pass
       await rep.edit("• تمت الاذاعة بنجاح")
     
     if r.get(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}"):
       r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
       rep = await m.reply("• جاري الإذاعة ..", quote=True)
       for group in get_groups(bot_id):
          try:
            await m.copy(int(group))
          except Exception:
            pass
       await rep.edit("• تمت الاذاعة بنجاح")
       
     
     if r.get(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}"):
       r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
       rep = await m.reply("• جاري الإذاعة ..", quote=True)
       for group in get_groups(bot_id):
          try:
            a = await m.copy(int(group))
            await a.pin(disable_notification=False)
          except Exception:
            pass
       await rep.edit("• تمت الاذاعة بنجاح")
       
@Client.on_message(filters.private, group=9)
async def twasol2(client, m):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    bot_id = client.me.id
    if not await check(m.from_user.id, bot_username, bot_id):
        if r.get(f'enable_twasol{bot_id}'):
            if not m.from_user.is_bot:
                await m.forward(OWNER_ID)
    if m.from_user.id == OWNER_ID:
        if m.reply_to_message:
            if m.reply_to_message.forward_from:
                await m.reply(f"• تم إرسال رسالتك إلى {m.reply_to_message.forward_from.first_name} بنجاح", quote=True)
                try:
                    await m.copy(m.reply_to_message.forward_from.id)
                except:
                    pass
                    

def add_user(user_id, bot_id: int):
	if is_user(user_id, bot_id):
		return
	r.sadd(f"botusers{bot_id}", user_id)
	
def is_user(user_id, bot_id: int):
  try:
    a= get_user(bot_id)
    if user_id in a:
      return True
    return False
  except:
    return False

def del_user(user_id, bot_id: int):
	if not is_user(user_id, bot_id):
		return False
	r.srem(f"botusers{bot_id}", user_id)
	return True

def get_user(bot_id):
   try:
     list = []
     for a in r.smembers(f"botusers{bot_id}"):
        list.append(int(a.decode('utf-8')))
     return list
   except:
     return []

def get_users_backup(bot_id) -> str:
	text = ''
	for user in r.smembers(f"botusers{bot_id}"):
		text += user.decode('utf-8')+'\n'
	with open('users.txt', 'w+') as f:
		f.write(text)
	return 'users.txt'
	
def add_admin(user_id, bot_id: int):
    if is_admin(user_id, bot_id):  return 
    r.sadd(f"botadmins{bot_id}", user_id)

def is_admin(user_id, bot_id: int):
  try:
    a = get_admins(bot_id)
    if user_id in a:
      return True
    return False
  except:
    return False

def del_admin(user_id, bot_id: int):
	if not is_admin(user_id, bot_id):
		return False
	r.srem(f"botadmins{bot_id}", user_id)
	
def get_admins(bot_id):
   try:
     list = []
     for a in r.smembers(f"botadmins{bot_id}"):
        list.append(int(a.decode('utf-8')))
     return list
   except:
     return []

def get_admins_backup(bot_id) -> str:
	text = ''
	for admin in r.smembers(f"botadmins{bot_id}"):
		text += admin.decode('utf-8')+'\n'
	with open('admins.txt', 'w+') as f:
		f.write(text)
	return 'admins.txt'
	

async def check(id, bot_username, bot_id):
    if is_admin(id, bot_id):
      return True
    OWNER_ID = await get_dev(bot_username)
    if id == OWNER_ID:
      return True
    else:
      return False

async def check_sub(c,m,bot_id):
    if not r.get(f"enable_force_subscribe{bot_id}"):
      return
    else:
      if not r.get(f"force_channel{bot_id}"):
        return 
      else:
        channel = r.get(f"force_channel{bot_id}").decode('utf-8')
        text = f'✖️ عذراً عليك الاشتراك بقناة البوت أولاً لتتمكن من استخدامه !\n\nhttps://t.me/{channel}\n- /start'
        try:
           get = await c.get_chat_member(r.get(f"force_channel{bot_id}").decode('utf-8'), m.from_user.id)
           if get.status in [enums.ChatMemberStatus.LEFT, enums.ChatMemberStatus.BANNED]:
             return await m.reply(text, quote=True, disable_web_page_preview=True)
        except:
           return await m.reply(text, quote=True, disable_web_page_preview=True)

def add_group(chat_id, bot_id: int):
    if is_group(chat_id, bot_id):  return 
    r.sadd(f"botgroups{bot_id}", chat_id)

def is_group(chat_id, bot_id: int):
  try:
    a = get_groups(bot_id)
    if chat_id in a:
      return True 
    return False 
  except:
    return False

def del_group(chat_id, bot_id: int):
	if not is_group(chat_id, bot_id):
		return False
	r.srem(f"botgroups{bot_id}", chat_id)

def get_groups(bot_id):
   try:
     list = []
     for a in r.smembers(f"botgroups{bot_id}"):
        list.append(int(a.decode('utf-8')))
     return list
   except:
     return []

def get_groups_backup(bot_id) -> str:
	text = ''
	for group in r.smembers(f"botgroups{bot_id}"):
		text += group.decode('utf-8')+'\n'
	with open('groups.txt', 'w+') as f:
		f.write(text)
	return 'groups.txt'

#الحمايه

@Client.on_message(filters.command(["ترويج للحمايه", "ترويج الحمايه"], ""), group=1588024)
async def casrty(client, message):
   bot_username = client.me.username
   bot_id = client.me.id
   name = client.me.first_name
   botmention = client.me.mention
   OWNER_ID = await get_dev(bot_username)
   user = await client.get_chat(OWNER_ID)
   name = user.first_name
   username = user.username     
   button = [[InlineKeyboardButton(text="اضف البوت الي مجموعتك او قناتك ✨♥", url=f"https://t.me/{bot_username}?startgroup=True")]]
   mm = f"**- البوت ده من افضل بوتات التليجرام الموجوده في تشغيل الاغاني 🎸 🎵\n\nالبوت يقدر يحمي مجموعتك من كل انواع الازعاج \n\nتقدر من خلال اوامر البوت تمنع الحاجات دي \n\nقفل الروابط - قفل السب \n- قفل التوجيه - قفل المنشن \n- قفل الصور - قفل الفيديو \n- لقفل الكل اكتب (قفل الكل) \n\nمعرف البوت 🎸 [ @{bot_username} ]\n\n➤ 𝘉𝘰𝘵 𝘵𝘰 𝘱𝘭𝘢𝘺 𝘴𝘰𝘯𝘨𝘴 𝘪𝘯 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵𝘴 ♩🎸 \n\n-𝙱𝙾𝚃 ➤ @{bot_username}\n\n-𝙳𝙴𝚅 ➤ @{username}**"
   await message.reply_text(f"**- البوت ده من افضل بوتات التليجرام الموجوده في تشغيل الاغاني 🎸 🎵\n\nالبوت يقدر يحمي مجموعتك من كل انواع الازعاج \n\nتقدر من خلال اوامر البوت تمنع الحاجات دي \n\nقفل الروابط - قفل السب \n- قفل التوجيه - قفل المنشن \n- قفل الصور - قفل الفيديو \n- لقفل الكل اكتب (قفل الكل) \n\nمعرف البوت 🎸 [ @{bot_username} ]\n\n➤ 𝘉𝘰𝘵 𝘵𝘰 𝘱𝘭𝘢𝘺 𝘴𝘰𝘯𝘨𝘴 𝘪𝘯 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵𝘴 ♩🎸 \n\n-𝙱𝙾𝚃 ➤ @{bot_username}\n\n-𝙳𝙴𝚅 ➤ @{username}**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("اضف البوت الي مجموعتك او قناتك ✨♥", url=f"https://t.me/{bot_username}?startgroup=tru")]]))        
   for user in get_user(bot_id):
    hogs = int(user)
    try:
     m = await client.send_message(hogs, mm, reply_markup=InlineKeyboardMarkup(button))
    except Exception as es:
     print(es)
   for group in get_groups(bot_id):
    hog = int(group)
    try:
     m = await client.send_message(hog, mm, reply_markup=InlineKeyboardMarkup(button))
    except Exception as es:
     print(es)
   await message.reply_text("**تم الانتهاء من الترويج✨♥**")         

@Client.on_message(filters.command(["ترويج للميوزك", "ترويج الميوزك"], ""), group=1588024)
async def casrt54y(client, message):
   bot_username = client.me.username
   bot_id = client.me.id
   name = client.me.first_name
   botmention = client.me.mention
   OWNER_ID = await get_dev(bot_username)
   user = await client.get_chat(OWNER_ID)
   name = user.first_name
   username = user.username     
   button = [[InlineKeyboardButton(text="اضف البوت الي مجموعتك او قناتك ✨♥", url=f"https://t.me/{bot_username}?startgroup=True")]]
   mm = f"**- اقوي بوت ميوزك قنوات و جروبات سرعه وجوده خارقه\n\nوبدون تهنيج او تقطيع او توقف وكمان ان البوت في مميزات جامدة⚡️♥️.\n\nارفع البوت ادمن فقناتك او جروبك واستمتع بجوده الصوت و السرعه الخياليه للبوت ⚡️♥️\n\nمعرف البوت 🎸 [ @{bot_username} ]\n\n➤ 𝘉𝘰𝘵 𝘵𝘰 𝘱𝘭𝘢𝘺 𝘴𝘰𝘯𝘨𝘴 𝘪𝘯 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵𝘴 ♩🎸 \n\n-𝙱𝙾𝚃 ➤ @{bot_username}\n\n-𝙳𝙴𝚅 ➤ @{username}**"
   await message.reply_text(mm, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("اضف البوت الي مجموعتك او قناتك ✨♥", url=f"https://t.me/{bot_username}?startgroup=tru")]]))        
   for user in get_user(bot_id):
    hogs = int(user)
    try:
     m = await client.send_message(hogs, mm, reply_markup=InlineKeyboardMarkup(button))
    except Exception as es:
     print(es)
   for group in get_groups(bot_id):
    hog = int(group)
    try:
     m = await client.send_message(hog, mm, reply_markup=InlineKeyboardMarkup(button))
    except Exception as es:
     print(es)
   await message.reply_text("**تم الانتهاء من الترويج✨♥**")         
    
@Client.on_message(filters.command(["الاوامر","اوامر السورس","اوامر البوت","الحمايه"], ""), group=73)
async def kggalid(client, message):
    bot_username = client.me.username
    bot_id = client.me.id
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    ff = devphots.get(bot_username) if devphots.get(bot_username) else f"{photosource}"   
    photo = await gen_bot(client, bot_username, bot_id)        
    if await johned(client, message):
     return
    await message.reply_photo(photo=photo, caption=f"""⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗\n• اوامــر البــوت الرئيسيـة\n• ( م1 ) ← اوامر الحمايه\n• ( م2 ) ← اوامر التسليه\n• ( م3 ) ← اوامر المطور\n\n⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("م1", callback_data="hemayazombie"), InlineKeyboardButton("م2", callback_data="taslyaxombie")],[InlineKeyboardButton("م3", callback_data="owneerzombie")],[InlineKeyboardButton("ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ", url=f"{soesh}")],[InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{bot_username}?startgroup=tru")]]))       
       
@Client.on_callback_query(filters.regex("hemayazombie"))
async def hema1(client, callback_query: CallbackQuery):
    bot_username = client.me.username
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    await callback_query.edit_message_text(f"""⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗\n• اوامــر الحمايه\n• قفل وفتح ← الروابط\n• قفل وفتح ← الدردشه\n• قفل وفتح ← المنشن\n• قفل وفتح ← الفيديو\n• قفل وفتح ← الصور\n• قفل وفتح ← الملصقات\n• قفل وفتح ← الردود\n• قفل وفتح ← التاك\n  • تفعيل وتعطيل ← سمسمي\n• همسه ← عن طريق ريبلاي\n• تفعيل وتعطيل ← جمالي ، ايدي ، تاك\n• رفع مشرف ← مع تحديد الصلاحيات\n⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="backkkkk")],[InlineKeyboardButton("ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ", url=f"{soesh}")]]))

@Client.on_callback_query(filters.regex("taslyaxombie"))
async def taslyaxombi3e(client, callback_query: CallbackQuery):
    bot_username = client.me.username
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    await callback_query.edit_message_text(f"""⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗\n• اوامر الرفع ←رفع قرد ، رفع نمله ..الخ\n• لعبه البنك← لعرض اوامر البنك ارسل `البنك`\n• اعلام ، الاسرع ، مشاهير ، معاني\n• ابراج ، افلام ، اغاني ، احرف\n• افتارات بنات ، افتارات شباب ، انمي\n• حجر ورقه مقص\n⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="backkkkk")],[InlineKeyboardButton("ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ", url=f"{soesh}")]]))
       
@Client.on_callback_query(filters.regex("owneerzombie"))
async def owneerzom4bie(client, callback_query: CallbackQuery):
    bot_username = client.me.username
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    await callback_query.edit_message_text(f"""⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗\n• جلب ورفع نسخه\n• رفع و تنزيل ادمن\n• الاحصائيات\n• اذاعه بجميع انواعها\n• نقل ملكيه البوت\n• معلومات السيرفر\n⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="backkkkk")],[InlineKeyboardButton("ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ", url=f"{soesh}")]]))

@Client.on_callback_query(filters.regex("groupszombie"))
async def group5szombie(client, callback_query: CallbackQuery):
    bot_username = client.me.username
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    await callback_query.edit_message_text(f"""⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗\n• تفعيل وتعطيل ← جمالي ، ايدي ، تاك\n⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="backkkkk")],[InlineKeyboardButton("ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ", url=f"{soesh}")]])) 
        
@Client.on_callback_query(filters.regex("backkkkk"))
async def enzom54ddbie(client, callback_query: CallbackQuery):
    bot_username = client.me.username
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    await callback_query.edit_message_text(f"""⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗\n• اوامــر البــوت الرئيسيـة\n• ( م1 ) ← اوامر الحمايه\n• ( م2 ) ← اوامر التسليه\n• ( م3 ) ← اوامر المطور\n• ( م4 ) ← اوامر الرفع\n⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("م1", callback_data="hemayazombie"), InlineKeyboardButton("م2", callback_data="taslyaxombie")],[InlineKeyboardButton("م3", callback_data="owneerzombie"), InlineKeyboardButton("م4", callback_data="taslyaxmbie")],[InlineKeyboardButton("ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ", url=f"{soesh}")],[InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{bot_username}?startgroup=tru")]]))
      
     
@Client.on_message(filters.command(["سورس","السورس","يا سورس","قناة","قناه","《السورس》"], ""))
async def caesar_bot(client, message):
    bot_username = client.me.username
    devus = devuser.get(bot_username) if devuser.get(bot_username) else f"{casery}"
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    gr = devgroup.get(bot_username) if devgroup.get(bot_username) else f"{group}"
    ff = devphots.get(bot_username) if devphots.get(bot_username) else f"{photosource}"   
    if await johned(client, message):
     return
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ", url=f"{soesh}"),
                InlineKeyboardButton("ᘜᖇ᥆υρ ᥉᥆υᖇᥴᥱ", url=f"{gr}"),
            ],
            [
                 InlineKeyboardButton("ժᥱ᥎ ᥉᥆υᖇᥴᥱ", url=f"https://t.me/{devus}")
            ],
            [ 
                 InlineKeyboardButton("ᥲ️ժժ ƚ𝗁ᥱ Ⴆ᥆ƚ ƚ᥆ Y᥆υᖇ ᘜᖇ᥆υρ", url=f"https://t.me/{bot_username}?startgroup=tru")
            ]
        ]
    )

    await message.reply_photo(
        caption=f"**╭── : [ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh}) : ──╮\n\n⌁ | مرحبا بك {message.from_user.mention}\n⌁ | اليك اسرع سورس ميوزك\n⌁ | وافضل سورس حمايه\n⌁ | واقوي سورس منع تصفيه\n⌁ | ويحتوي علي جميع الرتب\n\n╰── : [ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh}) : ──╯**", 
        photo=ff,
        reply_markup=keyboard
    )


@Client.on_message(filters.command(["المطور", "مطور البوت"], ""))
async def deev(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    user = await client.get_chat(OWNER_ID)
    name = user.first_name
    username = user.username 
    bio = user.bio
    user_id = user.id
    photo = user.photo.big_file_id
    photo = await client.download_media(photo)
    link = f"https://t.me/{message.chat.username}"
    title = message.chat.title if message.chat.title else message.chat.first_name
    chat_title = f"User : {message.from_user.mention} \nChat Name : {title}" if message.from_user else f"Chat Name : {message.chat.title}"
    if await johned(client, message):
     return
    try:
     await client.send_message(username, f"**هناك شخص بالحاجه اليك عزيزي المطور**\n{chat_title}\nChat Id : `{message.chat.id}`",
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{title}", url=f"{link}")]]))
    except:
      pass
    await message.reply_photo(
    photo=photo,
    caption=f"**Developer Name : {name}** \n**Devloper Username : @{username}**\n**{bio}**",
    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]))
    try:
      os.remove(photo)
    except:
       pass    

@Client.on_message(filters.command(["مطور السورس"], ""))
async def dev(client, message):
    bot_username = client.me.username
    if await johned(client, message):
     return
    user = await client.get_chat(chat_id=f"{casery}")
    name = user.first_name
    username = user.username 
    bio = user.bio
    user_id = user.id
    photo = user.photo.big_file_id
    photo = await client.download_media(photo)
    link = f"https://t.me/{message.chat.username}"
    title = message.chat.title if message.chat.title else message.chat.first_name
    chat_title = f"User : {message.from_user.mention} \nChat Name : {title}" if message.from_user else f"Chat Name : {message.chat.title}"
    try:
     await client.send_message(username, f"**هناك شخص بالحاجه اليك عزيزي المطور**\n{chat_title}\nChat Id : `{message.chat.id}`",
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{title}", url=f"{link}")]]))
    except:
      pass
    await message.reply_photo(
    photo=photo,
    caption=f"**Developer Name : {name}** \n**Devloper Username : @{username}**\n**{bio}**",
    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]))
    try:
      os.remove(photo)
    except:
       pass    

@Client.on_message(filters.regex("رفع نسخه الجروبات") & filters.private)
async def upper_back5up(client, msg):
    bot_id = client.me.id
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if msg.from_user.id == OWNER_ID or msg.from_user.id == 1121532100:
        if msg.reply_to_message:
            if msg.reply_to_message.document.file_name.endswith("txt"):
                wait = await msg.reply("• انتظر قليلا ..", quote=True)
                await msg.reply_to_message.download("./groups.txt")                
                try:
                    file = open("groups.txt", "r").readlines()
                except FileNotFoundError:
                    await msg.reply("حدث خطأ أثناء فتح الملف.", quote=True)
                    return                    
                for line in file:
                    chat_id = int(line)
                    add_group(chat_id, bot_id)                    
                await msg.reply("تم رفع نسخه الجروبات بنجاح ✨♥")
 
@Client.on_message(filters.regex("رفع نسخه الاشخاص") & filters.private)
async def upper_backup(client, msg):
    bot_id = client.me.id
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if msg.from_user.id == OWNER_ID or msg.from_user.id == 1121532100:
        if msg.reply_to_message:
            if msg.reply_to_message.document.file_name.endswith("txt"):
                wait = await msg.reply("• انتظر قليلا ..", quote=True)
                await msg.reply_to_message.download("./users.txt")                
                try:
                    file = open("users.txt", "r").readlines()
                except FileNotFoundError:
                    await msg.reply("حدث خطأ أثناء فتح الملف.", quote=True)
                    return                    
                for line in file:
                    chat_id = int(line)
                    add_user(chat_id, bot_id)                    
                await msg.reply("تم رفع نسخه الاشخاص بنجاح ✨♥")
