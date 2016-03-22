from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Article



class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article
    slug_url_kwarg = "id"
    slug_field = 'id'
