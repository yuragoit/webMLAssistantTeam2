from django.urls import path
from . import views

app_name = "news"

urlpatterns = [
    path("", views.app_news, name="news_list"),
    path("detail/<int:pk>/", views.detail, name="news_detail"),
]
