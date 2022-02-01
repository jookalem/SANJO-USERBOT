# @greyyvbss

from time import sleep
from userbot import ALIVE_NAME, CMD_HELP, IG_ALIVE, REPO_NAME, GROUP_LINK, bot
from userbot.events import register
from telethon import events


@register(outgoing=True, pattern='^.thanks(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("●▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬●\n"
                     "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄\n"
                     "╔══╦╗────╔╗─╔╗╔╗\n"
                     "╚╗╔╣╚╦═╦═╣╚╗║╚╝╠═╦╦╗\n"
                     "─║║║║║╬║║║╩║╚╗╔╣║║║║\n"
                     "─╚╝╚╩╩╩╩╩╩╩╝─╚╝╚═╩═╝\n"
                     "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄\n"
                     "●▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬●")


@register(outgoing=True, pattern='^.malam(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("╔═╦═╦╗╔═╦══╦═╦══╗\n"
                     "║═╣═╣║║╬║║║║╬╠╗╔╝\n"
                     "╠═║═╣╚╣║║║║║║║║║\n"
                     "╚═╩═╩═╩╩╩╩╩╩╩╝╚╝\n\n"
                     "╔══╦═╦╗╔═╦══╗\n"
                     "║║║║╬║║║╬║║║║\n"
                     "║║║║║║╚╣║║║║║\n"
                     "╚╩╩╩╩╩═╩╩╩╩╩╝")


@register(outgoing=True, pattern='^.rumah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAMBAR RUMAH**\n"
                     "╱◥◣\n"
                     "│∩ │◥███◣ ╱◥███◣\n"
                     "╱◥◣ ◥████◣▓∩▓│∩ ║\n"
                     "│╱◥█◣║∩∩∩ ║◥█▓ ▓█◣\n"
                     "││∩│ ▓ ║∩田│║▓ ▓ ▓∩ ║\n"
                     "๑۩๑๑۩๑๑ ۩๑๑۩๑▓๑۩๑๑۩๑")


@register(outgoing=True, pattern='^.join(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("_/﹋\\_\n"
                     "(҂`_´)\n"
                     "<,︻╦╤─ ҉\n"
                     r"_/﹋\_"
                     "\n**ᴊᴏɪɴ ʟɪɴᴋ ᴅɪ ʙɪᴏ😡**")
    
    
@register(outgoing=True, pattern='^.lari(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("──▄█▀█▄─────────██\n"
                     "▄████████▄───▄▀█▄▄▄▄\n"
                     "██▀▼▼▼▼▼─▄▀──█▄▄\n"
                     "█████▄▲▲▲─▄▄▄▀───▀▄\n"
                     "██████▀▀▀▀─▀────────▀▀\n"
                     " **LARI IPINN**\n")
    
    
@register(outgoing=True, pattern='^.mobil(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("──────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▌\n"
                     "───▄▄██▌█░░░░░░░░░░░░▐\n"
                     "▄▄▄▌▐██▌█░░░░░░░░░░░░▐\n"
                     "███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▌\n"
                     "▀❍▀▀▀▀▀▀▀❍❍▀▀▀▀▀▀❍❍▀\n")
    
    
CMD_HELP.update({
    "animasi2":
    ".thanks\
\nUsage: Thank You.\
    \n\n.malam\
\nUsage: Selamat Malam.\
    \n\n.rumah\
\nUsage: Gambar Rumah.\
    \n\n.join\
\nUsage: Join Link Di Bio.\
    \n\n.lari\
\nUsage: Lari Ipin.\
    \n\n.mobil\
\nUsage: Gambar Mobil."

})    
