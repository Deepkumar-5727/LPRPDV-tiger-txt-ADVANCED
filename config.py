import os

API_ID = API_ID = 23011537

API_HASH = os.environ.get("API_HASH", "cd59a9fc8cbdca6ae2b405f149cc3c8a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7483811838:AAHTexAJ5IQIMjOSOag6bNV5QTPC5DHlS54")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5389632871))

LOG = -1002341764297

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5389632871").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


