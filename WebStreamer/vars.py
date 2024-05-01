# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]
import os
import sys
from os import environ
from dotenv import load_doten

load_dotenv()


class Var(object):
    MULTI_CLIENT = False
    API_ID = int(environ.get("API_ID", 23250755))
    API_HASH = str(environ.get("API_HASH", "25e52089df623e32713c20639be18be3"))
    BOT_TOKEN = str(environ.get("BOT_TOKEN", "7014567806:AAH2M6OMQ3wUeWlAakfl380cDfbCyJF4Tmw"))
    SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))  # 1 minte
    WORKERS = int(environ.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    BIN_CHANNEL = int(
        environ.get("BIN_CHANNEL", -1001609280362))
      # you NEED to use a CHANNEL when you're using MULTI_CLIENT
    PORT = int(environ.get("PORT", 8080))
    BIND_ADDRESS = str(environ.get("WEB_SERVER_BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    HAS_SSL = str(environ.get("HAS_SSL", "1").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(environ.get("NO_PORT", "1").lower()) in ("1", "true", "t", "yes", "y")
    HASH_LENGTH = int(environ.get("HASH_LENGTH", 6))
    if not 5 < HASH_LENGTH < 64:
        sys.exit("Hash length should be greater than 5 and less than 64")
    FQDN = str(environ.get("FQDN", "egyptstreaming6969.onrender.com"))
    URL = "http{}://{}{}/".format(
            "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
    )
    KEEP_ALIVE = str(environ.get("KEEP_ALIVE", "1").lower()) in  ("1", "true", "t", "yes", "y")
    DEBUG = str(environ.get("DEBUG", "1").lower()) in ("1", "true", "t", "yes", "y")
    USE_SESSION_FILE = str(environ.get("USE_SESSION_FILE", "1").lower()) in ("1", "true", "t", "yes", "y")
    ALLOWED_USERS = [x.strip("@ ") for x in str(environ.get("ALLOWED_USERS", "") or "").split(",") if x.strip("@ ")]
