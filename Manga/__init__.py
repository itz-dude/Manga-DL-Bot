import config as C
from pyrogram import Client, filters

app = Client(
  "manga",
  api_id=C.API_ID,
  api_hash=C.API_HASH,
  bot_token=C.TOKEN
)

print("[INFO]: STARTING BOT")
app.start()

print("[INFO]: GATHERING INFO")
x = app.get_me()
BOT_NAME = x.first_name
BOT_USERNAME = x.username
BOT_ID = x.id



def get_command(com):
  return filters.command([com, f"{com}@{BOT_USERNAME}"], prefixes=["/", "!", "."])
