from django.conf.urls import url, include
from rest_framework import routers
from snippets.views import SnippetViewSet, UserViewSet, GroupViewSet
from products.views import ProductViewSet


router = routers.DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'products', ProductViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
