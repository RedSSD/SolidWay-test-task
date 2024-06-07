import requests

from bot.config import TELEGRAM_API_URL
from bot.db import get_subscribers

from bot.message_templates import SUBSCRIPTION_NEW_ARTICLE_MESSAGE_TEMPLATE


def bot_notify_subscribers(article):
    # TODO create article url. mb inside serializers/views
    subscribers = get_subscribers()
    for subscriber_chat_id in subscribers:
        response = requests.post(
            TELEGRAM_API_URL + "sendMessage",
            data={
                'chat_id': subscriber_chat_id[0],
                'text': SUBSCRIPTION_NEW_ARTICLE_MESSAGE_TEMPLATE.format(
                    title=article["title"],
                    author=article["author"],
                    url=article["id"],
                )
            }
        )
