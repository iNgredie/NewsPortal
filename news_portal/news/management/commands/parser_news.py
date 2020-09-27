from django.core.management import BaseCommand
from newsapi import NewsApiClient

from news.models import News


class NewsParser:

    def get_news(self):
        newsapi = NewsApiClient(api_key='03adf0de54094295b2a5cdbdb0bc85e2')
        topheadlines = newsapi.get_top_headlines(sources='bbc-news,the-verge')

        articles = topheadlines['articles']

        for i in range(len(articles)):
            myarticles = articles[i]

            n = News(
                title=myarticles['title'],
                description=myarticles['description'],
                create_at=myarticles['publishedAt'],
                image=myarticles['urlToImage']
            ).save()


class Command(BaseCommand):
    help = 'Parsing news'

    def handle(self, *args, **options):
        n = NewsParser()
        n.get_news()