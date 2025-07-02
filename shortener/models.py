from django.db import models


class ShortenedURL(models.Model):
    original_url = models.URLField(max_length=2000, verbose_name="Original URL")
    shortened_url = models.CharField(
        max_length=20, unique=True, verbose_name="Shortened URL"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Shortened URL"
        verbose_name_plural = "Shortened URLs"

    def __str__(self):
        return f"{self.original_url} -> {self.shortened_url}"
