from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_index.as_view(), name = "home_index"),
    path("", views.search, name = "search"),
]
