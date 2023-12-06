from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home_page"),
    path("posts", views.AllPostsView.as_view(), name="posts_page"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post_detail_page"),
    path("read-later", views.ReadLaterView.as_view(), name="read_later"),
]
