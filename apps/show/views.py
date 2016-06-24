from django.shortcuts import render
from rest_framework import viewsets
from apps.show.models import Show
from apps.show.serializers import ShowSerializer


class ShowViewSet(viewsets.ModelViewSet):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer
