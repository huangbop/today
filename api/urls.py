from django.conf.urls import url, include
from rest_framework import routers
from snippets.views import SnippetViewSet, UserViewSet, GroupViewSet
from products.views import ProductViewSet


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
