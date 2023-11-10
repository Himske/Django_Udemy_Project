from datetime import date

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Fredrik",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": """
            There is nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what
            happened whilst I was enjoying the view!
        """,
        "content": """
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Ea veritatis mollitia optio iusto ullam
            exercitationem repellat unde harum ratione repudiandae! Nisi amet fuga nulla earum numquam quo ullam est
            aut.

            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Ea veritatis mollitia optio iusto ullam
            exercitationem repellat unde harum ratione repudiandae! Nisi amet fuga nulla earum numquam quo ullam est
            aut.

            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Ea veritatis mollitia optio iusto ullam
            exercitationem repellat unde harum ratione repudiandae! Nisi amet fuga nulla earum numquam quo ullam est
            aut.
        """,
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Fredrik",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """,
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Fredrik",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """,
    },
]


def get_date(post: dict) -> date:
    return post["date"]


# Create your views here.


def home_page(request: HttpRequest) -> HttpResponse:
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})


def post_detail(request: HttpRequest, slug: str) -> HttpResponse:
    post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {"post": post})
