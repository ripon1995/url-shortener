from rest_framework.serializers import ModelSerializer

from .models import ShortenedURL


class ShortenedURLSerializer(ModelSerializer):
    class Meta:
        model = ShortenedURL
        fields = ["original_url", "shortened_url", "created_at"]
        read_only_fields = ["shortened_url", "created_at"]
