from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [ 
    path("login/", auth_views.LoginView.as_view(template_name = "users/login.html"), name = "login"),
    path("logout/", auth_views.LogoutView.as_view(next_page = 'login'), name = "logout"),
    path("register/", views.Register, name = "register"),
    path("profile/", views.profile.as_view(), name = "profile"),
    path("profile/<int:pk>/", views.SpecificMedication.as_view(template_name = "home/SpecificMedication.html"), name = "med_details"),
    path("delete/<int:pk>/delete/", views.DeleteMedication.as_view(), name = "delete"),
    path("add/", views.AddMedication.as_view(template_name = "users/add.html"), name = "add"),
]