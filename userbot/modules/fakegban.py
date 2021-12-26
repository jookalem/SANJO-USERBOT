# This is a troll indeed ffs *facepalm*
# Ported from xtra-telegram by @heyworld
import asyncio
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins
#from userbot.utils import admin_cmd
from userbot.events import register
from userbot import ALIVE_NAME, CMD_HELP, DEVS, bot

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.fgban(?: |$)(.*)")
@register(incoming=True, from_users=DEVS, pattern=r"^\.cfgban(?: |$)(.*)")
async def gbun(event):
    if event.fwd_from:
        return
    gbunVar = event.text
    gbunVar = gbunVar[6:]
    mentions = f"`Warning!! User 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By` {DEFAULTUSER}\n"
    no_reason = "No Reason Given "
    await event.edit("**Memanggil palu gban yang perkasa ☠️**")
    asyncio.sleep(3.5)
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.from_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.from_id
        # make meself invulnerable cuz why not xD
        if idd == 1220829364:
            await reply_message.reply("`Tunggu sebentar, Ini tuanku!`\n**Beraninya kau mengancam untuk melarang tuan fatur ku yang tampan!**\n\n__Akun Anda telah diretas! Bayar $6969 ke tuan saya__ [Heyworld](tg://user?id=1937084611) __untuk melepaskan akun Anda__😏")
        else:
            jnl = ("`Warning!!`"
                   "[{}](tg://user?id={})"
                   f"` 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 oleh` {DEFAULTUSER}\n\n"
                   "**Name: ** __{}__\n"
                   "**ID : ** `{}`\n"
                   ).format(firstname, idd, firstname, idd)
            if usname is None:
                jnl += "**Username: ** `Ga ada usernamenya fiks jamet!`\n"
            elif usname != "None":
                jnl += "**Username** : @{}\n".format(usname)
            if len(gbunVar) > 0:
                gbunm = "`{}`".format(gbunVar)
                gbunr = "**Reason: **" + gbunm
                jnl += gbunr
            else:
                jnl += no_reason
            await reply_message.reply(jnl)
    else:
        mention = (
            f"Warning!! Pengguna 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 Oleh {DEFAULTUSER} \nReason: Kosong kek hati. ")
        await event.reply(mention)
    await event.delete()


CMD_HELP.update(
    {
        "faction": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.fgban`"
        "\n• : .fgban atau Balas alasan .fgban dan lihat sendiri"
    }
)
