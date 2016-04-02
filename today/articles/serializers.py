from rest_framework import serializers

from .models import Article


class ArticleSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Article
