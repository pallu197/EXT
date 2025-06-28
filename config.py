"""
from os import getenv


API_ID = int(getenv("API_ID", "21567814"))
API_HASH = getenv("API_HASH", "cd7dc5431d449fd795683c550d7bfb7e)
BOT_TOKEN = getenv("BOT_TOKEN", "7864597080:AAGBgPyZ-NJ0W_LfYLrGu708avBFnwmEp6c")
OWNER_ID = int(getenv("OWNER_ID", "6126688051"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6126688051 6039166844").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://daxxop:daxxop@daxxop.dg3umlc.mongodb.net/?retryWrites=true&w=majority")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002726534263"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002726534263"))

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

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5840594311 7621154046 7793979196 5798579221").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS"))

