from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy


# Create your views here.
def hello_world(request):
    return render(request, "accountapp/hello_world.html")


class AccountCreateView(CreateView):
    model = User  # 👈 Django의 내장된 User 모델 사용
    form_class = UserCreationForm  # 👈 Django의 내장된 Form 사용
    success_url = reverse_lazy(
        "accountapp:hello_world"
    )  # 👈 성공 시 이동할 곳, 반드시 reverse_lazy
    template_name = "accountapp/create.html"  # 👈 입력 받을 Template
