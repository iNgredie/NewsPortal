from django.views.generic import ListView
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from news.models import News
from news.serializers import NewsApiSerializer


class ListNews(ListView):
    model = News


class NewsApiViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsApiSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'create_at']
    ordering_fields = ['create_at', 'title']


class Search(ListView):
    template_name = 'news/search.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context