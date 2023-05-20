# Copyright (c) 2022 Itz-fork

import os


class Config(object):
    APP_ID = int(os.environ.get("APP_ID", '7068279'))
    API_HASH = os.environ.get("API_HASH", '2dc9a997317b0ff7a2d84d5a1bd7f91b')
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6151333130:AAGZVtU3Jx2cOrPe7UPLduSQTPqMn9ANdo8")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1690773526").split())
    IS_PUBLIC_BOT = os.environ.get("IS_PUBLIC_BOT") in ["False", "false"]
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL")) if os.environ.get("-906831722") else None
    # DON'T CHANGE THESE 2 VARS
    DOWNLOAD_LOCATION = "./NexaBots"
    TG_MAX_SIZE = 2040108421
    # Mega User Account
    MEGA_EMAIL = os.environ.get("binodtharu542@gmail.com")
    MEGA_PASSWORD = os.environ.get("bababoi69")
