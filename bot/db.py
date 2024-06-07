import psycopg2
from decouple import config

BOT_TOKEN = config('BOT_TOKEN')
TELEGRAM_API_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/'

DB_DATABASE = config('PG_NAME')
DB_USER = config('PG_USER')
DB_PASSWORD = config('PG_PASSWORD')
DB_HOST = config('PG_HOST')
DB_PORT = config('PG_PORT')


def get_database_cursor():
    connection = psycopg2.connect(
        database=DB_DATABASE,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
    )
    return connection, connection.cursor()


def add_or_remove_subscriber(telegram_chat_id):
    """Add or remove telegram_chat_id for article adding notification"""
    connection, cursor = get_database_cursor()

    cursor.execute(
        f"SELECT * FROM articles_notificationsubscriber WHERE telegram_chat_id={telegram_chat_id}::varchar"
    )
    subscriber = cursor.fetchone()

    if not subscriber:
        cursor.execute(
            f"INSERT INTO articles_notificationsubscriber (telegram_chat_id) VALUES ({telegram_chat_id})"
        )
        connection.commit()
        return True

    cursor.execute(
        f"DELETE FROM articles_notificationsubscriber WHERE telegram_chat_id={telegram_chat_id}::varchar"
    )
    connection.commit()

    cursor.close()
    connection.close()
    return False


def get_subscribers():
    connection, cursor = get_database_cursor()

    cursor.execute(
        f"SELECT telegram_chat_id FROM articles_notificationsubscriber"
    )
    subscribers = cursor.fetchall()
    cursor.close()
    connection.close()
    return subscribers
