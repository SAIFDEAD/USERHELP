import asyncio
import random
import time

from telethon.errors import FloodWaitError
from telethon.tl import functions
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest
from TelethonHell.DB.gvar_sql import gvarstat
from TelethonHell.plugins import *


@hell_cmd(pattern="autoname$")
async def _(event):
    hell = await eor(event, "`𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐀𝐮𝐭𝐨𝐍𝐚𝐦𝐞 𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭`")
    _id, HELL_USER, _ment = await client_id(event)
    await hell.edit(f"𝐀𝐮𝐭𝐨 𝐍𝐚𝐦𝐞 𝐡𝐚𝐬 𝐛𝐞𝐞𝐧 𝐬𝐭𝐚𝐫𝐭𝐞𝐝 𝐦𝐲 𝐌𝐚𝐬𝐭𝐞𝐫")
    await event.client.send_message(
        Config.LOGGER_ID, "#AUTONAME \n\nAutoname Started!!"
    )
    while True:
        HB = time.strftime("%d-%m-%y")
        HE = time.strftime("%H:%M")
        name = f"🕒{HE} ⚡{HELL_USER}⚡ 📅{HB}"
        LOGS.info(name)
        try:
            await event.client(functions.account.UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(60)


@hell_cmd(pattern="autobio$")
async def _(event):
    hell = await eor(event, "Starting AutoBio...")
    await hell.edit("AutoBio Activated...")
    await event.client.send_message(Config.LOGGER_ID, "#AUTOBIO \n\nAutoBio Started!!")
    while True:
        bio_ = gvarstat("BIO_MSG") or random.choice(bio_msgs)
        DEFAULTUSERBIO = bio_[:66]
        bio = f"“ {DEFAULTUSERBIO} ”"
        LOGS.info(bio)
        try:
            await event.client(functions.account.UpdateProfileRequest(about=bio))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(60)


@hell_cmd(pattern="reserved$")
async def mine(event):
    result = await event.client(GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"{channel_obj.title}\n@{channel_obj.username}\n\n"
    await eor(event, output_str)


CmdHelp("𝐀ᴜᴛᴏ_𝐏ʀᴏғɪʟᴇ").add_command(
    "ᴀᴜᴛᴏʙɪᴏ", None, "Changes your bio with random quotes. You can set your own bio by setting up gvar BIO_MSG."
).add_command(
    "ᴀᴜᴛᴏɴᴀᴍᴇ", None, "Changes your name with time."
).add_command(
    "ʀᴇsᴇʀᴠᴇᴅ", None, "Gives the list of usernames reserved by you. In short gives the list of public groups or channels that you are owner in."
).add_info(
    "ᴍᴀɴᴀɢᴇ ᴘʀᴏғɪʟᴇs"
).add_warning(
    "🚫 Potentially Harmful"
).add()
