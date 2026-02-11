import os
import sys

import dotenv

dotenv.load_dotenv(sys.argv[1] if len(sys.argv) > 1 else ".env")


API_ID = int(os.getenv("API_ID", "25480794"))
API_HASH = os.getenv("API_HASH", "407966028aecd3fa3062ae940355b884")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7823349477:AAH4VBIUendqG42GxikLtgZQzYArp73rxXE")
OWNER_ID = int(os.getenv("OWNER_ID", "880184388"))
DB_NAME = os.getenv("DB_NAME", "FsubJha")
DB_KEY = os.getenv("DB_KEY", "FsubJha")
FILE_KEY = os.getenv("FILE_KEY", "-1002262844601")
