# Jir keapus, lupa apa aja tulisannya :v

from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import EditGroupCallTitleRequest as settitle
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from telethon.tl.types import ChatAdminRights
from userbot import CMD_HELP
from userbot.events import register

NO_ADMIN = "`LU BUKAN ADMIN NGENTOT!!`"


async def get_call(event):
    diorbot = await event.client(getchat(event.chat_id))
    dior = await event.client(getvc(diorbot.full_chat.call))
    return dior.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i: i + n]


@register(outgoing=True, pattern=r"^\.startvc$", groups_only=True)
async def _(diorbot):
    chat = await diorbot.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        return await diorbot.edit(NO_ADMIN)
    new_rights = ChatAdminRights(invite_users=True)
    try:
        await diorbot.client(startvc(diorbot.chat_id))
        await diorbot.edit("`OBROLAN SUARA DIMULAI, GOSAH ONCAM MUKA LO JELEK...`")
    except Exception as ex:
        await diorbot.edit(f"`{str(ex)}`")


@register(outgoing=True, pattern=r"^\.stopvc$", groups_only=True)
async def _(diorbot):
    chat = await diorbot.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        return await diorbot.edit(NO_ADMIN)
    new_rights = ChatAdminRights(invite_users=True)
    try:
        await diorbot.client(stopvc(await get_call(diorbot)))
        await diorbot.edit("`OBROLAN SUARA DIMATIIN, TYPING AJA NGENTOT SUARA LU CEMPRENG...`")
    except Exception as ex:
        await diorbot.edit(f"`{str(ex)}`")


@register(outgoing=True, pattern=r"^\.vcinvite", groups_only=True)
async def _(diorbot):
    await diorbot.edit("`Memulai Invite member group...`")
    users = []
    z = 0
    async for x in diorbot.client.iter_participants(diorbot.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await diorbot.client(invitetovc(call=await get_call(diorbot), users=p))
            z += 6
        except BaseException:
            pass
    await diorbot.edit(f"`Menginvite {z} Member`")




@register(outgoing=True, pattern=r"^\.vctitle", groups_only=True)
async def _(diorbot):
    title = e.pattern_match.group(1)
    chat = await diorbot.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not title:
        return await diorbot.edit("**Silahkan Masukan Title Obrolan Suara Grup**")

    if not admin and not creator:
        return await diorbot.edit(f"**Maaf {ALIVE_NAME} Bukan Admin 👮**")
    try:
        await diorbot.edit(settitle(call=await get_call(e), title=title.strip()))
        await diorbot.edit( f"**Berhasil Mengubah Judul VCG Menjadi** `{title}`")
    except Exception as ex:
        await diorbot.edit(f"**ERROR:** `{ex}`")




CMD_HELP.update(
    {
        "vcg": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.startvc`\
         \n↳ : Memulai Obrolan Suara dalam Group.\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.stopvc`\
         \n↳ : `Menghentikan Obrolan Suara Pada Group.`\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vctitle`\
         \n↳ : `Untuk Mengubah title/judul voice chat group.`\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vcinvite`\
         \n↳ : Invite semua member yang berada di group. (Kadang bisa kadang kaga)."
    }
)
