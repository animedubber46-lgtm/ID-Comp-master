import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "20899529")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "0297693c81aac01b704702f334decddd") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7440573577:AAHtHk-u9fE6WEhwfjVDk-jx8aP8cApMrf8") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', 'Indian_Dubber') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://sakshamranjan7:8wBCaYilCTlgdNV3@cluster0.h184m7m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","Indian_Dubber") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "8002803133")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002560487530')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://files.catbox.moe/2uiu0q.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
**File Name**: {0}

**Original File Size:** {1}
**Encoded File Size:** {2}
**Compression Percentage:** {3}

__Downloaded in {4}__
__Encoded in {5}__
__Uploaded in {6}__
"""
