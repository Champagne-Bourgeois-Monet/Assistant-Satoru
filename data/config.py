# BOT TOKEN моего telegram бота.
import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))
PGPORT = str(os.getenv("PGPORT"))
PGDATABASE = str(os.getenv("PGDATABASE"))

admins = [
    1478600655,
    1031212769,
    1096326336
]

ip = os.getenv("ip")


