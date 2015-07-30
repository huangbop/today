from django.conf.urls import url, include
from rest_framework import routers
from snippets.views import SnippetViewSet


router = routers.DefaultRouter()
router.register(r'^$', SnippetViewSet)


urlpatterns = [
    url(r'^$', include(router.urls)),
]
