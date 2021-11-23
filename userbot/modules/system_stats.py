# System Stats DIOR-UBOT

import asyncio
from asyncio import create_subprocess_exec as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from platform import python_version, uname
from shutil import which
from os import remove
from telethon import version
from telethon import __version__, version
import platform
import sys
import time
from datetime import datetime
import psutil

from userbot import ALIVE_LOGO, ALIVE_NAME, BOT_VER, CMD_HELP, RAM_TEKS_KOSTUM, IG_ALIVE, REPO_NAME, GROUP_LINK, StartTime, bot
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


modules = CMD_HELP


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
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


@register(outgoing=True, pattern=r"^\.spc")
async def psu(event):
    uname = platform.uname()
    softw = "**Informasi Sistem**\n"
    softw += f"`Sistem   : {uname.system}`\n"
    softw += f"`Rilis    : {uname.release}`\n"
    softw += f"`Versi    : {uname.version}`\n"
    softw += f"`Mesin    : {uname.machine}`\n"
    # Boot Time
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    softw += f"`Waktu Hidup: {bt.day}/{bt.month}/{bt.year}  {bt.hour}:{bt.minute}:{bt.second}`\n"
    # CPU Cores
    cpuu = "**Informasi CPU**\n"
    cpuu += "`Physical cores   : " + \
        str(psutil.cpu_count(logical=False)) + "`\n"
    cpuu += "`Total cores      : " + \
        str(psutil.cpu_count(logical=True)) + "`\n"
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    cpuu += f"`Max Frequency    : {cpufreq.max:.2f}Mhz`\n"
    cpuu += f"`Min Frequency    : {cpufreq.min:.2f}Mhz`\n"
    cpuu += f"`Current Frequency: {cpufreq.current:.2f}Mhz`\n\n"
    # CPU usage
    cpuu += "**CPU Usage Per Core**\n"
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        cpuu += f"`Core {i}  : {percentage}%`\n"
    cpuu += "**Total CPU Usage**\n"
    cpuu += f"`Semua Core: {psutil.cpu_percent()}%`\n"
    # RAM Usage
    svmem = psutil.virtual_memory()
    memm = "**Memori Digunakan**\n"
    memm += f"`Total     : {get_size(svmem.total)}`\n"
    memm += f"`Available : {get_size(svmem.available)}`\n"
    memm += f"`Used      : {get_size(svmem.used)}`\n"
    memm += f"`Percentage: {svmem.percent}%`\n"
    # Bandwidth Usage
    bw = "**Bandwith Digunakan**\n"
    bw += f"`Unggah  : {get_size(psutil.net_io_counters().bytes_sent)}`\n"
    bw += f"`Download: {get_size(psutil.net_io_counters().bytes_recv)}`\n"
    help_string = f"{str(softw)}\n"
    help_string += f"{str(cpuu)}\n"
    help_string += f"{str(memm)}\n"
    help_string += f"{str(bw)}\n"
    help_string += "**Informasi Mesin**\n"
    help_string += f"`Python {sys.version}`\n"
    help_string += f"`Telethon {__version__}`"
    await event.edit(help_string)


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


@register(outgoing=True, pattern=r"^\.sysd$")
async def sysdetails(sysd):
    if not sysd.text[0].isalpha() and sysd.text[0] not in ("/", "#", "@", "!"):
        try:
            fetch = await asyncrunapp(
                "neofetch",
                "--stdout",
                stdout=asyncPIPE,
                stderr=asyncPIPE,
            )

            stdout, stderr = await fetch.communicate()
            result = str(stdout.decode().strip()) + \
                str(stderr.decode().strip())

            await sysd.edit("`" + result + "`")
        except FileNotFoundError:
            await sysd.edit("`Install neofetch first !!`")


@register(outgoing=True, pattern=r"^\.botver$")
async def bot_ver(event):
    if event.text[0].isalpha() or event.text[0] in ("/", "#", "@", "!"):
        return
    if which("git") is not None:
        ver = await asyncrunapp(
            "git",
            "describe",
            "--all",
            "--long",
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )
        stdout, stderr = await ver.communicate()
        verout = str(stdout.decode().strip()) + str(stderr.decode().strip())

        await event.edit(
            "✥ **Userbot Versi :** " f"`{verout}`" "\n✥ **Revisi :** " f"`{revout}`",
        )
    else:
        await event.edit(
            "Sayang sekali Anda tidak memiliki git, Anda menjalankan bot - 'v1.beta.4' anyway!"
        )


@register(outgoing=True, pattern=r"^\.pip(?: |$)(.*)")
async def pipcheck(pip):
    if pip.text[0].isalpha() or pip.text[0] in ("/", "#", "@", "!"):
        return
    pipmodule = pip.pattern_match.group(1)
    if pipmodule:
        await pip.edit("`Mencari...`")
        pipc = await asyncrunapp(
            "pip3",
            "search",
            pipmodule,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )

        stdout, stderr = await pipc.communicate()
        pipout = str(stdout.decode().strip()) + str(stderr.decode().strip())

        if pipout:
            if len(pipout) > 4096:
                await pip.edit("`Output Terlalu Besar, Dikirim Sebagai File`")
                file = open("output.txt", "w+")
                file.write(pipout)
                file.close()
                await pip.client.send_file(
                    pip.chat_id,
                    "output.txt",
                    reply_to=pip.id,
                )
                remove("output.txt")
                return
            await pip.edit(
                "**Query: **\n`"
                f"pip3 search {pipmodule}"
                "`\n**Result: **\n`"
                f"{pipout}"
                "`"
            )
        else:
            await pip.edit(
                "**Query: **\n`"
                f"pip3 search {pipmodule}"
                "`\n**Result: **\n`No Result Returned/False`"
            )
    else:
        await pip.edit("Gunakan `.help pip` Untuk Melihat Contoh")


@register(outgoing=True, pattern=r"^\.(?:alive|on)\s?(.)?")
async def amireallyalive(alive):
    user = await bot.get_me()
    await get_readable_time((time.time() - StartTime))
    await alive.edit("__Reconnect.__")
    await alive.edit("__Reconnect..__")
    await alive.edit("__Reconnect.__")
    await alive.edit("__Reconnect..__")
    await alive.edit("__Connecting...__")
    await alive.edit("__Connecting..__")
    await alive.edit("__Connecting...__")
    await alive.edit("⚡")
    await asyncio.sleep(3)
    output = (
        f"**[DIOR-UBOT](https://github.com/DIORrios285/DIOR-UBOT) is Up and Running.**\n\n"
        f"⚡ **Master :** {DEFAULTUSER} \n"
        f"⚡ **Modules :** `{len(modules)} Modules` \n"
        f"⚡ **Bot Version :** `{BOT_VER}` \n"
        f"⚡ **Python Version :** `{python_version()}` \n"
        f"⚡ **Telethon Version :** `{version.__version__}` \n\n"
        f"    **[𝗦𝘂𝗽𝗽𝗼𝗿𝘁](https://t.me/fandasupport)** | **[𝗖𝗵𝗮𝗻𝗻𝗲𝗹](https://t.me/diorplayingwords)** | **[𝗢𝘄𝗻𝗲𝗿](https://t.me/uurfavboys1)**"
    )
    if ALIVE_LOGO:
        try:
            logo = ALIVE_LOGO
            await alive.delete()
            msg = await bot.send_file(alive.chat_id, logo, caption=output)
            await asyncio.sleep(50)
            await msg.delete()
        except BaseException:
            await alive.edit(
                output + "\n\n *`Logo Yang Disediakan Tidak Valid."
                "\nPastikan Tautan Yang Anda Gunakan Valid`"
            )
            await asyncio.sleep(100)
            await alive.delete()
    else:
        await alive.edit(output)
        await asyncio.sleep(100)
        await alive.delete()


@register(outgoing=True, pattern=r"^\.(?:ralive)\s?(.)?")
async def amireallyalive(alive):
    user = await bot.get_me()
    await get_readable_time((time.time() - StartTime))
    output = (
        f"**ㅤㅤ     ⚡FANDA - PROJECT⚡** \n"
        f"╔═════════╬════╬═════════╗ \n"
        f"• `ᴏᴡɴᴇʀ    :`[DIOR](t.me/uurfavboys1)    \n"
        f"• `ꜱʏꜱᴛᴇᴍ   :`Android 10   \n"
        f"• `ᴛᴇʟᴇᴛʜᴏɴ  :`v.{version.__version__}   \n"
        f"• `ᴘʏᴛʜᴏɴ   :`v.{python_version()} ㅤ\n"
        f"• `ʙᴏᴛ      :`v.{BOT_VER}           \n"
        f"• `ᴍᴏᴅᴜʟᴇ   :`{len(modules)} ㅤ\n\n"
                  f"[𝗥𝗘𝗣𝗢](https://github.com/DIORrios285/DIOR-UBOT) **|** [𝗦𝗨𝗣𝗣𝗢𝗥𝗧](t.me/fandasupport) **|** [𝗢𝗪𝗡𝗘𝗥](t.me/uurfavboys1)"
    )
    if ALIVE_LOGO:
        try:
            logo = ALIVE_LOGO
            await alive.delete()
            msg = await bot.send_file(alive.chat_id, logo, caption=output)
            await asyncio.sleep(50)
            await msg.delete()
        except BaseException:
            await alive.edit(
                output + "\n\n *`Logo yang diberikan tidak valid."
                "\nPastikan link diarahkan ke gambar logo`"
            )
            await asyncio.sleep(100)
            await alive.delete()
    else:
        await alive.edit(output)
        await asyncio.sleep(100)
        await alive.delete()



@register(outgoing=True, pattern=r"^\.aliveu")
async def amireallyaliveuser(username):
    message = username.text
    output = ".aliveu [new user without brackets] nor can it be empty"
    if message != ".aliveu" and message[7:8] == " ":
        newuser = message[8:]
        global DEFAULTUSER
        DEFAULTUSER = newuser
        output = "Berhasil mengubah pengguna menjadi " + newuser + "!"
    await username.edit("`" f"{output}" "`")


@register(outgoing=True, pattern=r"^\.resetalive$")
async def amireallyalivereset(ureset):
    global DEFAULTUSER
    DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
    await ureset.edit("`" "Berhasil mengatur ulang pengguna untuk hidup!" "`")


CMD_HELP.update({
    "sistem":
    "`.sysd`\
\nUsage: Menampilkan informasi sistem menggunakan neofetch.\
\n\n`.alive|.on`\
\nUsage: Menunjukkan alive bot.\
\n\n`.ralive`\
\nUsage: Menampilkan alive repo.\
\n\n`.botver`\
\nUsage: Menunjukkan versi userbot.\
\n\n`.pip` <module(s)>\
\nUsage: Melakukan pencarian modul pip(s).\
\n\n`.start`\
\nUsage: Ketik .start untuk melihat apakah bot Anda berfungsi atau tidak.\
\n\n`.aliveu` <text>\
\nUsage: Changes the 'user' in alive to the text you want.\
\n\n`.resetalive`\
\nUsage: Resets the user to default.\
\n\n`.db`\
\nUsage:Shows database related info.\
\n\n.`.spc`\
\nUsage:Show system specification."
})
