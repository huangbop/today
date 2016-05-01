from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import viewsets

from .models import Flower
from .serializers import FlowerSerializer


class FlowerListView(ListView):
    model = Flower




class FlowerViewSet(viewsets.ModelViewSet):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer

