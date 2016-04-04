from django.conf.urls import url

from .views import DelicListView


urlpatterns = [
    url(r'^$', DelicListView.as_view(), name='list'),
]
