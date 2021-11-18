# kumpulin kosakata makanya bgst
# mks smsm

from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.puki(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`y`")
# dior cakep!
