from django.urls import path

from .views import CreateShortenerUrl

urlpatterns = [
    path("shorten/", CreateShortenerUrl.as_view(), name="create_shortened_url"),
]
