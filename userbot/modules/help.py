# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import asyncio
from userbot import ALIVE_NAME, CMD_HELP, REPO_NAME, EMOJI_HELP
from userbot.events import register
from platform import uname

modules = CMD_HELP

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(diorbot):
    """ For .help command,"""
    args = diorbot.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await diorbot.edit(str(CMD_HELP[args]))
        else:
            await diorbot.edit("**NGETIK APAANSI KONTOL!**")
            await asyncio.sleep(30)
            await diorbot.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += f"`\t {EMOJI_HELP}  "
        await diorbot.edit(f"**Daftar Bantuan dari {REPO_NAME}**\n\n"
                         f"➩ **ᴏᴡɴᴇʀ ʙᴏᴛ :** {DEFAULTUSER}\n"
                         f"➩ **ᴍᴏᴅᴜʟᴇs :** {len(modules)}\n\n"
                         f"**PLUGINS:**\n"
                         f"{EMOJI_HELP} {string}\n\n\n"
                         f"⚡ __Powered by **Fanda Project**__")
        await diorbot.reply(f"\n**Contoh** : Ketik ⟨`.help roasting`⟩ Untuk Informasi Pengunaan.")
        await asyncio.sleep(120)
        await diorbot.delete()
