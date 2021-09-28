from django.urls import path
from . import views

app_name = "subscribeapp"

urlpatterns = [
    path("subcribe/", views.SubscriptionView.as_view(), name="subcribe"),
    path("list/", views.SubscriptionListView.as_view(), name="list"),
]
