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