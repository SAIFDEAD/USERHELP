from telethon.errors.rpcerrorlist import YouBlockedUserError
from TelethonHell.plugins import *


@hell_cmd(pattern="ascii(?:\s|$)([\s\S]*)")
async def _(event):
    if not event.reply_to_msg_id:
        return await eod(event, "Reply to any user message.😒🤐")
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        return await eod(event, "Reply to media message😒🤐")
    bot = "@asciiart_bot"
    cid = await client_id(event)
    hell_mention = cid[2]
    kraken = await eor(event, "Wait making ASCII...🤓🔥🔥")
    async with event.client.conversation(bot) as conv:
        try:
            first = await conv.send_message("/start")
            response = await conv.get_response()
            second = await conv.send_message(reply_message)
            output_op = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await parse_error(event, "Unblock @asciiart_bot and try again.", False)
            return
    await event.client.send_file(
        event.chat_id,
        file=output_op,
        caption=f"ASCII art By :- {hell_mention}",
        force_document=False,
    )
    await kraken.delete()
    await event.client.delete_messages(
        conv.chat_id, [first.id, response.id, second.id, output_op.id]
    )


@hell_cmd(pattern="line(?:\s|$)([\s\S]*)")
async def _(event):
    if not event.reply_to_msg_id:
        await eod(event, "Reply to any user message.😒🤐")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await eod(event, "Reply to media message😒🤐")
        return
    bot = "@lines50bot"
    cid = await client_id(event)
    hell_mention = cid[2]
    kraken = await eor(event, "`Processing...`")
    async with event.client.conversation(bot) as conv:
        try:
            first = await conv.send_message("/start")
            response = await conv.get_response()
            second = await conv.send_message(reply_message)
            output_op = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await parse_error(event, "Unblock @Lines50Bot and try again.", False)
            return
    await event.client.send_file(
        event.chat_id,
        file=output_op,
        caption=f"Lines By :- {hell_mention}",
        force_document=False,
    )
    await kraken.delete()
    await event.client.delete_messages(
        conv.chat_id, [first.id, response.id, second.id, output_op.id]
    )


CmdHelp("𝐀sᴄɪɪ").add_command(
    "ᴀsᴄɪɪ", "reply to any image file", "Makes an image ascii style, try out your own"
).add_command(
    "ʟɪɴᴇ", "reply to any image file", "Makes an image in line style"
).add_info(
    "ʟɪɴᴇs ᴀɴᴅ ᴀsᴄɪɪ"
).add_warning(
    "✅ Harmless Module."
).add()
