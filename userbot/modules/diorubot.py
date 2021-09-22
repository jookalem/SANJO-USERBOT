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
    await typew.edit("**Panjul Kepala Suku☑️**")
    await typew.edit("**Panjul Kepala Suku✅**")
    sleep(2)
    await typew.edit("**Farhan Ribet☑️**")
    await typew.edit("**Farhan Ribet✅**")
    sleep(2)
    await typew.edit("**Muza Buaya Betina☑️**")
    await typew.edit("**Muza Buaya Betina✅**")
    sleep(2)
    await typew.edit("**Gita Bawel☑️**")
    await typew.edit("**Gita Bawel✅**")
    sleep(2)
    await typew.edit("**Nigel Wibu☑️**")
    await typew.edit("**Nigel Wibu✅**")
    sleep(2)
    await typew.edit("**Kiaa Cantik Banget☑️**")
    await typew.edit("**Kiaa Cantik Banget✅**")
    sleep(2)
    await typew.edit("**Manda Kesayangan Fatur☑️**")
    await typew.edit("**Manda Kesayangan Fatur✅**")
    sleep(2)
    await typew.edit("**FATUR PALING TAMPAN!**")


@register(outgoing=True, pattern='^.lahk(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Lahk, Lu Goblok Apa Tolol?`")
    sleep(2)
    await typew.edit("`Apa Autis?`")
    sleep(2)
    await typew.edit("`Gosah sokeras jelek`")
    sleep(1)
    await typew.edit("`Gua ga takut sama bocah bocah ampas kek lu!`")


@register(outgoing=True, pattern='^.war(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wah, Ada war gais...`")
    sleep(2)
    await typew.edit("`Tapi, kalo diliat-liat kesannya lebih ke stand up komedi😅`")
    sleep(2)
    await typew.edit("`eh iya, Lu kan badut🤡`")
    sleep(2)
    await typew.edit("`Disuruh war malah cerpen`")
    sleep(2)
    await typew.edit("`kebanyakan baca dongeng ya gini.`")
    sleep(2)
    await typew.edit("`Keras kaga dongo iya,kek badut ulang tahun yg kaga di gaji`")
    sleep(3)
    await typew.edit("`Bocah goblok yang goblok goblok banget seperti rucika mengalir sampai jauh, Lu lebih goblok lagi gobloknya keturunan sampai lahir!`")

CMD_HELP.update({
    "diorbot":
    "`.diorbot`\
    \nUsage: menampilkan alive bot.\
    \n\n`.sadboy`\
    \nUsage: hiks\
    \n\n`.punten` ; `.bf`\
    \nUsage: misi."
})
