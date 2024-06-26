from TelethonHell.DB.autopost_sql import (add_post, get_all_post, is_post,
                                          remove_post)
from TelethonHell.DB.gvar_sql import addgvar, delgvar, gvarstat
from TelethonHell.plugins import *


@hell_cmd(pattern="autopost(?:\s|$)([\s\S]*)")
async def _(event):
    if event.is_private:
        return await parse_error(event, "ᴀᴜᴛᴏᴘᴏsᴛ ᴄᴀɴ ᴏɴʟʏ ʙᴇ ᴜsᴇᴅ ғᴏʀ ᴄʜᴀɴɴᴇʟs & ɢʀᴏᴜᴘs.")
    hell = await eor(event, "ᴛʀʏɪɴɢ ᴛᴏ sᴛᴀʀᴛ ᴀᴜᴛᴏᴘᴏsᴛɪɴɢ ғʀᴏᴍ ʜᴇʀᴇ...")
    cid = await client_id(event)
    ForGo10God = cid[0]
    hel_ = event.text[10:]
    cli_ = ForGo10God
    checker = gvarstat(f"AUTOPOST_{str(cli_)}")
    if hel_ == "":
        return await eod(
            hell,
            f"Give correct command for working of autopost. \n`{hl}autopost channel_id`",
        )
    if str(hel_).startswith("-100"):
        kk = str(hel_).replace("-100", "")
    else:
        kk = hel_
    if not kk.isdigit():
        return await parse_error(hell, "Only channel ID is supported.")
    if is_post(kk, event.chat_id):
        if checker and checker == "True":
            return await eod(hell, "This channel is already in this client's autopost database.")
        else:
            addgvar(f"AUTOPOST_{str(cli_)}", "True")
            return await hell.edit(
                f"**📍 Started AutoPosting from** `{hel_}` for `{cli_}`"
            )
    add_post(kk, event.chat_id)
    addgvar(f"AUTOPOST_{str(cli_)}", "True")
    await hell.edit(f"**📍 Started AutoPosting from** `{hel_}` for `{cli_}`")


@hell_cmd(pattern="rmautopost(?:\s|$)([\s\S]*)")
async def _(event):
    if event.is_private:
        return await parse_error(event, "AutoPost Can Only Be Used For Channels.")
    hell = await eor(event, "Removing autopost...")
    cid = await client_id(event)
    ForGo10God = cid[0]
    hel_ = event.text[12:]
    cli_ = ForGo10God
    checker = gvarstat(f"AUTOPOST_{str(cli_)}")
    if hel_ == "":
        return await eod(
            hell,
            f"Give correct command for removing autopost. \n`{hl}autopost channel_id`",
        )
    if str(hel_).startswith("-100"):
        kk = str(hel_).replace("-100", "")
    else:
        kk = hel_
    if not kk.isdigit():
        return await parse_error(event, "Only channel ID is supported.")
    if not is_post(kk, event.chat_id):
        return await eod(event, "I don't think this channel is in AutoPost Database.")
    if is_post(kk, event.chat_id):
        if checker and checker == "True":
            remove_post(kk, event.chat_id)
            delgvar(f"AUTOPOST_{str(cli_)}")
            return await eod(hell, f"Removed `{hel_}` from `{cli_}` autopost database.")
        else:
            return await eod(
                hell, f"This channel is not in `{cli_}` autopost database."
            )


@hell_handler(incoming=True)
async def _(event):
    chat_id = str(event.chat_id).replace("-100", "")
    channels_set = get_all_post(chat_id)
    if channels_set == []:
        return
    cid = await client_id(event)
    ForGo10God = cid[0]
    cli_ = ForGo10God
    checker = gvarstat(f"AUTOPOST_{str(cli_)}")
    if checker and checker == "True":
        for chat in channels_set:
            if event.media:
                await event.client.send_file(int(chat), event.media, caption=event.text)
            elif not event.media:
                await event.client.send_message(int(chat), event.message)


CmdHelp("𝐀ᴜᴛᴏᴘᴏsᴛ").add_command(
    "ᴀᴜᴛᴏᴘᴏsᴛ", "<channel id>", "Auto Posts every new post from targeted channel to your channel.", "autopost <channelid> [in your channel]"
).add_command(
    "ʀᴍᴀᴜᴛᴏᴘᴏsᴛ", "<channel id>", "Stops AutoPost from targeted autoposting channel."
).add_info(
    "ᴀᴜᴛᴏᴘᴏsᴛ ғʀᴏᴍ ᴏɴᴇ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴀɴᴏᴛʜᴇʀ."
).add_warning(
    "✅ Harmless Module."
).add()
