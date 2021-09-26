# Gausah kesini ngentot!!
# NGEDIT CMD YG BENER KONTOL!!!


from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================

@register(outgoing=True, pattern='^.p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`𝐀𝐒𝐒𝐀𝐋𝐀𝐌𝐔𝐀𝐋𝐀𝐈𝐊𝐔𝐌 𝐀𝐍𝐀𝐊 𝐇𝐀𝐑𝐀𝐌!!`")


@register(outgoing=True, pattern='^.gdjm(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GA DULU JANGAN MAKSA**")


@register(outgoing=True, pattern='^.l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`𝐖𝐀𝐀𝐋𝐀𝐈𝐊𝐔𝐌𝐒𝐀𝐋𝐋𝐀𝐌 𝐉𝐄𝐋𝐄𝐊!!...`")


@register(outgoing=True, pattern='^.gjlg(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GA JELAS LU GOBLOK!!**")


@register(outgoing=True, pattern='^.yb(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Y BANG.**")


@register(outgoing=True, pattern='^.m(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MEKI MAK LU MASIH RAPET GA TUH?**")


@register(outgoing=True, pattern='^.k(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**KONTOL...PE HAH?**")


@register(outgoing=True, pattern='^.gdb(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GA DANTA BUSEHH....**")


@register(outgoing=True, pattern='^.gblk(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAJE BAT LU KONTOL....**")


@register(outgoing=True, pattern='^.kljs(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**KOK LU JELEK SIH?**")


@register(outgoing=True, pattern='^.gls(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GA, LU SANGEAN..**")


@register(outgoing=True, pattern='^.bsl(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BAU SAWI LU..!!**")


@register(outgoing=True, pattern='^.hai(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**HAI, ANAK YANG TERLAHIR TANPA AYAH ATAU KATA LEMBUTNYA YATIM!!**")


@register(outgoing=True, pattern='^.em(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**EH, MONYET!!!**")


@register(outgoing=True, pattern='^.eh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**APAANSI MANGGIL - MANGGIL MUKA LU JELEK BANGSAT...!**")


@register(outgoing=True, pattern='^.jagoan(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ANJING LO, JAGOAN MANA LU???**")


@register(outgoing=True, pattern='^.hey(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**HEY, SAMPAH MASYARAKAT TELEGRAM**")


@register(outgoing=True, pattern='^.loh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ANJING MASIH HIDUP AJA NI GC, BUBARIN AJA GC BEGINIAN MAH GA ADA GUNA NYA NGOTORIN TELEGRAM BAE**")

CMD_HELP.update({
    "salam3":
    ".p\
\nUsage:\
\n\n.l\
\nUsage:\
\n\n.gdjm\
\nUsage:\
\n\n.gjn\
\nUsage:\
\n\n.gjlb\
\nUsage:\
\n\n.yb\
\nUsage:\
\n\n.gblk\
\nUsage:"
})

CMD_HELP.update({
    "salam4":
    ".gbgn\
\nUsage:\
\n\n.bsl\
\nUsage:\
\n\n.hai\
\nUsage:\
\n\n.eh\
\nUsage:\
\n\n.em\
\nUsage:\
\n\n.gls\
\nUsage:\
\n\n.hey\
\nUsage:\
\n\n.loh\
\nUsage:\
\n\n.jagoan\
\nUsage:\
\n\n.m\
\nUsage:\
\n\n.kljs\
\nUsage:"
})
