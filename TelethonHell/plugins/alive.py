import datetime
import random
import time
from unicodedata import name

from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot
from TelethonHell.DB.gvar_sql import gvarstat, addgvar
from TelethonHell.plugins import *

# -------------------------------------------------------------------------------

ALIVE_TEMP = """
<b><i>⚡ 𝐋ɛɢɛռɖaʀʏ 𝐎ғ 𝐒αιғβσтƨ 𝐇ɛ˩ρ⚡</i></b>
<b><i>↼ Øwñêr ⇀</i></b> : 『 {hell_mention} 』
╭──────────────
┣─ <b>» 𝐓ᴇʟᴇᴛʜᴏɴ:</b> <i>{telethon_version}</i>
┣─ <b>» 𝐒αιғβσтƨ :</b> <i>{hellbot_version}</i>
┣─ <b>» 𝐒ᴜᴅᴏ:</b> <i>{is_sudo}</i>
┣─ <b>» 𝐔ᴘᴛɪᴍᴇ:</b> <i>{uptime}</i>
┣─ <b>» 𝐏ɪɴɢ:</b> <i>{ping}</i>
╰──────────────
<b><i>»»» <a href='https://t.me/SAIFHELPGC'>[⚡ 𝐒αιғβσтƨ ⚡]</a> «««</i></b>
"""

msg = """{}\n
<b><i> 𝐁ᴏᴛ 𝐒ᴛᴀᴛs 🥀 </b></i>
<b>ᴛᴇʟᴇᴛʜᴏɴ 🔥≈</b>  <i>{}</i>
<b> 𝐒αιғβσтƨ ⚡≈</b>  <i>{}</i>
<b>𝐔ᴘᴛɪᴍᴇ 🥳≈</b>  <i>{}</i>
<b>𝐀ʙᴜsᴇ 🌻≈</b>  <i>{}</i>
<b>𝐒ᴜᴅᴏ 🦋≈</b>  <i>{}</i>
"""
# -------------------------------------------------------------------------------


@hell_cmd(pattern="alivetemp$")
async def set_alive_temp(event):
    hell = await eor(event, "`Fetching template ...`")
    reply = await event.get_reply_message()
    if not reply:
        alive_temp = gvarstat("ALIVE_TEMPLATE") or ALIVE_TEMP
        to_reply = await hell.edit("Below is your current alive template 👇")
        await event.client.send_message(event.chat_id, alive_temp, parse_mode=None, link_preview=False, reply_to=to_reply)
        return
    addgvar("ALIVE_TEMPLATE", reply.text)
    await hell.edit(f"`ALIVE_TEMPLATE` __changed to:__ \n\n`{reply.text}`")


@hell_cmd(pattern="alive$")
async def _(event):
    start = datetime.datetime.now()
    userid, hell_user, hell_mention = await client_id(event, is_html=True)
    hell = await eor(event, "`Building Alive....`")
    reply = await event.get_reply_message()
    uptime = await get_time((time.time() - StartTime))
    name = gvarstat("ALIVE_NAME") or hell_user
    alive_temp = gvarstat("ALIVE_TEMPLATE") or ALIVE_TEMP
    a = gvarstat("ALIVE_PIC")
    pic_list = []
    if a:
        b = a.split(" ")
        if len(b) >= 1:
            for c in b:
                pic_list.append(c)
        PIC = random.choice(pic_list)
    else:
        PIC = "https://te.legra.ph/file/ea9e11f7c9db21c1b8d5e.mp4"
    end = datetime.datetime.now()
    ping = (end - start).microseconds / 1000
    alive = alive_temp.format(
        hell_mention=hell_mention,
        telethon_version=telethon_version,
        hellbot_version=hellbot_version,
        is_sudo=is_sudo,
        uptime=uptime,
        ping=ping,
    )
    await event.client.send_file(
        event.chat_id,
        file=PIC,
        caption=alive,
        reply_to=reply,
        parse_mode="HTML",
    )
    await hell.delete()


@hell_cmd(pattern="hell$")
async def hell_a(event):
    userid, _, _ = await client_id(event)
    uptime = await get_time((time.time() - StartTime))
    am = gvarstat("ALIVE_MSG") or "<b>»» нєℓℓвσт ιѕ σиℓιиє ««</b>"
    try:
        hell = await event.client.inline_query(Config.BOT_USERNAME, "alive")
        await hell[0].click(event.chat_id)
        if event.sender_id == userid:
            await event.delete()
    except (noin, dedbot):
        await eor(
            event,
            msg.format(am, telethon_version, hellbot_version, uptime, abuse_m, is_sudo),
            parse_mode="HTML",
        )


CmdHelp("alive").add_command(
    "alive", None, "Shows the default Alive message."
).add_command(
    "hell", None, "Shows inline Alive message."
).add_warning(
    "✅ Harmless Module"
).add()
