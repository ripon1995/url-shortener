from django.urls import path

from .views import ShortenUrlListCreateAPIView

urlpatterns = [
    path(
        "shortens/", ShortenUrlListCreateAPIView.as_view(), name="create_shortened_url"
    ),
]
