# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the UserListView
    url(r'^$', view=views.ArticleListView.as_view(), name='list'),
    url(r'^(?P<id>[0-9]+)/$', view=views.ArticleDetailView.as_view(), name='detail'),

]
