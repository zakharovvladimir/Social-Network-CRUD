"""Posts app."""
from django.apps import AppConfig


class PostsConfig(AppConfig):
    """Posts App config."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
