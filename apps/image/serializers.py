from rest_framework import serializers
from apps.image.models import Img
from apps.accounts.models import EmailUser


class ImageSerializer(serializers.ModelSerializer):
    upvoted = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=EmailUser.objects.all(),
        required=False
    )

    class Meta:
        model = Img
