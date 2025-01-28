# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "9972455"))
API_HASH = getenv("API_HASH", "5b1fd83b698e4e6670f3dcb053eecc06")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7679286299").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://sanjisama626:sanjisama626@sanjisama.lukxw8r.mongodb.net/?retryWrites=true&w=majority&appName=sanjisama")
LOG_GROUP = getenv("LOG_GROUP", "-1002410837275")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002182291545"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "2"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "1000"))
