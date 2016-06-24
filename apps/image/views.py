from django.shortcuts import render
from rest_framework import viewsets
from apps.image.models import Img
from apps.image.serializers import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Img.objects.all()
    serializer_class = ImageSerializer

    def perform_create(self, serializer):
        serializer_class.save(author=self.request.user)
