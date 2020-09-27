from django.urls import path

from news.views import ListNews, Search

urlpatterns = [
    path('', ListNews.as_view(), name='news'),
    path('search', Search.as_view(), name='search')
]


