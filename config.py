from dotenv import load_dotenv
from os import getenv

load_dotenv()

API_ID = int(getenv("API_ID", None))
API_HASH = str(getenv("API_HASH", None))
TOKEN = str(getenv("TOKEN", None))
