from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

import requests

from message_templates import (
    START_MESSAGE_TEMPLATE,
    HELP_MESSAGE_TEMPLATE,
    LATEST_ARTICLE_MESSAGE_TEMPLATE,
    SUBSCRIPTION_MESSAGE_TEMPLATE,
    SUBSCRIPTION_CANCELLING_MESSAGE_TEMPLATE
)

from db import (
    add_or_remove_subscriber
)

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(START_MESSAGE_TEMPLATE)


@router.message(Command("help"))
async def start_handler(msg: Message):
    await msg.answer(HELP_MESSAGE_TEMPLATE)


@router.message(Command("latest"))
async def latest_handler(msg: Message):
    latest_article = requests.get("http://localhost:8000/api/v1/articles/latest").json()

    await msg.answer(
        LATEST_ARTICLE_MESSAGE_TEMPLATE.format(
            title=latest_article["title"],
            author=latest_article["author"],
            url=latest_article["article_url"]
        )
    )


@router.message(Command("subscribe"))
async def subscribe_handler(msg: Message):

    if add_or_remove_subscriber(str(msg.chat.id)):
        answer = SUBSCRIPTION_MESSAGE_TEMPLATE
    else:
        answer = SUBSCRIPTION_CANCELLING_MESSAGE_TEMPLATE

    await msg.answer(
        answer
    )
