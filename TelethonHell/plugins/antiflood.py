import asyncio

from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
from TelethonHell.DB import antiflood_sql as sq
from TelethonHell.plugins import *

CHAT_FLOOD = sq.__load_flood_settings()
ANTI_FLOOD_WARN_MODE = ChatBannedRights(
    until_date=None, view_messages=None, send_messages=True
)


@hell_handler(incoming=True)
async def _(event):
    if not CHAT_FLOOD:
        return
    if str(event.chat_id) not in CHAT_FLOOD:
        return
    should_ban = sq.update_flood(event.chat_id, event.message.sender_id)
    if not should_ban:
        return
    try:
        await event.client(
            EditBannedRequest(
                event.chat_id, event.message.sender_id, ANTI_FLOOD_WARN_MODE
            )
        )
    except Exception as e:
        no_admin_privilege_message = await event.client.send_message(
            entity=event.chat_id,
            message="""**ᴀᴜᴛᴏᴍᴀᴛɪᴄ ᴀɴᴛɪғʟᴏᴏᴅᴇʀ**
@admin [user](tg://user?id={}) ɪs ғʟᴏᴏᴅɪɴɢ ᴛʜɪs ᴄʜᴀᴛ.
`{}`""".format(
                event.message.sender_id, str(e)
            ),
            reply_to=event.message.id,
        )
        await asyncio.sleep(10)
        await no_admin_privilege_message.edit(
            "ᴛʜɪs ɪs ᴜsᴇʟᴇss sᴘᴀᴍ ᴅᴜᴅᴇ. sᴛᴏᴘ ᴛʜɪs, ᴇɴᴊᴏʏ ᴄʜᴀᴛ ᴍᴀɴ ", link_preview=False
        )
    else:
        await event.client.send_message(
            entity=event.chat_id,
            message="""**Automatic AntiFlooder**
[User](tg://user?id={}) has been automatically restricted
because he reached the defined flood limit.""".format(
                event.message.sender_id
            ),
            reply_to=event.message.id,
        )


@hell_cmd(pattern="setflood(?:\s|$)([\s\S]*)")
async def _(event):
    input_str = event.pattern_match.group(1)
    event = await eor(event, "updating flood settings!")
    try:
        sq.set_flood(event.chat_id, input_str)
        sq.__load_flood_settings()
        await event.edit(
            "Antiflood updated to {} in the current chat".format(input_str)
        )
    except Exception as e:
        await parse_error(event, e)


CmdHelp("𝐀ɴᴛɪғʟᴏᴏᴅ").add_command(
    "sᴇᴛғʟᴏᴏᴅ", "<number>", "Warns the user if he/she spams the chat and if you are an admin then it mutes him/her in the grp"
).add_info(
    "ᴀɴᴛɪ sᴘᴀᴍᴍᴇʀ"
).add_warning(
    "✅ Harmless Module."
).add()
