# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '29849415'))
    API_HASH = str(getenv('API_HASH', '0dd6c10897b85d7f10a8dcdeb74f8b8a'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '6346630375:AAG63AqWrin_oe-QUtS1qmuNH-yNgaiIj8o'))
    name = str(getenv('name', 'file00449'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001909671162'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "6246777352").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'i_manjot_sidhu'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'https://file00449-952a34152a50.herokuapp.com')) if not ON_HEROKU or getenv('FQDN', 'manjotsidhu1-8c745768fdba.herokuapp.com') else APP_NAME+'manjotsidhu1-8c745768fdba.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://Jot43000:Jot43000@cluster0.6rg0tz5.mongodb.net/'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'goldmines_officialy'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1002017910387")).split()))     
