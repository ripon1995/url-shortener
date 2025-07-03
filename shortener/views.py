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


class ShortenUrlRetrieveUpdateDestroyAPIView(APIView):

    def get_object(self, pk):
        try:
            return ShortenedURL.objects.get(pk=pk)
        except ShortenedURL.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        shortened_url = self.get_object(pk)
        if not shortened_url:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ShortenedURLListCreateSerializer(shortened_url)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        shortened_url = self.get_object(pk)
        if not shortened_url:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ShortenedURLListCreateSerializer(shortened_url, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save(
            shortened_url=shorten_url(serializer.validated_data["original_url"])
        )
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        shortened_url = self.get_object(pk)
        if not shortened_url:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        shortened_url.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
