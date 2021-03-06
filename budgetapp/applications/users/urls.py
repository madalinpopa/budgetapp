"""
urls.py
"""
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

app_name = "users"

urlpatterns = [
    path(
        "login/",
        view=LoginView.as_view(),
        name="login",
    ),
    path(
        "logout/",
        view=LogoutView.as_view(),
        name="logout",
    ),
]
