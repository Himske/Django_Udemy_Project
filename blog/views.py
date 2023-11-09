from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def home_page(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/index.html")


def posts(request: HttpRequest) -> HttpResponse:
    pass


def post_detail(request: HttpRequest) -> HttpResponse:
    pass
