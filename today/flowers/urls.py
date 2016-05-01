from django.conf.urls import url

from .views import FlowerListView



urlpatterns = [
    url(r'^$', FlowerListView.as_view(), name='list'),
]
