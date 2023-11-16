from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Post

# Create your views here.


def home_page(request: HttpRequest) -> HttpResponse:
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request: HttpRequest) -> HttpResponse:
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})


def post_detail(request: HttpRequest, slug: str) -> HttpResponse:
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {"post": post, "tags": post.tags.all()})
