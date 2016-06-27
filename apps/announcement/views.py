from django.shortcuts import render
from rest_framework import viewsets
from apps.announcement.models import Announcement
from apps.announcement.serializers import AnnouncementSerializer


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
