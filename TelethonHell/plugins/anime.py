import requests
from telethon.errors.rpcerrorlist import ChatSendMediaForbiddenError
from TelethonHell.plugins import *


@hell_cmd(pattern="anime(?:\s|$)([\s\S]*)")
async def _(event):
    query = event.text[7:]
    if query == "":
        return await eor(event, "Please give anime name to search on Anilist.")
    hell = await eor(event, f"__Searching for__ `{query}` __on Anilist.__")
    qdb = rand_key()
    ANIME_DB[qdb] = query
    result = await get_anilist(qdb, 1)
    if len(result) == 1:
        return await hell.edit(result[0])
    pic, msg = result[0], result[1][0]
    try:
        await event.client.send_file(
            event.chat_id, file=pic, caption=msg, force_document=False
        )
        await hell.delete()
    except ChatSendMediaForbiddenError:
        await hell.edit(msg)
    if os.path.exists(pic):
        os.remove(pic)


@hell_cmd(pattern="manga(?:\s|$)([\s\S]*)")
async def _(event):
    query = event.text[7:]
    if query == "":
        await eor(event, "ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴍᴀɴɢᴀ ɴᴀᴍᴇ ᴛᴏ sᴇᴀʀᴄʜ..")
    hell = await eor(event, f"__sᴇᴀʀᴄʜɪɴɢ ғᴏʀ__ `{query}` ...")
    qdb = rand_key()
    MANGA_DB[qdb] = query
    result = await get_manga(qdb, 1)
    if len(result) == 1:
        return await hell.edit(result[0])
    pic, finals_ = result[0], result[1][0]
    try:
        await event.client.send_file(event.chat_id, file=pic, caption=finals_)
        await hell.delete()
    except ChatSendMediaForbiddenError:
        await hell.edit(finals_)
    if os.path.exists(pic):
        os.remove(pic)


@hell_cmd(pattern="character(?:\s|$)([\s\S]*)")
async def _(event):
    query = event.text[11:]
    if query == "":
        return await eor(event, "Give character name to get details.")
    hell = await eor(event, f"__Searching for__ `{query}`")
    qdb = rand_key()
    CHARC_DB[qdb] = query
    result = await get_character(qdb, 1)
    if len(result) == 1:
        return await hell.edit(result[0])
    img = result[0]
    cap_text = result[1][0]
    try:
        await event.client.send_file(event.chat_id, file=img, caption=cap_text)
        await hell.delete()
    except ChatSendMediaForbiddenError:
        await hell.delete(cap_text)
    if os.path.exists(img):
        os.remove(img)


@hell_cmd(pattern="fillers(?:\s|$)([\s\S]*)")
async def canon(event):
    hell = event.text[9:]
    if hell == "":
        return await eor(event, "`Give anime name to search filler episodes.`")
    nub = await eor(event, f"Searching Filler Episodes For `{hell}`")
    hel_ = search_filler(hell)
    if hel_ == {}:
        return await nub.edit(f"No filler found for `{hell}`")
    list_ = list(hel_.keys())
    if len(list_) == 1:
        result = parse_filler(hel_.get(list_[0]))
        msg = ""
        msg += f"<h2>Fillers for {list_[0]} :</h2>\n\n<b>Manga Canon Episodes :</b>\n"
        msg += f'<code>{str(result.get("total_ep"))}</code>'
        msg += "\n\n<b>Mixed/Canon fillers :</b>\n"
        msg += f'<code>{str(result.get("mixed_ep"))}</code>'
        msg += "\n\n<b>Fillers :</b>\n"
        msg += f'<code>{str(result.get("filler_ep"))}</code>'
        if result.get("ac_ep") is not None:
            msg += "\n\n<b>Anime Canon episodes :</b>\n"
            msg += f'<code>{str(result.get("ac_ep"))}</code>'
        paste = await telegraph_paste(f"📃 Fillers List For “ {list_[0]} ”", msg)
        await nub.edit(f"**📃 Filler Episode List For [“ {list_[0]} ”]({paste}) !!**")
        return
    hellbot = f"**📃 Filler Episode Lists :** \n\n"
    for i in list_:
        result = parse_filler(hel_.get(i))
        msg = ""
        msg += f"<h2>Fillers for {i} :</h2>\n\n<b>Manga Canon Episodes :</b>\n"
        msg += f'<code>{str(result.get("total_ep"))}</code>'
        msg += "\n\n<b>Mixed/Canon fillers :</b>\n"
        msg += f'<code>{str(result.get("mixed_ep"))}</code>'
        msg += "\n\n<b>Fillers :</b>\n"
        msg += f'<code>{str(result.get("filler_ep"))}</code>'
        if result.get("ac_ep") is not None:
            msg += "\n\n<b>Anime Canon episodes :</b>\n"
            msg += f'<code>{str(result.get("ac_ep"))}</code>'
        paste = await telegraph_paste(f"📃 Fillers List For “ {i} ”", msg)
        hellbot += f"• [{i}]({paste})\n"
    await nub.edit(hellbot)


