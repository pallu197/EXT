"""
from os import getenv


API_ID = int(getenv("API_ID", "26375665"))
API_HASH = getenv("API_HASH", "568839157ce65f4d3a91647f022b6737")
BOT_TOKEN = getenv("BOT_TOKEN", "8450499510:AAF-Hil0GQFPAWkVXdMvmqh4JIfYLGJER9M")
OWNER_ID = int(getenv("OWNER_ID", "6834250190"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6834250190").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://daxxop:daxxop@daxxop.dg3umlc.mongodb.net/?retryWrites=true&w=majority")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002788873966"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002788873966"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6834250190 7621154046 7793979196 5798579221").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS"))

