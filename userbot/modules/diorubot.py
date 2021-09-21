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
                     "\n**Permisi Aku mau nimbrung Kk..**")


@register(outgoing=True, pattern='^.mb(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Panjul Kepala Suku☑️**")
    await typew.edit("**Panjul Kepala Suku✅**")
    sleep(1)
    await typew.edit("**Farhan Ribet☑️**")
    await typew.edit("**Farhan Ribet✅**")
    sleep(2)
    await typew.edit("**Gita Cantik☑️**")
    await typew.edit("**Gita Cantik✅**")
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
    sleep(1)
    await typew.edit("`Apa Autis?`")
    sleep(1)
    await typew.edit("`Gosah sokeras jelek`")
    sleep(1)
    await typew.edit("`Gua ga takut sama bocah bocah ampas kek lu!`")


@register(outgoing=True, pattern='^.wah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wahh, War nya keren bang`")
    sleep(2)
    await typew.edit("`Tapi, Yang gua liat, kok Kaya lawakan`")
    sleep(2)
    await typew.edit("`Oh iya, Kan lo badut 🤡`")
    sleep(2)
    await typew.edit("`Kosa kata pas ngelawak, Jangan di pake war bang`")
    sleep(2)
    await typew.edit("`Kesannya lo ngasih kita hiburan.`")
    sleep(2)
    await typew.edit("`Kasian badut🤡, Ga di hargain pengunjung, Eh lampiaskan nya ke Tele, Wkwkwk`")
    sleep(3)
    await typew.edit("`Dah sana cabut, Makasih hiburannya, Udah bikin Gua tawa ngakak`")

CMD_HELP.update({
    "diorbot":
    "`.diorbot`\
    \nUsage: menampilkan alive bot.\
    \n\n`.sadboy`\
    \nUsage: hiks\
    \n\n`.punten` ; `.mb`\
    \nUsage: misi."
})
