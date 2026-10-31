from django.urls import path
from .views import SignUpView
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path(
        "login",
        auth_views.LoginView.as_view(template_name="pages/registration/login.html"),
        name="login",
    ),
]