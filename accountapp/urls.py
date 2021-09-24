from django.urls import path
from . import views

app_name = "accountapp"

urlpatterns = [
    path("hello_world", views.hello_world, name="hello_world"),
    path("login/", views.AccountLoginView.as_view(), name="login"),
    path("logout/", views.AccountLogoutView.as_view(), name="logout"),
    path("create", views.AccountCreateView.as_view(), name="create"),
]
