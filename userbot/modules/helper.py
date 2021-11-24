""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.helpmy$")
async def usit(e):
    await e.edit(
        f"**Hai {DEFAULTUSER} Kalau lu ga Tau cara buat Memerintah gua Ketik** `.helpme` **Atau** `.help` **atau Minta Bantuan Ke:**\n"
        f"✰ **Group Support :** [Fanda Support](t.me/fandasupport)\n"
        f"✰ **Channel support :** [Fanda Project](t.me/fandaproject)\n"
        f"✰ **Owner Repo :** [Fatur](t.me/uurfavboys1)\n"
        f"✰ **Repo :** [DIOR-UBOT](https://github.com/DIORrios285/DIOR-UBOT)\n"
    )



@register(outgoing=True, pattern="^.rvars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari** {DEFAULTUSER}:\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/DIORrios285/DIOR-UBOT/DIOR-UBOT/varshelper.txt)")


CMD_HELP.update({
    "helper":
    "`.helpmy`\
\nUsage: Bantuan Untuk DIOR-UBOT.\
\n`.rvars`\
\nUsage: Untuk Melihat Beberapa Daftar Vars."
})
