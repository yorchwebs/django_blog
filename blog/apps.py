"""Configuration for the blog app."""

from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Configuration for the blog app.

    Usage:
    >>> from blog.apps import BlogConfig
    >>> BlogConfig.name
    'blog'

    :return: str
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"
