import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "𝑪𝒓𝒂𝒛𝒚 𝑪𝒓𝒆𝒘 𝑯𝒐𝒖𝒓 🤓🤓")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "imnikkkk")
ALIVE_NAME = getenv("ALIVE_NAME", "nixstream")
BOT_USERNAME = getenv("BOT_USERNAME", "nikstream")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "imnikkkk")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "CCHour")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "CCHour")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/bf3d5334efaa345955275.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
IMG_1 = getenv("IMG_1","https://telegra.ph/file/c0af5af716aea44045a3d.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/c0af5af716aea44045a3d.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c0af5af716aea44045a3d.png")
