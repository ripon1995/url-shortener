from rest_framework.serializers import ModelSerializer

from .models import ShortenedURL


class ShortenedURLListCreateSerializer(ModelSerializer):
    class Meta:
        model = ShortenedURL
        fields = ["id", "original_url", "shortened_url", "created_at"]
        read_only_fields = ["shortened_url", "created_at"]
