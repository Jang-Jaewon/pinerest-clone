from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = "accountapp"

urlpatterns = [
    path("hello_world", views.hello_world, name="hello_world"),
    path(
        "login/", LoginView.as_view(template_name="accountapp/login.html"), name="login"
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("create", views.AccountCreateView.as_view(), name="create"),
]
