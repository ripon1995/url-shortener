from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ShortenedURLSerializer
from .utils import shorten_url


class CreateShortenerUrl(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ShortenedURLSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save(
            shortened_url=shorten_url(serializer.validated_data["original_url"])
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
