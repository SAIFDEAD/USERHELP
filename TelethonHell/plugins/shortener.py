from HellConfig import Config
from TelethonHell.plugins import *


@hell_cmd(pattern="shorten(?:\s|$)([\s\S]*)")
async def shortener(event):
    if not Config.SHORTENER_API:
        return await parse_error(event, "`SHORTENER_API` is not configured!", False)
    lists = event.text.split(" ", 1)
    if len(lists) != 2:
        return await parse_error(event, "𝐍𝐨𝐭𝐡𝐢𝐧𝐠 𝐠𝐢𝐯𝐞𝐧 𝐭𝐨 𝐬𝐡𝐨𝐫𝐭.")
    query = lists[1].strip()
    if not query:
        return await parse_error(event, "Nothing given to short.")
    hell = await eor(event, f"<b><i>Shortening “ {query} ”</i></b>", parse_mode="HTML")
    link = short(Config.SHORTENER_API, query)
    if not link:
        return await parse_error(hell, f"__There was an error while shortening the link.__ \n`Check logs for more details.`", False)
    await hell.edit(f"**••• Shortened Link •••** \n\n__» Short Url:__ {link} \n» Original Url: {query}")


def short(api_key, long_url):
    try:
        api_url = f"https://api.shareus.in/shortLink?token={api_key}&format=json&link={long_url}"
        response = requests.get(api_url)
        if response.ok:
            data = json.loads(response.text)
            return data['shortlink']
        else:
            return None
    except Exception as e:
        LOGS.exception(str(e))
        return None


CmdHelp("𝐒ʜᴏʀᴛᴇɴᴇʀ").add_command(
    "shorten", "<url>", "Shortens the given url."
).add_info(
    "Shorten using shareus"
).add_warning(
    "✅ Harmless Module."
).add()
