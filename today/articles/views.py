from django.shortcuts import render
from django.views.generic import ListView, DetailView
from rest_framework import viewsets

from .models import Article
from .serializers import ArticleSerilizer


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article
    slug_url_kwarg = "id"
    slug_field = 'id'


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerilizer
