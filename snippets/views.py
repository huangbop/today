from rest_framework import viewsets
from snippets.models import Snippet
from snippets.serilizers import SnippetSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serilizer_class = SnippetSerializer
