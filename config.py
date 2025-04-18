# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "9972455"))
API_HASH = getenv("API_HASH", "5b1fd83b698e4e6670f3dcb053eecc06")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8080218275").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://pandagaming17:vR5XKnFV57fubEnH@cluster0.efm8s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002532071035")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002532071035"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "2"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "1000"))
