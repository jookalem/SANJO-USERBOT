from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.f(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Hai Perkenalkan Namaku Fatur`")
    sleep(3)
    await typew.edit("16 Tahun`")
    sleep(1)
    await typew.edit("`Tinggal Di Kalimantan, Salam Kenal ya:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.manda(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Manda itu cantik`")
    sleep(3)
    await typew.edit("`Manda punya fatur...lu ganggu disambit pala lu!`")
    sleep(1)
    await typew.edit("`pada intinya fatur sayang banget sama manda`")
    sleep(1)
    await typew.edit("`I LOVE YOU MANDA💝💕`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bersemangat`")
    sleep(3)
    await typew.edit("`Jangan Bersedih`")
    sleep(1)
    await typew.edit("`NAFAS MANUALNYA KAKA...HAHAHA MAMPUS LO!`")
# Create by myself @localheart
