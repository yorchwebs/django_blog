"""Django models for the blog app."""

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


class PublishedManager(models.Manager):
    """
    Custom manager to retrieve only published posts.

    Usage:
    >>> from blog.models import Post
    >>> Post.published.all()
    <QuerySet [<Post: Example post>]>

    :return: QuerySet object
    """

    def get_queryset(self):
        """
        Override the default queryset to filter only published posts.

        Usage:
        >>> from blog.models import Post
        >>> Post.published.get_queryset()
        <QuerySet [<Post: Example post>]>

        :return: QuerySet object
        """
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    """
    A blog post.

    Usage:
    >>> from blog.models import Post
    >>> Post.objects.all()
    <QuerySet [<Post: Example post>]>

    :return: QuerySet object
    """

    class Status(models.TextChoices):
        """
        Choices for the status field.

        Usage:
        >>> from blog.models import Post
        >>> Post.Status.DRAFT 'DF' 'Draft'
        >>> Post.Status.PUBLISHED 'PB' 'Published'

        :return: str
        """

        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blog_posts",
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2, choices=Status, default=Status.DRAFT
    )

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        """
        Metadata for the Post model.

        Usage:
        >>> from blog.models import Post
        >>> Post._meta.get_field("title").max_length 250

        :return: int
        """

        ordering = ["-publish"]
        indexes = [
            models.Index(fields=["-publish"]),
        ]

    def __str__(self):
        """
        Return the title of the post.

        Usage:
        >>> from blog.models import Post
        >>> post = Post.objects.first()
        >>> post.__str__()
        'Example post'

        :return: str
        """
        return self.title

    def get_absolute_url(self):
        """
        Return the URL of the post detail page.

        Usage:
        >>> from blog.models import Post
        >>> post = Post.objects.first()
        >>> post.get_absolute_url() '/blog/1/'

        :return: str
        """
        return reverse(
            "blog:post_detail",
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug,
            ],
        )
