# Copyright (C) 2019 The Raphielscape Company LLC.
# Dyor
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import asyncio
import random
import time
from datetime import datetime

import redis
from speedtest import Speedtest

from userbot import ALIVE_NAME, CMD_HELP, StartTime, REPO_NAME
from userbot.events import register

sayang = [
    "**Hallo dior sayang** 😍",
    "**Eh ada bang dior** 😁",
    "**Hallo kak dior** 😉",
    "**Eh sayang, apa kabar ayang dior** 😘",
    "**Hai ganteng** 🥵",
    "**Hadir bro** 😎",
    "**Sayang kangen** 🥺",
]


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 50
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(incoming=True, from_users=1937084611, pattern=r"^.sayang$")
async def _(dior):
    await dior.reply(random.choice(sayang))


@register(outgoing=True, pattern="^.ping$")
@register(incoming=True, from_users=1937084611, pattern=r"^\.cping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**Assalamualaikum...Yesus memberkati...**")
    await asyncio.sleep(2)
    await pong.edit("✣")
    await pong.edit("✣✣")
    await pong.edit("✣✣✣")
    await pong.edit("✣✣✣✣")
    await pong.edit("**YO NGENTOOOT!**")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**PING!!!🍀**\n"
                    f"✣ **Pinger** - `%sms`\n"
                    f"✣ **Uptime** - `{uptime}` \n"
                    f"**✦҈͜͡Owner :** {ALIVE_NAME}"
    )


@register(outgoing=True, pattern="^Ping$")
@register(incoming=True, from_users=1937084611, pattern=r"^\.cpi$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("Connecting.")
    await pong.edit("Connecting..")
    await pong.edit("Connecting...")
    await pong.edit("Connecting....")
    await pong.edit("Connecting.")
    await pong.edit("Connecting..")
    await pong.edit("Connecting...")
    await pong.edit("Connecting....")
    await pong.edit("Connecting.")
    await pong.edit("Connecting..")
    await pong.edit("Connecting...")
    await pong.edit("Connecting....")
    await pong.edit("Connecting.....")
    await pong.edit("Connected ✅")
    await asyncio.sleep(2)
    await pong.edit(f"⚡")
    await asyncio.sleep(3)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"{REPO_NAME}!!\n"
                    f"**✦҈͜͡Owner :** {ALIVE_NAME}\n"
                    f"**✦҈͜͡Uptime :**`{uptime}` \n"
                    f"**✦҈͜͡Duration :** % (duration)")


@register(outgoing=True, pattern="^.speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Menjalankan Tes Kecepatan Jaringan...`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("**Kecepatan Jaringan:\n**"
                   "✧ **Dimulai Pada :** "
                   f"`{result['timestamp']}` \n"
                   f" **━━━━━━━━━━━━━━━━━**\n\n"
                   "✧ **Download:** "
                   f"`{speed_convert(result['download'])}` \n"
                   "✧ **Upload:** "
                   f"`{speed_convert(result['upload'])}` \n"
                   "✧ **Signal:** "
                   f"`{result['ping']}` \n"
                   "✧ **ISP:** "
                   f"`{result['client']['isp']}` \n"
                   f"✧ **BOT:** {REPO_NAME}")


def speed_convert(size):
    """
    Hai manusia, kamu tidak bisa membaca byte?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^.pong$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("Ping")
    await asyncio.sleep(1)
    await pong.edit("Pong")
    await asyncio.sleep(1)
    await pong.edit("Pler")
    await asyncio.sleep(1)
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit(f"**✦҈͜͡Owner** : {ALIVE_NAME}\n`%sms`" % (duration))


CMD_HELP.update({
    "ping": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ping` or `.pings`\
         \n↳ : Untuk Menunjukkan Ping Bot Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.speed`\
         \n↳ : Untuk Menunjukkan Kecepatan Jaringan Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.pong`\
         \n↳ : Sama Seperti Perintah Ping."})
