from articles.models import ThirdPartyArticle


def add_article_to_db(article_title, article_link):

    if ThirdPartyArticle.objects.filter(title=article_title, url=article_link).count() == 0:
        ThirdPartyArticle.objects.create(
            title=article_title,
            url=article_link
        )
        return True
    return False
