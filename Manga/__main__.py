from . import app, get_command, BOT_NAME, BOT_ID
from pyrogram import __version__
from pyrogram import filters, idle
from .utils import import *
from pykeyboard import InlineKeyboard, InlineButton

HELP_MSG = f"**This is {}'s Help Menu**\n» `/search <manga>`: Returns Search Results For Manga\n» `/manga <name> <chapter number>`: Returns Chapter of Manga"


HELP_MARKUP = InlineKeyboard(row_width=2)

HELP_MARKUP.add(
  InlineButton(
    text="Back", 
    callback_data="homeback"
  )
)

START_MSG = f"Hey There {message.from_user.first_name}\n\nI'm {BOT_NAME} a bot to provide manga\n» Click on `HELP` button to know commands\n» Click on `ABOUT` button to know about me"


START_MARKUP = InlineKeyboard(row_width=2)


START_MARKUP.add(
  InlineButton(
    text="HELP",
    callback_data="help_home"
  ),
  InlineButton(
    text="ABOUT",
    callback_data="about_home"
  )
)

ABOUT_MSG = f"**Hi This Is My Info**\n\n» **Pyrogram Version**: `{__version__}`\n\n–› Made By @TechzBots"
ABOUT_MARKUP = InlineKeyboard(row_width=2)
ABOUT_MARKUP.add(
  InlineButton(
    text="SUPPORT_CHAT",
    url="https://t.me/TechZBots_Support"
  ),
  InlineButton(
    text="UPDATES CHANNEL",
    url="https://t.me/TechZBots"
  ),
  InlineButton(
    text="DEV",
    user_id=5365575465
  ),
  InlineButton(
    text="REPO", 
    url="https://github.com/AuraMoon55/Manga-DL-BOT"
  ),
  InlineButton(
    text="Back",
    callback_data="homeback"
  )
)


@app.on_message(get_command("start"))
async def _start(_, message):
  return await message.reply_text(START_MSG, reply_markup=START_MARKUP)


@app.on_callback_query(filters.regex("help_home"))
async def _helpq(_, query):
  return await query.message.edit_text(text=HELP_MSG, reply_markup=HELP_MARKUP)



@app.on_callback_query(filters.regex("about_home"))
async def _aboutq(_, query):
  return await query.message.edit_text(text=ABOUT_MSG, reply_markup=ABOUT_MARKUP)




@app.on_message(get_command("help"))
async def _help(_, message):
  return await message.reply_text(text=HELP_MSG, reply_markup=HELP_MARKUP)



@app.on_message(get_command("about"))
async def _about(_, message):
  return await message.reply_text(text=ABOUT_MSG, reply_markup=ABOUT_MARKUP)


@app.on_callback_query(filters.regex("homeback"))
async def _hback(_, query):
  return await query.message.edit_text(START_MSG, reply_markup=START_MARKUP)



@app.on_message(get_command("search"))
async def searc(_, message):
  try:
    q = message.text.split(" ", maxsplit=1)[1]
  except IndexError:
    return await message.reply_text("**Usage**\n\n× /search One Piece")
  res = search(q)
  if isinstance(res, str):
    return await message.reply_text("No Results Found")
  else:
    if len(res) < 1:
      return await message.reply_text("No Results Found")
    else:
      key = searchkeyboard(res)
      text = f"**Showing Results for {q}**\n\n`Click on Button To Know First & Last Chapter Number`"
      return await message.reply_text(text=text, reply_markup=key)


@app.on_callback_query(filters.regex("mangainfo"))
async def chpnm(_, query):
  q = query.data.replace("mangainfo", "")
  res = detail(q)
  if isinstance(res, str):
    return await query.message.edit_text("An Exception Occured Report At @TechZBots_Support")
  else:
    if len(res['chapter']) < 1:
      return await query.message.edit_text("No Results For This Manga ")
    else:
      ch = chapkeyboard(res['chapter'])
      text = f"Chapters For {q.replace('-', ' ')}"
      return await query.message.edit_text(text=text, reply_markup=ch)

@app.on_message(get_command("manga"))
async def gib_chap(_, message):
  try:
    args = (message.text.split(" ", maxsplit=1)[1]).split(" ")
  except:
    return await message.reply_text("**Usage**:\n\n× /manga <manga> <chapter>")
  if len(args) <= 1:
    return await message.reply_text("**Usage**:\n\n× /manga <manga> <chapter>")
  else:
    if not isinstance(args[-1], int):
      return await message.reply_text("**Usage**:\n\n× /manga <manga> <chapter>")
    else:
      try:
        man = " ".join(args[:-1])
        chap = args[-1]
        res = detail(search(man)[0]['mangaid'])['chapter']
        for x in res:
          if x['num'] == chap:
            title, chap = telegra(x['url'])
            return await message.reply_text(f"[{title}]({chap})")
          else:
            pass
      except:
        return await message.reply_text("An Exception Occurred Report at @TechZBots_Support")
