"""This file is used to write tests for the blog app."""

from django.test import TestCase, RequestFactory
from django.urls import reverse

from .models import Post
from .views import post_list, post_detail
from django.utils import timezone


class PostListViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.post1 = Post.objects.create(
            title="Test Post 1",
            slug="test-post-1",
            body="Test Body 1",
            publish=timezone.now(),
            status=Post.Status.PUBLISHED,
        )
        self.post2 = Post.objects.create(
            title="Test Post 2",
            slug="test-post-2",
            body="Test Body 2",
            publish=timezone.now() + timezone.timedelta(days=1),  # Not published yet
            status=Post.Status.DRAFT,
        )

    
def test_post_list_view(self):
        request = self.factory.get(reverse("blog:post_list"))
        response = post_list(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post 1")
        self.assertNotContains(response, "Test Post 2")
        self.assertEqual(len(response.context["posts"]), 1)


class PostDetailViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.post = Post.objects.create(
            title="Test Detail Post",
            slug="test-detail-post",
            body="Test Body",
            publish=timezone.now(),
            status=Post.Status.PUBLISHED,
        )

    def test_post_detail_view(self):
        request = self.factory.get(
            reverse(
                "blog:post_detail",
                args=[
                    self.post.publish.year,
                    self.post.publish.month,
                    self.post.publish.
day,
                    self.post.slug,
                ],
            )
        )
        response = post_detail(
            request,
            self.post.publish.year,
            self.post.publish.month,
            self.post.publish.day,
            self.post.slug,
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Detail Post")
        self.assertEqual(response.context["post"], self.post)

    def test_post_detail_404(self):
        request = self.factory.get(
            reverse(
                "blog:post_detail",
                args=[
                    2024,
                    1,
                    1,
                    "invalid-post"
                ],
            )
        )
        with self.assertRaises(Exception) as context:
            post_detail(request, 2024, 1, 1, "invalid-post")

        self.assertEqual(context.exception.status_code, 404)
