# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "20571368")

API_HASH = os.environ.get("API_HASH", "c874d957737d24e17159005874a2d5bf")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7272469041:AAE-Jn1Z2xj0GzFr6CuujLv6YmWkjE8qG-E") 

FORCE_SUB = os.environ.get("FORCE_SUB", "ARA_HANIME_WORLD") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "ararename")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://ariyansarkar670:rn9eARu7Kuig5UKp@cluster0.gldqteo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1049652979').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
