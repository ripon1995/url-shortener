from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ShortenedURL
from .serializers import ShortenedURLListCreateSerializer
from .utils import shorten_url


class ShortenUrlListCreateAPIView(APIView):

    def get(self, request, *args, **kwargs):
        urls = ShortenedURL.objects.all()
        serializer = ShortenedURLListCreateSerializer(urls, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ShortenedURLListCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save(
            shortened_url=shorten_url(serializer.validated_data["original_url"])
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
