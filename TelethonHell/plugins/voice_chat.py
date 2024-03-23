from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.phone import (CreateGroupCallRequest,
                                         DiscardGroupCallRequest,
                                         GetGroupCallRequest,
                                         InviteToGroupCallRequest)
from TelethonHell.plugins import *


async def getvc(event):
    chat_ = await event.client(GetFullChannelRequest(event.chat_id))
    _chat = await event.client(GetGroupCallRequest(chat_.full_chat.call))
    return _chat.call


def all_users(a, b):
    for c in range(0, len(a), b):
        yield a[c : c + b]


@hell_cmd(pattern="startvc$")
async def _(event):
    try:
        await event.client(CreateGroupCallRequest(event.chat_id))
        await eod(event, "**Ѵσιcɛ Ɔнαт Ƨтαятɛ∂ Ƨʋccɛƨƨғʋℓℓʏ**")
    except Exception as e:
        await parse_error(event, f"`{str(e)}`")


@hell_cmd(pattern="endvc$")
async def _(event):
    try:
        await event.client(DiscardGroupCallRequest(await getvc(event)))
        await eod(event, "** Ѵσιcɛ Ɔнαт Єи∂ɛ∂ Ƨʋccɛƨƨғʋℓℓʏ !!**")
    except Exception as e:
        await parse_error(event, f"`{str(e)}`")


@hell_cmd(pattern="vcinvite$")
async def _(event):
    hell = await eor(event, "` Ɩиʏιтιиɢ Ʋƨɛяƨ Ƭσ Ѵσιcɛ Ɔнαт....`")
    users = []
    i = 0
    async for j in event.client.iter_participants(event.chat_id):
        if not j.bot:
            users.append(j.id)
    lists = list(all_users(users, 6))
    for k in lists:
        try:
            await event.client(
                InviteToGroupCallRequest(call=await getvc(event), users=k)
            )
            i += 6
        except BaseException:
            pass
    await parse_error(hell, f"**🚀 Ɩиʏιтɛ∂** `{i}` **users to Voice Chat.**")


CmdHelp("𝐕ᴏɪᴄᴇ_𝐂ʜᴀᴛ").add_command(
    "startvc", None, "Starts the voice chat in current group."
).add_command(
    "endvc", None, "Ends the voice chat in current group."
).add_command(
    "vcinvite", None, "Invites members of the current group to voice chat."
).add_info(
    "Voice Chat Tools."
).add_warning(
    "✅ Harmless Module."
).add()
