from rest_framework.response import Response
from rest_framework.views import APIView


class CreateShortenerUrl(APIView):
    def post(self, request, *args, **kwargs):

        return Response({"message": "Shortened URL created successfully!"})
