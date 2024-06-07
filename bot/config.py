from decouple import config

BOT_TOKEN = config('BOT_TOKEN')
TELEGRAM_API_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/'

DB_DATABASE = config('PG_NAME')
DB_USER = config('PG_USER')
DB_PASSWORD = config('PG_PASSWORD')
DB_HOST = config('PG_HOST')
DB_PORT = config('PG_PORT')
