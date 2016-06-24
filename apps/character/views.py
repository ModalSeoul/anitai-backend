from django.shortcuts import render
from rest_framework import viewsets
from apps.character.models import Character
from apps.character.serializers import CharacterSerializer


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
