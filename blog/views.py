"""Views for the blog app."""

from django.shortcuts import get_object_or_404, render

from .models import Post


def post_list(request):
    """
    Display a list of published posts.

    :param request: HttpRequest object

    :return: HttpResponse object
    """
    posts = Post.published.all()
    return render(request, "post/list.html", {"posts": posts})


def post_detail(request, id):
    """
    Display a single post.

    :param request: HttpRequest object

    :param id: int, post ID

    :return: HttpResponse object
    """
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, "post/detail.html", {"post": post})
