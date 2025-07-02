from django.urls import path

from .views import ShortenUrlListCreateAPIView, ShortenUrlRetrieveUpdateDestroyAPIView

urlpatterns = [
    path(
        "shortens/", ShortenUrlListCreateAPIView.as_view(), name="create_shortened_url"
    ),
    path(
        "shortens/<int:pk>/",
        ShortenUrlRetrieveUpdateDestroyAPIView.as_view(),
        name="retrieve_update_destroy_shortened_url",
    ),
]
