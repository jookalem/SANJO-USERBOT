from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Permisi Seleb Mau Nimbrung Kaka..**")


@register(outgoing=True, pattern='^.bf(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Joo Ganteng☑️**")
    await typew.edit("**Joo Ganteng✅**")
    sleep(3)
    await typew.edit("**Kyy Kang Coli☑️**")
    await typew.edit("**Kyy Kang Coli✅**")
    sleep(3)
    await typew.edit("**Skyzo Kuli Bangunan☑️**")
    await typew.edit("**Skyzo Kuli Bangunan✅**")
    sleep(3)
    await typew.edit("**Dior Sangean☑️**")
    await typew.edit("**Dior Sangean✅**")
    sleep(3)
    await typew.edit("**Skyzu Kuli Jawa☑️**")
    await typew.edit("**Skyzu Kuli Jawa✅**")
    sleep(3)
    await typew.edit("**Kyura Mirip Monyet☑️**")
    await typew.edit("**Kyura Mirip Monyet✅**")
    sleep(3)
    await typew.edit("**Cumi Cantik☑️**")
    await typew.edit("**Cumi Cantik✅**")
    sleep(3)
    await typew.edit("**Dita Tetenya Tepos☑️**")
    await typew.edit("**Dita Tetenya Tepos✅**")
    sleep(3)
    await typew.edit("**CUMAN JOO PALING TAMPAN, DAN TIDAK SOMBONG😎**")

@register(outgoing=True, pattern='^.pbl(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`PP Bule?`")
    sleep(2)
    await typew.edit("`ANJINK...Ada PP Bule`")
    sleep(2)
    await typew.edit("`BABI PP BULE!!!`")
    sleep(3)
    await typew.edit("`Udah PP Bule PINTEREST lagi, goblok!!!`")
    sleep(3)
    await typew.edit("`Kalo ga punya muka minimal modal lah BANGSAT...Dasar bocah pinterest`")


@register(outgoing=True, pattern='^.lahk(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Lahk, Lu Goblok Apa Tolol?`")
    sleep(2)
    await typew.edit("`Apa Autis?`")
    sleep(2)
    await typew.edit("`Gosa sokeras jelek`")
    sleep(1)
    await typew.edit("`Gua ga takut sama bocah bocah ampas kek lu gblk`")


@register(outgoing=True, pattern='^.war(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wah, Ada war gais...`")
    sleep(2)
    await typew.edit("`Tapi, kalo diliat-liat kesannya lebih ke stand up komedi😅`")
    sleep(3)
    await typew.edit("`Eh iya, Lu kan badut`")
    sleep(3)
    await typew.edit("`Disuruh war malah cerpen`")
    sleep(3)
    await typew.edit("`kebanyakan baca dongeng ya gini.`")
    sleep(3)
    await typew.edit("`Keras kaga dongo iya,kek badut ulang tahun yg kaga di gaji`")
    sleep(3)
    await typew.edit("`Bocah goblok yang gobloknya seperti rucika mengalir sampai jauh, Lu lebih goblok lagi gobloknya keturunan sampai lu lahir bgst`")

CMD_HELP.update({
    "diorbot":
    "`.sadboy`\
    \nUsage: hiks\
    \n\n`.punten` ; `.bf` ; `.war` ; `.lahk` ; `.pbl`\
    \nUsage: liat aza."
})
