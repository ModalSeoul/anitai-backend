from rest_framework import serializers
from apps.image.models import Img


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Img
