import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "11319890")

API_HASH = os.environ.get("API_HASH", "4965e574411647c42ffbd8b46040f0a5")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5977093025:AAHqridJ91UHBdu5tKhgax54j90gMkK3Y9I") 

FORCE_SUB = os.environ.get("FORCE_SUB", "") 

DB_NAME = os.environ.get("DB_NAME","Indonesia")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Indonesia:indonesia37@cluster0.7gxmrjn.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/1d911704c0de0b62a7d77.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1365582907').split()]

