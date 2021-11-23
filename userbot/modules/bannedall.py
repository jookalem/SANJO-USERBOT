# Dior nyoba kak

from telethon.tl.types import (
    ChannelParticipantsKicked,
)

from asyncio import sleep
from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest
from userbot.events import register
from userbot import CMD_HELP

@register(outgoing=True, pattern="^.bannedall(?: |$)(.*)")
async def testing(event):
    nikal = await event.get_chat()
    chutiya = await event.client.get_me()
    admin = nikal.admin_rights
    creator = nikal.creator
    if not admin and not creator:
        await event.edit("Lu bukan admin, NGENTOOOOTTTTTT!!")
        return
    await event.edit("Tidak Melakukan Apa-apa")
# Thank for Dark_Cobra
    everyone = await event.client.get_participants(event.chat_id)
    for user in everyone:
        if user.id == chutiya.id:
            pass
        try:
            await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None, view_messages=True)))
        except Exception as e:
            await event.edit(str(e))
        await sleep(.5)
    await event.edit("Tidak Ada yang Terjadi di sini🙃🙂")


@register(outgoing=True, pattern=r"^\.unbanall(?: |$)(.*)", groups_only=True)
async def _(event):
    await event.edit("`Sedang Mencari List Banning.`")
    p = 0
    (await event.get_chat()).title
    async for i in event.client.iter_participants(
        event.chat_id,
        filter=ChannelParticipantsKicked,
        aggressive=True,
    ):
        try:
            await event.client.edit_permissions(event.chat_id, i, view_messages=True)
            p += 1
        except BaseException:
            pass
    await event.edit("`Sukses Menghapus List Banning`")

CMD_HELP.update(
    {
        "bannedall": "**Plugin : **`cukup`\
    \n\n**Syntax : **`.bannedall`\
    \n**usage : **ban all members in 1 cmd\
    \n\n**Syntax : **`.unbanall`\
    \n**Usage : **unbanned semua member yang di ban dalam grup"
    }
)
