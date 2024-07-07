START_MESSAGE_TEMPLATE = (
    "I am bot for article API"
)

LATEST_ARTICLE_MESSAGE_TEMPLATE = (
    "Here is the latest article.\n\n"
    "{title}\n\n"
    "by {author}\n\n"
    "{url}"
)

HELP_MESSAGE_TEMPLATE = (
    "/start - start bot\n"
    "/help - show bot commands\n"
    "/latest - show latest article\n"
    "/subscribe - subscribe to news\n"
)

SUBSCRIPTION_MESSAGE_TEMPLATE = "You've successfully subscribed!"

SUBSCRIPTION_CANCELLING_MESSAGE_TEMPLATE = "You've successfully cancelled your subscription!"

SUBSCRIPTION_NEW_ARTICLE_MESSAGE_TEMPLATE = (
    "New article is added to our website.\n\n"
    "{title}\n\n"
    "by {author}\n\n"
    "{url}"
)
