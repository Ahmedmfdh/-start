from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/e250be48cfb059cef50b7.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/e250be48cfb059cef50b7.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/SOURCE_SAKRAN")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SOURCESAKRAN")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6950300507").split()))


FAILED = "https://telegra.ph/file/e250be48cfb059cef50b7.jpg"