@hell_cmd(pattern="airing(?:\s|$)([\s\S]*)")
async def _(event):
    query = event.text[8:]
    hell = await eor(event, f"__Searching airing details for__ `{query}`")
    if query == "":
        return await eod(hell, "Give anime name to seaech airing information.")
    vars_ = {"search": query}
    if query.isdigit():
        vars_ = {"id": int(query), "asHtml": True}
    result = await get_airing(vars_)
    if len(result) == 1:
        return await hell.edit(result[0])
    coverImg, out = result[0]
    try:
        await event.client.send_file(
            event.chat_id, coverImg, caption=out, force_document=False
        )
        await hell.delete()
    except ChatSendMediaForbiddenError:
        await hell.edit(out)
    if os.path.exists(coverImg):
        os.remove(coverImg)


@hell_cmd(pattern="aniuser(?:\s|$)([\s\S]*)")
async def _(event):
    query = event.text[9:]
    hell = await eor(event, "Searching user's Anilist Stats...")
    if query == "":
        return await hell.edit("No user found. Give anilist username.")
    qry = {"search": query}
    result = await get_user(qry)
    if len(result) == 1:
        return await eod(hell, result[0])
    pic, msg = result
    try:
        await event.client.send_file(
            event.chat_id,
            file=pic,
            caption=msg,
            force_document=False,
            parse_mode="HTML",
        )
        await hell.delete()
    except ChatSendMediaForbiddenError:
        await hell.edit(msg)
    if os.path.exists(pic):
        os.remove(pic)


@hell_cmd(pattern="aniquote$")
async def quote(event):
    hell = await eor(event, "(ﾉ◕ヮ◕)ﾉ*.✧")
    q = requests.get("https://animechan.vercel.app/api/random").json()
    await hell.edit(f"`{q['quote']}`\n\n—  **{q['character']}** (From __{q['anime']}__)")  # dimag ka bhosda hogya bc yha pe (*﹏*;)


CmdHelp("𝐀ɴɪᴍᴇ").add_command(
    "ᴀɴɪᴍᴇ", "<anime name>", "Searches for the given anime and sends the details.", "anime Darling in the franxx"
).add_command(
    "ᴍᴀɴɢᴀ", "<manga name>", "Searches for the given manga and sends the details.", "manga Naruto"
).add_command(
    "ᴄʜᴀʀᴀᴄᴛᴇʀ", "<character name>", "Searches for the given anime character and sends the details.", "character Mai Sakurajima"
).add_command(
    "𝐀ɴɪᴜsᴇʀ", "<anilist username>", "Searches for the Anilist Stats of the given user.", "aniuser saif is my dad"
).add_command(
    "𝐀ɪʀɪɴɢ", "<anime name>", "Searches for the airing info of given anime."
).add_command(
    "𝐅ɪʟʟᴇʀs", "<anime name>", "Searches for the filler episodes of given Anime.", "fillers Naruto"
).add_command(
    "𝐀ɴɪǫᴜᴏᴛᴇ", None, "Gives a random quote from Anime."
).add_info(
    "Anime Module based on Anilist API."
).add_warning(
    "✅ Harmless Module."
).add()
