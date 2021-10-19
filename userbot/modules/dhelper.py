""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.helpmy$")
async def usit(e):
    await e.edit(
        f"**Hai {DEFAULTUSER} Kalau lu ga Tau cara buat Memerintah gua Ketik** `.helpme` Atau `.help` atau Minta Bantuan Ke:\n"
        "\n[FATUR](t.me/uurfavboys1)"
        "\n\n[SUPPORT](https://t.me/diorplayingwords)"
        "\n\n[HELP](https://t.me/fandasupport)")


@register(outgoing=True, pattern="^.rvars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/DIORrios285/DIOR-UBOT/DIOR-UBOT/varshelper.txt)")


CMD_HELP.update({
    "diorhelper":
    "`.helpmy`\
\nPenjelasan: Bantuan Untuk DIOR-UBOT.\
\n`.rvars`\
\nPenjelasan: Untuk Melihat Beberapa Daftar Vars."
})
