from django.urls import path

from . import views

app_name = "news"

urlpatterns = [
	path("news/", views.HomeView.as_view(), name="list"),
	path("all-news/", views.AllNewsView.as_view(), name="all-news"),
	path("all-news/<int:pk>/", views.NewsDetailView.as_view(), name="news-detail"),
]

