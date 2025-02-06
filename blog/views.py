"""Views for the blog app."""

from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Post


def post_list(request):
    """
    Display a list of published posts.

    :param request: HttpRequest object

    :return: HttpResponse object
    """
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get("page", 1)
    posts = paginator.page(page_number)
    return render(request, "post/list.html", {"posts": posts})


def post_detail(request, year, month, day, post):
    """
    Display a single post.

    :param request: HttpRequest object

    :param id: int, post ID

    :return: HttpResponse object
    """
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(request, "post/detail.html", {"post": post})
