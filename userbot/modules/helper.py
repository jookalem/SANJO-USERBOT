""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.helpmy$")
async def usit(e):
    await e.edit(
        f"__Hai {DEFAULTUSER} Kalau lu ga Tau cara buat__ **Memerintah** gua **Ketik** `.helpme` Atau `.help` atau Minta **Bantuan** __Ke:__\n"
        f"β° **Channel support :** [Sanjo](t.me/gbtnyajo)\n"
        f"β° **Group Support :** [Sanjo Support](t.me/sanjosupport)\n"
        f"β° **Owner Repo :** [SANJO](t.me/jooneverdie)\n"
        f"β° **Repo :** [SANJO-USERBOT](https://github.com/DIORrios285/DIOR-UBOT)\n\n\n"
        f"__Powered by πΎππππ-ππππ__"
    )



@register(outgoing=True, pattern="^.rvars$")
async def var(m):
    await m.edit(
        f"**Daftar Vars** {DEFAULTUSER}:\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/DIORrios285/DIOR-UBOT/DIOR-UBOT/varshelper.txt)")


CMD_HELP.update({
    "helper":
    "`.helpmy`\
\nUsage: Bantuan Untuk SANJO-USERBOT.\
\n`.rvars`\
\nUsage: Untuk Melihat Beberapa Daftar Vars."
})
